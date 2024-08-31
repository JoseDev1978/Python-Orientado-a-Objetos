class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        super().__init__()
        self.__count = 0
        self.__max_count = 0
        self.__max_count_val = 0

    def get_counter(self):
        return self.__count
    
    def pop(self):
        val = super().pop()
        self.__count += 1
        if self.__count > self.__max_count:
            self.__max_count = self.__count
            self.__max_count_val = val

stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())