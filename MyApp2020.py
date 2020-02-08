# this is a starter in 2020

# read the config file
# ref https://pymotw.com/3/configparser/

from configparser import ConfigParser
import subprocess


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
subprocess.call("C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe")

# CALL FIREFOX

