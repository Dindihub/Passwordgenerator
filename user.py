class User:
    '''
    class creates instance for user accounts
    '''
    user_list=[]
    def __init__(self,user_name,user_password):
        self.user_name=user_name
        self.user_password=user_password


    def save_user(self):

        '''
        save_user method saves user details into user_list
        '''

        User.user_list.append(self)

    def delete_user(self):

        '''
        delete_user method deletes a saved account from the user_list
        '''

        User.user_list.remove(self)


    @classmethod
    def find_by_name(cls,user_name):
        '''
        Method that takes in a name and returns a user info that matches that name.
        '''
        for user in cls.user_list:
            if user.user_name == user_name:
                return user

    @classmethod
    def display_user(cls):
        '''
        method returns list of users
        '''

        for user in cls.user_list:
            # if contact.phone_number == number:
                return cls.user_list



class Credentials:
    '''
    Class that creates new instances of credentials
    ''' 
    account=[]
    def __init__(self,account_name,account_username,account_password_):
        '''
        defines properties for objectself
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
    def display_account(cls,name):
        '''
        Method returns list of accounts
        '''

        for account in cls.accounts:
        
                return cls.accounts

