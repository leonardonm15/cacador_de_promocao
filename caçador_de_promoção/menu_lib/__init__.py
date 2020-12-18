class Menu:
    def __init__(self, *args):
        self.args = [*args]

    def interface(self):
        print('=-=' * 10)
        c = 0
        for i in self.args:
            print(f'{c}- {i}')
            c += 1
        print('=-=' * 10)

    def input(self):
        len_list = len(self.args)
        _input = int(input('Qual a opção: '))
        if _input in range(len_list):
            return _input
        else:
            print('erro')
            return False
