from segno import helpers

qrcode = helpers.make_email("mariyav14012010@gmail.com", cc=None, bcc=None, subject="Qr code", body=":)")
qrcode.save("qr_codes/email_qr.png", dark="#8A2BE2", border=4, scale=5)
qrcode.show()