import os

COLORS = open('colors.txt').read().splitlines()

def main():
    print('Hello there! I see you have found me.')
    col = input('What is your favorite color?: ')
    if col.startswith('GET '):
        print("You appear to be using a browser to access this challenge, which won't work. Try netcat instead.")
    elif col.lower() not in COLORS:
        print(f'{col} is not a color I have ever heard of')
    else:
        print(f'What a coincidence, {col} is also MY favorite color.')
        print(os.environ.get('FLAG', 'fagl{notyourflag}'))

main()
