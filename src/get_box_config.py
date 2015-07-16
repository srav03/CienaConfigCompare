__author__ = 'snalam200'
import telnetlib
import sys

class CurrentConfig(object):
    def __init__(self):
        pass


def login_secure():
    tn = telnetlib.Telnet()
    print "Enter IP address or FQDN:"
    #96.123.111.39,  96.122.163.29
    ip_fqdn = raw_input()
    tn.open(ip_fqdn)
    f = open('current_config.txt', 'w')
    #print tn.read_until("username: ")
    tn.write(raw_input("Enter username") + '\r\n')
    #print tn.read_until("password: ")
    tn.write(raw_input("Enter pass") + '\r\n')
    tn.write("system shell set global-more off" + "\r\n")
    tn.write("config show\r\n")
    f.write(tn.read_all())
    tn.write("system shell set global-more on" + "\r\n")
    tn.write("exit\r\n")
    f.close()
    tn.close()



