"""This is a python implementation of grep module offered by unix systems.It includes full Perl regex support and -o, -r flags."""

import re
import argparse
import os
from os.path import join

class c:           #Coloring class for found grep objects
    red =  '\033[91m'
    green = '\033[92m'

def specific_color_string(string,part): #function for coloring specific parts of string
    partwords = part.split()

    for w in string.split():

        if w in partwords:
             print c.red+w,
        else:
            print c.green+w,

#Normal grep function
def grep(search_query,filename):
    cnt=0            #A hackish solution to prevent multiple printing

    for line in (open(filename).readlines()):
        for word in re.findall(search_query, line):
                if(cnt==0):
                    specific_color_string(line,word)
                    print "\n"
                cnt=1
        cnt=0

#only-matching grep function
def grep_onlymatching(search_query,filename):
    for line in (open(filename).readlines()):
        for word in re.findall(search_query, line):
                print word +"\n"

#recursive searching normal
def grep_recurse(search_query,path):
    cnt=0       #A hackish solution to prevent multiple printing
    regObj = re.compile(search_query)

    for dirpath, dirs, fnames in os.walk(top=path):
        for list_file in fnames:
            with open((os.path.join(dirpath, list_file))) as  f:
                for line in f.readlines():
                    for word in re.findall(search_query, line):

                        if(cnt==0):
                            specific_color_string(line,word)
                            print "\n"
                        cnt=1
                    cnt=0

#recursive searching only-matching
def grep_recurse_onlymatching(search_query,path):
    regObj = re.compile(search_query)

    for dirpath, dirs, fnames in os.walk(top=path):
        for list_file in fnames:
            with open((os.path.join(dirpath, list_file))) as  f:
                for line in f.readlines():
                    for word in re.findall(search_query, line):
                            print word +"\n"


#Argparse implementation
parser = argparse.ArgumentParser(description="Implementation of grep in python")
#Positionl Arguments
parser.add_argument("search_query", help="string to be searched")
parser.add_argument("filename",help="name of file to be searched")
#Optional Arguments
parser.add_argument("-o","--only_matching",action="store_true",help="show only the part of a line matching PATTERN")
parser.add_argument("-r","--recursive",action="store_true",help="like --directories=recurse")

args = parser.parse_args()

if (args.only_matching):
    if(args.recursive):
        grep_recurse_onlymatching(args.search_query,args.filename)
    else:
        grep_onlymatching(args.search_query,args.filename)

else:
    if(args.recursive):
        grep_recurse(args.search_query,args.filename)
    else:
        grep(args.search_query,args.filename)
#END_OF_SOURCE_CODE
