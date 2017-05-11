import datetime


class Notice:

    def __init__(self, shipmentNumber, supplierName, itemDetails, itemSpec, quantityDetails):
        self.shipmentNumber = shipmentNumber
        self.supplierName = supplierName
        self.itemDetails = itemDetails
        self.quantityDetails = quantityDetails
        self.itemSpec = itemSpec

    def _generateNotice(self, dep, errorDetails):
        print("*****Error******\nThe following notice is issued by %s\n%s\nThe error details are as follows:\nShipment Number: %s\nSupplier Name: %s\nItem Specification: %s\nQuantity Details: %s\n" %
              (dep, errorDetails, self.shipmentNumber, self.supplierName, self.itemSpec, self.quantityDetails), end='')
        print("Item Details: %s " % ', '.join(map(str, self.itemDetails)))


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
                [self.supplierId, self.supplierName, self.typeOfStock, self.address, self.phoneNumber])
        except KeyError:
            self.supplierDict[self.typeOfStock] = [
                self.supplierId, self.supplierName, self.typeOfStock, self.address, self.phoneNumber]

    @staticmethod
    def searchSupplier(stock):
        print("\n---Purchase order assigned to the supplier---\n")
        return [Supplier.supplierDict[key] for key in Supplier.supplierDict if stock == key]


class PurchaseOrder:
    poNumber = 34256  # some random number

    def __init__(self, Items, Quantity):
        self._items = Items
        self._quantity = Quantity
        self.orderDate = datetime.date.today()
        PurchaseOrder.poNumber += 1

    @property  # getter
    def items(self):
        return self._items

    @property  # getter
    def quantity(self):
        return self._quantity

    @items.setter
    def items(self, value):
        self._items = value

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    def generatePo(self):
        self.orderDate = datetime.date.today()
        print("\n---Purchase Department places an purchase order---\n")
        return [self.poNumber, self._items, self._quantity, self.orderDate]

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


class Shipment:
    shipmentNumber = 7887643  # some random number

    def __init__(self, itemDetails, expiry, quantity):

        self.itemDetails = itemDetails
        self.quantity = quantity
        self.expiry = expiry
        Shipment.shipmentNumber += 1

    def getShipment(self):
        print("\n---Supplier delivers the shipment---\n")
        print("Shipping details: ", (self.shipmentNumber,
                                     self.itemDetails, self.quantity, self.expiry))


class Bill:
    billNumber = 23456  # some randome number

    def __init__(self, totalAmt, itemDetails):
        self.Date = datetime.date.today()
        self.totalAmt = totalAmt
        self.itemDetails = itemDetails
        Bill.billNumber += 1
        print("\n---Supplier gives the Bill---\n")

    def generateBill(self):
        print("Billing:\nBill Number:%s\nDate:%s\nAmount:%s\nItem Details:%s" %
              (self.billNumber, self.Date, self.totalAmt, self.itemDetails))


class QualityCriteria:

    def __init__(self, itemNumber, itemName, qualitySpecs):
        self.itemNumber = itemNumber
        self.itemName = itemName
        self.qualitySpecs = qualitySpecs
        print("\n---Quality spec is created for Inspection---\n")

    def displayQualitySpecs(self):
        print("Quality specifications: \nItem Numer: % s\nItem Name: % s\nQuality spec: %s" % (
            self.itemNumber, self.itemName, self.qualitySpecs))


class AcceptedItem:

    def __init__(self, itemNumber, itemName, quantity):
        self.itemNumber = itemNumber
        self.itemName = itemName
        self.quantity = quantity
        print("\n---Inspector prepares accepted item---\n")

    def acceptItem(self):
        print("Accepted item details: %s" %
              [self.itemNumber, self.itemName, self.quantity])

    def updateQuantity(self, other):
        return self.quantity + other.actQuantity
