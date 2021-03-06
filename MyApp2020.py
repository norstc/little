# this is a starter in 2020

# read the config file
# ref https://pymotw.com/3/configparser/

import os
import webbrowser
import autoit
import time
from configparser import ConfigParser
import subprocess
from tkinter import *  # notice the little t, it's T for python 2.
from tkinter import ttk

# get the config file
ConfigFile = "config.properties";
cfparser = ConfigParser()
cfparser.read(ConfigFile)
cfsec = cfparser.sections()

# SET WORK ENV
JENKINS_MAIN = cfparser['WORK_ENV']['JENKINS_MAIN']
JENKINS_EUOP_CLOUD = cfparser['WORK_ENV']['JENKINS_EUOP_CLOUD']
RDMS = cfparser['WORK_ENV']['RDMS']
TESTLINK = cfparser['WORK_ENV']['TESTLINK']
MANTIS = cfparser['WORK_ENV']['MANTIS']
GERRIT = cfparser['WORK_ENV']['GERRIT']

# SET POMP LOGIN INFO
POMP_RES_URL = cfparser['POMP_RES']['URL']
POMP_RES_USERNAME = cfparser['POMP_RES']['USERNAME']
POMP_RES_MOBILE = cfparser['POMP_RES']['MOBILE']
POMP_LABS_URL = cfparser['POMP_LABS']['URL']
POMP_LABS_USERNAME = cfparser['POMP_LABS']['USERNAME']
POMP_LABS_MOBILE = cfparser['POMP_LABS']['MOBILE']
POMP_204_URL = cfparser['POMP_204']['URL']
POMP_204_USERNAME = cfparser['POMP_204']['USERNAME']
POMP_204_MOBILE = cfparser['POMP_204']['MOBILE']
POMP_208_URL = cfparser['POMP_208']['URL']
POMP_208_USERNAME = cfparser['POMP_208']['USERNAME']
POMP_208_MOBILE = cfparser['POMP_208']['MOBILE']

# SET EUOP LOGIN INFO
EUOP_RES_URL = cfparser['EUOP_RES']['URL']
EUOP_RES_USERNAME = cfparser['EUOP_RES']['USERNAME']
EUOP_RES_MOBILE = cfparser['EUOP_RES']['MOBILE']
EUOP_LABS_URL = cfparser['EUOP_LABS']['URL']
EUOP_LABS_USERNAME = cfparser['EUOP_LABS']['USERNAME']
EUOP_LABS_MOBILE = cfparser['EUOP_LABS']['MOBILE']
EUOP_175_URL = cfparser['EUOP_175']['URL']
EUOP_175_USERNAME = cfparser['EUOP_175']['USERNAME']
EUOP_175_MOBILE = cfparser['EUOP_175']['MOBILE']
EUOP_181_URL = cfparser['EUOP_181']['URL']
EUOP_181_USERNAME = cfparser['EUOP_181']['USERNAME']
EUOP_181_MOBILE = cfparser['EUOP_181']['MOBILE']

for section_name in cfparser.sections():
    print('section: ', section_name)
    print(' options: ', cfparser.options(section_name))
    for name, value in cfparser.items(section_name):
        print(' {} -> {}'.format(name, value))
    print()

## browser
Firefox = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe "
#chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe %s"
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'


# CALL BATFILE
# subprocess
# need \\

# subprocess.call("C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe")

# CALL FIREFOX

# gui TKinter
# We'll use pack and frame to do the layout, if the UI is complicated, grid should be considers.
# For this simple app, pack is enough.


def say_hi():
    print("hi, there, we love python")

def open_firefox_default():
    subprocess.call(Firefox + " -no-remote " + "https://cn.bing.com/?ensearch=1&FORM=BEHPTB")

def open_chrome_default():
    os.system('taskkill /im chrome.exe')
    #os.system('start chrome "https://cn.bing.com/?ensearch=1&FORM=BEHPTB" ' ) 这个会打开那个广告网页
    #subprocess.call(Chrome + JENKINS_MAIN + " "+RDMS)
    webbrowser.get(chrome_path).open(JENKINS_MAIN)
def open_pomp_res():
    subprocess.call(Firefox + " -no-remote -profile firefox_profile/pomp_res  " + POMP_RES_URL)
    autoit.win_wait_active("管理员登录 - Mozilla Firefox",15)
    time.sleep(3)
    autoit.send("{TAB}")
    autoit.send(POMP_RES_USERNAME)
    autoit.send("{TAB}")
    autoit.send(POMP_RES_MOBILE)


def open_pomp_labs():
    subprocess.call(Firefox + " -no-remote -profile firefox_profile/pomp_labs  " + POMP_LABS_URL)
    autoit.win_wait_active("管理员登录 - Mozilla Firefox",15)
    time.sleep(3)
    autoit.send("{TAB}")
    autoit.send(POMP_LABS_USERNAME)
    autoit.send("{TAB}")
    autoit.send(POMP_LABS_MOBILE)


def open_pomp_208():
    subprocess.call(Firefox + " -no-remote -profile firefox_profile/pomp_208  " + POMP_208_URL)
    autoit.win_wait_active("管理员登录 - Mozilla Firefox",15)
    time.sleep(3)
    autoit.send("{TAB}")
    autoit.send(POMP_208_USERNAME)
    autoit.send("{TAB}")
    autoit.send(POMP_208_MOBILE)


def open_pomp_204():
    subprocess.call(Firefox + " -no-remote -profile firefox_profile/pomp_204  " + POMP_204_URL)
    autoit.win_wait_active("管理员登录 - Mozilla Firefox",15)
    time.sleep(3)
    autoit.send("{TAB}")
    autoit.send(POMP_204_USERNAME)
    autoit.send("{TAB}")
    autoit.send(POMP_204_MOBILE)


def open_euop_res():
    subprocess.call(Firefox + " -no-remote -profile firefox_profile/euop_res  " + EUOP_RES_URL)
    autoit.win_wait_active("管理员登录 - Mozilla Firefox",15)
    time.sleep(3)
    autoit.send("{TAB}")
    autoit.send(EUOP_RES_USERNAME)
    autoit.send("{TAB}")
    autoit.send(EUOP_RES_MOBILE)


def open_euop_labs():
    subprocess.call(Firefox + " -no-remote -profile firefox_profile/euop_labs " + EUOP_LABS_URL)
    autoit.win_wait_active("管理员登录 - Mozilla Firefox",15)
    time.sleep(3)
    autoit.send("{TAB}")
    autoit.send(EUOP_LABS_USERNAME)
    autoit.send("{TAB}")
    autoit.send(EUOP_LABS_MOBILE)


def open_euop_181():
    subprocess.call(Firefox + " -no-remote -profile firefox_profile/euop_181 " + EUOP_181_URL)
    autoit.win_wait_active("管理员登录 - Mozilla Firefox",15)
    time.sleep(3)
    autoit.send("{TAB}")
    autoit.send(EUOP_181_USERNAME)
    autoit.send("{TAB}")
    autoit.send(EUOP_181_MOBILE)


def open_euop_175():
    subprocess.call(Firefox + " -no-remote -profile firefox_profile/euop_175 " + EUOP_175_URL)
    autoit.win_wait_active("管理员登录 - Mozilla Firefox",15)
    time.sleep(3)
    autoit.send("{TAB}")
    autoit.send(EUOP_175_USERNAME)
    autoit.send("{TAB}")
    autoit.send(EUOP_175_MOBILE)


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        # buttons for pomp
        self.pomp_204 = Button(self, text="POMP 204 top", fg='brown', command=open_pomp_204)
        self.pomp_208 = Button(self, text="POMP 208 top", fg='brown', command=open_pomp_208)
        self.pomp_labs = Button(self, text="POMP Labs top", fg='brown', command=open_pomp_labs)
        self.pomp_res = Button(self, text="POMP RES top", fg='brown', command=open_pomp_res)
        # buttons for euop
        self.euop_181 = Button(self, text="EUOP 181 top", fg='green', command=open_euop_181)
        self.euop_175 = Button(self, text="EUOP 175 top", fg='green', command=open_euop_175)
        self.euop_labs = Button(self, text="EUOP LABS top", fg='green', command=open_euop_labs)
        self.euop_res = Button(self, text="EUOP RES top", fg='green', command=open_euop_res)
        # buttons for default firefox
        self.firefox_default = Button(self, text="Firefox default", command=open_firefox_default)
        # buttons for default chrome
        self.chrome_default = Button(self, text="Chrome default", command=open_chrome_default)

        # buttons for other info
        self.hi_there = Button(self)
        self.quit = Button(self, text="QUIT", fg="red", command=self.master.destroy)

        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # hello button
        self.hi_there["text"] = "Hello Tk, click me!"
        self.hi_there["command"] = say_hi
        self.hi_there.pack(side="top")

        self.firefox_default.pack(side="top")
        self.chrome_default.pack(side="top")

        #  firefox button ->pomp_res
        self.pomp_res.pack(side="top")

        #  firefox button ->pomp_labs
        self.pomp_labs.pack(side="top")

        #  firefox button ->pomp_208
        self.pomp_208.pack(side="top")

        #  firefox button ->pomp_204
        self.pomp_204.pack(side="top")

        #  firefox button ->euop_res
        self.euop_res.pack(side="top")

        #  euop_labs
        self.euop_labs.pack(side="top")

        #  euop_175
        self.euop_175.pack(side="top")

        #  euop_181
        self.euop_181.pack(side="top")

        # quit button
        self.quit.pack(side="bottom")


def main():
    root = Tk()
    app = Application(master=root)
    app.master.title("My app in 2020")
    app.master.maxsize(1000, 400)
    app.mainloop()


if __name__ == '__main__':
    main()
