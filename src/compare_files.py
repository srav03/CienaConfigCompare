__author__ = 'snalam200'
import difflib


class CompareFiles(object):
    def __init__(self, text1, text2, cmp_text=''):
        self.text1 = text1
        self.text2 = text2
        self.cmp_text = cmp_text


def comparison(text1, text2):
    open(text1, 'r').readlines()
    open(text2, 'r').readlines()
    diff_object = difflib.HtmlDiff()
    comp_file = open('compare_file.html', 'w')
    comapre_textfiles = CompareFiles(text1, text2)
    comp_file.write(diff_object.make_file(comapre_textfiles.text1, comapre_textfiles.text2))
    text1.close()
    text2.close()

if __name__ == "__main__":
    comparison('current_config.txt', 'actual.txt')







