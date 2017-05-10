import sys
sys.path.append('./Inventory')
from Staff import *
from Item import InventoryItem
from Inventory import Supplier, PurchaseOrder, Shipment, Bill, QualityCriteria, InventoryClerk, AcceptedItem

# all this data has to be read from utility file
painkillers = InventoryItem('003', 'tablet', 'Painkillers', 10, 10)
antibiotics = InventoryItem('001', 'syrup', 'Anitbiotics', 25, 10)
antiseptics = InventoryItem('002', 'injection', 'Antiseptics', 25, 10)
antipyretics = InventoryItem('004', 'capsule', 'Antipyretics', 25, 10)

sup_cmpy1 = Supplier('001', 'sup_cmpy1', 'Bangalore', '23454', 'Antiseptics')
sup_cmpy2 = Supplier('002', 'sup_cmpy2', 'Chennai', '34524', 'Antipyretics')
sup_cmpy3 = Supplier('003', 'sup_cmpy3', 'Mangalore', '65768', 'Anitbiotics')
sup_cmpy4 = Supplier('004', 'sup_cmpy4', 'Hosur', '56785', 'Painkillers')

stockList = [painkillers, antibiotics, antiseptics, antipyretics]


purchaseclk = PurchaseClerk('432', 'PRCLERK')

category = purchaseclk.checkInventory(stockList)


# generates the PO
if category:

    for x, y in category.items():
        pOrd = PurchaseOrder(x, 20)
        pOrd.generatePo()

        suplist = Supplier.searchSupplier(pOrd.items)

        if suplist:
            shpment = Shipment(
                [pOrd.poNumber, pOrd.items, pOrd.orderDate], '6Months', pOrd.quantity)
            shpment.getShipment()

            # shpment.itemDetails = []  # ---> to check wrong billing
            billing = Bill(100, shpment.itemDetails)

            srclrk = SrClerk("3", "ram", shpment.shipmentNumber, suplist[
                             0][1], [pOrd.poNumber, pOrd.items, pOrd.orderDate], y.name,  pOrd.quantity)

            src_ret = srclrk.verifyShipment(billing)

            if src_ret != 0:

                qualspec = QualityCriteria(
                    pOrd.poNumber, suplist[0][1], '6Months')

                ins = Inspector("23", "QCIns", shpment.shipmentNumber, suplist[
                    0][1], [pOrd.poNumber, pOrd.items, pOrd.orderDate], y.name,  pOrd.quantity)

                ins_ret = ins.inspect(qualspec.qualitySpecs, shpment)

                if ins_ret != 0:
                    ac_it = AcceptedItem(y.itemId, y.name, ins.quantityDetails)
                    updated_quantity = ac_it.updateQuantity(y)
                    inv_clerk = InventoryClerk(345, "INVClerk")
                    updated_inv = inv_clerk.updateInventory(
                        y, updated_quantity)

                    print("Updated iventory list:\nID:%s\nMedicine Name: %s\nCategory: %s\nUpdated Quantity: %s\nEco Quantity:%s" % (
                        updated_inv.itemId, updated_inv.name, updated_inv.category, updated_inv.actQuantity, updated_inv.ecoOrderQuantity))
                else:
                    continue
            else:
                continue
else:
    print("All the items in the inventory are above the threshold value")
