# Andrew Keller
# 12/9/24
class ItemToPurchase:

    def __init__(self):
        self.item_name = 'none'
        self.item_price = 0.0
        self.item_quantity = 0
        self.item_description = 'none'

    def print_item_cost(self):
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${self.item_price * self.item_quantity:.2f}')

    def print_item_description(self):
        print(f'{self.item_name}: {self.item_description}')




class ShoppingCart:

    def __init__(self, customer_name='none', current_date='January 1, 2020'):
        self.customer_name = customer_name
        self.current_date = current_date  
        self.cart_items = []
        
    def add_item(self, ItemToPurchase): 
        self.cart_items.append(ItemToPurchase)

    def remove_item(self, item_name):
        count = 0
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                count += 1
        if count == 0:
            print('Item not found in cart. Nothing removed')

    def modify_item(self, ItemToPurchase):
        count = 0
        for item in self.cart_items:
            if item.item_name == ItemToPurchase:
                if item.item_description == 'none':
                    item.item_description = input('Enter the item description. ')
                if item.item_price == 0.0:
                    item.item_price = float(input('Enter the price of the item. '))
                if item.item_quantity == 0:
                    item.item_quantity = int(input('Enter the quantity to purhase. '))
                count += 1
        if count == 0:
            print('Item not found in cart. Nothing modified')

    def get_num_items_in_cart(self):
        count = 0
        for item in self.cart_items:
            count += item.item_quantity
        return count

    def get_cost_of_cart(self):
        cost = 0
        for item in self.cart_items:
            cost += item.item_quantity * item.item_price
        return cost

    def print_total(self):
        if len(self.cart_items) > 0:
            print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}')
            print(f'Number of Items: {self.get_num_items_in_cart()}')
            for item in self.cart_items:
                item.print_item_cost()
        else:
            print('SHOPPING CART IS EMPTY')
        print(f'Total: ${self.get_cost_of_cart():.2f}')

    def print_descriptions(self):
        print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}')
        print('Item Descriptions')
        for item in self.cart_items:
            item.print_item_description()

def main():
    customer_name = input('Enter customers name. ')
    current_date = input('Enter the current date. ')
    shop_cart = ShoppingCart(customer_name, current_date)
    print_menu(shop_cart)

def print_menu(shop_cart):
    option_list = ['a', 'r', 'c', 'i', 'o', 'q']
    print('MENU')
    print('a - Add itme to cart')
    print('r - Remove item from cart')
    print('c - Change item quantity')
    print('i - Output items\' descriptions')
    print('o - Output shopping cart')
    print('q - Quit')
    choice = input('Choose an option: ')
    while choice not in option_list:
        choice = input('Invalid option selected. Choose an option: ')
    while choice != 'q':
        if choice == 'a':
            item = ItemToPurchase()
            item.item_name = input('Enter the name of the item you would like to purchase. ')
            while len(item.item_name.strip()) < 1:
                item.item_name = input('Name cannot be left blank. Enter the name of the item you would like to purchase. ')
            item.item_price = input('Enter the price of the item. ')
            while isinstance(item.item_price, str):
                if item.item_price.replace('.','').isdigit():
                    item.item_price = float(item.item_price)
                else:
                    item.item_price = input('Price must be a number. Re-enter item price. ')
            item.item_quantity = input('Enter the quantity to purchase. ')
            while isinstance(item.item_quantity, str):
                if item.item_quantity.isdigit():
                    item.item_quantity = int(item.item_quantity)
                else:
                    item.item_quantity = input('Quantity must be a whole number. Enter the quantity you would like to purchase. ')
            item.item_description = input('Enter the product description. ')
            while len(item.item_description.strip()) < 1:
               item.item_description = input('Description cannot be left blank. Enter item description. ') 
            shop_cart.add_item(item)
        elif choice == 'r':
            item_to_remove = input('Enter the name of the item to remove. ')
            while len(item_to_remove.strip()) < 1:
                item_to_remove = input('Cannot be left blank. Enter the name of the item to remove')
            shop_cart.remove_item(item_to_remove)
        elif choice == 'c':
            item_to_modify = input('Enter the name of the item you would like to change quantity of. ')
            while len(item_to_modify.strip()) < 1:
                item_to_modify = input('Cannot be left blank. Enter the name of the item you would like to change quantity of. ')
            for item in shop_cart.cart_items:
                if item.item_name == item_to_modify:
                    item.item_quantity = input('Enter the quantity you would like to purchase. ')
                    while isinstance(item.item_quantity, str):
                        if item.item_quantity.isdigit():
                            item.item_quantity = int(item.item_quantity)
                        else:
                            item.item_quantity = input('Must be a whole number. Enter the quantity you would like to purchase. ')
        elif choice == 'i':
            shop_cart.print_descriptions()
        elif choice == 'o':
            shop_cart.print_total()
        print()
        print('MENU')
        print('a - Add itme to cart')
        print('r - Remove item from cart')
        print('c - Change item quantity')
        print('i - Output items\' descriptions')
        print('o - Output shopping cart')
        print('q - Quit')
        choice = input('Choose an option: ')
        while choice not in option_list:
            choice = input('Invalid option selected. Choose an option: ')
    
    
if __name__ == '__main__':         
    main()
