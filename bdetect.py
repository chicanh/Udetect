#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import shutil, errno
import os
import ConfigParser

#
#functions
#
def copyAll(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else: raise

#bdetect add path

#
#variables
#
count = 0
projectName = ""
config = ConfigParser.RawConfigParser()

#
#check argvs
#
if len(sys.argv) <= 1:
    print 'Bdetect v1.0 (c)2012 by S3K4 team - a very fast logon Joomla Cracker - support all version'
    print 'Website: http://www.uns.vn'
    print 'Mail   : zonesec@gmail.com'
    print ''
    print 'Syntax: python BJoomla [-u USER|-U FILE] [-p PASS|-P FILE] -h URL [OPT]'
    print ''
    print 'Options:'
    print 'add project_name source_directory - create a new project'
    print 'list - show all projects'
    print 'del project_name - delete a project'
    sys.exit()

for arg in sys.argv:
    if arg == 'add':
        projectName = sys.argv[count + 1]
        path = sys.argv[count + 2]
        #copy source
        shutil.copytree(path,'projects/' + projectName, symlinks=False, ignore=None)
        #create file config
        config.add_section(projectName)
        config.set(projectName, 'path', os.path.abspath(path))
        print './projects/' + projectName + '/.projects.cfg'
        with open('./projects/' + projectName + '/.projects.cfg', 'wb') as configfile:
            config.write(configfile)
    if arg == 'del':
        projectName = sys.argv[count + 1]
        shutil.rmtree('projects/' + projectName)
        #delete project
    if arg == 'check':
        projectName = sys.argv[count + 1]
        #check project
        #read file config
        config.read('./projects/' + projectName + '/.projects.cfg')
        src = config.get(projectName, 'path')
    if arg == 'list':
        #show list projects   
        for i in os.listdir('projects'):
        	print i
    if arg == 'help':
        print 'Help'
        #show list projects   
    count += 1