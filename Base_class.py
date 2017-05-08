from Inventory import SrClerk, InventoryItem

# InventoryItem.items = { 'id' : 001 , 'cat' : 'fruits', 'name':'apple', 'actqua' : 10, 'ecordqua' : 20
# }
# #notice = Notice('Abn1', 'corp1', 'book', '5')
invnt = InventoryItem('003','fancy', 'cap', '5', '7')
invnt.getQuantity('001')

srclrk = SrClerk("3", "ram", '1024', 'acb shipng', 'Books', '5')


#notice.generateNotice('srclerk', 'Ordered book. But pens are supplied.')
#srclrk.verifyShipment()
