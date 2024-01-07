import yaml

CODE = {' ': '_',
	"'": '.----.',
	'(': '-.--.',
	')': '-.--.-',
	',': '--..--',
	'-': '-....-',
	'.': '.-.-.-',
	'/': '-..-.',
	'0': '-----',
	'1': '.----',
	'2': '..---',
	'3': '...--',
	'4': '....-',
	'5': '.....',
	'6': '-....',
	'7': '--...',
	'8': '---..',
	'9': '----.',
	':': '---...',
	';': '-.-.-.',
	'?': '..--..',
	'A': '.-',
	'B': '-...',
	'C': '-.-.',
	'D': '-..',
	'E': '.',
	'F': '..-.',
	'G': '--.',
	'H': '....',
	'I': '..',
	'J': '.---',
	'K': '-.-',
	'L': '.-..',
	'M': '--',
	'N': '-.',
	'O': '---',
	'P': '.--.',
	'Q': '--.-',
	'R': '.-.',
	'S': '...',
	'T': '-',
	'U': '..-',
	'V': '...-',
	'W': '.--',
	'X': '-..-',
	'Y': '-.--',
	'Z': '--..',
	'_': '..--.-'}

def convert(sentence):
    sentence = sentence.upper()
    encoded = []
    for character in sentence:
        encoded.append(CODE[character])
    return ' '.join(encoded)


meta = yaml.safe_load(open('meta.yml'))
flag = meta['flags'][-1]['flag']

morse = convert(flag)
norse = morse.replace('.', 'ᚽ').replace('-', 'ᛅ')

with open('norse-code.txt', 'w') as f:
    f.write(norse)
    f.write('\n')
    f.close()
