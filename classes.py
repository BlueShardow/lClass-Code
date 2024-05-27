from tkinter import Message, messagebox, Entry, Tk, Label, simpledialog 
import pickle
# imports

review = []
stock = {}

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

class Admin: # class Admin 
  global stock
  
  def __init__(self, description, units, price): # constructor
    self.description = description
    self.units = units
    self.price = price
  # end of constructor
  
  def addItem(self, description, units, price): # addItem
    global stock
    stock[description] = (units, price)
  # end of addIem

  def addNewItems(self, root): # addNewItems
    global stock
    root = Tk()
    root.withdraw()

    self.description = simpledialog.askstring("Description", "What is the item's description?")
    self.units = simpledialog.askinteger("Units", "Enter the number of units in stock: ")
    self.price = simpledialog.askfloat("Price", "Enter the price of the item: ")

    stock[self.description] = (self.units, self.price)

    with open("stock.pickle", "wb") as s:
      pickle.dump(stock, s)

    return(self.description, self.units, self.price)
  # end of addNewItems

  def printStock(self): # printStock
    global stock
    message = ""
    
    for key, value in stock.items():
      message = message + f"\n\nDescription: {key}\nUnits: {value[0]}\nValue: ${value[1]:.2f}"
      
    messagebox.showinfo("Stock Review:", message)
  # end of printStock

  def reviewItems(self): # reviewItems
    review = []

    try:
      with open("review.pickle", "rb") as r:
        try:
          review = pickle.load(r)

        except EOFError:
          review = []

    except FileNotFoundError:
      with open("review.pickle", "wb") as r:
        pickle.dump(review, r)
      
    messagebox.showinfo("Review", "\n".join(review))
  # end of reviewItems

  def removeItems(self): # removeItems
    stock = {}
    
    try:
      with open("stock.pickle", "rb") as s:
        try:
          stock = pickle.load(s)

        except EOFError:
          stock = {}

    except FileNotFoundError:
      with open("stock.pickle", "wb") as s:
        pickle.dump(stock, s)

    stock = {}
    
    with open ("stock.pickle", "wb") as s:
      pickle.dump(stock, s)
  # end of removeItems
# end of class Admin

class Customer: # class Customer
  def __init__(self): # constructor
    self.itemsList = []
    self.itemsPrice = []
  # end of constructor

  def purchaseItem(self, itemDesc): # add item
    global stock
    itemF = stock[itemDesc][0]
    
    self.itemsList.append(itemDesc)
    self.itemsPrice.append(itemF)
  # end of add item

  def getTotal(self): # get total
    messagebox.showinfo("Total", f"${sum(self.itemsPrice): .2f}")
  # end of get total

  def totalPlusTax(self): # get total plus tax
    messagebox.showinfo("Total", f"${sum(self.itemsPrice) * 1.07: .2f}")
  # end of get total plus tax

  def showItems(self): # list items
    review = []
    
    try:
      with open("review.pickle", "rb") as r:
        try:
          review = pickle.load(r)

        except EOFError:
          review = []

    except FileNotFoundError:
      with open("review.pickle", "wb") as r:
        pickle.dump(review, r)
    
    for items in self.itemsList:
      review.append(items)

    with open("review.pickle", "wb") as r:
      pickle.dump(review, r)
    
    messagebox.showinfo("Check Out", f"Items: {self.itemsList}\nTotal: ${sum(self.itemsPrice) * 1.07: .2f}")

    self.itemsList = []
    self.itemsPrice = []
  # end of list items
# end of class Customer
