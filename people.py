class People:
    def __init__(self, extremely_rage, sliding):
        self.extremely_rage = extremely_rage
        self.sliding = sliding

    @staticmethod
    def rage():
        if extremely_rage:
            print('I cannot do anything......')
        else:print('Nothing is happening')

    def slide(self):
        pass

class Me(People):
    def __init__(self, extremely_rage, sliding):
       super().__init__(extremely_rage, sliding)

    def rage(self):
        if extremely_rage:
            print('I can fkn slide!')
            sliding = True
        else:print('Nothing is happening')

    def slide(self):
        if sliding:
            print('I just DETOUR AROUND THE BACK of a M1A2 by sliding and demolished it with my fists!')

"""SO, people != people #(汗)"""