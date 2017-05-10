from Inventory import SrClerk, InventoryItem, Supplier, PurchaseOrder, Staff

# InventoryItem.items = { 'id' : 001 , 'cat' : 'fruits', 'name':'apple', 'actqua' : 10, 'ecordqua' : 20
# }
# #notice = Notice('Abn1', 'corp1', 'book', '5')

painkillers = InventoryItem('003', 'tablet', 'Painkillers', '10', '10')
antibiotics = InventoryItem('001', 'syrup', 'Anitbiotics', '5', '10')
antiseptics = InventoryItem('002', 'injection', 'Antiseptics', '25', '10')
antipyretics = InventoryItem('002', 'capsule', 'Antipyretics', '15', '10')

sup_cmpy1 = Supplier('001', 'sup_cmpy1', 'Bangalore', '23454', 'Antiseptics')
sup_cmpy2 = Supplier('002', 'sup_cmpy2', 'Chennai', '34524', 'Antipyretics')
sup_cmpy3 = Supplier('003', 'sup_cmpy3', 'Mangalore', '65768', 'Anitbiotics')
sup_cmpy4 = Supplier('004', 'sup_cmpy4', 'Hosur', '56785', 'Painkillers')

stockList = [painkillers, antibiotics, antiseptics, antipyretics]


class PurchaseClerk(Staff):

    def __init__(self, empid, name):
        super(PurchaseClerk, self).__init__(empid, name)

    def checkInventory(self):
        category = []
        for invitem in stockList:
            cat = invitem.checkQuantity()
            if cat:
                category.append(cat)
        return category

purchaseCheck = PurchaseClerk('432', 'PRCLERK')

category = purchaseCheck.checkInventory()
print("Category", category)

# generates the PO
if category:
    #purchseOrder = {}
    #suplist = []
    for x in category:
        pOrd = PurchaseOrder(x, 20).generatePo()
        purchseOrder[pOrd[0]] = pOrd[1:]
        suplist = Supplier.searchSupplier(pOrd[1])
        if suplist:
            shpment = Shipment([], pOrd[2])
print ("Suplist", suplist)

# painkillers.checkQuantity()
#print (Supplier.searchSupplier('Painkillers'))
#po = PurchaseOrder('435', 'tablet', '10')

# po.generatePo()
#po.updatePo('glucose', '25')

# Supplier.searchSupplier('painkillers')

#painkillers.setQuantity('002', '60')

#srclrk = SrClerk("3", "ram", '1024', 'acb shipng', 'Books', '5')


#notice.generateNotice('srclerk', 'Ordered book. But pens are supplied.')
# srclrk.verifyShipment()
