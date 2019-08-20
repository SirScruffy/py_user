import os
#import mysql.connector

def eingabe():

    user = str(input('Geben Sie bitte den Accountnamen ein.\n'))
    password = str(input('Geben Sie bitte das Passwort  ein.\n'))
    #group = str(input('Geben Sie bitte die Gruppe an, zu der der User gehoert.\n'))

    add_user(user,password)
    return(user,password)


def add_user(user,password):
    os.system('useradd -d /home/'+user+' -m '+ user +' -p $(openssl passwd -1 '+ password +')')



(password, user) = eingabe()