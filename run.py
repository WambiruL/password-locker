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
