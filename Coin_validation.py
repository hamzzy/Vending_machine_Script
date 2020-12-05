from ReadData import Input


class Valuation:

    def __init__(self):
        """
        class Valuation manage manipulation of coin in the vending machine
        """
        self.amount = 0
        self.accept_input = self.accept_input

    def addCash(self) -> any:
        """
        add more coin if no more coin
        :return: none
        """
        money = float(self.accept_input('Add more Coin :'))
        self.amount = self.amount + money

    def insert_money(self) -> any:
        """
        func accept input needed to be
        :return:
        """
        self.amount += float(self.accept_input('insert Coin :'))

    def checkRefund(self) -> any:
        """
        func : help to refund change after buy a desired item
        :return:
        """
        if self.amount > 0: print(str(self.amount) + " refunded.")
        print('Thank you, have a nice day!\n')


class VendingMachineValidator(Valuation):

    def check_stock(self, wanted) -> bool:
        """
        This func check if the ietm is in stock
        :param wanted:
        :return: boolean
        """
        if wanted.get('stocks') == 0:
            return True

    def get_item(self, wanted) -> dict:
        """
        this get the specific item to be purchase
        :param wanted:
        :return: dictionary
        """
        ret = None
        for item in self.items:
            if item.get('name') == wanted:
                ret = item
                break
        return ret

    def continue_to_buy(self, ans) -> bool:
        """
        func helps user to
        :param ans:
        :return:
        """
        cont = True
        if (ans == 'y') and (self.amount == 0.0):
            self.addCash()
            cont = False
        elif ans == "y" and self.amount != 0:
            cont = False
            pass
        else:
            self.checkRefund()
            return cont