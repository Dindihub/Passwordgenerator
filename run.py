#!/usr/bin/env python3.8
import string
from random import *
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
    log_in = User.log_in(user_name, user_password)
    if log_in != False:
        return User.log_in(user_name, user_password)

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

#     print('''   Short codes:
#         CU - create a Password Manager account \n
#         DU - display names of current Password Manager users \n
#         LG- Log into password manager account
#         CC- Create credentail
#         DC - display credentials for the logged in user\n
#         CG - storing a credential with a generated password\n
#         EX - exit the Password Manager account''')

    print("Welcome to Password manager")
    print("Pick CU to create a new user account or LG to log in")
    print("\n")

    option=input().upper()
    if option == "CU":
        print("Create user account")
        print('*'*10)
        print("Enter your user name...")
        user_name=input()
        print("Enter your password...")
        user_password=input()
        save_user(create_user(user_name,user_password))
        print("Your account has been successfully created ")
        print(f"name:{user_name},password:{user_password}")

    while True:
        # print("CC - create credential\n, D - display credential\n, FC-finedential\n,EX-exit credential account")
        print ("Pick CC to create a new account\n DC to display account\n and FC to find account\n DLT to delete credential \n EX to exit application")
        
        option=input().upper()
        if  option == "CC":
            print("Create new credentails")
            print("Enter your account name...")
            account_name=input()
            print("Enter your account username...")
            account_username=input()
            print("Enter your account password...")
            account_password=input()
            save_account(create_account(account_name,account_username,account_password))
            print("Your account has been successfully created")
            print(f"Account Name:{account_name}\n Account Username:{account_username} \n Account Password:{account_password}")
            
        elif option == "DC":
                if display_account():
                    print("Display your credentials")
                    for credentials in display_account():
                        print(f"Account Name: {credentials.account_name}\n Account Username: {credentials.account_username} \n Account Password: {credentials.account_password}")
                        print('\n')
                else:
                    print('\n')
                    print("You don't seem to have any credentials saved yet")
                    print('\n') 
        elif option == "FC":
            print("Find a credential by entering the account name")
            find_credential=input()
            if find_account(find_credential):
                find_credential=find_account(find_credential)
                print(f"Account Name: {find_credential.account_name}")
            else:
                print("Account does not exist")

        elif option == "DLT":
            print("Delete credential by account name")
            find_credential=input()
            if find_account(find_credential):
                find_credential=find_account(find_credential)
                find_credential.delete_account()
                print(f"Account Name:{find_credential.account_name} deleted successfully")
            else:
                print("The credential does not exist")

        elif option == "EX":
            print("Bye!")
            break
        else:
            print("Please pick the correct codes")

         

if __name__ == '__main__':
    main()
   
    
    