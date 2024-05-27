from gui import Menu
from tkinter import Tk, messagebox, Entry
import pickle
# imports

menu = Menu()
# vars

# main
menu.mainMenu()

stock = {}
review = []

try:
  with open("stock.pickle", "rb") as s:
    try:
      stock = pickle.load(s)

    except EOFError:
      stock = {}

except FileNotFoundError:
  with open("stock.pickle", "wb") as s:
    pickle.dump(stock, s)

try:
  with open("review.pickle", "rb") as r:
    try:
      review = pickle.load(r)

    except EOFError:
      review = []

except FileNotFoundError:
  with open("review.pickle", "wb") as r:
    pickle.dump(review, r)
# main
