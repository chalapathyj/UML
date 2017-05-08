from Inventory import SrClerk
#notice = Notice('Abn1', 'corp1', 'book', '5')
srclrk = SrClerk("3", "ram", '1024','acb shipng', 'Books', '5')

#notice.generateNotice('srclerk', 'Ordered book. But pens are supplied.')
srclrk.verifyShipment()
