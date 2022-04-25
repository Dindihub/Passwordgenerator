# Password Manager
## By Sandra Dindi
## Description
This App allows a user to generate and store passwords for various accounts. A user navigates through the application using short codes on the terminal. <br/>
The short codes are:
* CU - Create Password user account
* LG - Login as a user with existing account
* DU - Display the names of the current Password Manager users
* CC - Create a Password Credential account
* DC - Display Password credentials for the logged in user
* CG - Storing a credential with a generated password
* DLT- Delete a credential account
* EX - Exit for Password manager account and also exit the terminal app
## User Stories
As a user I would like:
* To create an account with my details - log in and password
* Store my existing login credentials
* Generate a password for a new credential
## Specifications
| Behavior        | Input           | Outcome  |
| ------------- |:-------------:| -----:|
| Create an account | User Name : Jane <br/> Password : Doe | An account is created |
| Display account names | N/A | Display a list of user names for Password manager accounts |
| Log into an account | User Name : Jane <br/> Password : Doe| Log into the users account |
| Store existing log in credential | Account : Github <br/> Password : doe1 | Create and save the user's credentials | 
| Display a specific users credentials | N/A | List of the user's credentials | 
| Generate a password for a new credential | Account : Password Manager | Generate a password for the user. <br/> Create and save the user's credential with the generated password | 
| Log out | N/A | Log out of Password Manager account |

## Setup/Installation Requirements
* Clone [this repository](git@github.com:Dindihub/Passwordgenerator.git) and run the `.\run.py` file

## Known Bugs
No known bugs
## Technologies Used
- Python3.8
### License
MIT (c) 2022 **[Sandra Dindi](https://github.com/Dindihub/Passwordgenerator)**

