class Test:
    def __init__(self, foo):
         self._foo = foo

    def _bar(self):
        print(self._foo)
        print("__bar")

test = Test("hello")

test._bar()
print(test._foo)

