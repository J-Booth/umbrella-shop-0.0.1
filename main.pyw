# =============================================================================
# Author: Joshua Peter Booth
# Purpose: Umbrella Shop (GUI)
# File name: main.pyw
# From: 12/06/2017 - 30/06/2017
# =============================================================================

from __init__ import *

logger.disabled = False


class UmbrellaShop(tk.Tk):

    def __init__(self, *args, **kwargs):
        """
        Creation of the Umbrella Shop
        """
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
        """
        A tkinter frame where the user can order an umbrella.
        """
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Header Image
        self.logo = tk.PhotoImage(file="img/logo.gif")
        self.logo_label = tk.Label(self, image=self.logo)
        self.logo_label.grid(row=0, rowspan=12, column=0, columnspan=16)

        # Header
        new_order_label = ttk.Label(self, text="New order:", font=MEDIUM_FONT)
        new_order_label.grid(row=13, column=4, columnspan=8, pady=30)

        # Umbrella colour labels and prices

        # Red umbrella label, price and amount entry
        self.red_label = ttk.Label(self, text="Red", font=SMALL_FONT,
                                   foreground="red")
        self.red_label.grid(row=14, column=1, columnspan=5, pady=10,
                            sticky="W")
        self.red_price = ttk.Label(self, text="$39.00", font=SMALL_FONT)
        self.red_price.grid(row=14, column=7, columnspan=3, pady=10)
        red_vcmd = (self.register(self.confirm), '%P', '%S', 'red')
        self.red_amount = ttk.Entry(self, validate="key", justify="center",
                                    validatecommand=red_vcmd)
        self.red_amount.grid(row=14, column=11, columnspan=2, pady=10)

        # Blue umbrella label, price and amount entry
        self.blue_label = ttk.Label(self, text="Blue", font=SMALL_FONT,
                                    foreground="blue")
        self.blue_label.grid(row=15, column=1, columnspan=5, pady=10,
                             sticky="W")
        self.blue_price = ttk.Label(self, text="$39.00", font=SMALL_FONT)
        self.blue_price.grid(row=15, column=7, columnspan=3, pady=10)
        blue_vcmd = (self.register(self.confirm), '%P', '%S', 'blue')
        self.blue_amount = ttk.Entry(self, validate="key", justify="center",
                                     validatecommand=blue_vcmd)
        self.blue_amount.grid(row=15, column=11, columnspan=2, pady=10)

        # Light Green umbrella label, price and amount entry
        self.l_green_label = ttk.Label(self, text="Light Green",
                                       font=SMALL_FONT,
                                       foreground="light green")
        self.l_green_label.grid(row=16, column=1, columnspan=5, pady=10,
                                sticky="W")
        self.l_green_price = ttk.Label(self, text="$39.00", font=SMALL_FONT)
        self.l_green_price.grid(row=16, column=7, columnspan=3, pady=10)
        l_green_vcmd = (self.register(self.confirm), '%P', '%S', 'light_green')
        self.l_green_amount = ttk.Entry(self, validate="key", justify="center",
                                        validatecommand=l_green_vcmd)
        self.l_green_amount.grid(row=16, column=11, columnspan=2, pady=10)

        # Orange umbrella label, price and amount entry
        self.orange_label = ttk.Label(self, text="Orange", font=SMALL_FONT,
                                      foreground="orange")
        self.orange_label.grid(row=17, column=1, columnspan=5, pady=10,
                               sticky="W")
        self.orange_price = ttk.Label(self, text="$39.00", font=SMALL_FONT)
        self.orange_price.grid(row=17, column=7, columnspan=3, pady=10)
        orange_vcmd = (self.register(self.confirm), '%P', '%S', 'orange')
        self.orange_amount = ttk.Entry(self, validate="key", justify="center",
                                       validatecommand=orange_vcmd)
        self.orange_amount.grid(row=17, column=11, columnspan=2, pady=10)

        # Dark Grey umbrella label, price and amount entry
        self.d_grey_label = ttk.Label(self, text="Dark Grey", font=SMALL_FONT,
                                      foreground="dark grey")
        self.d_grey_label.grid(row=18, column=1, columnspan=5, pady=10,
                               sticky="W")
        self.d_grey_price = ttk.Label(self, text="$39.00", font=SMALL_FONT)
        self.d_grey_price.grid(row=18, column=7, columnspan=3, pady=10)
        d_grey_vcmd = (self.register(self.confirm), '%P', '%S', 'dark_grey')
        self.d_grey_amount = ttk.Entry(self, validate="key", justify="center",
                                       validatecommand=d_grey_vcmd)
        self.d_grey_amount.grid(row=18, column=11, columnspan=2, pady=10)

        # Clear umbrella label, price and amount entry
        self.clear_label = ttk.Label(self, text="Transparent", font=SMALL_FONT,
                                     foreground="black")
        self.clear_label.grid(row=19, column=1, columnspan=5, pady=10,
                              sticky="W")
        self.clear_price = ttk.Label(self, text="$39.00", font=SMALL_FONT)
        self.clear_price.grid(row=19, column=7, columnspan=3, pady=10)
        clear_vcmd = (self.register(self.confirm), '%P', '%S', 'clear')
        self.clear_amount = ttk.Entry(self, validate="key", justify="center",
                                      validatecommand=clear_vcmd)
        self.clear_amount.grid(row=19, column=11, columnspan=2, pady=10)

        # Buttons

        # Erase button
        self.erase_button = ttk.Button(self, text="Erase all",
                                       command=lambda: self.erase())
        self.erase_button.grid(row=20, column=10, columnspan=4, pady=5)

        # Cart button
        self.cart_img = tk.PhotoImage(file="img/cart_button.gif")
        cart_command = (lambda: self.controller.show_frame(BillingPage))
        self.cart_button = tk.Button(self, compound=tk.TOP, relief="flat",
                                     width=80, height=40, image=self.cart_img,
                                     command=cart_command, state='disabled')
        self.cart_button.grid(row=21, column=12, columnspan=16, pady=5)
        self.cart_button.image = self.cart_img

    def erase(self):
        """
        Removes all data from the entries.
        """
        self.red_amount.delete(0, 4)
        self.red_amount.insert(0, "")
        self.blue_amount.delete(0, 4)
        self.blue_amount.insert(0, "")
        self.l_green_amount.delete(0, 4)
        self.l_green_amount.insert(0, "")
        self.orange_amount.delete(0, 4)
        self.orange_amount.insert(0, "")
        self.d_grey_amount.delete(0, 4)
        self.d_grey_amount.insert(0, "")
        self.clear_amount.delete(0, 4)
        self.clear_amount.insert(0, "")

    def confirm(self, P, S, colour):
        """
        Disallow anything but a 1-4 digit integer. If the total of all values
        is greater than one, enable the cart button.

        :param P: allowed value (%P)
        :param S: text being inserted (%S)
        :param colour: the umbrella colour (str)
        :return: True or False
        """
        allowed_value = P  # So the values of P and S are understandable
        inserted_value = S  # But are set as param so that %P and %S are used.

        if len(allowed_value) == 0:
            inserted_value = 0
            allowed_value = "0"
        else:
            try:
                inserted_value = int(inserted_value)
                print("Input accepted.")
            except ValueError:
                print("Input is not an integer!")
        if isinstance(inserted_value, int) and 1 <= len(allowed_value) <= 4:
            with open(CURRENT_DATA_F, 'r') as file:
                current_data = [line.strip() for line in file]
            data = {}
            with open(CURRENT_DATA_F, 'r') as file:
                for line in file:
                    option, value = line.strip().split(':')
                    data[option] = value
            if data[colour] == str(allowed_value):
                print("No changes to be made to {}".format(CURRENT_DATA_F))
            else:
                current_data.remove('{}:{}'.format(colour, data[colour]))
                current_data.remove('{}:{}'.format('total', data['total']))
                data[colour] = int(allowed_value)
                data['total'] = 0
                total = 0
                for item in current_data:
                    item = item.split(':')
                    item.pop(0)
                    total += int(item[0])
                data['total'] = total + data[colour]
                current_data.append('{}:{}'.format(colour, data[colour]))
                current_data.append('{}:{}'.format('total', data['total']))
            if int(data['total']) > 0:
                self.cart_button.configure(state='normal')
            else:
                self.cart_button.configure(state='disabled')
            with open(CURRENT_DATA_F, 'w') as file:
                print("Writing new data to {}".format(CURRENT_DATA_F))
                file.write('\n'.join(current_data))
            return True
        else:
            self.bell()
            return False


class EditPage(tk.Frame):
    def __init__(self, parent, controller):
        """
        A tkinter frame where the user can edit their order
        """
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Header Image
        self.logo = tk.PhotoImage(file="img/logo.gif")
        self.logo_label = tk.Label(self, image=self.logo)
        self.logo_label.grid(row=0, rowspan=12, column=0, columnspan=16)

        # Header
        edit_label = ttk.Label(self, text="Edit:", font=MEDIUM_FONT)
        edit_label.grid(row=13, column=4, columnspan=8, pady=30)

        # Umbrella colour labels, prices and amounts

        # Red umbrella label, price and amount
        self.red_label = ttk.Label(self, text="Red", font=SMALL_FONT,
                                   foreground="red")
        self.red_label.grid(row=14, column=1, columnspan=5, pady=10,
                            sticky="W")
        self.red_price = ttk.Label(self, text="$39.00", font=SMALL_FONT)
        self.red_price.grid(row=14, column=7, columnspan=3, pady=10)
        red_vcmd = (self.register(self.confirm), '%P', '%S', 'red')
        self.red_amount = ttk.Entry(self, validate="key", justify="center",
                                    validatecommand=red_vcmd)
        self.red_amount.grid(row=14, column=11, columnspan=2, pady=10)

        # Blue umbrella label, price and amount
        self.blue_label = ttk.Label(self, text="Blue", font=SMALL_FONT,
                                    foreground="blue")
        self.blue_label.grid(row=15, column=1, columnspan=5, pady=10,
                             sticky="W")
        self.blue_price = ttk.Label(self, text="$39.00", font=SMALL_FONT)
        self.blue_price.grid(row=15, column=7, columnspan=3, pady=10)
        blue_vcmd = (self.register(self.confirm), '%P', '%S', 'blue')
        self.blue_amount = ttk.Entry(self, validate="key", justify="center",
                                     validatecommand=blue_vcmd)
        self.blue_amount.grid(row=15, column=11, columnspan=2, pady=10)

        # Light Green umbrella label, price and amount
        self.l_green_label = ttk.Label(self, text="Light Green",
                                       font=SMALL_FONT,
                                       foreground="light green")
        self.l_green_label.grid(row=16, column=1, columnspan=5, pady=10,
                                sticky="W")
        self.l_green_price = ttk.Label(self, text="$39.00", font=SMALL_FONT)
        self.l_green_price.grid(row=16, column=7, columnspan=3, pady=10)
        l_green_vcmd = (self.register(self.confirm), '%P', '%S', 'light_green')
        self.l_green_amount = ttk.Entry(self, validate="key", justify="center",
                                        validatecommand=l_green_vcmd)
        self.l_green_amount.grid(row=16, column=11, columnspan=2, pady=10)

        # Orange umbrella label, price and amount
        self.orange_label = ttk.Label(self, text="Orange", font=SMALL_FONT,
                                      foreground="orange")
        self.orange_label.grid(row=17, column=1, columnspan=5, pady=10,
                               sticky="W")
        self.orange_price = ttk.Label(self, text="$39.00", font=SMALL_FONT)
        self.orange_price.grid(row=17, column=7, columnspan=3, pady=10)
        orange_vcmd = (self.register(self.confirm), '%P', '%S', 'orange')
        self.orange_amount = ttk.Entry(self, validate="key",
                                       justify="center",
                                       validatecommand=orange_vcmd)
        self.orange_amount.grid(row=17, column=11, columnspan=2, pady=10)

        # Dark Grey umbrella label, price and amount
        self.d_grey_label = ttk.Label(self, text="Dark Grey",
                                      font=SMALL_FONT,
                                      foreground="dark grey")
        self.d_grey_label.grid(row=18, column=1, columnspan=5, pady=10,
                               sticky="W")
        self.d_grey_price = ttk.Label(self, text="$39.00", font=SMALL_FONT)
        self.d_grey_price.grid(row=18, column=7, columnspan=3, pady=10)
        d_grey_vcmd = (self.register(self.confirm), '%P', '%S', 'dark_grey')
        self.d_grey_amount = ttk.Entry(self, validate="key", justify="center",
                                       validatecommand=d_grey_vcmd)
        self.d_grey_amount.grid(row=18, column=11, columnspan=2, pady=10)

        # Clear umbrella label, price and amount
        self.clear_label = ttk.Label(self, text="Transparent", font=SMALL_FONT,
                                     foreground="black")
        self.clear_label.grid(row=19, column=1, columnspan=5, sticky="W")
        self.clear_price = ttk.Label(self, text="$39.00", font=SMALL_FONT)
        self.clear_price.grid(row=19, column=7, columnspan=3)
        clear_vcmd = (self.register(self.confirm), '%P', '%S', 'clear')
        self.clear_amount = ttk.Entry(self, validate="key",
                                      justify="center",
                                      validatecommand=clear_vcmd)
        self.clear_amount.grid(row=19, column=11, columnspan=2)

        # Current values
        self.current_red = ttk.Label(self, text="0", foreground="green")
        self.current_red.grid(row=14, column=14, columnspan=1, pady=10,
                              sticky="W")
        self.current_blue = ttk.Label(self, text="0", foreground="green")
        self.current_blue.grid(row=15, column=14, columnspan=1, pady=10,
                               sticky="W")
        self.current_l_green = ttk.Label(self, text="0", foreground="green")
        self.current_l_green.grid(row=16, column=14, columnspan=1, pady=10,
                                  sticky="W")
        self.current_orange = ttk.Label(self, text="0", foreground="green")
        self.current_orange.grid(row=17, column=14, columnspan=1, pady=10,
                                 sticky="W")
        self.current_d_grey = ttk.Label(self, text="0", foreground="green")
        self.current_d_grey.grid(row=18, column=14, columnspan=1, pady=10,
                                 sticky="W")
        self.current_clear = ttk.Label(self, text="0", foreground="green")
        self.current_clear.grid(row=19, column=14, columnspan=1, pady=10,
                                sticky="W")
        self.current_amount()

        # Type labels
        self.new_label = ttk.Label(self, text="*New", foreground="red")
        self.new_label.grid(row=20, column=11, columnspan=2, pady=10)
        self.current_label = ttk.Label(self, text="*Current",
                                       foreground="green")
        self.current_label.grid(row=20, column=12, columnspan=18, pady=10)

        # Cart button
        self.cart_img = tk.PhotoImage(file="img/cart_button.gif")
        cart_command = (lambda: self.controller.show_frame(BillingPage))
        self.cart_button = tk.Button(self, compound=tk.TOP, relief="flat",
                                     width=80, height=40, image=self.cart_img,
                                     command=cart_command)
        self.cart_button.grid(row=22, column=12, columnspan=16)
        self.cart_button.image = self.cart_img

    def confirm(self, P, S, colour):
        """
        Disallow anything but a 1-4 digit integer. If the total of all values
        is greater than one, enable the cart button.

        :param P: allowed value (%P)
        :param S: text being inserted (%S)
        :param colour: the umbrella colour (str)
        :return: True or False
        """
        allowed_value = P  # So the values of P and S are understandable
        inserted_value = S  # But are set as param so that %P and %S are used.

        if len(allowed_value) == 0:
            inserted_value = 0
            allowed_value = "0"
        else:
            try:
                inserted_value = int(inserted_value)
            except ValueError:
                print("Input is not an integer!")
        if isinstance(inserted_value, int) and 1 <= len(allowed_value) <= 4:
            with open(CURRENT_DATA_F, 'r') as file:
                current_data = [line.strip() for line in file]
            data = {}
            with open(CURRENT_DATA_F, 'r') as file:
                for line in file:
                    option, value = line.strip().split(':')
                    data[option] = value
            if data[colour] == str(allowed_value):
                print("No changes to be made to {}".format(CURRENT_DATA_F))
            else:
                current_data.remove('{}:{}'.format(colour, data[colour]))
                current_data.remove('{}:{}'.format('total', data['total']))
                data[colour] = int(allowed_value)
                data['total'] = 0
                total = 0
                for item in current_data:
                    item = item.split(':')
                    item.pop(0)
                    total += int(item[0])
                data['total'] = total + data[colour]
                current_data.append('{}:{}'.format(colour, data[colour]))
                current_data.append('{}:{}'.format('total', data['total']))
            if int(data['total']) > 0:
                self.cart_button.configure(state='normal')
                logger.info(data)
            else:
                self.cart_button.configure(state='disabled')
            with open(CURRENT_DATA_F, 'w') as file:
                print("Writing to {}".format(CURRENT_DATA_F))
                file.write('\n'.join(current_data))
            return True
        else:
            self.bell()
            return False

    def current_amount(self):
        """
        Displays the current number of umbrellas ordered for each colour.
        """
        data = {}
        with open(CURRENT_DATA_F, 'r') as file:
            for line in file:
                option, value = line.strip().split(':')
                data[option] = int(value)

        for colour in data:
            if colour == 'red' and int(data[colour]) >= 0:
                self.current_red.configure(text=data[colour])
            elif colour == 'blue' and int(data[colour]) >= 0:
                self.current_blue.configure(text=data[colour])
            elif colour == 'light_green' and int(data[colour]) >= 0:
                self.current_l_green.configure(text=data[colour])
            elif colour == 'orange' and int(data[colour]) >= 0:
                self.current_orange.configure(text=data[colour])
            elif colour == 'dark_grey' and int(data[colour]) >= 0:
                self.current_d_grey.configure(text=data[colour])
            elif colour == 'clear' and int(data[colour]) >= 0:
                self.current_clear.configure(text=data[colour])
            else:
                continue

        self.clear_label.after(1500, lambda: self.current_amount())


class BillingPage(tk.Frame):

    def __init__(self, parent, controller):
        """
        A tkinter frame where the user can confirm and pay for their order.
        """
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.order_number = 1  # Default order number

        # Header Image
        self.logo = tk.PhotoImage(file="img/logo.gif")
        self.logo_label = tk.Label(self, image=self.logo)
        self.logo_label.grid(row=0, rowspan=12, column=0, columnspan=16)

        # Header
        order_label = ttk.Label(self, text="Your order:", font=MEDIUM_FONT)
        order_label.grid(row=12, column=1, columnspan=8, pady=30, sticky="E")

        # Delivery labels and entries

        # Name label and entry
        self.name_label = ttk.Label(self, text="Full name:")
        self.name_label.grid(row=13, column=1, sticky='W')
        self.name = ttk.Entry(self)
        self.name.grid(row=13, column=2, columnspan=3, sticky="e", pady=5)

        # Phone label and entry
        self.phone_label = ttk.Label(self, text="Phone number:")
        self.phone_label.grid(row=13, column=7, sticky='W')
        self.phone = ttk.Entry(self)
        self.phone.grid(row=13, column=8, columnspan=7, sticky="e")

        # Address label and entry
        self.address_label = ttk.Label(self, text="Street address:")
        self.address_label.grid(row=14, column=1, sticky='W')
        self.address = ttk.Entry(self)
        self.address.grid(row=14, column=2, columnspan=3, sticky="e")

        # City label and entry
        self.city_label = ttk.Label(self, text="City:")
        self.city_label.grid(row=14, column=7, sticky='W')
        self.city = ttk.Entry(self)
        self.city.grid(row=14, column=8, columnspan=7, sticky="e")

        # Postcode label, entry and its validate command (vcmd)
        self.postcode_label = ttk.Label(self, text="Postcode:")
        self.postcode_label.grid(row=15, column=1, sticky='W')
        postcode_vcmd = (self.register(self.confirm), '%P', '%S')
        self.postcode = ttk.Entry(self, validate="key",
                                  validatecommand=postcode_vcmd)
        self.postcode.grid(row=15, column=2, columnspan=3, sticky="e", pady=5)

        # Order headers

        # Colour header
        self.colour_label = ttk.Label(self, text="Colour", font=SMALL_FONT)
        self.colour_label.grid(row=17, column=1, pady=10, sticky='W')

        # Quantity header
        self.quantity_label = ttk.Label(self, text="Quantity", font=SMALL_FONT)
        self.quantity_label.grid(row=17, column=2, columnspan=8, padx=5)

        # Total header
        self.total_label = ttk.Label(self, text="Total", font=SMALL_FONT)
        self.total_label.grid(row=17, column=8, columnspan=8)

        # Colour labels

        # Red umbrella label, amount and total cost
        self.red_label = ttk.Label(self, text=" ")
        self.red_label.grid(row=18, column=1, columnspan=2,
                            sticky='W', padx=20)
        self.red_amount_label = ttk.Label(self, text=" ")
        self.red_amount_label.grid(row=18, column=2, columnspan=8)
        self.red_total = " "
        self.red_total_label = ttk.Label(self, text=self.red_total)
        self.red_total_label.grid(row=18, column=8, columnspan=8)

        # Blue umbrella label, amount and total cost
        self.blue_label = ttk.Label(self, text=" ")
        self.blue_label.grid(row=19, column=1, columnspan=2, sticky='W',
                             padx=20)
        self.blue_amount_label = ttk.Label(self, text=" ")
        self.blue_amount_label.grid(row=19, column=2, columnspan=8)
        self.blue_total = " "
        self.blue_total_label = ttk.Label(self, text=self.blue_total)
        self.blue_total_label.grid(row=19, column=8, columnspan=8)

        # Light green umbrella label, amount and total cost
        self.l_green_label = ttk.Label(self, text=" ")
        self.l_green_label.grid(row=20, column=1, columnspan=2, sticky='W',
                                padx=20)
        self.l_green_amount_label = ttk.Label(self, text=" ")
        self.l_green_amount_label.grid(row=20, column=2, columnspan=8)
        self.l_green_total = " "
        self.l_green_total_label = ttk.Label(self, text=self.l_green_total)
        self.l_green_total_label.grid(row=20, column=8, columnspan=8)

        # Orange umbrella label, amount and total cost
        self.orange_label = ttk.Label(self, text=" ")
        self.orange_label.grid(row=21, column=1, columnspan=2, sticky='W',
                               padx=20)
        self.orange_amount_label = ttk.Label(self, text=" ")
        self.orange_amount_label.grid(row=21, column=2, columnspan=8)
        self.orange_total = " "
        self.orange_total_label = ttk.Label(self, text=self.orange_total)
        self.orange_total_label.grid(row=21, column=8, columnspan=8)

        # Dark grey umbrella label, amount and total cost
        self.d_grey_label = ttk.Label(self, text=" ")
        self.d_grey_label.grid(row=22, column=1, columnspan=2, sticky='W',
                               padx=20)
        self.d_grey_amount_label = ttk.Label(self, text=" ")
        self.d_grey_amount_label.grid(row=22, column=2, columnspan=8)
        self.d_grey_total = " "
        self.d_grey_total_label = ttk.Label(self, text=self.d_grey_total)
        self.d_grey_total_label.grid(row=22, column=8, columnspan=8)

        # Transparent umbrella label, amount and total cost
        self.clear_label = ttk.Label(self, text=" ")
        self.clear_label.grid(row=23, column=1, columnspan=2, sticky='W',
                              padx=20)
        self.clear_amount_label = ttk.Label(self, text=" ")
        self.clear_amount_label.grid(row=23, column=2, columnspan=8)
        self.clear_total = " "
        self.clear_total_label = ttk.Label(self, text=self.clear_total)
        self.clear_total_label.grid(row=23, column=8, columnspan=8)

        # Final cost label and final cost amount
        self.final_cost_label = ttk.Label(self, text="Final Cost:",
                                          font=SMALL_FONT)
        self.final_cost_label.grid(row=24, column=2, columnspan=5, pady=5)
        self.final_cost = " "
        self.final_cost_amount = ttk.Label(self, text=self.final_cost,
                                           font=SMALL_FONT)
        self.final_cost_amount.grid(row=24, column=5, columnspan=7)

        # Final cost includes delivery label
        delivery_message = "* Final cost includes the cost of delivery"
        self.delivery_label = ttk.Label(self, text=delivery_message)
        self.delivery_label.grid(row=25, column=2, columnspan=7)

        # Buttons

        # Confirm button
        self.confirm_img = tk.PhotoImage(file="img/confirm_button.gif")
        confirm_command = (lambda: self.print_order())
        self.confirm_button = tk.Button(self, compound=tk.TOP, relief="flat",
                                        width=200, height=40,
                                        image=self.confirm_img,
                                        command=confirm_command,
                                        state='disabled')
        self.confirm_button.grid(row=26, column=1, columnspan=10, sticky="E",
                                 pady=5, padx=10)
        self.confirm_button.image = self.confirm_img

        # Edit button
        self.edit_img = tk.PhotoImage(file="img/edit_button.gif")
        edit_command = (lambda: controller.show_frame(EditPage))
        self.edit_button = tk.Button(self, compound=tk.TOP, relief="flat",
                                     width=80, height=40, image=self.edit_img,
                                     command=edit_command)
        self.edit_button.grid(row=30, column=4, columnspan=4, sticky="W",
                              pady=5)
        self.edit_button.image = self.edit_img

        # New order button
        self.new_img = tk.PhotoImage(file="img/new_button.gif")
        new_command = (lambda: controller.show_frame(OrderPage))
        self.new_button = tk.Button(self, compound=tk.TOP, relief="flat",
                                    width=80, height=40, image=self.new_img,
                                    command=new_command)
        self.new_button.grid(row=30, column=13, columnspan=4, sticky="W",
                             pady=5)
        self.new_button.image = self.new_img

        # Order form
        self.order_form()

    @staticmethod
    def order_no(increase=0):
        """
        Get the current order number.
        """
        with open(ORDER_NUMBER_F, 'r') as file:
            order_number = int(file.read())
        if increase > 0:
            with open(ORDER_NUMBER_F, 'w') as file:
                order_number += 1
                file.write(str(order_number))
        elif increase < 0:
            return None
        elif increase == 0:
            pass
        else:
            logger.error("Received unexpected input!")
        return order_number

    def print_order(self):
        """
        Write the order to a newly created file.
        """
        self.order_number = self.order_no()
        try:
            # Save order files to the 'saves' directory
            order_file = "saves\order_{}.txt".format(self.order_number)

            fullname = self.name.get()
            address = self.address.get()
            postcode = self.postcode.get()
            city = self.city.get()
            phone = self.phone.get()

            red_amount = int(self.red_amount_label.cget("text")) \
                if self.red_amount_label.cget("text") != ' ' else 0
            red_total = int(self.red_total) \
                if self.red_total != ' ' and red_amount != 0 else 0
            blue_amount = int(self.blue_amount_label.cget("text")) \
                if self.blue_amount_label.cget("text") != ' ' else 0
            blue_total = int(self.blue_total) \
                if self.blue_total != ' ' and blue_amount != 0 else 0
            l_green_amount = int(self.l_green_amount_label.cget("text")) \
                if self.l_green_amount_label.cget("text") != ' ' else 0
            l_green_total = int(self.l_green_total) \
                if self.l_green_total != ' ' and l_green_amount != 0 else 0
            orange_amount = int(self.orange_amount_label.cget("text")) \
                if self.orange_amount_label.cget("text") != ' ' else 0
            orange_total = int(self.orange_total) \
                if self.orange_total != ' ' and orange_amount != 0 else 0
            d_grey_amount = int(self.d_grey_amount_label.cget("text")) \
                if self.d_grey_amount_label.cget("text") != ' ' else 0
            d_grey_total = int(self.d_grey_total) \
                if self.d_grey_total != ' ' and d_grey_amount != 0 else 0
            clear_amount = int(self.clear_amount_label.cget("text")) \
                if self.clear_amount_label.cget("text") != ' ' else 0
            clear_total = int(self.clear_total) \
                if self.clear_total != ' ' and clear_amount != 0 else 0

            total_items = red_amount + blue_amount + l_green_amount + \
                orange_amount + d_grey_amount + clear_amount

            total_cost = red_total + blue_total + l_green_total + \
                orange_total + d_grey_total + clear_total

            if total_items == 1:
                delivery_cost = 4
            elif total_items == 2 or total_items == 3:
                delivery_cost = 7
            elif total_items >= 4:
                delivery_cost = 13
            else:
                delivery_cost = "False"
                logger.error("total_items failed to convert to an integer.")

            final_cost = total_cost + delivery_cost \
                if isinstance(delivery_cost, int) \
                else logger.critical("Failed to convert delivery cost to int.")

            order = """
-----------------------------------
            Umbrella Shop
            Order No. {0}

Deliver to:
{1}
{5}
{2}
{4} {3}


Colour:       Quantity:     Total:
Red               {6}         ${7:1.2f}
Blue              {8}         ${9:1.2f}
Light Green       {10}         ${11:1.2f}
Orange            {12}         ${13:1.2f}
Dark Grey         {14}         ${15:1.2f}
Transparent       {16}         ${17:1.2f}

Total items:       {18}
Total item cost:  ${19}.00
Delivery cost:    ${20}.00
Final cost:       ${21}.00

         Thanks for shopping
        at the Umbrella Shop !
-----------------------------------
            """.format(self.order_number, fullname, address, postcode, city,
                       phone, red_amount, red_total, blue_amount, blue_total,
                       l_green_amount, l_green_total, orange_amount,
                       orange_total, d_grey_amount, d_grey_total, clear_amount,
                       clear_total, total_items, total_cost, delivery_cost,
                       final_cost)
            if delivery_cost == "False":
                logger.error("delivery_cost is set to 'False'!")
                raise ValueError
            else:
                with open(order_file, 'w') as file:
                    file.write(order)
                os.startfile(order_file)
                self.order_no(increase=1)
                self.controller.show_frame(OrderPage)
        except AttributeError:
            logger.error("One of the attributes of the BillingPage failed!")
        except FileNotFoundError:
            logger.error("File cannot be found!")

    def order_form(self):
        """
        Create the order form to be displayed in the BillingPage frame.
        """
        data = {}
        with open(CURRENT_DATA_F, 'r') as file:
            for line in file:
                option, value = line.strip().split(':')
                data[option] = int(value)

        for colour in data:
            if colour == 'red' and int(data[colour]) > 0:
                self.red_label.configure(text='Red')
                self.red_amount_label.configure(text=data[colour])
                self.red_total = int(data['red']) * 39
                self.red_total_label.configure(text="${:.2f}".format(
                                               self.red_total))
            elif colour == 'red' and int(data[colour]) == 0:
                self.red_label.configure(text=" ")
                self.red_amount_label.configure(text=" ")
                self.red_total_label.configure(text=" ")

            if colour == 'blue' and int(data[colour]) > 0:
                self.blue_label.configure(text='Blue')
                self.blue_amount_label.configure(text=data[colour])
                self.blue_total = int(data[colour]) * 39
                self.blue_total_label.configure(text="${:.2f}".format(
                                                self.blue_total))
            elif colour == 'blue' and int(data[colour]) == 0:
                self.blue_label.configure(text=" ")
                self.blue_amount_label.configure(text=" ")
                self.blue_total_label.configure(text=" ")

            if colour == 'light_green' and int(data[colour]) > 0:
                self.l_green_label.configure(text='Light green')
                self.l_green_amount_label.configure(text=data[colour])
                self.l_green_total = int(data[colour]) * 39
                self.l_green_total_label.configure(text="${:.2f}".format(
                                                   self.l_green_total))

            elif colour == 'light_green' and int(data[colour]) == 0:
                self.l_green_label.configure(text=" ")
                self.l_green_amount_label.configure(text=" ")
                self.l_green_total_label.configure(text=" ")

            if colour == 'orange' and int(data[colour]) > 0:
                self.orange_label.configure(text=colour.title())
                self.orange_amount_label.configure(text=data[colour])
                self.orange_total = int(data[colour]) * 39
                self.orange_total_label.configure(text="${:.2f}".format(
                                                  self.orange_total))

            elif colour == 'orange' and int(data[colour]) == 0:
                self.orange_label.configure(text=" ")
                self.orange_amount_label.configure(text=" ")
                self.orange_total_label.configure(text=" ")

            if colour == 'dark_grey' and int(data[colour]) > 0:
                self.d_grey_label.configure(text='Dark grey')
                self.d_grey_amount_label.configure(text=data[colour])
                self.d_grey_total = int(data[colour]) * 39
                self.d_grey_total_label.configure(text="${:.2f}".format(
                                                  self.d_grey_total))

            elif colour == 'dark_grey' and int(data[colour]) == 0:
                self.d_grey_label.configure(text=" ")
                self.d_grey_amount_label.configure(text=" ")
                self.d_grey_total_label.configure(text=" ")

            if colour == 'clear' and int(data[colour]) > 0:
                self.clear_label.configure(text='Transparent')
                self.clear_amount_label.configure(text=data[colour])
                self.clear_total = int(data[colour]) * 39
                self.clear_total_label.configure(text="${:.2f}".format(
                                                 self.clear_total))

            elif colour == 'clear' and int(data[colour]) == 0:
                self.clear_label.configure(text=" ")
                self.clear_amount_label.configure(text=" ")
                self.clear_total_label.configure(text=" ")

        if int(data['total']) > 0:
            total_cost = int(data['total'] * 39) \
                if data['total'] != ' ' else 0
            if total_cost == UMBRELLA_COST:
                delivery_cost = 4
            elif total_cost == 2 * UMBRELLA_COST \
                    or total_cost == 3 * UMBRELLA_COST:
                delivery_cost = 7
            elif total_cost >= 4 * UMBRELLA_COST:
                delivery_cost = 13
            elif total_cost == 0:
                delivery_cost = 0
            else:
                delivery_cost = "False"
                logger.error("total_cost failed to convert to an integer.")

            final_cost = total_cost + delivery_cost \
                if isinstance(delivery_cost, int) \
                else logger.critical("Failed to convert delivery cost to int.")
            self.final_cost_amount.config(text="${:.2f}".format(final_cost))

        elif int(data['total']) == 0:
            self.final_cost_amount.config(text=" ")
        else:
            logger.error("Invalid data '{}' was received!"
                         .format(data['total']))
        self.clear_label.after(1500, lambda: self.order_form())

    def confirm(self, P, S):
        """
        Disallow anything but a 4 digit integer.

        :param P: allowed value (%P)
        :param S: text being inserted (%S)
        :return: True or False
        """
        self.order_form()
        allowed_value = P   # So the values of P and S are understandable
        inserted_value = S  # But are set as param so that %P and %S are used.
        if len(allowed_value) == 0:
            inserted_value = 0
            allowed_value = "0"
        else:
            try:
                inserted_value = int(inserted_value)
            except ValueError:
                print("Input is not an integer!")
        if isinstance(inserted_value, int) and 1 <= len(allowed_value) <= 4:
            if (len(allowed_value) == 4 and
                    self.final_cost_label.cget("text") != ' '):
                self.confirm_button.configure(state='normal')
            else:
                self.confirm_button.configure(state='disabled')
            return True
        else:
            self.bell()
            return False


def reset_order_data():
    """ Resets the CURRENT_DATA_F file. """
    order_data = ['red', 'blue', 'light_green', 'orange', 'dark_grey', 'clear',
                  'total']
    new_data = []
    with open(CURRENT_DATA_F, 'w') as file:
        for data in order_data:
            new_data.append('{}:0'.format(data))
        file.write('\n'.join(new_data))


def main():
    """
    Start of the program.
    """
    reset_order_data()
    app = UmbrellaShop()

    width = 450  # width for the Tk root
    height = 600  # height for the Tk root

    # get screen width and height
    ws = app.winfo_screenwidth()  # width of the screen
    hs = app.winfo_screenheight()  # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws/2) - (width/2)
    y = (hs/2) - (height/2)

    # set the dimensions of the screen
    # and where it is placed, being the centre of the screen
    app.geometry('%dx%d+%d+%d' % (width, height, x, y))
    app.resizable(width=False, height=False)
    app.mainloop()  # starts the Umbrella Shop

    reset_order_data()

if __name__ == '__main__':
    main()
