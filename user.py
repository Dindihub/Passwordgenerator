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
    def find_user_by_name(cls,user_name):
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
        return cls.user_list





