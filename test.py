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

def sum(event):
    num1 = int(document.getElementById('first-num').value)
    num2 = int(document.getElementById('second-num').value)
    output = num1 + num2
    display(output, target="equals", append=False)

def difference(event):
    num1 = int(document.getElementById('first-num').value)
    num2 = int(document.getElementById('second-num').value)
    output = num1 - num2
    display(output, target="equals", append=False)

def product(event):
    num1 = int(document.getElementById('first-num').value)
    num2 = int(document.getElementById('second-num').value)
    output = num1 * num2
    display(output, target="equals", append=False)

def quotient(event):
    num1 = int(document.getElementById('first-num').value)
    num2 = int(document.getElementById('second-num').value)
    output = num1 / num2
    display(output, target="equals", append=False)