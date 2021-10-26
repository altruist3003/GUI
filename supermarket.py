from tkinter import *
from tkinter import ttk
# random library for taking random values
from random import randint
# install pillow library to work with images using pip install pillow
#PIL is the Python Imaging Library which provides the python interpreter with image editing capabilitie
from PIL import Image, ImageTk


class SuperMarket(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.root = root
        self.root.title("Smart Shopping") #Adding Title to the window
        self.root.geometry("1350x690+0+0") #root geometry
        root.minsize(1350,690) #minimum size of the window upto which we can minimize it
        root.maxsize(1350,690) #maximum size of the window upto which we can maximize it

        self.root.config(background="#D2691E") # for adding background to window
        MainFrame = Frame(self.root, bg="#D2691E",bd=0, relief=RIDGE) # adding frame to a mainFrame
        MainFrame.grid()
        #dividing window in two parts left frame and right frame we have added several widget into left frame and adding canvas to right window
        LeftFrame = Frame(MainFrame, width=290,height=690,padx=10, bg="grey",highlightbackground="#fff",highlightthickness=2, relief=GROOVE)
        LeftFrame.grid(row=0,column=0,sticky="W")
        RightFrame = Frame(MainFrame,width=1060,height=690,padx=10,bg="black",highlightbackground="#fff",highlightthickness=2,relief=GROOVE)
        RightFrame.grid(row=0,column=1,sticky="W")
        #declaring variables that will be used as a text variable for entry widget
        self.x = IntVar()
        self.y = IntVar()
        self.no_of_carts = IntVar()
        self.no_of_receivers = IntVar()
        #label for x co-ordinate variable
        self.lblx= Label(LeftFrame, text="X",font=('arial',13,'bold'),padx=2, pady=3, fg="black", bg="grey").place(x=0,y=20)
        # text field for accepting co-ordinate x
        self.txtx = Entry(LeftFrame, font=('arial',13,'bold'),width=10, textvariable=self.x)
        self.txtx.place(x=170,y=20)
        # pointing curser to it when withdow loads or program runs
        self.txtx.focus()
        #label for y co-ordinate variable
        self.lbly= Label(LeftFrame, text="Y",font=('arial',13,'bold'),padx=2, pady=3, fg="black", bg="grey").place(x=0,y=60)
        # text field for accepting co-ordinate y
        self.txty = Entry(LeftFrame, font=('arial',13,'bold'),width=10, textvariable=self.y)
        self.txty.place(x=170,y=60)
        #label for number of carts
        self.lblnoofCarts= Label(LeftFrame, text="No. of Carts",font=('arial',13,'bold'),padx=2, pady=3, fg="black", bg="grey").place(x=0,y=530)
        #entry widget for number of carts
        self.txtnoofCarts = Entry(LeftFrame, font=('arial',13,'bold'),width=10, textvariable=self.no_of_carts)
        self.txtnoofCarts.place(x=170,y=530)
        #label for number of receivers
        self.lblnoofReceivers= Label(LeftFrame, text="No. of Receivers",font=('arial',13,'bold'),padx=2, pady=3, fg="black", bg="grey").place(x=0,y=570)
        #entry widget for number of receivers
        self.txtnoofReceivers = Entry(LeftFrame, font=('arial',13,'bold'),width=10, textvariable=self.no_of_receivers)
        self.txtnoofReceivers.place(x=170,y=570)
        # reset button
        self.btnReset = Button(LeftFrame, bd=5, fg="black", font=('arial',14,'bold'), width=5, height=1, bg="#D2691E", text="Reset").place(x=0,y=620)
        # start button
        self.btnStart = Button(LeftFrame, bd=5, fg="black", font=('arial',14,'bold'), width=5, height=1, bg="#D2691E", text="Start").place(x=95,y=620)
        # ok Button
        self.btnOk = Button(LeftFrame, bd=5, fg="black", font=('arial',14,'bold'), width=5, height=1, bg="#D2691E", text="OK").place(x=190,y=620)
        #canvas for adding images and provide them momement
        self.canvas = Canvas(RightFrame, width=1018, height =638,bg="grey")
        self.canvas.place(x=10,y=20)
        #looping for creating lines
        for i in range(80) :
            x = 20 + (i * 20)
            #create line function for creating horizontal lines
            self.canvas.create_line(x,638,x,-638,width = 2,fill="black")
        #looping for creating lines
        for i in range(80) :
            y = 20 - (i * 20)
            self.canvas.create_line(1018,-y,0,-y,width = 2,fill="black")

        #co-ordinates for positioning of cart images
        self.cart_positions = [(130, 130),(290, 290),(390, 390),(630,290),(830,90),(930,530)]
        #co-ordinates for positioning of receiver images
        self.receiver_positions = [(30, 10),(190, 10),(390, 10),(590,10),(790,10),(990,10)]

        #function call for loading assets/images
        self.load_assets()
        #function call for creating objects for images
        self.create_objects()

    def load_assets(self):
        try:
            #Image.open() Opens and Identifies given image
            self.receiver_body_image = Image.open("./assets/receiver.png")
            """
            The ImageTk module contains support to create and modify Tkinter BitmapImage and
            PhotoImage objects from PIL images and filedialog is used for the dialog box to
            appear when you are opening file from anywhere in your system or saving your file
            in a particular position or place.
            """
            self.receiver_body = ImageTk.PhotoImage(self.receiver_body_image)

            self.cart_image = Image.open("./assets/shopping-cart.png")
            self.cart = ImageTk.PhotoImage(self.cart_image)

        except Exception as e:
            self.root.destroy()
            raise e

    def create_objects(self):
        #looping for self.receiver_positions that contains co-ordinate for x and y position
        for x_position, y_position in self.receiver_positions:
            #To display a graphics image on a canvas we use convas.create image
            self.canvas.create_image(
                x_position, y_position, image=self.receiver_body, tag="receiver"
            )
        for x_position1, y_position1 in self.cart_positions:
            self.canvas.create_image(
                x_position1, y_position1, image=self.cart, tag="cart"
            )
#calling the main function
if __name__ == '__main__':
    #creating tkinter object
    root = Tk()
    # creating object for class SuperMarker
    app = SuperMarket()
    #mainloop() tells Python to run the Tkinter event loop
    app.mainloop()
