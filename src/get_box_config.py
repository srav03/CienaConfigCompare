__author__ = 'snalam200'
import telnetlib
import sys
import getpass


class CurrentConfig(object):
    def __init__(self):
        pass

    def login_secure(self):
        tn = telnetlib.Telnet()
        tn.read_until("login: ")
        password = getpass.getpass()
        if password:
            tn.read_until("Password: ")
            tn.write(password + "\n")

        tn.write("ls \n")
        tn.write("exit \n")
        print tn.read_all()



