# use pip or pip3 to install g,tkinter.
from g.shizimoms.shop.unicode_symbols import __UNICODE__
from tkinter import Tk
imput = input("enter unicode starting with u\u:\n")
if imput is in __UNICODE__:
  root = Tk()
  x = 5
  y = 5
  button_symbols[x, y] = imput.pop()
  x = x + 5
  y = y + 5
else:
  return " 404 error:unicode symbol not found"
