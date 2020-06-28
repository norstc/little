# this is a starter in 2020

# read the config file
# ref https://pymotw.com/3/configparser/

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
print(cfsec)
print("hello")
print(cfparser['POMP_208']['HOST'])
print(cfsec[0][0])
print(cfparser['POMP_204']['HOST'])

print(cfparser.get('POMP_208', 'USERNAME'))
print(cfparser.get('POMP_204', 'USERNAME'))

# SET POMP LOGIN INFO
POMP_RES_URL = cfparser['POMP_RES']['URL']
POMP_LABS_URL = cfparser['POMP_LABS']['URL']
POMP_204_URL = cfparser['POMP_204']['URL']
POMP_208_URL = cfparser['POMP_208']['URL']
POMP_208_USERNAME = cfparser['POMP_208']['USERNAME']
POMP_208_MOBILE = cfparser['POMP_208']['MOBILE']

# SET EUOP LOGIN INFO
EUOP_RES_URL = cfparser['EUOP_RES']['URL']
EUOP_RES_USERNAME = cfparser['EUOP_RES']['USERNAME']
EUOP_RES_MOBILE = cfparser['EUOP_RES']['MOBILE']
EUOP_LABS_URL = cfparser['EUOP_LABS']['URL']
EUOP_175_URL = cfparser['EUOP_175']['URL']
EUOP_181_URL = cfparser['EUOP_181']['URL']

for section_name in cfparser.sections():
    print('section: ', section_name)
    print(' options: ', cfparser.options(section_name))
    for name, value in cfparser.items(section_name):
        print(' {} -> {}'.format(name, value))
    print()

## browser
Firefox = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe "


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


def open_pomp_res():
    subprocess.call(Firefox + " -no-remote -profile firefox_profile/pomp_res  " + POMP_RES_URL)


def open_pomp_labs():
    subprocess.call(Firefox + " -no-remote -profile firefox_profile/pomp_labs  " + POMP_LABS_URL)


def open_pomp_208():
    subprocess.call(Firefox + " -no-remote -profile firefox_profile/pomp_208  " + POMP_208_URL)
    autoit.win_wait_active("管理员登录 - Mozilla Firefox")
    time.sleep(3)
    autoit.send("{TAB}")
    autoit.send(POMP_208_USERNAME)
    autoit.send("{TAB}")
    autoit.send(POMP_208_MOBILE)


def open_pomp_204():
    subprocess.call(Firefox + " -no-remote -profile firefox_profile/pomp_204  " + POMP_204_URL)


def open_euop_res():
    subprocess.call(Firefox + " -no-remote -profile firefox_profile/euop_res  " + EUOP_RES_URL)
    autoit.win_wait_active("管理员登录 - Mozilla Firefox")
    time.sleep(3)
    autoit.send("{TAB}")
    autoit.send(EUOP_RES_USERNAME)
    autoit.send("{TAB}")
    autoit.send(EUOP_RES_MOBILE)



def open_euop_labs():
    subprocess.call(Firefox + " -no-remote -profile firefox_profile/euop_labs " + EUOP_LABS_URL)


def open_euop_181():
    subprocess.call(Firefox + " -no-remote -profile firefox_profile/euop_181 " + EUOP_181_URL)


def open_euop_175():
    subprocess.call(Firefox + " -no-remote -profile firefox_profile/euop_175 " + EUOP_175_URL)


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
