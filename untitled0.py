# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 15:46:38 2021

@author: stephen.vickery
"""

from cryptography.fernet import Fernet

def genewrite_key():
    key= Fernet.generate_key()
    with open("pass.key","wb") as key_file:
        key_file.write(key)
        
def get_key():
    key= open("pass.key","rb").read()
    return key

genewrite_key()
msg=input("Enter the message you want to ENCRYPT : ")
text=msg.encode()
key= get_key()
print(key)
a= Fernet(key)
encrypted_msg= a.encrypt(text)


decoded_text = a.decrypt(encrypted_msg)

print (decoded_text)
if msg == decoded_text:
    print('True')
    
print(decoded_text)
