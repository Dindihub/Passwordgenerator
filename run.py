#!/usr/bin/env python3.8
import string
from random import *

from click import password_option
from user import User
from credentials import Credentials

def create_user( user_name,user_password):
    newuser= User(user_name,user_password)
    return newuser

def save_user(user):
    return User.save_user(user)

def delete_user(user):
     return User.delete_user()

def find_user_by_name(cls,user_name):
    return User.find_user_by_name()

def display_user():
    return User.display_user()

def user_log_in(user_name, user_password):
    log_in = User(user_name, user_password)
    if log_in != False:
        return User(user_name, user_password)

def create_account( account_name,account_username,account_password):
    newaccount= Credentials(account_name,account_username,account_password)
    return newaccount

def save_account(account):
    return Credentials.save_account(account)
def display_account():   
        return Credentials.display_account()  

def delete_account(account_name):
    return Credentials.delete_account(account_name)

def find_account(account_name):
    return Credentials.find_account(account_name)

def generate_password():
    return Credentials.generate_password()

def main():

    print("Welcome to Password manager")
    print("Pick CU to create a new user account or LG to log in")
    print("\n")

    option=input().upper()

    if option == "CU":
        print("Create user account")
        print('*'*10)
        print("Enter your user name...")
        user_name=input()
        while True : 
            print("Choose password type ...Enter own password -OP- or Generate password -GP- ")
            password_option=input()
            if password_option == "OP":
                print("Enter your password")
                user_password=input()
                print('*'*10)
                break
            elif password_option == "GP":
                user_password = generate_password()
                break
            else:
                print("Invalid choice")
        # print("Enter your password...")
        # user_password=input()
        # print('*'*10)
        save_user(create_user(user_name,user_password))
        print("Your account has been successfully created ")
        print(f"name:{user_name},password:{user_password}")
        print('*'*10)
    elif option == "LG":
        print("Enter username")
        user_name = input()
        print("Enter password")
        user_password= input()
        log_in = user_log_in(user_name,user_password)

    while True:
        # print("CC - create credential\n, D - display credential\n, FC-finedential\n,EX-exit credential account")
        print (" Short-codes for navigation:\n CC - Create a new account\n LG - Log in to Application \n DC - Display account\n FC - Find account\n DLT - Delete credential \n EX - Exit application")
        print('*'*10)
        option=input().upper()
        if  option == "CC":
            print("Create new credentials")
            print('*'*10)
            print("Enter your account name...")
            account_name=input()
            print("Enter your account username...")
            account_username=input()
            while True : 
                print("Choose password type ...Enter own password -OP- or Generate password -GP- ")
                password_option=input()
                if password_option == "OP":
                    print("Enter your password")
                    account_password=input()
                    break
                elif password_option == "GP":
                    account_password = generate_password()
                    break
                else:
                    print("Invalid choice")
            # print("Enter your account password...")
            # account_password=input()
            print('*'*10)
            save_account(create_account(account_name,account_username,account_password))
            print("Your account has been successfully created")
            print(f"Account Name:{account_name}\n Account Username:{account_username} \n Account Password:{account_password}")
            print('*'*10)
            print('\n')
        elif option == "DC":
                if display_account():
                    print("Display your credentials")
                    for credentials in display_account():
                        print(f"Account Name: {credentials.account_name}\n Account Username: {credentials.account_username} \n Account Password: {credentials.account_password}")
                        print('*'*10)
                        print('\n')

        
                else:
                    print('\n')
                    print("You don't seem to have any credentials saved yet")
                    print('\n')
                    print('*'*10)
                    print('\n')

        elif option == "FC":
            print("Find a credential by entering the account name")
            find_credential=input()
            if find_account(find_credential):
                find_credential=find_account(find_credential)
                print(f"Account Name: {find_credential.account_name}")
                print(f"Account userName: {find_credential.account_username}")
                print(f"Account Password: {find_credential.account_password}")
                print('*'*10)
                print('\n')
            else:
                print("Account does not exist")
                print('*'*10)

        elif option == "DLT":
            print("Delete credential by account name")
            find_credential=input()
            if find_account(find_credential):
                find_credential=find_account(find_credential)
                find_credential.delete_account()
                print(f"Account Name:{find_credential.account_name} deleted successfully")
                print('*'*10)
            else:
                print('\n')
                print("The credential does not exist")
                print('*'*10)
                print('\n')

        elif option == "EX":
            print("Bye!")
            break

        else:
            print("Please pick the correct codes")

         

if __name__ == '__main__':
    main()
   
    
    