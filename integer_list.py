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
        for i in self.list:
            if isinstance(i, (int, float)):
                somme = somme + i
        return somme

    def get_variance(self): 
        global som, variance
        moy = self.get_average()

        for i in self.list:
            som = som + (i - moy)**2

        if moy != 0:
            variance = som / moy

        return variance

    def get_ecartype(self):
        val = self.get_variance()
        ecart = math.sqrt(val)
        return ecart


