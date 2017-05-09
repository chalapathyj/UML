import datetime


class Item:

    def __init__(self, itemId, name):
        self.itemId = itemId
        self.name = name

    def add(self):
        pass

    def item(self):
        pass


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
        print("Quantity left in the inventory for the category %s : %s" %
              (self.category, self.actQuantity))


class Notice:

    def __init__(self, shipmentNumber, supplierName, itemDetails, quantityDetails):
        self.shipmentNumber = shipmentNumber
        self.supplierName = supplierName
        self.itemDetails = itemDetails
        self.quantityDetails = quantityDetails

    def _generateNotice(self, dep, errorDetails):
        print("The following notice is issued by %s and the error details are as follows:\nShipment Number: %s\nSupplier Name: %s\nItem details: %s\nQuantity Details: %s\nError: %s" % (
            dep, self.shipmentNumber, self.supplierName, self.itemDetails, self.quantityDetails, errorDetails))


class Supplier:
    supplierDict = {}

    def __init__(self, supplierId, supplierName, address, phoneNumber, typeOfStock):
        self.supplierId = supplierId
        self.supplierName = supplierName
        self.address = address
        self.phoneNumber = phoneNumber
        self.typeOfStock = typeOfStock
        # appending more than one supplier for a stock.
        try:
            self.supplierDict[self.typeOfStock].append(
                [self.supplierId, self.supplierName, self.address, self.phoneNumber])
        except KeyError:
            self.supplierDict[self.typeOfStock] = [
                self.supplierId, self.supplierName, self.address, self.phoneNumber]

    @staticmethod
    def searchSupplier(stock):
        return [Supplier.supplierDict[key] for key in Supplier.supplierDict if stock == key]


class PurchaseOrder:

    def __init__(self, PoNumber, Items, Quantity):
        self.poNumber = PoNumber
        self._items = Items
        self._quantity = Quantity
        self.orderDate = datetime.date.today()

    @property  # getter
    def items(self):
        return self._items

    @property  # getter
    def quantity(self):
        return self._quantity

    @items.setter
    def items(self, value):
        self._items = value

    @items.setter
    def quantity(self, value):
        self._quantity = value

    def generatePo(self):
        self.orderDate = datetime.date.today()
        print("The purchase order:\nOrder No: %s\nMedicine name: %s\nQuantity: %s\nDate: %s" % (
            self.poNumber, self._items, self._quantity, self.orderDate))

    def updatePo(self, val1='', val2=''):
        if val1 != '':
            self.items = val1
        if val2 != '':
            self.quantity = val2

        print("The updated purchase order:\nOrder No: %s\nMedicine name: %s\nQuantity: %s\nDate: %s" % (
            self.poNumber, self._items, self._quantity, self.orderDate))

    def displayPo(self):
        print("The displaying purchase order:\nOrder No: %s\nMedicine name: %s\nQuantity: %s\nDate: %s" % (
            self.poNumber, self._items, self._quantity, self.orderDate))


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

    def generateErrorNotice(self, name='SRCLERK', msg=''):
        if msg != '':
            msg = 'Mismatch in purchase order and shipment'
            self._generateNotice(name, msg)

    def verifyShipment(self):
        self.generateErrorNotice(1)


class Inspector(SrClerk):

    def __init__(self, empid, name,):
        super(Inspector, self).__init__(empid, name)

    def inspect(self):
        pass
