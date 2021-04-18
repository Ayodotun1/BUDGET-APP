asterics = "*" * 10
class Budget:
    def __init__(self):
        self.category_list = []  # ["food", "clothing", and "entertainment"] etc
        self.category_balance = {}   # {"food":0, "clothing":0, "entertainment":0} etc
    
    
   # Start of the App
    """
    This checks if the category list is empty, if empty then user should create categories
    else proceed to operations to be performed.
    Try initializindg any or both of them to test this function
    """
    def launch(self):
        print(asterics + "WELCOME TO BUDGET APP" + asterics)
        if not(self.category_list and self.category_balance):
            print("Your Categories are empty, please add categories")
            self.create_categories()
        else:
            self.operation()
        
   
       

    """
    To create fresh category list.
    This grabs the categories in the list and also display their available balances.
    """
    def create_categories(self):
        opt = False
        print('The following are the availale categories to create: 1. Food 2. Entertainment 3. Clothing')
        number_of_categories = int(input("How many categories do you want to create?: \n"))
        while opt == False:
            if number_of_categories <= 3:
                opt = True

                for number in range(number_of_categories):
                    num = number+1
                    supply_category = input(f' Suppy Category Name {num}: ')
                self.category_list.append(supply_category)
                for category in self.category_list:
                    self.category_balance[category] = 0
                    print(asterics + 'Categories successfully added' + asterics)
                    self.operation()
            else:
                print('Only 3 categories are allowed')
                number_of_categories = int(input("How many categories do you want to create?: "))
    
    # To perform basic operations
    def operation(self):
        print("""These are the operations that can be performed\n
            [1] - DEPOSIT TO CATEGORY.
            [2] - WITHDRAWAL FROM CATEGORY.
            [3] - GET CATEGORY BALANCE.
            [4] - TRANSFER BETWEEN CATEGORIES.
            [5] - OVERALL BALANCE
            [0] - EXIT.
        """)
        try:
            action = int(input("Which operation do you want to perform?\n "))
            if action == 1:
                self.deposit_funds()
                
            elif action == 2:
                self.withdraw_funds()
                
            elif action == 3:
                self.get_balance()
                
            elif action == 4:
                self.transfer_funds()
            
            elif action == 5:
                self.get_total_balance()
                
            elif action == 0:
                self.exit_app()
                
            else:
                print("You have supplied an invalid input, please try again\n")
                self.operation()   
        except ValueError:
            print("Numerical value  is expected")
            self.operation()


    # Deposit funds to any category
    def deposit_funds(self):
        print("The below are the categories available for deposit?")
        for category in self.category_list:
            print(self.category_list.index(category)+1, category) # Returns index+1 of category and category name
        try:
            select_category = int(input("Select a category to deposit funds to: \n"))
            selected_category = select_category - 1 # subtracts 1 from number supplied to match the real index of the select category in category list.
            category = self.category_list[selected_category] # Pass selected category into a variable
            print(f"you have chosen to deposit funds to  {category}".capitalize())
            deposit_amount = int(input(f"How much do you want to deposit to {category}: \n"))
            self.category_balance[category] += deposit_amount
            print(f"You have deposited {deposit_amount} to {category}")
            print(f"Your New Balance:  {self.category_balance}")
            try:
                reply = input("would you like to perform another operation? Y/N: \n")
                if reply == "Y":
                    self.operation()  
                elif reply =="N":
                    print(asterics + "Thanks for using this app" + asterics)
                    exit()  
                else:
                    print("invalid input")
            except ValueError:
                print("A response between Y or N is expected, please try again")
        except:
            print("Numerical value required")
            self.operation()

        
    # Withdraw funds from any category
    def withdraw_funds(self):
        print("The below are the categories available for deposit?")
        for category in self.category_list:
            print(self.category_list.index(category)+1, category) # Returns index+1 of category and category name
        try:
            select_category = int(input("Select a category to withdraw funds from: \n"))
            selected_category = select_category - 1 # subtracts 1 from number supplied to match the real index of the select category in category list.
            category = self.category_list[selected_category]
            print(f"you have chosen to withdraw funds from  {category}")
            withdrawal_amount = int(input(f"How much do you want to Withdraw from {category}: \n"))
            if withdrawal_amount >= self.category_balance[category] or self.category_balance[category] <= 0:
                print(f"Insufficient funds, your current balance is {self.category_balance[category]}")
                try:
                    response = input("Would you like to make a deposit? Y or N \n) 
                    if response == "Y":
                        self.deposit_funds()
                    elif response == "N":
                        try:
                            reply = input("would you like to perform another operation? Y or N \n)
                            if reply == "Y":
                                self.operation()
                            elif reply =="N":
                                print(asterics + "Thanks for using this app" + asterics)
                                exit()
                            else:
                                print("invalid value supplied")
                                self.operation() 
                        except ValueError:
                            print("A value of Y or N is expected")
                            self.operation()
                       
                    else:
                        print("invalid parameter supplied")
                        self.operation()   
                except ValueError:
                    print("A value of Y or N is expected")
                    self.operation()
            else:
                self.category_balance[category] -= withdrawal_amount
                print(f"{withdrawal_amount} successfully withdrawn from {category}")
                print(f"Updated List and Balance:  {self.category_balance}")
                try:
                    reply = input("would you like to perform another operation? Y or N \n")
                    if reply == "Y":
                        self.operation()
                    elif reply =="N":
                        print(asterics + "Thanks for using this app" + asterics)
                        exit()
                    else:
                        print("invalid value supplied")
                        self.operation()
                except ValueError:
                    print("A value of Y or N is expected")
                    self.operation()           
        except ValueError:
            print("A numerical value is expected")
            self.operation()


    # Transfer funds from one category to the other
    def transfer_funds(self):
        try:
            # Category sending funds
            print("The below are the categories available for deposit?")
            for category in self.category_list:
                print(self.category_list.index(category)+1, category.upper())
            selected_category1 = int(input("Select a category to transfer funds from: \n"))
            sending_category = selected_category1 - 1
            category1 = self.category_list[sending_category]
            
            # Category receiving funds
            selected_category2 = int(input("Select category to transfer funds to: \n"))
            for category in self.category_list:
                print(self.category_list.index(category)+1, category)
            receiving_category =  selected_category2 - 1
            category2 = self.category_list[receiving_category]
            
            
            print(f"you have chosen to transfer funds from  {category1} to {category2}")
            withdrawal_amount = int(input(f"How much do you want to transfer from {category1} to {category2}: \n"))
            if withdrawal_amount >= self.category_balance[category1] or self.category_balance[category1] <= 0:
                print(f"Insufficient funds, your current balance is {self.category_balance[category1]}")
                try:
                    response = input("Would you like to make a deposit? Y or N \n") 
                    if response == "Y":
                        self.deposit_funds()
                    elif response == "N":
                        try:
                            reply = input("would you like to perform another operation? Y or N \n")
                            if reply == "Y":
                                self.operation()
                            elif reply =="N":
                                print(asterics + "Thanks for using this app" + asterics)
                                exit()
                            else:
                                print("invalid value supplied")
                                self.operation()
                        except ValueError:
                            print("A value of Y or N is expected")
                            self.operation()
                    else:
                        print("invalid parameter supplied")
                        self.deposit_funds()   
                except ValueError:
                    print("A value of Y or N is expected")
                    self.deposit_funds()
            else:
                self.category_balance[category1] -= withdrawal_amount
                self.category_balance[category2] += withdrawal_amount
                print(f"{withdrawal_amount} Successfully transfered from {category1} to {category2}")
                print(f"Updated List and Balance:  {self.category_balance}")
                try:
                    response = input("Would you like to make another transfer? Y or N \n") 
                    if response == "yes" or response == "y":
                        self.transfer_funds()
                    elif response == "no" or response =="n":
                        try:
                            reply = input("would you like to perform another operation? Y/N: \n")
                            if reply == "Y":
                                self.operation()
                            elif reply =="N":
                                print(asterics + "Thanks for using this app" + asterics)
                                self.operation()
                            else:
                                print("invalid value supplied")
                                self.operation() 
                        except ValueError:
                            print("A response of Y or N is expected")
                            self.operation()
                    else:
                        print("invalid parameter supplied")
                        self.operation()   
                except ValueError:
                    print("A response of Y or N is expected")
                    self.operation()
        except ValueError:
            print("Numerical value Expected")
            self.transfer_funds()
     
    
    # Get balance of each category
    def get_balance(self):
        for category in self.category_balance:
            balance = self.category_balance[category]
        print(f"{category} balance: # {balance}")
        try:
            response = input("would you like to perform another operation? Y or N \n")
            if response == "Y":
                self.operation()
            elif response =="N":
                print(asterics + "Thanks for using this app" + asterics)
                exit()
            else:
                print("input not found, please try again")
                self.get_balance() 
        except ValueError:
            print("A response of Y or N is needed")
            self.operation()

    
    # Get total balance of the categories all-together      
    def get_total_balance(self):
        total_balance = 0
        for category in self.category_balance:
            balance = self.category_balance[category]
            total_balance += balance
            print(f"Total Balance : # { total_balance}")
            try:
                response = input("would you like to perform another operation? Y/N\n)
                if response == "Y":
                    self.operation()  
                elif response =="N":
                    print(asterics + "Thanks for using this app" + asterics)
                    exit()
                else:
                    print("input not found, please try again")
                    self.get_total_balance()
            except ValueError:
                print("A response between Y or N is needed")
                self.operation()
        
    
    
    def exit_app(self):
        print(f"{asterics}Thanks for using this app{asterics}\n".upper())
        exit()
Budget().launch()