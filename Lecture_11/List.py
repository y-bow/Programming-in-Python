class my_List:
    def __init__(self):
        self.l = [0,0,0,0,0]
        self.count = 0
    def my_Append(self,value):
        self.l[self.count] = value
        self.count += 1
    def print_list(self):
        print("[", end = "")
        for i in range(self.count):
            print(self.l[i], end = " ")
        print("]")
    def my_Pop(self, value):
        self.l[self.count] = value
        self.count -= 1

l1 = my_List()
l1.my_Append(5)
l1.my_Append(6)
l1.my_Append(7)
l1.my_Append(8)
l1.print_list()
l1.my_Pop(8)
l1.print_list()