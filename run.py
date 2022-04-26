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
        print("CREATE USER ACCOUNT")
        print('*'*10)
        print("ENTER YOUR USERNAME...")
        user_name=input()
        while True : 
            print("To enter your own password use  -OP- or Generate new password -GP- ")
            password_option=input()
            if password_option == "OP":
                print("ENTER YOUR PASSWORD")
                user_password=input()
                print('*'*10)
                break
            elif password_option == "GP":
                user_password = generate_password()
                break
            else:
                print("Invalid choice!!!!!!. Please choose a short-code")
        # print("Enter your password...")
        # user_password=input()
        # print('*'*10)
        save_user(create_user(user_name,user_password))
        print("YOUR ACCOUNT HAS BEEN SUCCESSFULLY CREATED!")
        print(f"name:{user_name},password:{user_password}")
        print('*'*10)
    elif option == "LG":
        print("ENTER YOUR USERNAME")
        user_name = input()
        print('\n')
        print("ENTER YOUR PASSWORD")
        user_password= input()
        log_in = user_log_in(user_name,user_password)
        print('\n')

    while True:
        # print("CC - create credential\n, D - display credential\n, FC-finedential\n,EX-exit credential account")
        print (" Use these Short-codes to navigate through App :\n CC - Create a new account\n LG - Log in to Application \n DC - Display account\n FC - Find account\n DLT - Delete credential \n EX - Exit application")
        print('\n')
        print('*'*10)
        option=input().upper()
        if  option == "CC":
            print("CREATE NEW CREDENTIALS")
            print('*'*10)
            print("ENTER YOUR ACCOUNT NAME...")
            account_name=input()
            print("ENTER YOUR USERNAME...")
            account_username=input()
            while True : 
                print("To enter your own password use  -OP- or Generate new password -GP- ")
                password_option=input()
                if password_option == "OP":
                    print("ENTER YOUR PASSWORD")
                    account_password=input()
                    break
                elif password_option == "GP":
                    account_password = generate_password()
                    break
                else:
                    print('\n')
                    print("INVALID CHOICE")
                    print('\n')
            # print("Enter your account password...")
            # account_password=input()
            print('*'*10)
            save_account(create_account(account_name,account_username,account_password))
            print("YOUR ACCOUNT HAS BEEN SUCCESSFULLY CREATED")
            print(f"Account Name:{account_name}\n Account Username:{account_username} \n Account Password:{account_password}")
            print('*'*10)
            print('\n')
        elif option == "DC":
                if display_account():
                    print("DISPLAY YOUR CREDENTIALS")
                    for credentials in display_account():
                        print(f"Account Name: {credentials.account_name}\n Account Username: {credentials.account_username} \n Account Password: {credentials.account_password}")
                        print('*'*10)
                        print('\n')

        
                else:
                    print('\n')
                    print("YOU DO NOT SEEM TO HAVE AN ACCOUNT YET.TYPE CC TO CREATE ONE")
                    print('\n')
                    print('*'*10)
                    print('\n')

        elif option == "FC":
            print("FIND ACCOUNT BY ENTERING AN ACCOUNT NAME")
            find_credential=input()
            if find_account(find_credential):
                find_credential=find_account(find_credential)
                print(f"Account Name: {find_credential.account_name}")
                print(f"Account userName: {find_credential.account_username}")
                print(f"Account Password: {find_credential.account_password}")
                print('*'*10)
                print('\n')
            else:
                print('\n')
                print("ACCOUNT DOES NOT EXIST!")
                print('\n')
            

        elif option == "DLT":
            print("DELETE ACCOUNT BY ACCOUNT NAME")
            find_credential=input()
            if find_account(find_credential):
                find_credential=find_account(find_credential)
                find_credential.delete_account()
                print(f"Account Name:{find_credential.account_name} DELETED SUCCESSFULLY")
                print('*'*10)
            else:
                print('\n')
                print("THIS ACCOUNT DOES NOT EXIST")
                print('*'*10)
                print('\n')

        elif option == "EX":
            print("BYE!")
            break

        else:
            print('\n')
            print("PLEASE PICK THE RIGHT CODES")
            print('\n')

         

if __name__ == '__main__':
    main()
   
    
    