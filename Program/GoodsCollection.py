class GoodsCollection(object):
    def __init__(self):
        self.goods = []
        self.maxIndex = 0
    def __str__(self):
        return "\n".join(str(good) for good in self.goods)

    def add(self, good):
        self.maxIndex += 1
        good.goodID = self.maxIndex
        self.goods.append(good)
    def delete(self, goodID):
        flag = 0
        for good in self.goods:
            if good.goodID == goodID and goodID > -1:
                for index, good in enumerate(self.goods):
                    if (good.goodID == goodID and index > -1):
                        self.goods.pop(index)
                flag = 1
                self.maxIndex -= 1
        for index, good in enumerate(self.goods):
            good.goodID = index + 1
        if flag == 0:
            raise Exception("Wrong index.")
    def edit(self, goodID, editChoice, typesCollection, name = "", price = 0, id = 0):
        if editChoice == 1:
            for index, good in enumerate(self.goods):
                if good.goodID == goodID:
                    self.goods[index].goodName = name
        elif editChoice == 2:
            for index, good in enumerate(self.goods):
                if good.goodID == goodID:
                    self.goods[goodID].goodPrice = price
        elif editChoice == 3:
            for index, good in enumerate(self.goods):
                if good.goodID == goodID:
                    flag = 0
                    newTypeID = 0
                    while(flag == 0):
                        try:
                            newTypeID = id
                            if (newTypeID - 1 <= typesCollection.goodTypes.__len__()):
                                flag = 1
                            else:
                                print("The good's type with such ID does not exist.")
                        except ValueError:
                            print("Input error: the value must be numeric.")

                    self.goods[goodID].gtID = newTypeID
        elif editChoice == 0:
            for index, good in enumerate(self.goods):
                if good.goodID == goodID:
                    self.goods[goodID].goodName = input("Input new good's name: ")
                    self.goods[goodID].goodPrice = eval(input("Input new good's price: "))
                    flag = 0
                    newTypeID = 0
                    while (flag == 0):
                        try:
                            newTypeID = eval(input("Input new good's type's ID: "))
                            if (newTypeID <= typesCollection.__len__()):
                                flag = 1
                            else:
                                print("The good's type with such ID does not exist.")
                        except ValueError:
                            print("Input error: the value must be numeric.")
                    self.goods[goodID].gtID = newTypeID
        else:
            return

    def composewHigherPriceSearch(self, typesCollection):
        resultstring = "Types' names:"
        marked = []
        for good in self.goods:
            if good.goodPrice > 10 and not (good.goodID in marked):
                for type in typesCollection.goodTypes:
                    resultstring += ' '
                    if(good.gtID == type.gtID):
                        resultstring += type.gtName + ','

        return (resultstring[0:(resultstring.__len__() - 1)] + '.')