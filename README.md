# Password Manager
## By Sandra Dindi
## Description
This is a Python application that allows a user to generate and store passwords for various accounts. The application runs on the terminal and the user navigates through the app by using short codes. <br/>
The short codes are:
* CU - create Password Locker account
* DU - display the names of the current Password Locker users
* CC - storing an existing log in credential
* DC - display credentials for the logged in user
* CG - storing a credential with a generated password
* EX - exit for Password Locker account and also exit the terminal app
## User Stories
As a user I would like:
* To create an account with my details - log in and password
* Store my existing login credentials
* Generate a password for a new credential
## Specifications
| Behavior        | Input           | Outcome  |
| ------------- |:-------------:| -----:|
| Create an account | User Name : John <br/> Password : doe | An account is created |
| Display account names | N/A | Display a list of user names for Password manager accounts |
| Log into an account | User Name : Mary <br/> Password : Jane | Log into the users account |
| Store existing log in credential | Account : Githib <br/> Password : doe1 | Create and save the user's credentials | 
| Display a specific users credentials | N/A | List of the user's credentials | 
| Generate a password for a new credential | Account : Password Manager | Generate a password for the user. <br/> Create and save the user's credential with the generated password | 
| Log out | N/A | Log out of Password Manager account |

## Setup/Installation Requirements
* Clone [this repository](git@github.com:Dindihub/Passwordgenerator.git) and run the `.\run.py` file.


## Known Bugs
No known bugs
## Technologies Used
- Python3.8
### License
MIT (c) 2020 **[Sandra Dindi](https://github.com/Dindihub/Passwordgenerator)**

