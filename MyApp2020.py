# this is a starter in 2020

# read the config file
# ref https://pymotw.com/3/configparser/

from configparser import ConfigParser
import subprocess
from tkinter import * # notice the little t, it's T for python 2.
from tkinter import ttk

## get the config file
ConfigFile = "config.properties";
cfparser = ConfigParser()
cfparser.read(ConfigFile)
cfsec = cfparser.sections()
print(cfsec)
print("hello")
print(cfparser['POMP208']['HOST'])
print(cfsec[0][0])
print(cfparser['POMP204']['HOST'])

print(cfparser.get('POMP208','USERNAME'))
print(cfparser.get('POMP204','USERNAME'))

POMP_RES_URL=cfparser['POMP_RES']['URL']

## browser
Firefox = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe "
for section_name in cfparser.sections():
    print('section: ', section_name)
    print(' options: ', cfparser.options(section_name))
    for name, value in cfparser.items(section_name):
        print(' {} -> {}'.format(name,value))
    print()
# CALL BATFILE
# subprocess
# need \\

# subprocess.call("C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe")

# CALL FIREFOX

# gui TKinter
# We'll use pack and frame to do the layout, if the UI is complicated, grid should be considers.
# For this simple app, pack is enough.

class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # hello button
        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello Tk, click me!"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")


        #call firefox button ->pomp_res
        self.pomp_res=Button(self,text="POMP RES top", command=self.open_pomp_res)
        self.pomp_res.pack(side="top")

        # call firefox button ->pomp_labs
        self.pomp_res = Button(self, text="POMP Labs top", command=self.open_pomp_res)
        self.pomp_res.pack(side="top")

        # call firefox button ->pomp_208
        self.pomp_res = Button(self, text="POMP 208 top", command=self.open_pomp_res)
        self.pomp_res.pack(side="top")

        # call firefox button ->pomp_204
        self.pomp_res = Button(self, text="POMP 204 top", command=self.open_pomp_res)
        self.pomp_res.pack(side="top")

        # call firefox button ->euop_res
        self.pomp_res = Button(self, text="EUOP RES top", command=self.open_pomp_res)
        self.pomp_res.pack(side="top")

        # quit button
        self.quit = Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi, there, we love python")

    def open_pomp_res(self):
        subprocess.call(Firefox + " -no-remote -profile pomp_res  " + POMP_RES_URL)

root=Tk()
app = Application(master=root)
app.master.title("My app in 2020")
app.master.maxsize(1000, 400)
app.mainloop()

