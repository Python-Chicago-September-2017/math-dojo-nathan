class MathDojo(object):
    def __init__(self):
        self.result = 0
    def add(self,number1,number2 = 0,number3 = 0):

        for test in locals().values():
            if isinstance(test, int):
                self.result += test
            elif isinstance(test, list):
                add = 0
                for i in range(len(test)):
                    add += test[i]
                self.result += add

        return self
    def subtract(self,number1,number2 = 0, number3 = 0):

        for test in locals().values():
            if isinstance(test, int):
                self.result -= test
            elif isinstance(test, list):
                sub = 0
                for i in range(len(test)):
                    sub += test[i]
                self.result -= sub

        return self

md = MathDojo()
print md.add(1,2).add([3,3]).subtract(3,[3,3]).result