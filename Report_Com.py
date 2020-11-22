import amino
import os
red="\033[0;31m"
client=amino.Client()
email=input("Type Your Email: ")
password=input("Type Your Password: ")
try:
	client.login(email=email ,password=password)
	print ("Done")
except:
	print ("Your email or password is incorrect")
	os._exit()
comlink=input("Type Community Link: ")
com=client.get_from_code(comlink)
comId=com.path[1:com.path.index('/')]
subclient=amino.SubClient(comId=comId ,profile=client.profile)

reason=input("Type Your Reason: ")
while True:
	try:
		subclient.flag_community(comId=comId, reason=reason ,flagType=3 , isGuest=False)
		print(red + "Report Send")
	except:
		pass
		print ("Fail Sending Report")
