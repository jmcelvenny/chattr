#!/usr/bin/python
from googlevoice import Voice
from chatterbotapi import ChatterBotFactory, ChatterBotType
import sms
import sys
import time

#tested, works

#credential file:
# credentials.txt
	#	example@gmail.com:mypassword
def getCredentials():
	fin = open("credentials.txt", "r")
	line = fin.readline()
	credentials = line.split(":")
	return credentials

def __main__():
	#check arguments
	if (len(sys.argv) != 3):
		print "Usage: python clever.py XXXXXXXXXX \"starting message\""
		exit()

	#login to gv
	d = getCredentials()
	voice = Voice()
	voice.login(d[0], d[1])
	print "connected to GV successfully..."

	#setup chatbot
	factory = ChatterBotFactory()
	bot = factory.create(ChatterBotType.CLEVERBOT)
	botsession = bot.create_session()
	print "cleverbot session created sucessfully..."
	print "first message: %s " % sys.argv[2]
	sms.sendSMS(sys.argv[1], sys.argv[2], voice)

	#main bot loop
	while(1):
		if (sms.hasReplied(sys.argv[1], voice)):
			print "HAS replied"
			reply = sms.pullRecent(sys.argv[1], voice)
			print "msg obtained: %s" % reply
			s = botsession.think(reply)
			print "bot reply to msg: %s" % s
			sms.sendSMS(sys.argv[1], s, voice)
			print "sending sms..."
		else:
			print "has NOT replied"
		time.sleep(5)

__main__()