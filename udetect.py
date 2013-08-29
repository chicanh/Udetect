#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, os
import shutil, errno
sys.path.insert(0, 'libs')
import funcs

#
#variables
#
count = 0
projectName = ""

#Determine OS type and use appropriate path seperator. 
if os.name == "posix":
    pathSep = "/"
elif os.name == "nt":
    pathSep = "\\"
else:
    print "can not detect OS!"
    exit(2)


#
#check argvs
#
if len(sys.argv) <= 1:
    funcs.help()

for arg in sys.argv:
    if arg == 'create':
        projectName = sys.argv[count + 1]
        dirSrc = sys.argv[count + 2]
        funcs.createProject(projectName, dirSrc)
    if arg == 'del':        #delete project
        projectName = sys.argv[count + 1]
        funcs.delProject(projectName)
        print "Deleted project: " + projectName
    if arg == 'check':        #check project
        projectName = sys.argv[count + 1]
        if '--all' in sys.argv:
            funcs.check(projectName, "all")
        else:
            funcs.check(projectName)
    if arg == 'list':        #show list projects   
        for i in os.listdir('projects'):
        	print i
    if arg == 'update':
        projectName = sys.argv[count + 1]
        funcs.updateProject(projectName)
     
    if arg == 'help':
        funcs.help()
    if arg == 'test':
        funcs.test('/home/pentester/wordpress')
  
    count += 1