
import unittest
from user import User
from credentials import Credentials
import string

'''
import User and Credentials class from class files
'''

class TestUser(unittest.TestCase):
    '''
    Testuser class defines test cases for user class
    '''
    def setUp(self):
        '''
        setup method to run before each test cases
        '''
        self.new_user = User("James","+254")
        self.new_account=Credentials("Twitter","Tim42","twitter254")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name,"James")
        self.assertEqual(self.new_user.user_password,"+254")
        self.assertEqual(self.new_account.account_name,"Twitter")
        self.assertEqual(self.new_account.account_username,"Tim42")
        self.assertEqual(self.new_account.account_password,"twitter254")


    def test_save_user(self):
            '''
            test_save_user test case to test if the user object is saved into
            the user_list
            '''
            self.new_user.save_user() # saving the new user
            self.assertGreater(len(User.user_list),0)

    def test_delete_user(self):
            '''
            test_delete_user to test if we can remove a user from our user list
            '''
            self.new_user.save_user()
            test_user = User("Test","user") # new user
            test_user.save_user()

            self.new_user.delete_user()# Deleting a user object
            self.assertGreater(len(User.user_list),0)

        
    def test_find_user_by_name(self):
            '''
            test to check if we can find a user by user name and display information
            '''

            self.new_user.save_user()
            test_user = User("Test","user") # new user
            test_user.save_user()

            found_user = User.find_user_by_name("Test")

            self.assertEqual(found_user.user_name,"Test")


    def test_save_account(self):
            '''
            test_save_accounts test case to test if the accounts object is saved into
            the credentials account list
            '''
            self.new_account.save_account() # saving the new account
            self.assertGreater(len(Credentials.accounts),0)

    def test_delete_account(self):
            '''
            test_delete_account to test if we can remove an account from accounts list
            '''
            self.new_account.save_account()
            test_account = Credentials("Twitter","Tim42", "twitter254") # new account
            test_account.save_account()

            self.new_account.delete_account()# Deleting a account object
            self.assertGreater(len(Credentials.accounts),0)

        
    def test_find_account(self):
                '''
                test to check if we can find an account by name of account and display information
                '''

                test_account = Credentials("Twitter","Tim42","twitter254") 
                test_account.save_account()
              
                found_account = Credentials.find_account("Twitter")

                self.assertEqual(found_account.account_name,"Twitter")


    def test_generate_password(self):
                '''
                Test method to test if a user can log into their credentials
                '''
        
                generated_password = self.new_account.generate_password()
                self.assertEqual(len(generated_password),8)   
    

if __name__ == '__main__':
    unittest.main()




 
       

    



 