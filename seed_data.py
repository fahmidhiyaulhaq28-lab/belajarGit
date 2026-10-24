print("data percobaan pertama")

from datetime import date
from models import Product, StockBatch

def get_seed_inventory():
    # Produk 1: Indomie
    p1 = Product(plu="1001", name="Indomie Goreng", price=3500, 
                 shelf_location="A1-Rak Atas (Shelving)", min_shelf_stock=5, shelf_capacity=30)
    p1.shelf_stock = 4
    p1.batches_gudang = [
        StockBatch("B001", "1001", 10, date(2026, 11, 5)),  # paling dekat expired
        StockBatch("B002", "1001", 15, date(2025, 10, 20)), # INI EXPIRED, akan di-skip sistem
        StockBatch("B003", "1001", 20, date(2026, 12, 10)),
    ]

    # Produk 2: Aqua
    p2 = Product(plu="1002", name="Aqua 600ml", price=4000,
                 shelf_location="B2-Shelving Minuman", min_shelf_stock=10, shelf_capacity=50)
    p2.shelf_stock = 8
    p2.batches_gudang = [
        StockBatch("B004", "1002", 30, date(2026, 12, 1)),
    ]

    return [p1, p2]