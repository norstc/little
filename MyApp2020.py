# this is a starter in 2020

# read the config file
# ref https://pymotw.com/3/configparser/

from configparser import ConfigParser
import subprocess
import tkinter  as tk # notice the little t, it's T for python 2.


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


class Application(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello Tk, click me!"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")
        self.quit = tk.Button(self,text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi, there, we love python")


root=tk.Tk()
app = Application(master=root)
app.mainloop()

