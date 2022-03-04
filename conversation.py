import os
import discord
import dotenv
import json
import random


#Test switch case

def january():
    return “January”

def february():

    return “February”

def march():

    return “march”

def april():

    return “April”

def may():

    return “may”

def june():

    return “June”

def july():

    return “July”

def august():

    return “august”

def september():

    return “September”

def october():

    return “October”

def november():

    return “November” 

def december():

    return “December”

def default():

    return “Incorrect month”

    

switcher = {

    0: ‘january’,

    1: ‘february’,

    2: ‘march’,

    3: ‘april’,

    4: ‘may’,

    5: ‘june’,

    6: ‘july’,

    7: ‘august’,

    8: ‘september’,

    9: ‘october’,

    10: ‘november’,

    11: ‘december’

    }

def month(monthOfYear):

    return switcher.get(monthOfYear, default)()

print(switch(1))

print(switch(0))