import os
from mysql.connector import Error
import MySQLdb
import time


def eingabe():
    #clue is in the name.

    host = str(input('Geben Sie bitte den Host ein z.B. localhost.\n'))
    db_user = str(input('Geben Sie bitte den Accountnamen ein.\n'))
    database = str(input('Geben Sie bitte die Benutzerdatenbank ein.\n'))
    # password = str(input('Geben Sie bitte das Passwort  ein.\n'))

    db_connect(host, db_user, database)


def add_user(user, password):
    #Anlegen des Benutzers
    os.system('useradd -d /home/' + user + ' -m ' + user + ' -p $(openssl passwd -1 ' + password + ')')

    date = time.strftime('%Y%m%d')
    system_time = time.strftime('%H%M%S')
    logfile = open('logfile.txt', 'a+')
    logfile.write('Der Benutzer',user,'wurde am',date,'um',system_time,'angelegt.')
    logfile.close()


def db_connect(host, db_user, database):
    #Aufbau der Verbindung zur Datenbank sowie Ueberpruefung der Eingabe

    try:
        connection = MySQLdb.connect(host=host,user=db_user,)


        if connection.is_connected():
            print("Verbindung erfolgreich.")
            cursor = connection.cursor()
            cursor.execute("use",database,";")
            userlist = cursor.execute('select * from user_tb')
            cursor.close()
            connection.close()

            #print(userlist)

    except Error as error:
        print("Fehler bei der der Verbindung zur MySQL Datenbank: ", error)
        print("Geben Sie die Daten neu ein.")
        eingabe()

    cleaner(userlist)


def cleaner(userlist):
    #Hier wird der Username und das Passwort aus userliste ausgelesen
    #username an zweiter Stelle und password an dritter
    #dies klappt nur, da meine Test Datenbank so aufgebaut ist.
    user = userlist[1]
    password = userlist[2]

    #zum Schluss werden die Daten an die add_user Funktion Uebergeben
    add_user(user,password)


(host, db_user, database) = eingabe()
