print("percobaan pertama")

from inventory import Inventory
from seed_data import get_seed_inventory

def main():
    inventory = Inventory()
    
    # Load seed data otomatis
    for product in get_seed_inventory():
        inventory.add_product(product)
    
    print("=== PANTAUTOKO CLI - Demo F3 FEFO Transfer ===")
    print("Data seed berhasil diload.")

    while True:
        print("\n--- MENU ---")
        print("1. Lihat semua produk & stok gudang")
        print("2. F3 - Transfer Gudang ke Rak (FEFO)")
        print("3. Keluar")
        
        pilih = input("Pilih: ").strip()

        if pilih == "1":
            for plu, p in inventory.products.items():
                print(f"\nPLU {plu} - {p.name} | Rak: {p.shelf_stock}/{p.shelf_capacity} di {p.shelf_location}")
                for b in p.batches_gudang:
                    status = "EXPIRED" if b.is_expired() else "OK"
                    print(f"  - {b.batch_id}: {b.qty} pcs, exp {b.exp_date} [{status}]")

        elif pilih == "2":
            plu = input("Input PLU (contoh 1001): ").strip()
            try:
                jumlah = int(input("Input jumlah yang mau dipindah: ").strip())
                sukses, pesan = inventory.f3_fefo_transfer(plu, jumlah)
                print("\n>> " + pesan)
            except ValueError:
                print("Jumlah harus angka!")

        elif pilih == "3":
            print("Keluar...")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()