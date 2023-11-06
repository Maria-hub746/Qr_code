import segno


qrcode = segno.make_qr('https://github.com/Maria-hub746')

qrcode.save('mariia.png', dark="#e393f8", border=4, scale=5)
qrcode.show()