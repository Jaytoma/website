# main.py
from pyscript import document, display

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