import math


class IntegerList:

    def __init__(self, maList):
        self.list = maList

    def add_integer(self, num):
        self.list.append(num)

    def remove_integer(self, num):
        self.list.remove(num)

    def get_average(self):
        if len(self.list) == 0:
            return 0  # Retourner 0 si la liste est vide

        avg = 0
        count = 0
        for i in self.list:
            if isinstance(i, (int, float)):  # Vérifier si l'élément est un nombre
                avg += i
                count += 1

        if count == 0:
            return 0  # Retourner 0 si aucun élément int ou float n'est trouvé

        avg = avg / count
        return avg
    
    def get_max(self):
        elem = self.list[0]

        for i in self.list: 
            if i > elem:
                elem = i
        return elem

    def get_min(self):
        elem = self.list[0]

        for i in self.list: 
            if i < elem:
                elem = i
        return elem

    def get_sum(self):
        global somme
        somme = 0
        for i in self.list:
            if isinstance(i, (int, float)):
                somme = somme + i
        return somme



