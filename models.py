print("model percobaan pertama")

from datetime import date, datetime

class Product:
    def __init__(self, plu, name, price, shelf_location, min_shelf_stock, shelf_capacity):
        self.plu = plu
        self.name = name
        self.price = price
        self.shelf_location = shelf_location
        self.min_shelf_stock = min_shelf_stock
        self.shelf_capacity = shelf_capacity
        self.shelf_stock = 0
        self.batches_gudang = []  # list StockBatch

class StockBatch:
    def __init__(self, batch_id, plu, qty, exp_date):
        self.batch_id = batch_id
        self.plu = plu
        self.qty = qty
        self.exp_date = exp_date # date object

    def is_expired(self):
        return self.exp_date <= date.today()

class Transfer:
    def __init__(self, plu, qty, from_loc, to_loc):
        self.plu = plu
        self.qty = qty
        self.from_loc = from_loc
        self.to_loc = to_loc
        self.time = datetime.now()

class Sale:
    def __init__(self, plu, qty):
        self.plu = plu
        self.qty = qty
        self.time = datetime.now()