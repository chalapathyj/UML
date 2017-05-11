class Item:

    def __init__(self, itemId, name):
        self.itemId = itemId
        self.name = name

    # def add(self):
    #     pass

    # def item(self):
    #     pass


class InventoryItem(Item):

    def __init__(self, itemId, name, category, actQuantity='20', ecoOrderQuantity='10'):
        super(InventoryItem, self).__init__(itemId, name)
        self.category = category
        self.actQuantity = actQuantity
        self.ecoOrderQuantity = ecoOrderQuantity

    def getQuantity(self):
        print(self.itemId, self.name, self.actQuantity)

    def setQuantity(self, qnty):
        self.actQuantity = qnty

    def checkQuantity(self):
        if int(self.actQuantity) <= 10:

            print("Quantity less than the threshold(less or eq to 10) in the inventory:\nID:%s\nMedicine Name: %s\nCategory: %s\nUpdated Quantity: %s\nEco Quantity:%s" % (
                self.itemId, self.name, self.category, self.actQuantity, self.ecoOrderQuantity))
            return self.category
