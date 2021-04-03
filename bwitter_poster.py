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
        print (self.loginguy.text)
        #print (self.s.cookies.get_dict())
        self.context = input("What are you doing? Say it: ")
        self.topost = {"content":self.context}
        self.contextguy = self.s.post("https://bwitter.me/bweet", data = self.topost)
        print (self.contextguy.text)
    
bwitter = Bwitter()
bwitter.login()

