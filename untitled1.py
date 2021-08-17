# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 13:07:23 2021

@author: stephen.vickery
"""
from cryptography.fernet import Fernet
import os.path
from os import path
import csv
from csv import DictWriter


#establish whether user file exists already or not
does_user_file_exist = path.exists('C:/Users/stephen.vickery/Desktop/userfile.csv')

#create user file with default admin user if not already created
filename = 'C:/Users/stephen.vickery/Desktop/userfile.csv'

if does_user_file_exist != True:
    with open(filename,'w', newline='') as userfile:
        user_file_header =['user','active','admin','password']
        writer = csv.DictWriter(userfile, fieldnames=user_file_header)
        writer.writeheader()
        writer.writerow({'user':'Admin','active':'Y','admin':'Y','password':'test'})
        userfile.close

#create list of dictonaries of users from CSV

with open(filename, "r") as userfile:
    reader = csv.DictReader(userfile)
    account_holder_list = list(reader)
    userfile.close
print (account_holder_list)


# password encryption library


# functions for password encryption
def genewrite_key():
    key= Fernet.generate_key()
    with open("pass.key","wb") as key_file:
        key_file.write(key)
        
def get_key():
    key= open("pass.key","rb").read()
    return key


#creates new user and adds to library of dicotnaries
new_account_holder_name = input('What is the name of the new account holder?')
# encrypts password provided by user
genewrite_key()
new_account_holder_password = input('Please enter the users password?').encode()
key= get_key()
a= Fernet(key)
encrypted_password= a.encrypt(new_account_holder_password)
user_file_entry = {'user':new_account_holder_name,'active':'Y','admin':'N','password':encrypted_password}
account_holder_list.append(user_file_entry)
print (account_holder_list)


user_file_header =['user','active','admin','password']


with open(filename,'a') as userfile:
    dictwriter_object = DictWriter(userfile, fieldnames=user_file_header)
    dictwriter_object.writerow(user_file_entry)
    userfile.close
    

