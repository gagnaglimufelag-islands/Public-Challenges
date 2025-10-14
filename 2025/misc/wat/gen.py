from fpdf import FPDF
from random import shuffle


# should beA fIaäg HERĘ
# gg{yay_you_found_me!}

srange = list(range(32, 500))
shuffle(srange)
pdf = FPDF()
pdf.set_compression(compress=False)
pdf.set_author('Wat')
pdf.set_creator('Wat')
pdf.set_title('Wat')
pdf.set_subject('Wat')
pdf.add_page()
pdf.add_font('Flag', '', 'FlagFont-Regular.ttf', uni=True)
pdf.add_font('OpenSans', '', 'OpenSans-Regular.ttf', uni=True)
pdf.set_font('OpenSans', '', 16)
pdf.cell(40, 10, 'should beA fIaäg HERĘ', 0, 1)
pdf.set_font('Flag', '', 16)
pdf.cell(40, 10, '\u0266\u027e\u028b\u2691\u0296\u028c\u0292\u2691\u0283\u0286\u028b\u0281\u2691\u0286\u0291?', 0, 1)
pdf.set_font('Flag', '', 1)
pdf.set_text_color(255)
pdf.multi_cell(40, 10, ''.join(chr(a) for a in srange), 0)
pdf.output('wat.pdf')


producer = b'PyFPDF 1.7.2 http://pyfpdf.googlecode.com/'
with open('wat.pdf', 'rb') as f:
    doc = f.read()


with open('wat.pdf', 'wb') as f:
    f.write(doc.replace(producer, (b'WATwat' * 10)[:len(producer)]))

