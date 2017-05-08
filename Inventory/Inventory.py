class InventoryItem:
    items = {'001': {'category': 'fruits', 'name': 'apple', 'quantity': '10',          'ecquantity': '20'},
             '002': {'category': 'vegetables', 'name': 'carrot', 'quantity': '25', 'ecquantity': '60'
                     },
             }

    def __init__(self, itemId, name, category, actQuantity, ecoOrderQuantity):
        self. itemId = itemId
        self.name = name
        self.category = category
        self.actQuantity = actQuantity
        self.ecoOrderQuantity = ecoOrderQuantity
        self.items[itemId] = {'category': category, 'name': name,
                              'quantity': actQuantity, 'ecquantity': ecoOrderQuantity}

    def getQuantity(self, itmid):
        for x, y in self.items[itmid].items():
            print(x, y)

    def setQuantity(self):
        self.items[itemId] = {'category': category, 'name': name,
                              'quantity': actQuantity, 'ecquantity': ecoOrderQuantity}

    def checkQuantity(self):
        pass


class Notice:

    def __init__(self, shipmentNumber, supplierName, itemDetails, quantityDetails):
        self.shipmentNumber = shipmentNumber
        self.supplierName = supplierName
        self.itemDetails = itemDetails
        self.quantityDetails = quantityDetails

    def _generateNotice(self, dep, errorDetails):
        print("The following notice is issued by %s and the error details are as follows:\nShipment Number: %s\nSupplier Name: %s\nItem details: %s\nQuantity Details: %s\nError: %s" % (
            dep, self.shipmentNumber, self.supplierName, self.itemDetails, self.quantityDetails, errorDetails))


class Staff:

    def __init__(self, empid, name):
        self.empid = empid
        self.name = name


class SrClerk(Staff, Notice):

    def __init__(self, empid, name, shipmentNumber, supplierName, itemDetails, quantityDetails):
        # super(SrClerk, self).__init__(empid, name)
        Staff.__init__(self, empid, name)
        Notice.__init__(self, shipmentNumber, supplierName,
                        itemDetails, quantityDetails)

    def generateErrorNotice(self, err_flg=''):
        if (err_flg):
            msg = 'Ordered book. But pens are delivered'
            self._generateNotice('SRCLERK', msg)
        else:
            print("No issues")

    def verifyShipment(self):
        self.generateErrorNotice(1)
