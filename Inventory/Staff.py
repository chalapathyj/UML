from Inventory import Notice


class Staff:

    def __init__(self, empid, name):
        self.empid = empid
        self.name = name


class SrClerk(Staff, Notice):

    def __init__(self, empid, name, shipmentNumber, supplierName, itemDetails, itemSpec, quantityDetails):
        Staff.__init__(self, empid, name)
        Notice.__init__(self, shipmentNumber, supplierName,
                        itemDetails, itemSpec, quantityDetails)

    def generateErrorNotice(self, name='SRCLERK', msg=''):
        if msg == '':
            msg = 'Mismatch in purchase order and billing'
        self._generateNotice(name, msg)

    def verifyShipment(self, other):
        print("\n---SRclerk verifies Bill against the Purchase order---\n")
        print(self.itemDetails, "compared with", other.itemDetails)
        if self.itemDetails == other.itemDetails:
            print("Passed verification")
            return 1
        else:
            print("\n---SRclerk raises shipment error notice---\n")
            self.generateErrorNotice()
            print("----Returned to the supplier----")
            return 0


class Inspector(SrClerk):

    def __init__(self, empid, name, shipmentNumber, supplierName, itemDetails, itemSpec, quantityDetails):
        super(Inspector, self).__init__(empid, name, shipmentNumber,
                                        supplierName, itemDetails, itemSpec, quantityDetails)

    def defectiveErrorNotice(self, a, b):
        msg = 'Quality specification didnt match.\nExpected Expiry: ' + \
            a + "\nShipped product's expiry:" + b
        self._generateNotice('Inspector', msg)

    def inspect(self, qspec, other):
        print("\n---Inspector uses quality specs to inspect the shipment---\n")
        print("Checks for Expiry month, expected: %s and actual: %s" %
              (qspec, other.expiry))
        if qspec <= other.expiry:
            print("Passed inspection")
            return 1
        else:
            print("\n---Inspector raises an defective error notice---\n")
            self.defectiveErrorNotice(qspec, other.expiry)
            print("----Returned to the supplier----")
            return 0


class InventoryClerk(Staff):

    def __init__(self, inventoryName, inventoryId):
        super(InventoryClerk, self).__init__(inventoryName, inventoryId)

    def checkInventory(self, stockList):
        print("\n---Purchase Clerk checks the Inventory---\n")
        category = {}
        for invitem in stockList:
            cat = invitem.checkQuantity()
            if cat:
                category[cat] = invitem
        return category

    def updateInventory(self, other1, other2):
        print("\n---Inspector forwards it to Inventory Clerk---\n")
        print("Updates the quantity if itemid: %s and name: %s matches with the inventory item's id: %s and name: %s" % (
            other1.itemId, other1.name, other2.itemNumber, other2.itemName))

        if (other1.itemId == other2.itemNumber and other1.name == other2.itemName):
            other1.setQuantity(other1.actQuantity + other2.quantity)
        print("\n---Inventory Clerk uses accepted list and updates the Inventory Item---\n")
        return other1


class PurchaseClerk(InventoryClerk):

    def __init__(self, empid, name):
        super(PurchaseClerk, self).__init__(empid, name)
