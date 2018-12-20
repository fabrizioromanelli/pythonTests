import smtplib
server = smtplib.SMTP('66.249.93.111', '587')

server.login("fabrizio.romanelli@gmail.com", "cxxxcxc")

msg = "NO!"

server.sendmail("fabrizio.romanelli@gmail.com", "fabrizio.romanelli@gmail.com", msg)
