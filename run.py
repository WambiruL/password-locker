#!/usr/bin/python3.6
from passlock import User,Credentials

def create_new_user(username,password):
    """
    Function to create a new user with a username and password
    """

    new_user=User(username,password)
    return new_user

def save_user(user):
    """
    Function to save new user
    """

    user.save_user()

def display_user():
    """
    Function to display existing user
    """

    return User.display_user()

def login_user(username,password):
    """
    Function that checks whether a user exists and then login the user
    """

    check_user=Credentials.user_exist(username,password)
    return check_user

def create_new_credentials(account,username,password):
    """
    Function to save credentials to credentials list
    """
    new_credential= Credentials(account,username,password)
    return new_credential

def save_credentials(credentials):
    """
    Function to save credentials to credentials list
    """
    credentials.save_credentials()

def display_accounts_details():
    """
    Function that returns all saved contacts
    """

    return Credentials.display_credentials()

def delete_credential(credentials):
    """
    Function to delete a Credentials from credentials list
    """
    credentials.delete_credentials()

def find_credentials(account):
    """
    Function that finds a Credentials by an account name and returns the Credentials that belong to that account
    """
    return Credentials.find_credentials(account)

def check_credentials(account):
    """
    Function that check if a Credentials exists with that account name and return true or false
    """
    return Credentials.if_credential_exist(account)

def generate_Password():
    '''
    generates a random password for the user.
    '''
    auto_password=Credentials.generatePassword()
    return auto_password