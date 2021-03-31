# bwitter api thingy

import requests

class Bwitter():
    def __init__(self):
        self.logincookies = {}
        self.session = requests.Session()
        self.phpsess = ""

    def login(self):
        self.uname = input("Enter your username: ")
        self.pword = input("Enter your password: ")
        self.credentials = {"username_or_email":self.uname,"password":self.pword}
        self.loginguy = self.session.post("https://bwitter.me/sessions/", data=self.credentials)
        print (self.session.cookies.get_dict())
        self.logincookies = self.session.cookies.get_dict()
    
    def post(self):
        self.login2 = {"PHPSESSID":""}
        self.context = input("What are you doing? Say it: ")
        self.topost = {"content":self.context}
        self.contextguy = requests.post("https://bwitter.me/bweet", data = self.topost, cookies = self.login2)
        print (self.contextguy.text)
    
bwitter = Bwitter()
bwitter.post()
