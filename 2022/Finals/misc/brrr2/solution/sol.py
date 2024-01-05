from requests import Session

# URL = 'http://localhost:5000'
URL = 'https://brrr2.finals.ggc.tf'

s = Session()
s.get(URL)

def flip(c):
    return {'R': 'B', 'B': 'R'}[c]

for _ in range(100):
    res = s.post(f'{URL}/api/start')
    comp = res.json()['computer_seq']
    mine = [flip(comp[1]), *comp[:2]]
    res = s.post(f'{URL}/api/play', json={'seq': mine})

print(s.post(f'{URL}/api/start').json())


