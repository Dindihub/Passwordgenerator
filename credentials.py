
import string
from random import choice
class Credentials:
    '''
    Class that creates new instances of credentials account
    ''' 
    accounts=[]
    def __init__(self,account_name,account_username,account_password):
        '''
        defines properties for object self
        ''' 
        self.account_name=account_name
        self.account_username=account_username
        self.account_password=account_password

    def save_account(self):

        '''
        save_account method saves new instances of credentials
        ''' 
        
        Credentials.accounts.append(self)

    def delete_account(self):
        '''
        delete_account method deletes credentials
        '''
        Credentials.accounts.remove(self)

    @classmethod
    def find_account(cls,account_name):
        '''
        Method returns list of accounts
        '''

        for account in cls.accounts:
            if account.account_name == account_name:
                return account

    @classmethod
    def display_account(cls):
        '''
        method returns list of account
        '''     
        return cls.accounts

    @classmethod
    def generate_password(cls):
        '''
        Method that generates a random alphanumeric password
        '''
        # Length of the generated password
        size = 8
        # Generate random alphanumeric 
        alphanum = string.ascii_uppercase + string.digits + string.ascii_lowercase
        # Create password
        password = ''.join( choice(alphanum) for num in range(size) )
        
        return password