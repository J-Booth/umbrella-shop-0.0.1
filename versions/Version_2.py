from __init__ import *

logger.disabled = False


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
        self.logo = tk.PhotoImage(file="img/logo2.gif")
        self.logo_label = tk.Label(self, image=self.logo)
        self.logo_label.grid(row=0, rowspan=12, column=0, columnspan=16)

        # Header
        new_order_label = ttk.Label(self, text="New order:", font=MEDIUM_FONT)
        new_order_label.grid(row=13, column=4, columnspan=8, pady=30)

        # Red Umbrella Label, price and amount
        self.red_label = ttk.Label(self, text="Red", font=SMALL_FONT,
                                   foreground="red")
        self.red_label.grid(row=14, column=1, columnspan=5, pady=10, sticky="W")
        self.red_price = ttk.Label(self, text="$39.00", font=SMALL_FONT)
        self.red_price.grid(row=14, column=6, columnspan=3, pady=10)
        red_vcmd = (self.register(self.confirm), '%P', '%S', 'red')
        self.red_amount = ttk.Entry(self, validate="key", justify="center",
                                    validatecommand=red_vcmd)
        self.red_amount.grid(row=14, column=10, columnspan=2, pady=10)

        # Blue Umbrella Label, price and amount
        self.blue_label = ttk.Label(self, text="Blue", font=SMALL_FONT,
                                    foreground="blue")
        self.blue_label.grid(row=15, column=1, columnspan=5, pady=10,
                             sticky="W")
        self.blue_price = ttk.Label(self, text="$39.00", font=SMALL_FONT)
        self.blue_price.grid(row=15, column=6, columnspan=3, pady=10)
        blue_vcmd = (self.register(self.confirm), '%P', '%S', 'blue')
        self.blue_amount = ttk.Entry(self, validate="key", justify="center",
                                     validatecommand=blue_vcmd)
        self.blue_amount.grid(row=15, column=10, columnspan=2, pady=10)

        # Light Green Umbrella Label, price and amount
        self.light_green_label = ttk.Label(self, text="Light Green",
                                           font=SMALL_FONT, 
                                           foreground="light green")
        self.light_green_label.grid(row=16, column=1, columnspan=5, pady=10,
                                    sticky="W")
        self.light_green_price = ttk.Label(self, text="$39.00", font=SMALL_FONT)
        self.light_green_price.grid(row=16, column=6, columnspan=3, pady=10)
        light_green_vcmd = (self.register(self.confirm), '%P', '%S',
                            'light_green')
        self.light_green_amount = ttk.Entry(self, validate="key",
                                            justify="center",
                                            validatecommand=light_green_vcmd)
        self.light_green_amount.grid(row=16, column=10, columnspan=2, pady=10)

        # Orange Umbrella Label, price and amount
        self.orange_label = ttk.Label(self, text="Orange", font=SMALL_FONT,
                                      foreground="orange")
        self.orange_label.grid(row=17, column=1, columnspan=5, pady=10,
                               sticky="W")
        self.orange_price = ttk.Label(self, text="$39.00", font=SMALL_FONT)
        self.orange_price.grid(row=17, column=6, columnspan=3, pady=10)
        orange_vcmd = (self.register(self.confirm), '%P', '%S', 'orange')
        self.orange_amount = ttk.Entry(self, validate="key",
                                       justify="center",
                                       validatecommand=orange_vcmd)
        self.orange_amount.grid(row=17, column=10, columnspan=2, pady=10)

        # Dark Grey Umbrella Label, price and amount
        self.dark_grey_label = ttk.Label(self, text="Dark Grey",
                                         font=SMALL_FONT,
                                         foreground="dark grey")
        self.dark_grey_label.grid(row=18, column=1, columnspan=5, pady=10,
                                  sticky="W")
        self.dark_grey_price = ttk.Label(self, text="$39.00", font=SMALL_FONT)
        self.dark_grey_price.grid(row=18, column=6, columnspan=3, pady=10)
        dark_grey_vcmd = (self.register(self.confirm), '%P', '%S', 'dark_grey')
        self.dark_grey_amount = ttk.Entry(self, validate="key",
                                          justify="center",
                                          validatecommand=dark_grey_vcmd)
        self.dark_grey_amount.grid(row=18, column=10, columnspan=2, pady=10)

        # Clear Umbrella Label, price and amount
        self.clear_label = ttk.Label(self, text="Transparent", font=SMALL_FONT,
                                     foreground="black")
        self.clear_label.grid(row=19, column=1, columnspan=5, pady=10,
                              sticky="W")
        self.clear_price = ttk.Label(self, text="$39.00", font=SMALL_FONT)
        self.clear_price.grid(row=19, column=6, columnspan=3, pady=10)
        clear_vcmd = (self.register(self.confirm), '%P', '%S', 'clear')
        self.clear_amount = ttk.Entry(self, validate="key",
                                      justify="center",
                                      validatecommand=clear_vcmd)
        self.clear_amount.grid(row=19, column=10, columnspan=2, pady=10)

        self.cart_img = tk.PhotoImage(file="img/cart_button.gif")
        cart_command = (lambda: self.cart())
        self.cart_button = tk.Button(self, compound=tk.TOP, relief="flat",
                                     width=80, height=40, image=self.cart_img,
                                     command=cart_command)
        self.cart_button.grid(row=20, column=9, columnspan=4, sticky="W",
                              pady=5)
        self.cart_button.image = self.cart_img

    def cart(self):
        self.controller.show_frame(BillingPage)

    def confirm(self, P, S, colour):
        """ 
        Disallow anything but a 1-4 digit integer.

        :param P: allowed value (%P)
        :param S: text being inserted (%S)
        :param colour: the umbrella colour (str)
        :return: True or False
        """
        allowed_value = P   # So the values of P and S are understandable
        inserted_value = S  # But are set as param so that %P and %S are used.
        try:
            inserted_value = int(inserted_value)
        except ValueError:
            print("Input is not an integer!")
        if isinstance(inserted_value, int) and 1 <= len(allowed_value) <= 4:
            with open('current_data.txt', 'r') as file:
                current_data = [line.strip() for line in file]
            data = {}
            with open('current_data.txt', 'r') as file:
                for line in file:
                    option, value = line.strip().split(':')
                    data[option] = value
                if data[colour] == str(int(allowed_value)):
                    print('No changes to be made to the current_data.txt file.')
                else:
                    current_data.remove('{}:{}'.format(colour, data[colour]))
                    current_data.remove('{}:{}'.format('total', data['total']))
                    data[colour] = int(allowed_value)
                    data['total'] = int(data['total'])
                    total = 0 + data[colour]
                    for item in current_data:
                        item = item.split(':')
                        item.pop(0)
                        total += int(item[0])
                    data['total'] += data[colour]
                    current_data.append('{}:{}'.format(colour, data[colour]))
                    current_data.append('{}:{}'.format('total', str(total)))
            with open('current_data.txt', 'w') as file:
                print('Writing to current_data.txt')
                file.write('\n'.join(current_data))
            return True
        else:
            self.bell()
            return False


class EditPage(tk.Frame):

    def __init__(self, parent, controller):
        """ Where the user can edit their order """
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.logo = tk.PhotoImage(file="img/logo2.gif")
        self.logo_label = tk.Label(self, image=self.logo)
        self.logo_label.grid(row=0, rowspan=12, column=0, columnspan=16)
        
        # Header
        edit_label = ttk.Label(self, text="Edit:", font=MEDIUM_FONT)
        edit_label.grid(row=13, column=4, columnspan=8, pady=30)

        # Red Umbrella Label, price and amount
        self.red_label = ttk.Label(self, text="Red", font=SMALL_FONT,
                                   foreground="red")
        self.red_label.grid(row=14, column=1, columnspan=5, pady=10, sticky="W")
        self.red_price = ttk.Label(self, text="$39.00", font=SMALL_FONT)
        self.red_price.grid(row=14, column=6, columnspan=3, pady=10)
        self.red_amount = ttk.Entry(self, validate="key", justify="center")
        self.red_amount.grid(row=14, column=10, columnspan=2, pady=10)

        # Blue Umbrella Label, price and amount
        self.blue_label = ttk.Label(self, text="Blue", font=SMALL_FONT,
                                    foreground="blue")
        self.blue_label.grid(row=15, column=1, columnspan=5, pady=10,
                             sticky="W")
        self.blue_price = ttk.Label(self, text="$39.00", font=SMALL_FONT)
        self.blue_price.grid(row=15, column=6, columnspan=3, pady=10)
        self.blue_amount = ttk.Entry(self, validate="key", justify="center")
        self.blue_amount.grid(row=15, column=10, columnspan=2, pady=10)

        # Light Green Umbrella Label, price and amount
        self.light_green_label = ttk.Label(self, text="Light Green",
                                           font=SMALL_FONT, 
                                           foreground="light green")
        self.light_green_label.grid(row=16, column=1, columnspan=5, pady=10,
                                    sticky="W")
        self.light_green_price = ttk.Label(self, text="$39.00", font=SMALL_FONT)
        self.light_green_price.grid(row=16, column=6, columnspan=3, pady=10)
        self.light_green_amount = ttk.Entry(self, validate="key",
                                            justify="center")
        self.light_green_amount.grid(row=16, column=10, columnspan=2, pady=10)

        # Orange Umbrella Label, price and amount
        self.orange_label = ttk.Label(self, text="Orange", font=SMALL_FONT,
                                      foreground="orange")
        self.orange_label.grid(row=17, column=1, columnspan=5, pady=10,
                               sticky="W")
        self.orange_price = ttk.Label(self, text="$39.00", font=SMALL_FONT)
        self.orange_price.grid(row=17, column=6, columnspan=3, pady=10)
        self.orange_amount = ttk.Entry(self, validate="key",
                                       justify="center")
        self.orange_amount.grid(row=17, column=10, columnspan=2, pady=10)

        # Dark Grey Umbrella Label, price and amount
        self.dark_grey_label = ttk.Label(self, text="Dark Grey",
                                         font=SMALL_FONT,
                                         foreground="dark grey")
        self.dark_grey_label.grid(row=18, column=1, columnspan=5, pady=10,
                                  sticky="W")
        self.dark_grey_price = ttk.Label(self, text="$39.00", font=SMALL_FONT)
        self.dark_grey_price.grid(row=18, column=6, columnspan=3, pady=10)
        self.dark_grey_amount = ttk.Entry(self, validate="key",
                                          justify="center")
        self.dark_grey_amount.grid(row=18, column=10, columnspan=2, pady=10)

        # Clear Umbrella Label, price and amount
        self.clear_label = ttk.Label(self, text="Transparent", font=SMALL_FONT,
                                     foreground="black")
        self.clear_label.grid(row=19, column=1, columnspan=5, pady=10,
                              sticky="W")
        self.clear_grey_price = ttk.Label(self, text="$39.00", font=SMALL_FONT)
        self.clear_grey_price.grid(row=19, column=6, columnspan=3, pady=10)
        self.clear_grey_amount = ttk.Entry(self, validate="key",
                                           justify="center")
        self.clear_grey_amount.grid(row=19, column=10, columnspan=2, pady=10)

        self.cart_img = tk.PhotoImage(file="img/cart_button.gif")
        cart_command = (lambda: controller.show_frame(BillingPage))
        self.cart_button = tk.Button(self, compound=tk.TOP, relief="flat",
                                     width=80, height=40, image=self.cart_img,
                                     command=cart_command)
        self.cart_button.grid(row=20, column=9, columnspan=4, sticky="W",
                              pady=5)
        self.cart_button.image = self.cart_img

        # self.cart_img = tk.PhotoImage(file="img/cart_button.gif")
        # cart_command = (lambda: controller.show_frame(BillingPage))
        # self.cart_button = tk.Button(self, compound=tk.TOP, relief="flat",
        #                              width=80, height=40, image=self.cart_img,
        #                              command=cart_command)
        # self.cart_button.grid(row=20, column=9, columnspan=4, sticky="W",
        #                       pady=5)
        # self.cart_button.image = self.cart_img
        #
        # self.new_img = tk.PhotoImage(file="img/new_button.gif")
        # new_command = (lambda: controller.show_frame(OrderPage))
        # self.new_button = tk.Button(self, compound=tk.TOP, relief="flat",
        #                             width=80, height=40, image=self.new_img,
        #                             command=new_command)
        # self.new_button.grid(row=20, column=13, columnspan=4, sticky="W",
        #                      pady=5)
        # self.new_button.image = self.new_img


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
        vcmd = (self.register(self.confirm), '%P', '%S')
        self.postcode = ttk.Entry(self, validate="key", validatecommand=vcmd)
        self.postcode.grid(row=15, column=2, columnspan=3, sticky="e", pady=5)

        # Order Form
        self.order_form()

        self.colour_label = ttk.Label(self, text="Colour", font=SMALL_FONT)
        self.colour_label.grid(row=17, column=1, pady=10, sticky='W')

        self.quantity_label = ttk.Label(self, text="Quantity", font=SMALL_FONT)
        self.quantity_label.grid(row=17, column=2, columnspan=8, padx=5)

        self.total_label = ttk.Label(self, text="Total", font=SMALL_FONT)
        self.total_label.grid(row=17, column=8, columnspan=8)

        self.red_label = ttk.Label(self, text=" ")
        self.red_label.grid(row=18, column=1, sticky='W', padx=20)
        self.red_amount_label = ttk.Label(self, text=" ")
        self.red_amount_label.grid(row=18, column=2, columnspan=8)
        self.red_total = " "
        self.red_total_label = ttk.Label(self, text=self.red_total)
        self.red_total_label.grid(row=18, column=8, columnspan=8)

        self.blue_label = ttk.Label(self, text=" ")
        self.blue_label.grid(row=19, column=1, sticky='W', padx=20)
        self.blue_amount_label = ttk.Label(self, text=" ")
        self.blue_amount_label.grid(row=19, column=2, columnspan=8)
        self.blue_total = " "
        self.blue_total_label = ttk.Label(self, text=self.blue_total)
        self.blue_total_label.grid(row=19, column=8, columnspan=8)

        self.light_green_label = ttk.Label(self, text=" ")
        self.light_green_label.grid(row=20, column=1, sticky='W', padx=20)
        self.light_green_amount_label = ttk.Label(self, text=" ")
        self.light_green_amount_label.grid(row=20, column=2, columnspan=8)
        self.light_green_total = " "
        self.light_green_total_label = ttk.Label(self,
                                                 text=self.light_green_total)
        self.light_green_total_label.grid(row=20, column=8, columnspan=8)

        self.orange_label = ttk.Label(self, text=" ")
        self.orange_label.grid(row=21, column=1, sticky='W', padx=20)
        self.orange_amount_label = ttk.Label(self, text=" ")
        self.orange_amount_label.grid(row=21, column=2, columnspan=8)
        self.orange_total = " "
        self.orange_total_label = ttk.Label(self, text=self.orange_total)
        self.orange_total_label.grid(row=21, column=8, columnspan=8)

        self.dark_grey_label = ttk.Label(self, text=" ")
        self.dark_grey_label.grid(row=22, column=1, sticky='W', padx=20)
        self.dark_grey_amount_label = ttk.Label(self, text=" ")
        self.dark_grey_amount_label.grid(row=22, column=2, columnspan=8)
        self.dark_grey_total = " "
        self.dark_grey_total_label = ttk.Label(self, text=self.dark_grey_total)
        self.dark_grey_total_label.grid(row=22, column=8, columnspan=8)

        self.clear_label = ttk.Label(self, text=" ")
        self.clear_label.grid(row=23, column=1, sticky='W', padx=20)
        self.clear_amount_label = ttk.Label(self, text=" ")
        self.clear_amount_label.grid(row=23, column=2, columnspan=8)
        self.clear_total = " "
        self.clear_total_label = ttk.Label(self, text=self.clear_total)
        self.clear_total_label.grid(row=23, column=8, columnspan=8)

        self.final_cost_label = ttk.Label(self, text="Final Cost:",
                                          font=SMALL_FONT)
        self.final_cost_label.grid(row=24, column=2, columnspan=5, pady=10)
        self.final_cost = " "
        self.final_cost = ttk.Label(self, text=self.final_cost, font=SMALL_FONT)
        self.final_cost.grid(row=24, column=5, columnspan=7)

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

    @staticmethod
    def order_no(increase=0):
        """ Get the current order number. """
        with open("order_num.txt", 'r') as file:
            order_number = int(file.read())
        if increase > 0:
            with open("order_num.txt", 'w') as file:
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
        """ Writes the order to a newly created file. """
        self.order_number = self.order_no()
        try:
            order_file = "saves\order_{}.txt".format(self.order_number)

            fullname = self.name.get()
            address = self.address.get()
            postcode = self.postcode.get()
            city = self.city.get()
            phone = self.phone.get()

            red_amount = self.red_amount_label.cget("text")
            red_total = self.red_total
            blue_amount = self.blue_amount_label.cget("text")
            blue_total = self.blue_total
            light_green_amount = self.light_green_amount_label.cget("text")
            light_green_total = self.light_green_total
            orange_amount = self.orange_amount_label.cget("text")
            orange_total = self.orange_total
            dark_grey_amount = self.dark_grey_amount_label.cget("text")
            dark_grey_total = self.dark_grey_total
            clear_amount = self.clear_amount_label.cget("text")
            clear_total = self.clear_total

            item_totals = {"red": red_amount, "blue": blue_amount,
                           "orange": orange_amount, "clear": clear_amount,
                           "light_green": light_green_amount,
                           "dark_grey": dark_grey_amount}
            total_items = 0
            for item in item_totals:
                if item_totals[item] == ' ':
                    item_totals[item] = 0
                else:
                    try:
                        item_totals[item] = int(item_totals[item])
                    except ValueError:
                        logger.error("Failed to convert '{}' to integer"
                                     .format(type(item_totals[item])))
                total_items += item_totals[item]

            item_total_costs = {"red": red_total, "blue": blue_total,
                                "orange": orange_total, "clear": clear_total,
                                "light_green": light_green_total,
                                "dark_grey": dark_grey_total}
            total_cost = 0
            for item in item_total_costs:
                if item_total_costs[item] == ' ':
                    item_total_costs[item] = 0
                else:
                    try:
                        item_totals[item] = int(' ')  # item_total_costs[item] = int(item_total_costs[item])
                    except ValueError:
                        logger.error("Failed to convert '{}' to integer"
                                     .format(type(item_total_costs[item])))
                total_cost += item_total_costs[item]

            if total_items == 1:
                delivery_cost = 4
            elif total_items == 2 or total_items == 3:
                delivery_cost = 7
            elif total_items >= 4:
                delivery_cost = 13
            else:
                delivery_cost = "False"
                logger.error("total_items failed to convert to an integer.")

            final_cost = total_cost + delivery_cost

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
Red               {6}         ${7:1}.00
Blue              {8}         ${9:1}.00
Light Green       {10}         ${11:1}.00
Orange            {12}         ${13:1}.00
Dark Grey         {14}         ${15:1}.00
Transparent       {16}         ${17:1}.00

Total items:       {18}
Total item cost:  ${19}.00
Delivery cost:    ${20}.00
Final cost:       ${21}.00

         Thanks for shopping 
        at the Umbrella Shop !
-----------------------------------
            """.format(self.order_number, fullname, address, postcode, city,
                       phone, red_amount, red_total, blue_amount, blue_total,
                       light_green_amount, light_green_total, orange_amount,
                       orange_total, dark_grey_amount, dark_grey_total,
                       clear_amount, clear_total, total_items, total_cost,
                       delivery_cost, final_cost)

            with open(order_file, 'w') as file:
                print("__{}__".format(blue_amount))
                file.write(order)
            os.startfile(order_file)
            self.order_no(increase=1)
        except AttributeError:
            logger.error("One of the attributes of the BillingPage failed!")
        except FileNotFoundError:
            logger.error("File cannot be found!")

    def order_form(self):
        """ Creates the order form to be displayed in the BillingPage frame. 
        """
        data = {}
        test_list = []
        with open('current_data.txt', 'r') as file:
            for line in file:
                option, value = line.strip().split(':')
                data[option] = value
                if option != 'total':
                    test_list.append('{}:{}'.format(option, data[option]))
        print(test_list)
        item_data = {}
        for i in test_list:
            colour, amount = i.strip().split(':')
            print(i, colour, amount)
            item_data[colour] = amount
            if int(item_data[colour]) > 0:
                if colour == 'red' and int(item_data[colour]) > 0:
                    self.red_label.configure(text=colour.title())
                    self.red_amount_label.configure(text=item_data[colour])
                    total = int(item_data[colour]) * 39
                    self.red_total = total
                    self.red_total_label.configure(text="${:.2f}".format(
                                                   self.red_total))
                if colour == 'blue' and int(item_data[colour]) > 0:
                    self.blue_label.configure(text=colour.title())
                    self.blue_amount_label.configure(text=item_data[colour])
                    total = int(item_data[colour]) * 39
                    self.blue_total = total
                    self.blue_total_label.configure(text="${:.2f}".format(
                                                   self.blue_total))
                if colour == 'light_green' and int(item_data[colour]) > 0:
                    self.light_green_label.configure(text='Light green')
                    self.light_green_amount_label.configure(text=
                                                            item_data[colour])
                    total = int(item_data[colour]) * 39
                    self.light_green_total = total
                    self.light_green_total_label.configure(text=
                        "${:.2f}".format(self.light_green_total))
                if colour == 'orange' and int(item_data[colour]) > 0:
                    self.orange_label.configure(text=colour.title())
                    self.orange_amount_label.configure(text=item_data[colour])
                    total = int(item_data[colour]) * 39
                    self.orange_total = total
                    self.orange_total_label.configure(text="${:.2f}".format(
                                                   self.orange_total))
                if colour == 'dark_grey' and int(item_data[colour]) > 0:
                    self.dark_grey_label.configure(text='Dark grey')
                    self.dark_grey_amount_label.configure(text=
                                                          item_data[colour])
                    total = int(item_data[colour]) * 39
                    self.dark_grey_total = total
                    self.dark_grey_total_label.configure(text="${:.2f}".format(
                                                   self.dark_grey_total))
                if colour == 'clear' and int(item_data[colour]) > 0:
                    self.clear_label.configure(text='Transparent')
                    self.clear_amount_label.configure(text=item_data[colour])
                    total = int(item_data[colour]) * 39
                    self.clear_total = total
                    self.clear_total_label.configure(text="${:.2f}".format(
                                                   self.clear_total))

    def confirm(self, P, S):
        """ 
        Disallow anything but a 4 digit integer.
        
        :param P: allowed value (%P)
        :param S: text being inserted (%S)
        :return: True or False
        """
        allowed_value = P   # So the values of P and S are understandable
        inserted_value = S  # But are set as param so that %P and %S are used.
        try:
            inserted_value = int(inserted_value)
        except ValueError:
            print("Input is not an integer!")
        if isinstance(inserted_value, int) and 1 <= len(allowed_value) <= 4:
            if len(allowed_value) == 4:
                self.order_form()
                self.confirm_button.configure(state='normal')
            elif len(allowed_value) != 4:
                self.confirm_button.configure(state='disabled')
            return True
        else:
            self.bell()
            return False


def reset_order_data():
    order_data = ['red', 'blue', 'light_green', 'orange', 'dark_grey', 'clear',
                  'total']
    new_data = []
    with open('current_data.txt', 'w') as file:
        for data in order_data:
            new_data.append('{}:0'.format(data))
        file.write('\n'.join(new_data))


def main():
    """ Start of the program. """
    reset_order_data()
    app = UmbrellaShop()

    w = 450  # width for the Tk root
    h = 600  # height for the Tk root

    # get screen width and height
    ws = app.winfo_screenwidth()  # width of the screen
    hs = app.winfo_screenheight()  # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    # set the dimensions of the screen
    # and where it is placed
    app.geometry('%dx%d+%d+%d' % (w, h, x, y))
    app.resizable(width=False, height=False)
    app.mainloop()  # starts the Umbrella Shop

    reset_order_data()

if __name__ == '__main__':
    main()
    # os.startfile('log_file.txt')  # Displays the saved user data
