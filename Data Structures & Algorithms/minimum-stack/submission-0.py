class MinStack:

    def __init__(self):
        self.array =[]
        self.i = 0
        self.min_array = []

    def push(self, val: int) -> None:
        self.array.append(val)
        if self.i!=0:
            if self.min_array[-1] > val:
                self.min_array.append(val)
            else :
                self.min_array.append(self.min_array[-1])
        else :
            self.min_array.append(val)
        self.i +=1
        

    def pop(self) -> None:
        if self.i != 0:
            pop_item = self.array.pop()
            self.min_array.pop()
            self.i -= 1
            

    def top(self) -> int:
        if self.i != 0:
            print(self.i)
            print(self.array)
            top_item = self.array[self.i-1]
            return top_item

    def getMin(self) -> int:
        if self.i != 0:
            return self.min_array[-1]
