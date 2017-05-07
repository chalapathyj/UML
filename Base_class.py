from Inventory import Notice, SrClerk
#notice = Notice('Abn1', 'corp1', 'book', '5')
srclrk = SrClerk("3", "ram")

#notice.generateNotice('srclerk', 'Ordered book. But pens are supplied.')
srclrk.generateErrorNotice('Ordered book. But pens are delivered.')