class Credentials:
    '''
    Class that creates new instances of credentials account
    ''' 
    account=[]
    def __init__(self,account_name,account_username,account_password_):
        '''
        defines properties for object self
        ''' 
        self.account_name=account_name
        self.account_username=account_username
        self.account_password_=account_password_

    def save_account(self):

        '''
        save_account method saves new instances of credentials
        ''' 

        Credentials.account.append(self)

    def delete_account(self):
        '''
        delete_account method deletes credentials
        '''
        Credentials.account.remove(self)

    @classmethod
    def find_account_name_account(cls,account_name):
        '''
        Method returns list of accounts
        '''

        for account in cls.accounts:
            if account.account_name == account_name:
                return cls.accounts