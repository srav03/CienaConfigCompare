__author__ = 'snalam200'
import telnetlib



tn = telnetlib.Telnet()
print "Enter IP address or FQDN:"
    #96.123.111.39,  96.122.163.29
ip_fqdn = raw_input()
tn.open(ip_fqdn)
if 'username' in tn.read_all():
    print "works"
else:
    print "Nah"

    #print tn.read_until("username: ")
    tn.write(raw_input("Enter username") + '\r\n')
    #print tn.read_until("password: ")
    tn.write(raw_input("Enter pass") + '\r\n')

    f = open('current_config.txt', 'w')
    tn.write("system shell set global-more off" + "\r\n")
    tn.write("config show\r\n")
    f.write(tn.read_all())
    tn.write("system shell set global-more on" + "\r\n")
    tn.write("exit\r\n")
    f.close()
    tn.close()


def login_secure():
    tn = telnetlib.Telnet()
    print "Enter IP address or FQDN:"
    #96.123.111.39,  96.122.163.29
    ip_fqdn = raw_input()
    tn.open(ip_fqdn)
    for i in range(0, 3):
        if 'username' in tn.read_all():
            tn.write(raw_input("Enter username") + '\r\n')
            tn.write(raw_input("Enter pass") + '\r\n')
            if 'username' not in tn.read_all():
                f = open('current_config.txt', 'w')
                tn.write("system shell set global-more off" + "\r\n")
                tn.write("config show\r\n")
                f.write(tn.read_all())
                tn.write("system shell set global-more on" + "\r\n")
                tn.write("exit\r\n")
                f.close()
                tn.close()
                break
    print "You have entered Incorrect username/password thrice. Please try again"
