import smtplib # send emails in python
import sys # exit and stuff
from threading import Thread
#import optparse

your_email = "your_email" # email that sends
your_password = "your_password" # password to that email

go = int(input("\n[1]: gmail\n[2]: outlook\n>> "))
if go == 1:
	serv = 'smtp.gmail.com'
if go == 2:
	serv = 'smtp-mail.outlook.com'

print("\n--------------------------------")
their_email = input("To-Email : ")
message = input("Message  : ")
print("--------------------------------")

received = 0

def send():
	global received
	global serv

	try:
		server = smtplib.SMTP(str(serv), 587)# connect to server
		server.starttls() 
		server.login(your_email, your_password) # person sending
		server.sendmail(your_email, their_email, message) # send the message
		server.quit() # close

		received += 1
		print(str(received) + " sent")
		
		
	except smtplib.SMTPRecipientsRefused:
		print("\nYou may have entered an invalid email")

	except KeyboardInterrupt:
		print("\n[-] quiting")
		sys.exit()


def endless():
	print("\n---------------\n")
	while True:
		send()


def amount():
	print("\n---------------")
	amounts = int(input("amount	 : "))
	print("---------------\n")
	for x in range(1, amounts + 1):
		send()
	
	print(str(x) + " Sent")
	print("\nDone!")


ea = int(input("\n[1]: endless\n[2]: amount\n>> "))

if ea == 1:
	endless()

if ea == 2:
	amount()

else:
	print("thats not an option bud")
