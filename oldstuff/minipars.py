#!/usr/bin/python
# -*- coding: utf8 -*-


# importing modules
from __future__ import division
import csv, cPickle, itertools, copy



# -- FUNCTIONS

# save, load etc.



# -- CLASSES
class Lex (object):
    ''' lexical object with features
            
        ex.  mynode = Node(this, is, mynode)        
        
    '''

    def __init__ (self, text = ' ',  *args):
        
        self.features = []
        self.text = text
        for newfeature in args:
            
            new_feature = (newfeature)
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

        output = self.kind +", " + type_int + ", " + type_val
        
        return output


   
        
      

def preprocess(sentence):
        words = sentence.split()
        lexes = []
        for word in words:
            for entry in lexicon:
                if word.endswith("s") and word.rstrip("s") == entry.text:
                    lexes = lexes.extend([Lex(word.rstrip("s"), entry.features), Lex("s", Feature("fin", True, True), Feature("3sg", False, False))])
                elif word == entry.text:
                    lexes.append(Lex(word, entry.features)) 
                #else:
                 #   print  "%s not found" % (word)
        print lexes
def parse(lexes):
        output = []
        trees = [[Node(lex) for lex in lexes]]
        newlyconnected = [Node(lex) for lex in lexes]
        nodes = [Node(lex) for lex in lexes]
        while trees:
            for tree in trees:
                justconnected = []
                for word in tree:
                    if word in newlyconnected:
                        for word2 in tree:
                            for feature in word.frfcc:
                                if (feature.interpretable == False) and (feature.valued == False):
                                    for feature2 in word2.mother.features:
                                        if (feature.kind == feature2.kind) and feature2.interpretable:
                                            trees.append(copy.deepcopy(tree))
                                            feature.valued = True
                                            word.sister1 = word
                                            word.sister2 = word2
                                            word.mother = word2
                                            justconnected.append(word)
                                            nodes.append(word)
                            for feature in word2.frfcc:
                                if (feature.interpretable == False) and (feature.valued == False):
                                    for feature2 in word.mother.features:
                                        if (feature.kind == feature2.kind) and feature2.interpretable:
                                            trees.append(copy.deepcopy(tree))
                                            feature.valued = True
                                            word.sister1 = word
                                            word.sister2 = word2
                                            justconnected.append(word)
                                            nodes.append(word)
                for word in tree:
                    if word in newlyconnected:
                        for word2 in nodes:
                            for feature in word.frfcc:
                                if (feature.interpretable == False) and (feature.valued == False):
                                    for feature2 in word2.mother.features:
                                        if (feature.kind == feature2.kind) and feature2.interpretable:
                                            trees.append(copy.deepcopy(tree))
                                            feature.valued = True
                                            word.sister1 = word
                                            word.sister2 = word2
                                            word.mother = word2
                                            word.mother.text = "moved" + word.mother.text
                                            justconnected.append(word)
                                            nodes.append(word)
                if newlyconnected == justconnected:
                    trees.remove(tree)
                elif len(tree) == 1 and (False in [valued.feature for feature in tree[0].frfcc] == False):
                    output.append(tree)
                    #trees.remove(tree)
                else:
                    newlyconnected = copy.deepcopy(justconnected)
        return output
lexicon = [Lex("s", Feature("fin", True, True), Feature("3sg", False, False), Feature("v", False, False)), Lex("john", Feature("3sg", True, True), Feature("fin", False, False), Feature("v", False, False)), Lex("sleep",Feature("v", True, True), Feature("3sg", False, False), Feature("fin", False, False))]
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
        if isinstance(mother, Lex) and isinstance (sister1, Lex) and isinstance(sister2, Lex):
            self.frfcc = self.mother.features.append(self.sister1.frfcc.append(self.sister2.frfcc))
        
    def __repr__(self):  
        output = ""
        output += "mother:\n %s\n" % (self.mother)
        output += "sister sx:\n %s\n" % (self.sister1)
        output += "sister dx:\n %s\n" % (self.sister2)       
        return output

    
    pass
    
    



