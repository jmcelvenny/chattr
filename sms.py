#!/usr/bin/python
import sys
import BeautifulSoup
import json

def hasReplied(to_number, voice):
	for message in voice.sms().messages:
		if message.phoneNumber == to_number:
			return (message.isRead==False)
	return False

def pullRecent(to_number, voice):
	for message in voice.sms().messages:
		if message.phoneNumber == to_number:
			voice.sms()
			jdata = extractsms(voice.sms.html)
			jsonObj = []
			for obj in jdata:
				if obj['id']==message.id:
					jsonObj.append(obj)
			text=jsonObj[len(jsonObj)-1]['text']
			message.mark(1)
			return text
	return "invalid"

def sendSMS(to_number, message, voice):
	voice.send_sms(to_number, message)

def extractsms(htmlsms) :
    msgitems = []
    tree = BeautifulSoup.BeautifulSoup(htmlsms)	
    conversations = tree.findAll("div",attrs={"id" : True},recursive=False)
    for conversation in conversations :
        rows = conversation.findAll(attrs={"class" : "gc-message-sms-row"})
        for row in rows :
            msgitem = {"id" : conversation["id"]}
            spans = row.findAll("span",attrs={"class" : True}, recursive=False)
            for span in spans :	
                cl = span["class"].replace('gc-message-sms-', '')
                msgitem[cl] = (" ".join(span.findAll(text=True))).strip()
            msgitems.append(msgitem)
    return msgitems