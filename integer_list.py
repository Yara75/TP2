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

    """def get_max(self):
        return max(self.list)

    def get_min(self):
        return min(self.list) """

    def get_max(maList):
        elem = maList[0]

        for i in maList: 
            if maList[i] > elem:
                elem = maList
        return elem

    def get_min(maList):
        elem = maList[0]
        print(elem)

        for i in maList: 
            if maList[i] < elem:
                elem = maList
        return elem