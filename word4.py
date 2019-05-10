# -*- coding: utf-8 -*-
import logging

##init logger
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler("krds_hamaster_log_monitor.log")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class word4():
    def __init__(self):
        self.data = []
        with open("4word.all.txt", 'r') as f:
            for line in f.readlines():
                self.data.append(line.decode('utf8').strip())

        if len(self.data) == 0:
            logger.error("init error: data file read error!")
        else:
            logger.info("%d word4 loaded..." % len(self.data))

    # find word by one character
    def searchByChar(self, char, pos):
        ret = []
        if pos not in [0, 1, 2, 3, 4]:
            print "pos should in [0 1 2 3 4]"
            return ret

        for word in self.data:
            if pos == 0 and char in word:
                ret.append(word)
            elif char == word[pos - 1]:
                ret.append(word)
            else:
                pass
        return ret

    # find word by tow characters
    def searchBy2Char(self, ch1, ch2):
        ret = []
        for word in self.data:
            if ch1 in word and ch2 in word:
                ret.append(word)
        return ret

    # find words with a string (words must be made up by characters in string)
    def findByString(self, str):
        ret = []
        for char in str:
            w = self.searchByChar(char, 0)
            for word in w:
                if self.wordInString(word, str) and word not in ret:
                    ret.append(word)
                    break
        #find left
        list_str=list(str)
        for word in ret:
            for char in word:
                try:
                    list_str.remove(char)
                except:
                    pass

        print "left chars: %d " % len(list_str)
        return ret

    # if 4 characters all in a string
    def wordInString(self, word, string):
        list_str = list(string)
        for char in word:
            if char not in list_str:
                return False
            else:
                list_str.remove(char)
        return True


def main():
    w4 = word4()
    print "> test searchByChar:"
    list = w4.searchByChar(u'刘', 3)
    for i in list:
        print i
    print "> test searchBy2Char:"
    list = w4.searchBy2Char(u'大', u'鬼')
    for i in list:
        print i
    print "> test wordInString:"
    print w4.wordInString(u"长风破浪",u'长阿塞阀赛风风奥赛法赛法赛法赛安防破阿塞阀赛风浪')
    print w4.wordInString(u"大大小小", u'大大小奥赛法赛法赛风')
    print "> test findByString:"
    list = w4.findByString(u'人小鬼大擘两分星长风破浪食饥息劳安国富民')
    for i in list:
        print i


if __name__ == "__main__":
    main()
