from requests import Session

# URL = 'http://localhost:5000'
URL = 'https://brrr1.finals.ggc.tf'

s = Session()
s.get(URL)

for _ in range(100):
    res = s.post(f'{URL}/api/start')
    comp = res.json()['computer_seq']
    res = s.post(f'{URL}/api/play', json={'seq': comp})

print(s.post(f'{URL}/api/start').json())


