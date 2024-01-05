import qrcode
import yaml

flag = yaml.safe_load(open('./meta.yml'))['flags']

qr = qrcode.QRCode()
qr.add_data(flag)
qr.make()
print('\n'.join([','.join(['x' if i else '' for i in row]) for row in qr.modules]))

