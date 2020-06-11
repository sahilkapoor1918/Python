#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib
import requests

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""
    # +++your code here+++
    with open (filename,'r') as fh:
        a=fh.read()
        #print(a)
    subjpg1=re.findall('.*GET (.*/puzzle/.*jpg).*', a)
    #print(subjpg1)
    #print('SUNJPG1 : ',len(subjpg1))
    
    subjpg1=list(set(subjpg1))
    subjpg1=sorted(subjpg1,key=sortedJpg)
    
    #print(subjpg1)
    #print('SUNJPG1 : ',len(subjpg1))
          
    subjpg2=[]
    for i in subjpg1:
        path='http://code.google.com'+i
        subjpg2.append(path)
        
    #print(subjpg2)
    #print('SUNJPG2 : ',len(subjpg2))
    return subjpg2

def sortedJpg(jpg):
    #print(jpg)
    return jpg[-8:-4]

def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """
    # +++your code here+++

    if not os.path.isdir(dest_dir):
        os.mkdir(dest_dir)
        
    for i in range(len(img_urls)):
        with open(dest_dir+'pic'+str(i)+'.jpg','wb')as handle:
            response = requests.get(img_urls[i], stream=True)
            print('Downloading : pic'+str(i))
            
            if not response.ok:
                print (response)

            for block in response.iter_content(1024):
                if not block:
                    break

                handle.write(block)
    
    str1=''
    for i in range(len(img_urls)):
        str1=str1+'<img src="{path}pic{number}.jpg">'.format(path=dest_dir,number=i)
        
    #print(str1)
    str2='''<verbatim>
        <html>
        <body>
        {}
        </body>
        </html>'''.format(str1)
    with open('index.html','w') as fh:
        fh.write(str2)

def main():
    args = sys.argv[1:]

    if not args:
        print ('usage: [--todir dir] logfile ')
        sys.exit(1)

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    img_urls = read_urls(args[0])

    if todir:
        download_images(img_urls, todir)
    else:
        print ('\n'.join(img_urls))

if __name__ == '__main__':
    main()
