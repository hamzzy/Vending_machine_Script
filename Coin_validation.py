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
        money = float(self.accept_input('Please add more Coins :'))
        self.amount = self.amount + money

    def insert_money(self) -> any:
        """
        func accept input needed to be
        :return:
        """
        self.amount += float(self.accept_input('Please Insert Coins :'))

    def checkRefund(self) -> any:
        """
        func : help to refund change after buy a desired item
        :return:
        """
        if self.amount > 0: print(str(self.amount) + " refunded.")
        print('Thank you, have a nice day!\n')


class VendingMachineValidator(Valuation):
    """
      class VendingMachineValidator  validate user input
      - check_stock
      - get_item
      - continue_to_buy
    """
    def check_stock(self, wanted) -> bool:
        """
        This func check if the ietm is in stock
        :param wanted:
        :return: boolean
        """
        if wanted.get('stock') == 0:
            return True
        else:
            pass

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

    def continue_to_buy(self, ans:str) -> bool:
        """
        func : accept user input to  buy more item and validate
        :param ans:
        :return:
        """
        cont = True
        if (ans == 'y') :
            return cont
        elif ans == "y":
            return cont
        else:
            self.checkRefund()
            return cont
