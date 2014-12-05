#!/usr/bin/python
# -*- coding: utf8 -*-


# importing modules
from __future__ import division
import csv, cPickle, itertools, copy



# -- FUNCTIONS

# save, load etc.



# -- CLASSES


class Parser (object):
    ''' create a parse object from a tree.
        
        ex.  myparse = Parser (mytree)        
        
    '''

# this above is is how we write the documentation


    pass
    

class Tree (object):
    
# sets the nodes as an empty list by default    
    def __init__ (self, nodes = []):
        self.nodes = nodes

    def __repr__(self):
        
        pass
        
    
class Node (object):
    ''' contains mother and 2 sisters
            
        ex.  mynode = Node(this, is, mynode)        
        
    '''

    def __init__ (self, mother  = None, sister1 = None, sister2 = None):
    
        self.mother = mother
        self.sister1 = sister1
        self.sister2 = sister2
        
    def __repr__(self):  
        output = ""
        output += "mother:\n %s\n" % (self.mother)
        output += "left sister: \n %s\n" % (self.sister1)
        output += "right sister:\n %s\n" % (self.sister2)       
        return output

    
    pass
    
class Lex (object):
    ''' lexical object with features
            
        ex.  mynode = Node(this, is, mynode)        
        
    '''

    def __init__ (self, text = ' ',  *args):
        
        self.features = []
        self.text = text
        for newfeature in args:
            
            new_feature = Feature(*newfeature)
            self.features.append(new_feature)
        
    def __repr__(self):  
        output =  "text: %s \nfeatures: " % (self.text)
        for feature in self.features:
             output += '[%s] ' % (feature)

        return output

        
             
 

    
class Feature (object):

    def __init__ (self, kind = " ", interpretable = True, valued = True):
        self.kind = kind
        self.interpretable = interpretable
        self.valued = valued
        
    def __repr__(self):  
        if self.interpretable:
             type_int = 'i'
        else:
             type_int = 'ui'

        if self.valued:
             type_val = 'val'
        else:
             type_val = 'non-val'

        output =  type_int + ", " + self.kind + ", " + type_val
        
        return output


    




