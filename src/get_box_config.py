__author__ = 'snalam200'
import telnetlib
import sys

class CurrentConfig(object):
    def __init__(self):
        pass


def login_secure():
    tn = telnetlib.Telnet()
    print "Enter IP address or FQDN:"
    ip_fqdn = raw_input()
    tn.open(ip_fqdn)
    print tn.read_until("username: ")
    tn.write(raw_input("Enter username") + '\r\n')
    #tn.read_until("password: ")
    print tn.read_until("password: ")
    #tn.write(password + "\n")
    tn.write(raw_input("Enter pass") + '\r\n')
    #print tn.read_all()
    tn.write("terminal length 0" + "\r\n")
    print tn.read_all()
    tn.write("config show\f\n")
    print tn.read_all()
    tn.close()



