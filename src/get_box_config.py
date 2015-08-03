__author__ = 'snalam200'
import telnetlib
import socket
import sys
import time
#from src.scratch.test import login_secure as login_secure_test


class CienaConfig(object):
    def __init__(self, ip_fqdn, config_txt=''):
        self.ip_fqdn = ip_fqdn.strip()
        self.config_txt = config_txt


def check_prompt(prompt_list, prompt_read):
    success = False
    for prompt in prompt_list:
        if prompt in prompt_read:
            success = True
    return success


def get_configs(ciena_config, tn):
    f = open('current_config.txt', 'w')
    time.sleep(3)
    tn.read_until(b'> ')
    tn.write("system shell set global-more off" + "\n")
    time.sleep(3)
    tn.read_until(b'> ')
    tn.write("config show\n")
    ciena_config.config_txt = tn.read_until(b'> ')
    f.write(ciena_config.config_txt)
    time.sleep(5)
    tn.write("system shell set global-more on" + "\n")
    time.sleep(3)
    tn.write("exit\n")
    f.close()
    tn.close()


def login_secure():
    tn = telnetlib.Telnet()
    #96.123.111.39,  96.122.163.29
    ip_fqdn = raw_input("Enter IP address or FQDN:")
    current_config = CienaConfig(ip_fqdn)
    retry = 2

    for attempt in range(0, retry):
        try:
            tn.open(current_config.ip_fqdn, 23, 300)
            #tn.open('96.122.163.29', 23, 300)
        except Exception, ex:
            print "Caught error {}".format(ex)
            sys.exit(1)
        else:
            login_str_a = 'username: '
            login_str_b = 'login: '
            password_str = 'assword: '

            user_prompt = tn.read_until(login_str_a or login_str_b, 5)
            if check_prompt([login_str_a, login_str_b], user_prompt)is True:
                print user_prompt
                tn.write(raw_input().strip() + '\n')
            else:
                print "Couldn't locate username prompt. Telnet session not available."
                tn.close()
                continue

            pass_prompt = tn.read_until("assword: ")
            if check_prompt([password_str], pass_prompt)is True:
                print pass_prompt
                tn.write(raw_input().strip() + '\n')
            else:
                print "Couldn't locate password prompt. This Telnet session is not available."
                tn.close()
                continue
            time.sleep(2)
            read_txt = tn.read_until(b'> ')
            if 'username' not in read_txt:
                get_configs(current_config, tn)
                break
            else:
                print "Incorrect username/password "
                tn.close()
                if attempt == 0:
                    continue
                else:
                    sys.exit(1)


if __name__ == "__main__":
    login_secure()

