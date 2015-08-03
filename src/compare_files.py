__author__ = 'snalam200'
import difflib
import sys
import get_box_config


class CompareFiles(object):
    def __init__(self, file_name1, file_name2, comp_html=''):
        self.text1 = open(file_name1, 'r').readlines()
        self.text2 = open(file_name2, 'r').readlines()
        self.cmp_text = comp_html

    def compare(self, desktop_path):
        diff_object = difflib.HtmlDiff()
        try:
            comp_file = open(desktop_path+'compare_file.html', 'w')
        except IOError:
            print "Incorrect NT-Login ID. Please enter as it is in your C:\\Users\\xxxxxx"
            sys.exit(1)
        comp_file.write(diff_object.make_file(self.text1, self.text2))
        comp_file.close()


if __name__ == "__main__":
    get_box_config.login_secure()
    nt_login_id = raw_input("Enter your NT-Login ID:").strip()
    desktop_path = 'C:\\Users\\'+nt_login_id+'\\Desktop\\'
    CompareFiles('current_config.txt', desktop_path+'actual.txt').compare(desktop_path)


