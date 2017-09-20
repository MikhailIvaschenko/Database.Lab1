class GoodType(object):
    def  __init__(self, gtName, gtManufacturer, gtID = 0):
        self.gtID = 0
        self.gtName = gtName
        self.gtManufacturer = gtManufacturer
    def __str__(self):
        return 'Name of the type:  %s.\nGood\'s type\' manufacturer: %s.\nCurrent ID: %d.\n-----------------------------' % (self.gtName, self.gtManufacturer, self.gtID)