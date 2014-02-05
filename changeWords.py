# -*- coding: iso-8859-15 -*-

###################################################################
#                       ChangeWords v1.0                          #
#                                                                 #
# Script to change one word in a lot of files.                    #
# Designed to translate websites, but it can give you other uses. #
###################################################################

import sys
import subprocess
import os
import codecs
import htmlentities
import re
import unicodedata

def obtainWordsTxt(file):
    words1 = []
    words2 = []
    f = open(file, 'r')
    line = f.readline() 
    while line != "":
        word = line.split('\t')
        words1.append(word[0])
        words2.append(word[1])
        line = f.readline()
    f.close()
    return(words1, words2)

def obtainWordsXls(file):
    try:
        from xlrd import open_workbook,XL_CELL_TEXT
    except:
        print('Install xlrd with: pip install xlrd')
    words1 = []
    words2 = []
    book = open_workbook(file)
    sheet = book.sheet_by_index(0)
    return(sheet.col_values(0), sheet.col_values(1))
    
if not len(sys.argv) in (2,4):
    print('python changeWords.py help')
    sys.exit(1)
    
if sys.argv[1] == "help":
    print('Usage:\n\tchangeWords.py options file_with_words path_change\n\nOptions:\n\ta\tComplete without question\n\tc\tExact match\n\nRemember: You can use xls files and txt files')
    sys.exit(1)
    
if sys.argv[1][0] != '-':
    print('Bad options')
    sys.exit(1)

script_name =  sys.argv[0]
if sys.argv[1].find('a') >= 0:
    auto_complete = True
else:
    auto_complete = False
if sys.argv[1].find('c') >= 0:
    flag_complete = True
else:
    flag_complete = False

file_with_words = sys.argv[2]
try:
    path_change = sys.argv[3]
except:
    path_change = ""

if not os.path.exists(sys.argv[2]):
    print('Cannot open '+sys.argv[2])
    sys.exit(1)
    
if not os.path.exists(sys.argv[3]):
    print('cannot open %s', sys.argv[3])
    sys.exit(1)

extension = file_with_words.split('.')[-1]

if not extension in ('txt','xls'):
    print('The file_with_words is incorrect')
    sys.exit(1)

if extension == 'txt':
    (words1,  words2) = obtainWordsTxt(file_with_words)
elif extension == 'xls':
    (words1,  words2) = obtainWordsXls(file_with_words)

if words1 == None or words2 == None:
    print('Not obtain the words in file_with_words')
    sys.exit(1)

for word1, word2 in zip(words1, words2):
    print('\nChange \'%s\' to \'%s\'\n\nFinding...\n\n'%(word1, word2))
    if extension == 'xls':
      word1 = ''.join((c for c in unicodedata.normalize('NFD', word1) if unicodedata.category(c) != 'Mn'))
    word1 = word1.replace(" ","\ ").replace("?","\?").replace("(","\(").replace("*","\*").replace(")","\)")
    process = subprocess.Popen("grep -lir '"+word1+"' "+path_change+"*",
                               stdout=subprocess.PIPE, shell=True)
    (files,  error) = process.communicate()
    files = files.split('\n')
    files.pop()
    if not auto_complete:
        print('(y/n)\nDo you want change \''+word1+'\' in...\n')
    for file in files:
        if not file in(script_name, file_with_words):
            if not auto_complete:
                answer = raw_input(file+'? ')
            else:
                print file + '\n'
                answer = ''
            if answer in ('yes','y') or auto_complete:
                f = codecs.open(file, encoding='iso-8859-15', mode='r')
                data = f.read()
                f.close()
                data = htmlentities.decode(data)
                data = ''.join((c for c in unicodedata.normalize('NFD', data) if unicodedata.category(c) != 'Mn'))
                data = re.sub(word1,word2,data)
                if not flag_complete:
                  data = re.sub(word1.lower(),word2.lower(),data)
                  data = re.sub(word1.upper(),word2.upper(),data)
                f = codecs.open(file, encoding='iso-8859-15', mode='w')
                f.write(data)
                f.close()

print('\nCOMPLETED THE CHANGE OF WORDS')
