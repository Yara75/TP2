class IntegerList:

    def __init__(self, maList):
        self.list = maList

    def add_integer(self, num):
        self.list.append(num)

    def remove_integer(self, num):
        self.list.remove(num)

    def get_average(self):
        avg = 0
        for i in self.list:
            avg += i
        avg = avg / len(self.list)
        return avg

    def get_max(self):
        return max(self.list)

    def get_min(self):
        return min(self.list)
