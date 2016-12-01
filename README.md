# chattr
A simple SMS chat bot powered by Cleverbot
  
# What exactly does it do?
Chattr allows you to talk to a friendly bot all the time. Or let a friend talk to a bot all the time. And maybe even not tell them it's a bot. You can specify a friend's phone number, and an initial message to send but then the AI chat bot takes the conversation away from there!

# How?
Chattr utilizes two other projects to function. This project would not be possible without 
  - [chatterbotapi](https://github.com/pierredavidbelanger/chatter-bot-api)
  - [pygooglevoice](https://github.com/pettazz/pygooglevoice)
  
# Installation
```
sudo easy_install simplejson pygooglevoice BeautifulSoup
```
  
# Setup
There's not much to set up. Be sure you have a Google Voice account with a phone number already set up. Put your credentials in a file called credentials.txt in this format:

```
example.email@gmail.com:mypassword
```
  
# How do I run it?
Run it like this:

```
python chattr.py +15551234567 "Hey there!"
```
