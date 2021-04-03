# bwitter api thingy

import requests

class Bwitter():
    def __init__(self):
        self.s = requests.Session()

    def login(self):
        self.uname = input("Enter your username: ")
        self.pword = input("Enter your password: ")
        self.credentials = {"username_or_email":self.uname,"password":self.pword, "remember_me":"1"}
        self.loginguy = self.s.post("https://bwitter.me/sessions", data=self.credentials)
        #print (self.loginguy.text)
        #print (self.s.cookies.get_dict())
    def post(self):
        self.context = input("What are you doing? Say it: ")
        self.topost = {"content":self.context}
        self.contextguy = self.s.post("https://bwitter.me/bweet", data = self.topost)
        #print (self.contextguy.text)

    def commands(self):
        self.command = input("Type login to login, post to post(must login), x to exit: ")
    
bwitter = Bwitter()
quit = False
while not quit:
    bwitter.commands()
    try:
        if bwitter.command == "login":
            bwitter.login()
        elif bwitter.command == "post":
            if not bwitter.uname and not bwitter.pword:
                bwitter.login()
            else:
                bwitter.post()
        elif bwitter.command == "x":
            quit = True
    except:
        print ("Command not found")
