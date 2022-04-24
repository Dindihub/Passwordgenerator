import string
from random import *
from user import User
from user import Credentials

def create_user( user_name,user_password):
    newuser= User(user_name,user_password)
    return newuser

def save_user(user):
    return User.save_user()

def delete_user(user):
     return User.delete_user()

def find_by_name(cls,user_name):
    return User.find_by_name()

def display_user(cls,name):
    return User.display_user()

def save_account(self):
    return Credentials.save_account()

def delete_account(self):
    return Credentials.delete_account()

def display_account(cls):
    return Credentials.display_account()

def main():
        while true:
        print("Welcome to password manager write SU or LG to start")
        print("SU -or- LG")
        option= input()
        if option == "SU":
            print("create ")
