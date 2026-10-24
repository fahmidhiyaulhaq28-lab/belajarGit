print("percobaan pertama")

from datetime import date
from models import Transfer

class Inventory:
    def __init__(self):
        self.products = {} # key: plu
        self.history_transfer = []

    def add_product(self, product):
        self.products[product.plu] = product

    # F3: FEFO Transfer Gudang ke Rak
    def f3_fefo_transfer(self, plu, jumlah_minta):
        # 1. Cek PLU
        if plu not in self.products:
            return False, f"PLU {plu} tidak ditemukan."

        product = self.products[plu]
        today = date.today()

        # 2. Filter batch layak jual (qty > 0 dan tidak EXPIRED)
        layak_jual = [b for b in product.batches_gudang if b.qty > 0 and b.exp_date > today]

        if not layak_jual:
            return False, "GAGAL: Tidak ada stok layak jual di gudang. Semua EXPIRED atau kosong."

        # 3. FEFO: urutkan expiry terdekat duluan
        layak_jual.sort(key=lambda b: b.exp_date)

        # 4. Cek apakah stok cukup, jika tidak ditolak
        total_layak = sum(b.qty for b in layak_jual)
        if total_layak < jumlah_minta:
            return False, f"DITOLAK: Stok layak jual tidak cukup. Minta {jumlah_minta}, tersedia {total_layak}."

        # 5. Buat rencana pemindahan
        rencana = []
        sisa_minta = jumlah_minta

        for batch in layak_jual:
            if sisa_minta <= 0:
                break
            ambil = min(batch.qty, sisa_minta)
            rencana.append({"batch": batch, "ambil": ambil})
            sisa_minta -= ambil

        # 6. Tampilkan rencana
        print("\n--- RENCANA PEMINDAHAN FEFO ---")
        for r in rencana:
            b = r["batch"]
            print(f"{b.batch_id} (exp {b.exp_date}) x {r['ambil']}")
        print(f"Tujuan: Gudang -> {product.shelf_location} ({product.name})")
        print(f"Total akan dipindah: {jumlah_minta} pcs")

        # Cek kapasitas shelving
        if product.shelf_stock + jumlah_minta > product.shelf_capacity:
            print(f"PERINGATAN: Rak over capacity! Kapasitas {product.shelf_capacity}, isi sekarang {product.shelf_stock}")

        # 7. Konfirmasi petugas y/n
        konfirmasi = input("Konfirmasi petugas (y/n): ").strip().lower()
        if konfirmasi != 'y':
            return False, "Transfer dibatalkan petugas."

        # 8. Eksekusi pemindahan
        for r in rencana:
            r["batch"].qty -= r["ambil"]

        product.shelf_stock += jumlah_minta
        self.history_transfer.append(Transfer(plu, jumlah_minta, "GUDANG", "RAK"))

        return True, f"SUKSES: {jumlah_minta} pcs PLU {plu} berhasil dipindah ke rak."