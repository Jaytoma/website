# main.py
from pyscript import *
x_turn = True

def my_button_function(event):
    # This targets the specific div with the id 'output-target'
    input = document.getElementById('user-input')
    text = input.value
    greeting = f'Hello there {text}!'
    display(greeting, target="output-target", append=False)

def greetkey(event):
    if event.key == "Enter":
        my_button_function(event)

def checkdigit(event):
    code = document.getElementById('barcode').value
    sum1 = 0
    sum2 = 0
    for i in range(12):
        if i % 2 == 0:
            sum1 += int(code[i])
        else:
            sum2 += int(code[i])
    sum2 *= 3
    sum = sum1 + sum2
    sum %= 10
    sum = (10 - sum) % 10
    display(sum, target="checkout", append=False)

def barcodekey(event):
    if event.key == "Enter":
        checkdigit(event)

def one(event):
    global x_turn
    if x_turn == True:
        display('x', target='one', append=False)
        x_turn = False
    else:
        display('o', target='one', append=False)
        x_turn = True
    one = document.getElementById('one').innerText
    two = document.getElementById('two').innerText
    three = document.getElementById('three').innerText
    four = document.getElementById('four').innerText
    five = document.getElementById('five').innerText
    six = document.getElementById('six').innerText
    seven = document.getElementById('seven').innerText
    eight = document.getElementById('eight').innerText
    nine = document.getElementById('nine').innerText
    if one == two == three or four == five == six or seven == eight == nine or one == four == seven or two == five == eight or three == six == nine or one == five == nine or three == five == seven:
        if x_turn == False:
            display('Player X has won!', target='result', append=False)
        else:
            display('Player O has won!', target='result', append=False)

def two(event):
    global x_turn
    if x_turn == True:
        display('x', target='two', append=False)
        x_turn = False
    else:
        display('o', target='two', append=False)
        x_turn = True
    one = document.getElementById('one').innerText
    two = document.getElementById('two').innerText
    three = document.getElementById('three').innerText
    four = document.getElementById('four').innerText
    five = document.getElementById('five').innerText
    six = document.getElementById('six').innerText
    seven = document.getElementById('seven').innerText
    eight = document.getElementById('eight').innerText
    nine = document.getElementById('nine').innerText
    if one == two == three or four == five == six or seven == eight == nine or one == four == seven or two == five == eight or three == six == nine or one == five == nine or three == five == seven:
        if x_turn == False:
            display('Player X has won!', target='result', append=False)
        else:
            display('Player O has won!', target='result', append=False)

def three(event):
    global x_turn
    if x_turn == True:
        display('x', target='three', append=False)
        x_turn = False
    else:
        display('o', target='three', append=False)
        x_turn = True
    one = document.getElementById('one').innerText
    two = document.getElementById('two').innerText
    three = document.getElementById('three').innerText
    four = document.getElementById('four').innerText
    five = document.getElementById('five').innerText
    six = document.getElementById('six').innerText
    seven = document.getElementById('seven').innerText
    eight = document.getElementById('eight').innerText
    nine = document.getElementById('nine').innerText
    if one == two == three or four == five == six or seven == eight == nine or one == four == seven or two == five == eight or three == six == nine or one == five == nine or three == five == seven:
        if x_turn == False:
            display('Player X has won!', target='result', append=False)
        else:
            display('Player O has won!', target='result', append=False)

def four(event):
    global x_turn
    if x_turn == True:
        display('x', target='four', append=False)
        x_turn = False
    else:
        display('o', target='four', append=False)
        x_turn = True
    one = document.getElementById('one').innerText
    two = document.getElementById('two').innerText
    three = document.getElementById('three').innerText
    four = document.getElementById('four').innerText
    five = document.getElementById('five').innerText
    six = document.getElementById('six').innerText
    seven = document.getElementById('seven').innerText
    eight = document.getElementById('eight').innerText
    nine = document.getElementById('nine').innerText
    if one == two == three or four == five == six or seven == eight == nine or one == four == seven or two == five == eight or three == six == nine or one == five == nine or three == five == seven:
        if x_turn == False:
            display('Player X has won!', target='result', append=False)
        else:
            display('Player O has won!', target='result', append=False)

def five(event):
    global x_turn
    if x_turn == True:
        display('x', target='five', append=False)
        x_turn = False
    else:
        display('o', target='five', append=False)
        x_turn = True
    one = document.getElementById('one').innerText
    two = document.getElementById('two').innerText
    three = document.getElementById('three').innerText
    four = document.getElementById('four').innerText
    five = document.getElementById('five').innerText
    six = document.getElementById('six').innerText
    seven = document.getElementById('seven').innerText
    eight = document.getElementById('eight').innerText
    nine = document.getElementById('nine').innerText
    if one == two == three or four == five == six or seven == eight == nine or one == four == seven or two == five == eight or three == six == nine or one == five == nine or three == five == seven:
        if x_turn == False:
            display('Player X has won!', target='result', append=False)
        else:
            display('Player O has won!', target='result', append=False)

def six(event):
    global x_turn
    if x_turn == True:
        display('x', target='six', append=False)
        x_turn = False
    else:
        display('o', target='six', append=False)
        x_turn = True
    one = document.getElementById('one').innerText
    two = document.getElementById('two').innerText
    three = document.getElementById('three').innerText
    four = document.getElementById('four').innerText
    five = document.getElementById('five').innerText
    six = document.getElementById('six').innerText
    seven = document.getElementById('seven').innerText
    eight = document.getElementById('eight').innerText
    nine = document.getElementById('nine').innerText
    if one == two == three or four == five == six or seven == eight == nine or one == four == seven or two == five == eight or three == six == nine or one == five == nine or three == five == seven:
        if x_turn == False:
            display('Player X has won!', target='result', append=False)
        else:
            display('Player O has won!', target='result', append=False)

def seven(event):
    global x_turn
    if x_turn == True:
        display('x', target='seven', append=False)
        x_turn = False
    else:
        display('o', target='seven', append=False)
        x_turn = True
    one = document.getElementById('one').innerText
    two = document.getElementById('two').innerText
    three = document.getElementById('three').innerText
    four = document.getElementById('four').innerText
    five = document.getElementById('five').innerText
    six = document.getElementById('six').innerText
    seven = document.getElementById('seven').innerText
    eight = document.getElementById('eight').innerText
    nine = document.getElementById('nine').innerText
    if one == two == three or four == five == six or seven == eight == nine or one == four == seven or two == five == eight or three == six == nine or one == five == nine or three == five == seven:
        if x_turn == False:
            display('Player X has won!', target='result', append=False)
        else:
            display('Player O has won!', target='result', append=False)

def eight(event):
    global x_turn
    if x_turn == True:
        display('x', target='eight', append=False)
        x_turn = False
    else:
        display('o', target='eight', append=False)
        x_turn = True
    one = document.getElementById('one').innerText
    two = document.getElementById('two').innerText
    three = document.getElementById('three').innerText
    four = document.getElementById('four').innerText
    five = document.getElementById('five').innerText
    six = document.getElementById('six').innerText
    seven = document.getElementById('seven').innerText
    eight = document.getElementById('eight').innerText
    nine = document.getElementById('nine').innerText
    if one == two == three or four == five == six or seven == eight == nine or one == four == seven or two == five == eight or three == six == nine or one == five == nine or three == five == seven:
        if x_turn == False:
            display('Player X has won!', target='result', append=False)
        else:
            display('Player O has won!', target='result', append=False)

def nine(event):
    global x_turn
    if x_turn == True:
        display('x', target='nine', append=False)
        x_turn = False
    else:
        display('o', target='nine', append=False)
        x_turn = True
    one = document.getElementById('one').innerText
    two = document.getElementById('two').innerText
    three = document.getElementById('three').innerText
    four = document.getElementById('four').innerText
    five = document.getElementById('five').innerText
    six = document.getElementById('six').innerText
    seven = document.getElementById('seven').innerText
    eight = document.getElementById('eight').innerText
    nine = document.getElementById('nine').innerText
    if one == two == three or four == five == six or seven == eight == nine or one == four == seven or two == five == eight or three == six == nine or one == five == nine or three == five == seven:
        if x_turn == False:
            display('Player X has won!', target='result', append=False)
        else:
            display('Player O has won!', target='result', append=False)

def reset_board(event):
    global x_turn
    display('1', target='one', append=False)
    display('2', target='two', append=False)
    display('3', target='three', append=False)
    display('4', target='four', append=False)
    display('5', target='five', append=False)
    display('6', target='six', append=False)
    display('7', target='seven', append=False)
    display('8', target='eight', append=False)
    display('9', target='nine', append=False)
    display('Tic Tac Toe', target='result', append=False)
    x_turn = True


