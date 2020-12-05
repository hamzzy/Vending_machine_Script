import json


class ReadData:
    def read_data(self, src: str):
        """
         Read data from json source
        :return: list
        """
        file = open(src)
        data = json.load(file)
        return data['goods']


class Input:
    """
    class that control how data is input
    """

    def accept_input(self, msg: any) -> any:
        """

        :param msg: text to fill data  input
        :return:  input of anything
        """
        data = input(msg)
        return data
