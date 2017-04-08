#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import commands

__author__ = 'johnny'
__email__ = 'zhaozy93@outlook.com'


localdir = '/Users/johnny/Project/blog'
branch = 'master'



os.chdir(localdir)
commands.getstatusoutput('git add -A')

while True:
    commit_type = raw_input('pls choose your commit type [init] = i, [UPDATE] = u, [FIX] = f:')
    if commit_type == 'u' or commit_type == 'f' or commit_type == 'i':
        if commit_type == 'u':
            commit_type = '[UPDATE]'
        elif commit_type == 'f':
            commit_type = '[FIX]'
        elif commit_type == 'i':
            commit_type = '[init]'
        break
comment = raw_input('pls enter your commit comment:')
commands.getstatusoutput('git commit -m\'' + commit_type + comment + '\'')
print commands.getstatusoutput('git push origin ' + branch)[1]
