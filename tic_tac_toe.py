import pprint

theBoard = {'top-L': '', 'top-M':'',
            'top-R':'', 'mid-L':'',
            'mid-M':'', 'mid-R':'',
            'low-L':'', 'low-M':'',
            'low-R':''}

pprint.pprint(theBoard)
theBoard['mid-M'] = 'X'
pprint.pprint(theBoard)
theBoard['top-L'] = 'O'
theBoard['top-M'] = 'O'
theBoard['top-R'] = 'O'
theBoard['mid-L'] = 'X'
theBoard['low-R'] = 'X'

print('\n')

def printBoard(board):
    print(board['top-L'] + ' | ' + board['top-M'] + ' | '  + board['top-R'])
    print('_____')
    print( board['mid-L'] + ' | ' + board['mid-M'] + ' | ' + board['mid-R'])
    print('_____')
    print(board['low-L'] + ' | ' + board['low-M'] + ' | ' + board['low-R'])

print(printBoard(theBoard))