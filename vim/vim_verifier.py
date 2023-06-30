# This is a collection of verification tools for the vim notebooks

import json


def oneCon(check):
    if check:
        return True
    else:
        print('Give it another try!')
    return False



def twoCon(check1,check2):
    if check1 and check2:
        return True
    else:
        print('Sorry, try again')
    return False



# This is the verification program for exercise 5
def exFive():
    exercise = 5
    f = open('01.01-vim_normal.ipynb')
    book = json.load(f)
    [start,end] = startEnd(book,exercise)
    
    # This checks that the correct number of cells are present and that the middle cell is the original cell
    if end-start == 9 and book['cells'][start+4]['source'][0] == '# Please insert some cells above me and below me!':
        return True
    else:
        print('Maybe you forgot to save?')
    return False



# This is the verification program for exercise 7
def exSeven():
    exercise = 7
    f = open('01.01-vim_normal.ipynb')
    book = json.load(f)
    [start,end] = startEnd(book,exercise)
    
    # This assigns truth values to the exercise conditions
    raw = book['cells'][start+1]['cell_type']=='raw'
    markdown = book['cells'][start+2]['cell_type']=='markdown'
    code = book['cells'][start+3]['cell_type']=='code'
    if raw and markdown and code:
        return True
    else:
        print('Maybe you forgot to save?')
    return False



def exThirteen():
    exercise = 13
    f = open('01.02-vim_jupyter.ipynb')
    book = json.load(f)
    [start,end] = startEnd(book,exercise)
    
    # This checks that the correct number of cells are present and that the middle cell is the original cell
    if end-start == 9 and book['cells'][start+4]['source'][0] == '# Please insert some cells above me and below me!':
        return True
    else:
        print('Maybe you forgot to save?')
    return False



def exFifteen():
    exercise = 15
    f = open('01.02-vim_jupyter.ipynb')
    book = json.load(f)
    hidden = True
    shown = True
    [start,end] = startEnd(book,exercise)
    
    i = start + 1

    while i < start + 7:
        if len(book['cells'][i]['metadata']) == 1:
            hidden = False
        i = i + 1
    
    while i < start + 13:
        if len(book['cells'][i]['metadata']) != 1:
            shown = False
        shown = shown and True
        i = i + 1
    
    if hidden and shown:
        return True
    else:
        print('Maybe you forgot to save?')
    return False



#This is a support function that finds the start and end of an exercise
def startEnd(book,exercise):
    i = 0
    start = 0
    end = 0
    while i < len(book['cells'])-1:
        if len(book['cells'][i]['source']) != 0:
            contents = book['cells'][i]['source'][0]
            if contents[:3] == '## ':
                n = contents.index(' ')
                m = contents.index(')')
                l = contents[n+1:m]
                if int(l) == exercise:
                    start = i;
                elif int(l) == exercise+1:
                    end = i;
        i = i + 1
    return [start,end]