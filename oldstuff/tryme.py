#!/usr/bin/python
# -*- coding: utf8 -*-

# imports the minimalist parser
from mini_pars_001 import *

# creates lexical items with features

this = Lex('this',['Dem', True, True], ['p', False, True])
isreally = Lex('isreally',['V', True, True], ['fin', False, True] )
mysentence = Lex('mysentence',['N', True, True], ['count', False, True] )


# creates one node
mynode = Node(this, isreally, mysentence)

print mynode

# creates one tree with one node

mytree = Tree([mynode])