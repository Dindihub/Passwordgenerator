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

def save_account(self):
    return Credentials.save_account()

def delete_account(self):
    return Credentials.delete_account()

def find_account_by_name(cls,account_name):
    return Credentials.find_account_by_name()
def generate_password(self):
    return Credentials.generate_password()

def main():
    '''
    Function running the Password Manager app
    '''

    print('''Welcome to Password Manager \n
Use these short codes to get around''')

    while True:
        '''
        Loop that is running the entire application
        '''

        print('''   Short codes:
        CU - create a Password Manager account \n
        DU - display names of current Password Manager users \n
        EX - exit the Password Manager account''')

    
        short_code = input().lower()

        if short_code == 'CU':
            '''
            Creating a Password Manager account
            '''

            print("\n")
            print("New Password Manager Account")
            print("-"*10)

            print("User name ...")
            user_name = input()

            print("Password ...")
            user_password = input()

            save_user(create_user(user_name, user_password))

            print("\n")
            print(f"{user_name} welcome to Password Manager")
            print("\n")

        elif short_code == 'DU':
            '''
            Display the names of the current users 
            '''

            if display_user():
                print("\n")
                print("Here are the current users of Password Manager")
                print("*"*10)

                for user in display_user():
                    print(f"{user.user_name}")
                    print("*"*10)
            else:
                print("\n")
                print("Password Manager has no current user.\n  Be the first user :)")
                print("\n")

        elif short_code == 'EX':
            '''
            Exit Password Manager
            '''
            print("\n")
            print("Bye .....")

            break

        else:
            print("\n")
            print(f'''Come again, what's {short_code}?
    Please use the short codes''')
            print("\n")

    

if __name__ == '__main__':
    main()
