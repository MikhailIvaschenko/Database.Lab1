class GoodsTypesCollection(object):
    def __init__(self):
        self.goodTypes = []
        self.maxIndex = 0
    def __str__(self):
        return "\n".join(str(goodType) for goodType in self.goodTypes)

    def add(self, goodType):
        for type in self.goodTypes:
            if (type.gtName == goodType.gtName and type.gtManufacturer == goodType.gtManufacturer):
                raise Exception("Such record already exists.")
        self.maxIndex += 1
        goodType.gtID = self.maxIndex
        self.goodTypes.append(goodType)
    def delete(self, gtID, goodsCollection):
        for index, type in enumerate(self.goodTypes):
            if (type.gtID == gtID and gtID > -1 and index > -1):
                self.goodTypes.pop(index)
        self.maxIndex -= 1
        for index, goodType in enumerate(self.goodTypes):
            goodType.gtID = index + 1

    def edit(self, gtID, editChoice, name = "", manufacturer = ""):
        if editChoice == '1':
            for index, type in enumerate(self.goodTypes):
                if type.gtID == gtID:
                    self.goodTypes[index].gtName = name
        elif editChoice == '2':
            for index, type in enumerate(self.goodTypes):
                if type.gtID == gtID:
                    self.goodTypes[index].gtManufacturer = manufacturer
        elif editChoice == '3':
            for index, type in enumerate(self.goodTypes):
                if type.gtID == gtID:
                    self.goodTypes[index].gtName = name
                    self.goodTypes[index].gtManufacturer = manufacturer
        else:
            return