from functools import reduce
from ReadData import ReadData, Input
from Coin_validation import VendingMachineValidator


class VendingMachine(ReadData,Input,VendingMachineValidator):
    def __init__(self, data):
        """
         A Vending machine View
        :param data:
        """
        super().__init__()
        self.amount = self.amount
        self.items = [n for n in self.read_data(data)]
        self.accept_input = self.accept_input

    def showItems(self) -> any:
        """
         Print data from the json file
        :return: a print of
        """
        print('Welcome to the vending machine!\n***************')

        print('\nitems available \n***************')
        for item in self.items:
            print(item['name'] + " " + "price: " + str(item['price']) + " dollars")
        print('***************\n')

    def buyItem(self, selected: list) -> any:
        """

        :param selected:
        :return:
        """
        item = self.get_item(selected)
        take_stock: bool = self.check_stock(item)
        if self.amount < item.get('price') and take_stock == True:
            print('***************\n')

            print('You can\'t buy this item. Insert more coins.')
            print("out of stock")
            print('***************\n')
            self.addCash()

        elif self.amount > item.get('price') and take_stock == True:
            print('***************\n')
            print("out of stock")
            print('***************\n')

        else:
            self.amount -= item.get('price')
            print('***************\n')

            print('You got ' + item.get('name'))
            print('Cash remaining: ' + str(self.amount))
            print('***************\n')



