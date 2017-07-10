import tkinter as tk
from tkinter import ttk

# Fonts
LARGE_FONT = ("Verdana", 40)
MEDIUM_FONT = ("Verdana", 25)
SMALL_FONT = ("Verdana", 15)


class UmbrellaShop(tk.Tk):

    def __init__(self, *args, **kwargs):
        """ Creation of the Umbrella Shop """
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Umbrella Shop")
        container = ttk.Frame(self)
        container.grid(row=0, column=0)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        for page in (OrderPage, EditPage, BillingPage):
            frame = page(container, self)
            self.frames[page] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(OrderPage)

    def show_frame(self, cont):
        """ Bring frame to the user's view """
        frame = self.frames[cont]
        frame.tkraise()


class OrderPage(tk.Frame):

    def __init__(self, parent, controller):
        """ Where the user can order an umbrella """
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Header Image
        self.Logo = tk.PhotoImage(file="img/logo2.gif")
        self.login_page_logo = tk.Label(self, image=self.Logo)
        self.login_page_logo.grid(row=0, rowspan=12, column=0, columnspan=16)

        # Header
        new_order_label = ttk.Label(self, text="New order:", font=MEDIUM_FONT)
        new_order_label.grid(row=13, column=4, columnspan=8, pady=30)

        # Red Umbrella Label, price and amount
        self.red_label = ttk.Label(self, text="Red", font=SMALL_FONT,
                                   foreground="red")
        self.red_label.grid(row=14, column=1, columnspan=5, pady=10, sticky="W")
        self.red_price = ttk.Label(self, text="$39.00", font=SMALL_FONT)
        self.red_price.grid(row=14, column=6, columnspan=3, pady=10)
        self.red_amount = ttk.Entry(self, justify="center")
        self.red_amount.grid(row=14, column=10, columnspan=2, pady=10)

        # Blue Umbrella Label, price and amount
        self.blue_label = ttk.Label(self, text="Blue", font=SMALL_FONT,
                                    foreground="blue")
        self.blue_label.grid(row=15, column=1, columnspan=5, pady=10,
                             sticky="W")
        self.blue_price = ttk.Label(self, text="$39.00", font=SMALL_FONT)
        self.blue_price.grid(row=15, column=6, columnspan=3, pady=10)
        self.blue_amount = ttk.Entry(self, justify="center")
        self.blue_amount.grid(row=15, column=10, columnspan=2, pady=10)

        # Light Green Umbrella Label, price and amount
        self.light_green_label = ttk.Label(self, text="Light Green",
                                           font=SMALL_FONT, 
                                           foreground="light green")
        self.light_green_label.grid(row=16, column=1, columnspan=5, pady=10,
                                    sticky="W")
        self.light_green_price = ttk.Label(self, text="$39.00", font=SMALL_FONT)
        self.light_green_price.grid(row=16, column=6, columnspan=3, pady=10)
        self.light_green_amount = ttk.Entry(self, justify="center",)
        self.light_green_amount.grid(row=16, column=10, columnspan=2, pady=10)

        # Orange Umbrella Label, price and amount
        self.orange_label = ttk.Label(self, text="Orange", font=SMALL_FONT,
                                      foreground="orange")
        self.orange_label.grid(row=17, column=1, columnspan=5, pady=10,
                               sticky="W")
        self.orange_price = ttk.Label(self, text="$39.00", font=SMALL_FONT)
        self.orange_price.grid(row=17, column=6, columnspan=3, pady=10)
        self.orange_amount = ttk.Entry(self, justify="center",)
        self.orange_amount.grid(row=17, column=10, columnspan=2, pady=10)

        # Dark Grey Umbrella Label, price and amount
        self.dark_grey_label = ttk.Label(self, text="Dark Grey",
                                         font=SMALL_FONT,
                                         foreground="dark grey")
        self.dark_grey_label.grid(row=18, column=1, columnspan=5, pady=10,
                                  sticky="W")
        self.dark_grey_price = ttk.Label(self, text="$39.00", font=SMALL_FONT)
        self.dark_grey_price.grid(row=18, column=6, columnspan=3, pady=10)
        self.dark_grey_amount = ttk.Entry(self, justify="center",)
        self.dark_grey_amount.grid(row=18, column=10, columnspan=2, pady=10)

        # Clear Umbrella Label, price and amount
        self.clear_label = ttk.Label(self, text="Transparent", font=SMALL_FONT,
                                     foreground="black")
        self.clear_label.grid(row=19, column=1, columnspan=5, pady=10,
                              sticky="W")
        self.clear_grey_price = ttk.Label(self, text="$39.00", font=SMALL_FONT)
        self.clear_grey_price.grid(row=19, column=6, columnspan=3, pady=10)
        self.clear_grey_amount = ttk.Entry(self, justify="center",)
        self.clear_grey_amount.grid(row=19, column=10, columnspan=2, pady=10)

        self.cart_img = tk.PhotoImage(file="img/cart_button.gif")
        cart_command = (lambda: controller.show_frame(BillingPage))
        self.cart_button = tk.Button(self, compound=tk.TOP, relief="flat",
                                     width=80, height=40, image=self.cart_img,
                                     command=cart_command)
        self.cart_button.grid(row=20, column=9, columnspan=4, sticky="W",
                              pady=5)
        self.cart_button.image = self.cart_img


class EditPage(tk.Frame):

    def __init__(self, parent, controller):
        """ Where the user can edit their order """
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.Logo = tk.PhotoImage(file="img/logo2.gif")
        self.login_page_logo = tk.Label(self, image=self.Logo)
        self.login_page_logo.grid(row=0, rowspan=12, column=0, columnspan=16)
        
        # Header
        welcome_label = ttk.Label(self, text="Edit:", font=MEDIUM_FONT)
        welcome_label.grid(row=13, column=4, columnspan=8, pady=30)

        # Red Umbrella Label, price and amount
        self.red_label = ttk.Label(self, text="Red", font=SMALL_FONT,
                                   foreground="red")
        self.red_label.grid(row=14, column=1, columnspan=5, pady=10, sticky="W")
        self.red_price = ttk.Label(self, text="$39.00", font=SMALL_FONT)
        self.red_price.grid(row=14, column=6, columnspan=3, pady=10)
        self.red_amount = ttk.Entry(self, justify="center")
        self.red_amount.grid(row=14, column=10, columnspan=2, pady=10)

        # Blue Umbrella Label, price and amount
        self.blue_label = ttk.Label(self, text="Blue", font=SMALL_FONT,
                                    foreground="blue")
        self.blue_label.grid(row=15, column=1, columnspan=5, pady=10,
                             sticky="W")
        self.blue_price = ttk.Label(self, text="$39.00", font=SMALL_FONT)
        self.blue_price.grid(row=15, column=6, columnspan=3, pady=10)
        self.blue_amount = ttk.Entry(self, justify="center")
        self.blue_amount.grid(row=15, column=10, columnspan=2, pady=10)

        # Light Green Umbrella Label, price and amount
        self.light_green_label = ttk.Label(self, text="Light Green",
                                           font=SMALL_FONT, 
                                           foreground="light green")
        self.light_green_label.grid(row=16, column=1, columnspan=5, pady=10,
                                    sticky="W")
        self.light_green_price = ttk.Label(self, text="$39.00", font=SMALL_FONT)
        self.light_green_price.grid(row=16, column=6, columnspan=3, pady=10)
        self.light_green_amount = ttk.Entry(self, justify="center")
        self.light_green_amount.grid(row=16, column=10, columnspan=2, pady=10)

        # Orange Umbrella Label, price and amount
        self.orange_label = ttk.Label(self, text="Orange", font=SMALL_FONT,
                                      foreground="orange")
        self.orange_label.grid(row=17, column=1, columnspan=5, pady=10,
                               sticky="W")
        self.orange_price = ttk.Label(self, text="$39.00", font=SMALL_FONT)
        self.orange_price.grid(row=17, column=6, columnspan=3, pady=10)
        self.orange_amount = ttk.Entry(self, justify="center")
        self.orange_amount.grid(row=17, column=10, columnspan=2, pady=10)

        # Dark Grey Umbrella Label, price and amount
        self.dark_grey_label = ttk.Label(self, text="Dark Grey",
                                         font=SMALL_FONT,
                                         foreground="dark grey")
        self.dark_grey_label.grid(row=18, column=1, columnspan=5, pady=10,
                                  sticky="W")
        self.dark_grey_price = ttk.Label(self, text="$39.00", font=SMALL_FONT)
        self.dark_grey_price.grid(row=18, column=6, columnspan=3, pady=10)
        self.dark_grey_amount = ttk.Entry(self, justify="center")
        self.dark_grey_amount.grid(row=18, column=10, columnspan=2, pady=10)

        # Clear Umbrella Label, price and amount
        self.clear_label = ttk.Label(self, text="Transparent", font=SMALL_FONT,
                                     foreground="black")
        self.clear_label.grid(row=19, column=1, columnspan=5, pady=10,
                              sticky="W")
        self.clear_grey_price = ttk.Label(self, text="$39.00", font=SMALL_FONT)
        self.clear_grey_price.grid(row=19, column=6, columnspan=3, pady=10)
        self.clear_grey_amount = ttk.Entry(self, justify="center")
        self.clear_grey_amount.grid(row=19, column=10, columnspan=2, pady=10)

        self.cart_img = tk.PhotoImage(file="img/cart_button.gif")
        cart_command = (lambda: controller.show_frame(BillingPage))
        self.cart_button = tk.Button(self, compound=tk.TOP, relief="flat",
                                     width=80, height=40, image=self.cart_img,
                                     command=cart_command)
        self.cart_button.grid(row=20, column=9, columnspan=4, sticky="W",
                              pady=5)
        self.cart_button.image = self.cart_img


class BillingPage(tk.Frame):

    def __init__(self, parent, controller):
        """ Where the user can confirm and pay for their order """
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.order_number = 1

        # Header Image
        self.Logo = tk.PhotoImage(file="img/logo2.gif")
        self.login_page_logo = tk.Label(self, image=self.Logo)
        self.login_page_logo.grid(row=0, rowspan=12, column=0, columnspan=16)

        # Header
        welcome_label = ttk.Label(self, text="Your order:", font=MEDIUM_FONT)
        welcome_label.grid(row=12, column=1, columnspan=8, pady=30, sticky="E")

        # Delivery Labels and Entries
        self.name_label = ttk.Label(self, text="Full name:")
        self.name_label.grid(row=13, column=1, sticky='W')
        self.name = ttk.Entry(self)
        self.name.grid(row=13, column=2, columnspan=3, sticky="e", pady=5)

        self.phone_label = ttk.Label(self, text="Phone number:")
        self.phone_label.grid(row=13, column=7, sticky='W')
        self.phone = ttk.Entry(self)
        self.phone.grid(row=13, column=8, columnspan=7, sticky="e")

        self.address_label = ttk.Label(self, text="Street address:")
        self.address_label.grid(row=14, column=1, sticky='W')
        self.address = ttk.Entry(self)
        self.address.grid(row=14, column=2, columnspan=3, sticky="e")

        self.city_label = ttk.Label(self, text="City:")
        self.city_label.grid(row=14, column=7, sticky='W')
        self.city = ttk.Entry(self)
        self.city.grid(row=14, column=8, columnspan=7, sticky="e")

        self.postcode_label = ttk.Label(self, text="Postcode:")
        self.postcode_label.grid(row=15, column=1, sticky='W')
        self.postcode = ttk.Entry(self)
        self.postcode.grid(row=15, column=2, columnspan=3, sticky="e", pady=5)

        # Buttons
        self.confirm_img = tk.PhotoImage(file="img/confirm_button.gif")
        confirm_command = (lambda: self.print_order())
        self.confirm_button = tk.Button(self, compound=tk.TOP, relief="flat",
                                        width=200, height=40,
                                        image=self.confirm_img,
                                        command=confirm_command,
                                        state='disabled')
        self.confirm_button.grid(row=25, column=1, columnspan=10, sticky="E",
                                 pady=5, padx=10)
        self.confirm_button.image = self.confirm_img

        self.edit_img = tk.PhotoImage(file="img/edit_button.gif")
        edit_command = (lambda: controller.show_frame(EditPage))
        self.edit_button = tk.Button(self, compound=tk.TOP, relief="flat",
                                     width=80, height=40, image=self.edit_img,
                                     command=edit_command)
        self.edit_button.grid(row=30, column=4, columnspan=4, sticky="W",
                              pady=5)
        self.edit_button.image = self.edit_img

        self.new_img = tk.PhotoImage(file="img/new_button.gif")
        new_command = (lambda: controller.show_frame(OrderPage))
        self.new_button = tk.Button(self, compound=tk.TOP, relief="flat",
                                    width=80, height=40, image=self.new_img,
                                    command=new_command)
        self.new_button.grid(row=30, column=13, columnspan=4, sticky="W",
                             pady=5)
        self.new_button.image = self.new_img


def main():
    """ Start of the program. """
    app = UmbrellaShop()

    w = 450
    h = 600

    ws = app.winfo_screenwidth()
    hs = app.winfo_screenheight()

    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    app.geometry('%dx%d+%d+%d' % (w, h, x, y))
    app.resizable(width=False, height=False)
    app.mainloop()

if __name__ == '__main__':
    main()
