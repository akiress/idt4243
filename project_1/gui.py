# -*- coding: iso-8859-1 -*-

# Name:             Project 1
# Purpose:          CSC 4243
# Author:           Benjamin K Guitreau
# Copyright:
# Licence:          GPL

# OS dev:           Windows 7 & Funtoo Linux
# Python dev:       2.7
# Revision:         1.00

# Dependencies:     Python 2.7 32-bit, Beautiful Soup 4

from Tkinter import Frame, Tk, Label, RAISED, W, E, N, S, LEFT, Button
from Tkinter import Listbox
from ttk import Style
from PIL import Image, ImageTk
from bs4 import BeautifulSoup
import urllib2
from sets import Set

from soupscraper import scrapeStart

"""
Frame Layout to better help me place items

Frame0 = Frame(parent, bg = "black")
Frame0.grid(row = 0, column = 0, columnspan = 8, sticky = W+E+N+S)
Frame1 = Frame(parent, bg = "yellow")
Frame1.grid(row = 1, column = 2, rowspan = 10, columnspan = 4, sticky = W+E+N+S)
Frame1a = Frame(parent, bg = "grey")
Frame1a.grid(row = 1, column = 0, rowspan = 10, columnspan = 2, sticky = W+E+N+S)
Frame1b = Frame(parent, bg = "grey")
Frame1b.grid(row = 1, column = 6, rowspan = 10, columnspan = 2, sticky = W+E+N+S)

Frame2a = Frame(parent, bg = "red")
Frame2a.grid(row = 11, column = 0, rowspan = 12, columnspan = 2, sticky = W+E+N+S)
Frame2b = Frame(parent, bg = "blue")
Frame2b.grid(row = 11, column = 2, rowspan = 12, columnspan = 2, sticky = W+E+N+S)
Frame2b = Frame(parent, bg = "red")
Frame2b.grid(row = 11, column = 4, rowspan = 12, columnspan = 2, sticky = W+E+N+S)
Frame2b = Frame(parent, bg = "blue")
Frame2b.grid(row = 11, column = 6, rowspan = 12, columnspan = 2, sticky = W+E+N+S)

Frame3a = Frame(parent, bg = "orange")
Frame3a.grid(row = 23, column = 0, rowspan = 12, columnspan = 8, sticky = W+E+N+S)

Frame4a = Frame(parent, bg = "green")
Frame4a.grid(row = 35, column = 0, rowspan = 12, columnspan = 8, sticky = W+E+N+S)

Frame5a = Frame(parent, bg = "#232323")
Frame5a.grid(row = 47, column = 0, rowspan = 12, columnspan = 8, sticky = W+E+N+S)

FrameBtns = Frame(parent, bg = "purple")
FrameBtns.grid(row =59, column = 0, rowspan = 12, columnspan = 8, sticky = W+E+N+S)
FrameB1 = Frame(parent, bg = "cyan")
FrameB1.grid(row = 61, column = 1, rowspan = 3, columnspan = 2, sticky = W+E+N+S)
FrameB2 = Frame(parent, bg = "cyan")
FrameB2.grid(row = 61, column = 5, rowspan = 3, columnspan = 2, sticky = W+E+N+S)
"""

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.parent = master

        self.dict = scrapeStart()
        self.initUI()


    def initUI(self):
        """ Build the grid """
        self.grid()
        for r in range(66):
            self.parent.rowconfigure (r, weight = 1)
        for c in range(8):
            self.parent.columnconfigure (c, weight = 1)
        """ Center the window on the display """
        width = 768
        height = 1024

        screenWidth = self.parent.winfo_screenwidth()
        screenHeight = self.parent.winfo_screenheight()

        x = (screenWidth - width) / 2
        y = (screenHeight - height) / 2

        self.parent.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.parent.configure(bg = "grey10")

        status = "home"
        self.drawScreen(status)


    def drawScreen(self, status):
        print ("%s is the status" % status)

        if (status == "home"):
            self.drawHome()
        elif (status == "film"):
            self.drawFilm()
        elif (status == "recipes"):

            self.drawRecipes()
        else:
            print('Bad mojo')


    def drawHome(self):
        infoText = ("Some Louisiana urban environments have a multicultural, multilingual heritage, being so strongly "
            "by an admixture of 18th century French, Spanish, Native American (Indian), and African cultures that they "
            "are considered to be somewhat exceptional in the U.S. Before the American influx and statehood at the "
            "beginning of the 19th century, the territory of current Louisiana State had been both a Spanish and "
            "French colony. In addition, the pattern of development included importing numerous African slaves in "
            "the 18th century, with many from the same region of West Africa, thus concentrating their culture.")

        self.img = ImageTk.PhotoImage(Image.open("louisiana.png"))

        self.title = Label(self.parent, width = 1, height = 1, text = "Louisiana", fg = "white", bg = "grey30",
                        font = ("Times 48 italic"), bd = 5, relief = RAISED)
        self.title.grid(row = 1, column = 2, rowspan = 10, columnspan = 4, sticky = W+E+N+S)

        self.info = Label(self.parent, width = 1, height = 1, text = infoText, fg = "white", bg = "grey30",
                        font = ("Times 14"), bd = 5, relief = RAISED, wraplength = 350, justify = LEFT)
        self.info.grid(row = 23, column = 4, rowspan = 24, columnspan = 4, sticky = W+E+N+S)

        self.image1 = Label(self.parent, width = 1, height = 1, image = self.img, bg = "grey10")
        self.image1.grid(row = 23, column = 0, rowspan = 24, columnspan = 4, sticky = W+E+N+S)

        self.Button1 = Button(self.parent, text = "Film", command = lambda: self.drawScreen("film"))
        self.Button1.grid(row = 61, column = 1, rowspan = 3, columnspan = 2, sticky = W+E+N+S)

        self.Button2 = Button(self.parent, text = "Recipes", command = lambda: self.drawScreen("recipes"))
        self.Button2.grid(row = 61, column = 5, rowspan = 3, columnspan = 2, sticky = W+E+N+S)

        self.Button3 = Button()
        self.Button3.grid_remove()
        self.Button4 = Button()
        self.Button4.grid_remove()
        self.Button5 = Button()
        self.Button5.grid_remove()
        self.listbox = Listbox()
        self.listbox.grid_remove()
        self.image2 = Label()
        self.image2.grid_remove()


    def drawFilm(self):
        self.title = Label(self.parent, text = "Film", fg="white", bg="grey30", font=("Times 48 italic"),
                        bd = 5, relief = RAISED)
        self.title.grid(row = 1, column = 2, rowspan = 10, columnspan = 4, sticky = W+E+N+S)

        self.Button1 = Button(self.parent, text = "Recipes", command = lambda: self.drawScreen("recipes"))
        self.Button1.grid(row = 61, column = 1, rowspan = 3, columnspan = 2, sticky = W+E+N+S)

        self.Button2 = Button(self.parent, text = "Home", command = lambda: self.drawScreen("home"))
        self.Button2.grid(row = 61, column = 5, rowspan = 3, columnspan = 2, sticky = W+E+N+S)

        self.info.grid_remove()
        self.image1.grid_remove()
        self.image2.grid_remove()
        self.Button3.grid_remove()
        self.Button4.grid_remove()
        self.Button5.grid_remove()
        self.listbox.grid_remove()


    def drawRecipes(self):
        self.title = Label(self.parent, text = "Recipes", fg="white", bg="grey30", font=("Times 48 italic"),
                        bd = 5, relief = RAISED)
        self.title.grid(row = 1, column = 2, rowspan = 10, columnspan = 4, sticky = W+E+N+S)

        self.Button1 = Button(self.parent, text = "Film", command = lambda: self.drawScreen("film"))
        self.Button1.grid(row = 61, column = 1, rowspan = 3, columnspan = 2, sticky = W+E+N+S)

        self.Button2 = Button(self.parent, text = "Home", command = lambda: self.drawScreen("home"))
        self.Button2.grid(row = 61, column = 5, rowspan = 3, columnspan = 2, sticky = W+E+N+S)

        self.Button3 = Button(self.parent, text = "Gumbo", command = self.drawRecipeList)
        self.Button3.grid(row = 24, column = 3, rowspan = 3, columnspan = 2, sticky = W+E+N+S)

        self.Button4 = Button(self.parent, text = "Jambalaya", command = self.quit)
        self.Button4.grid(row = 29, column = 3, rowspan = 3, columnspan = 2, sticky = W+E+N+S)

        self.Button5= Button(self.parent, text = "Seafood", command = self.quit)
        self.Button5.grid(row = 34, column = 3, rowspan = 3, columnspan = 2, sticky = W+E+N+S)

        self.info.grid_remove()
        self.image1.grid_remove()
        self.listbox.grid_remove()
        self.image2.grid_remove()


    def drawRecipeList(self):
        self.Button3.grid_remove()
        self.Button4.grid_remove()
        self.Button5.grid_remove()
        self.image2.grid_remove()

        self.Button1 = Button(self.parent, text = "Film", command = lambda: self.drawScreen("film"))
        self.Button1.grid(row = 61, column = 1, rowspan = 3, columnspan = 2, sticky = W+E+N+S)

        self.Button2 = Button(self.parent, text = "Home", command = lambda: self.drawScreen("home"))
        self.Button2.grid(row = 61, column = 5, rowspan = 3, columnspan = 2, sticky = W+E+N+S)

        self.listbox = Listbox(self.parent)
        for key in self.dict:
            index = 1
            self.listbox.insert(index, key)
            index += 1
        self.listbox.grid(row = 29, column = 1, rowspan = 12, columnspan = 6, sticky = W+E+N+S)
        self.listbox.bind("<<ListboxSelect>>", self.get_List)


    def get_List(self, *args):
        self.info.grid_remove()
        self.image1.grid_remove()
        self.image2.grid_remove()
        self.Button3.grid_remove()
        self.Button4.grid_remove()
        self.Button5.grid_remove()
        self.listbox.grid_remove()

        self.index = self.listbox.curselection()

        self.Button1 = Button(self.parent, text = "Film", command = lambda: self.drawScreen("film"))
        self.Button1.grid(row = 61, column = 1, rowspan = 3, columnspan = 2, sticky = W+E+N+S)

        self.Button2 = Button(self.parent, text = "Home", command = lambda: self.drawScreen("home"))
        self.Button2.grid(row = 61, column = 5, rowspan = 3, columnspan = 2, sticky = W+E+N+S)

        self.img2 = ImageTk.PhotoImage(Image.open("creole_gumbo.png"))
        self.image2 = Label(self.parent, width = 1, height = 1, image = self.img2, bg = "grey10")
        self.image2.grid(row = 21, column = 1, rowspan = 34, columnspan = 6, sticky = W+E+N+S)

def main():
    root = Tk()

    app = Application(root)
    root.mainloop()


if __name__ == '__main__':
    main()
