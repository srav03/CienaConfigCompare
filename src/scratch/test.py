__author__ = 'snalam200'
import telnetlib

def login_secure():
    tn = telnetlib.Telnet()
    print "Enter IP address or FQDN:"
    ip_fqdn = raw_input()
    tn.open(ip_fqdn, 23, 300)
    f = open('current_config1.txt', 'w')
    print tn.read_until("username: " or "login: ")
    tn.write(raw_input() + '\n')
    print tn.read_until("password: " or "Password:")
    tn.write(raw_input() + '\n')
    #time.sleep(1)
    tn.read_until('> ')
    tn.write("system shell set global-more off\r")
    #time.sleep(1)
    tn.read_until('> ')
    tn.write("config show \r\n")
    '''data = ''
    while data.find('>') == -1:
        data += tn.read_all()
    f.write(data)
    '''
    f.write(tn.read_until('>'))
    f.close()
    #tn.read_until('> ')
    time.sleep(2)
    tn.write("system shell set global-more on" + "\r\n")
    #time.sleep(1)
    print tn.read_until('> ')
    tn.write("exit\r\n")
    print tn.read_until('.', 5)
    tn.close()