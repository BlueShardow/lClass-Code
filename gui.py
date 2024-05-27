import pickle
from tkinter import Button, Tk, Label, Text, DISABLED, Entry
from classes import Admin, Customer
# imports

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

class Menu: # class Menu
  def mainMenu(self): # mainMenu
    #output
    root = Tk()
    root.title("Storefront")
    root.geometry("720x480")
    root.configure(bg = "lightblue")
    root.grid_rowconfigure(0, weight = 1)
    root.grid_columnconfigure(0, weight=1)
    # end of output

    # placements
    # storefrontLabel
    storefrontLabel = Label(root, text = "Welcome to lStore!", font = ("Comic Sans", 16), bg = "white")
    storefrontLabel.grid(row = 0, column = 1, padx = 80, pady = 150, sticky = "nsew")
    # end of storefrontLabel

    # admin
    adminButton = Button(root, text = "Admin Access", font = ("Comic Sans", 12), bg = "white", command = menu.adminMenu)
    adminButton.grid(row = 1, column = 2, padx = 20, pady = 20, sticky = "ew")
    # end of admin

    # customer
    customerButton = Button(root, text = "Customer Access", font = ("Comic Sans", 12), bg = "white", command = menu.customerMenu)
    customerButton.grid(row = 1, column = 0, padx = 20, pady = 20, sticky = "ew")
    # end of customer
    # end of placements

    root.mainloop() # loop
  # end of mainMenu

  def adminMenu(self): # adminMenu
    # output
    root = Tk()
    root.title("Admin Access")
    root.geometry("720x480")
    root.configure(bg = "white")
    root.grid_rowconfigure(0, weight = 1)
    root.grid_columnconfigure(0, weight =1 )
    # end of output

    # placements
    # addItem
    addItemButton = Button(root, text = "Add Item", font = ("Comic Sans", 12), bg = "lightblue", command = lambda: admin.addNewItems(root))
    addItemButton.grid(row = 0, column = 0, padx = 20, pady = 20, sticky = "nsew")
    # end of addItem

    # printItems
    printItemsButton = Button(root, text = "Print Items", font = ("Comic Sans", 12), bg = "lightblue", command = admin.printStock)
    printItemsButton.grid(row = 1, column = 0, padx = 20, pady = 20, sticky = "nsew")
    # end of printItems

    # review
    printReviewButton = Button(root, text = "Review Items", font = ("Comic Sans", 12), bg = "lightblue", command = admin.reviewItems)
    printReviewButton.grid(row = 1, column = 1, padx = 20, pady = 20, sticky = "nsew")
    # end of review

    # removeItem
    removeItemsButton = Button(root, text = "Remove All Items", font = ("Comic Sans", 12), bg = "lightblue", command = admin.removeItems)
    removeItemsButton.grid(row = 0, column = 1, padx = 20, pady = 20, sticky = "nsew")
    # end of revomeItem
    # end of placements

    root.mainloop() # loop
  # end of adminMenu

  def customerMenu(self): # customerMenu
    # output
    root = Tk()
    root.title("Customer Access")
    root.geometry("720x480")
    root.configure(bg = "white")
    root.grid_rowconfigure(0, weight = 1)
    root.grid_columnconfigure(0, weight = 1)
    # end of output

    # placements
    stockText = "" 

    for item in stock:
      stockText += f"{item}: ${stock[item][0]:.2f}, {stock[item][1]}\n"

    stockText += "Type in the descritption/name\nof the item and the hit\n'Add Item' to add it to your cart."
    
    stockListLabel = Label(root, text = "Stock Items", font = ("Comic Sans", 12), bg = "lightblue")
    stockListLabel.grid(row = 0, column = 1, padx = 20, pady = 20, sticky = "nsew")

    stockListText = Label(root, text = stockText, bg = "lightblue")
    stockListText.grid(row = 1, column = 1, padx = 20, pady = 20, sticky = "nsew")

    stockAddItemButton = Button(root, text = "Add Item", font = ("Comic Sans", 12), bg = "lightblue", command = lambda: customer.purchaseItem(stockItemsEntry.get()))
    stockAddItemButton.grid(row = 3, column = 0, padx = 20, pady = 20, sticky = "w")

    stockGetTotalButton = Button(root, text = "Get Total", font = ("Comic Sans", 12), bg = "lightblue", command = customer.getTotal)
    stockGetTotalButton.grid(row = 3, column = 2, padx = 20, pady = 20, sticky = "e")

    stockGetTotalPlusTaxButton = Button(root, text = "Get Total + Tax", font = ("Comic Sans", 12), bg = "lightblue", command = customer.totalPlusTax)
    stockGetTotalPlusTaxButton.grid(row = 3, column = 1, padx = 20, pady = 20, sticky = "ns")

    stockCheckoutButton = Button(root, text = "Checkout", font = ("Comic Sans", 12), bg = "lightblue", command = customer.showItems)
    stockCheckoutButton.grid(row = 4, column = 1, padx = 20, pady = 20, sticky = "nsew")

    stockItemsEntry = Entry(root, font = ("Comic Sans", 12), bg = "lightblue")
    stockItemsEntry.grid(row = 2, column = 1, padx = 20, pady = 20, sticky = "nsew")
    # end of placements
  # end of customerMenu
# end of class Menu

menu = Menu()
description = "Sample item"
units = 5
price = 10.99
admin = Admin(description, units, price)
customer = Customer()
# vars
