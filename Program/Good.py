class Good(object):
    def __init__(self, goodName, goodPrice, gtID, goodID = 0):
        self.goodID = 0
        self.goodName = goodName
        self.gtID = gtID
        self.goodPrice = goodPrice
    def __str__(self):
        return 'Name of the good:  %s.\nPrice: %d.\nCurrent type\'s ID: %d.\nCurrent ID: %d.\n-----------------------------' % (self.goodName, self.goodPrice, self.gtID, self.goodID)