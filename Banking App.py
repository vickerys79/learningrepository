# -*- coding: utf-8 -*-
"""
Steve's banking app

Libraries used in the application
"""
# password encryption library
from cryptography.fernet import Fernet
# used for csv manipulation
import os.path
from os import path
import csv
from csv import DictWriter

"""
Steve's banking app

Catalogue of functions used in the application

"""

# functions for password encryption
def genewrite_key():
    key= Fernet.generate_key()
    with open("pass.key","wb") as key_file:
        key_file.write(key)
        
def get_key():
    key= open("pass.key","rb").read()
    return key

# define admin menu choices and actions
def admin_menu():
    print ('Please choose from the following options')
    print ('1. Create New Account Holder')
    print ('2. Create New Account')
    print ('3. Print Account Holders')
    print ('4. Print Account Holders / Accounts')
    print ('5. Quit')
    admin_menu_choice = input('What is your choice?')
    if admin_menu_choice == '1':
        add_new_account_holder()
    elif admin_menu_choice == '2':
        add_new_account()
    elif admin_menu_choice == '3':
        print_account_holders()
        admin_menu()
    elif admin_menu_choice == '4':
        print_account_holders_accounts()
        admin_menu()
    elif admin_menu_choice == '5':
        global is_session_on
        is_session_on = False
                
# function to add new account holder
def add_new_account_holder():
    new_account_holder_name = input('What is the name of the new account holder?')
# encrypts password provided by user
    genewrite_key()
    new_account_holder_password = input('Please enter the users password?').encode()
    key= get_key()
    a= Fernet(key)
    encrypted_password= a.encrypt(new_account_holder_password)
# adds account holder to list of dictonaries
    user_file_entry = {'user':new_account_holder_name,'active':'Y','admin':'N','password':encrypted_password}
    account_holder_list.append(user_file_entry)
    print_account_holders()
# adds account holder to account holder csv file
    user_file_header =['user','active','admin','password']
    with open(filename,'a', newline='') as userfile:
        dictwriter_object = DictWriter(userfile, fieldnames=user_file_header)
        dictwriter_object.writerow(user_file_entry)
        userfile.close
# returns to admin menu
    admin_menu()
    
# function to add new account for holder
def add_new_account():
    account_for_valid_user = False
    user_for_new_account = input('For what user are you wanting to create the account?')
    print_account_holders()
    for account_holder in account_holder_list:
        if account_holder['user'] == user_for_new_account:
            account_for_valid_user = True
    if account_for_valid_user == True:
        print ('What type of account are you wanting to create?')    
        print ('1. Savings Account')
        print ('2. Current Account')
        print ('3. Go back to admin menu')
        new_account_type = input ('Please select an account?')
        if new_account_type == '1':
            account_list.append({'user':user_for_new_account,'active':'Y','account_type':'Savings'})
            print_account_holders_accounts()
            admin_menu()
        elif new_account_type == '2':
            account_list.append({'user':user_for_new_account,'active':'Y','account_type':'Current'})
            print_account_holders_accounts()
            admin_menu()
        elif new_account_type == '3':
            admin_menu()
        else:
            print ('You have not picked a valid option please try again')
            add_new_account()
    elif account_for_valid_user == False:
        print ('Sorry this is not a valid user in our system, please try again')
        add_new_account()
    
    
# function to print all account holders   
def print_account_holders():
    print ('User'.ljust(15, ' '), ' | ', 'Active'.ljust(15, ' '), ' | ','Admin'.ljust(15, ' '))
    for account_holder in account_holder_list:
        if account_holder['active'] == 'Y':
            print (account_holder['user'].ljust(15, ' '), ' | ',account_holder['active'].ljust(15,' '), ' | ',account_holder['admin'].ljust(15,' '))
    
# function to print all accounts
def print_account_holders_accounts():
    print ('User'.ljust(15, ' '), ' | ', 'Active'.ljust(15, ' '), ' | ','Account Type'.ljust(15, ' '))
    for account in account_list:
        if account['active'] == 'Y':
            print (account['user'].ljust(15, ' '), ' | ',account['active'].ljust(15,' '), ' | ',account['account_type'].ljust(15,' '))

"""
Steve's banking app

Main Program 

"""

# define global variables    
is_session_on = True
is_customer = False
is_admin = False
valid_password = False

#establish whether user file exists already or not
does_user_file_exist = path.exists('C:/Users/stephen.vickery/Desktop/userfile.csv')

filename = 'C:/Users/stephen.vickery/Desktop/userfile.csv'
if does_user_file_exist != True:
    # encrypts Admin password
    genewrite_key()
    new_account_holder_password = ('test').encode()
    key= get_key()
    a= Fernet(key)
    encrypted_password= a.encrypt(new_account_holder_password)
#create user file with default admin user if not already created    
    with open(filename,'w', newline='') as userfile:
        user_file_header =['user','active','admin','password']
        writer = csv.DictWriter(userfile, fieldnames=user_file_header)
        writer.writeheader()
        writer.writerow({'user':'Admin','active':'Y','admin':'Y','password':encrypted_password})
        userfile.close

#create list of dictonaries of users from CSV
with open(filename, "r") as userfile:
    reader = csv.DictReader(userfile)
    account_holder_list = list(reader)
    userfile.close
    
print(account_holder_list)
    
# creates account list dictonary which is pre-populated with the system admin user current account
account_list = [{'user':'Admin','active':'Y','account_type':'Current'}]

# starts user session
while is_session_on is True:
    print ("Welcome to Steve's banking application.")
    current_user = input('What is your username?')
    user_password = input('What is your password?')
    
    # confirms whether user is valid or not
    for account_holder in account_holder_list:
        if is_customer == False and is_session_on == True:
            if account_holder['user'] == current_user:
                is_customer = True
                #decrypt password
                key= get_key()
                a= Fernet(key)
                decrypted_password = account_holder['password']
                decrypted_password = a.decrypt(decrypted_password)
                print(decrypted_password)
                print (user_password)
                if decrypted_password == user_password:
                    valid_password = True
    # checks to see whether user is an admin user or not
                    if account_holder['admin'] == 'Y':
                        is_admin = True
                        print ('You are now logged in as an Admin User')
                        admin_menu()
                    else:
                        print('Welcome to the app')
                
    if is_customer == False or valid_password == False:
        print ('Sorry logon credentials are incorrect, we will now exit you from the program')
        is_session_on = False

print("You are now exiting Steve's banking app, Goodbye")