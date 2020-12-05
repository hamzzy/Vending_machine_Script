from vend_machine import VendingMachine


def run():
    machine = VendingMachine('shop.json')
    machine.showItems()
    machine.insert_money()
    while True:
        selected = machine.accept_input('select item: ')
        try:

            machine.buyItem(selected)
            a = machine.accept_input('buy something else? (y/n): ')
            if machine.continue_to_buy(ans=a):
                break
            else:
                continue

        except:
            print("incorrect input")


if __name__ == '__main__':
    run()
