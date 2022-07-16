########### FUNGSI UNTUK MENAMPILKAN SAHAM SAHAM YANG HARUS DIBELI
# fungsi untu digunakan oleh semua program utama/main kecuali suoerior

def beli_saham(df, h_predik):
    beli_saham1 = df['Saham'][0] # mendapatkan saham pertama
    hargatr_shm1 = df['Harga Terakhir'][0]# mendapatkan harga terakhir saham pertama
    harga1psn_shm1 = df['Harga di 1%'][0]#mendapatkan Harga 1% saham pertama
    hargab2_shm1 = df['Batas Harga (2%)'][0]#mendapatkan Harga 2% saham pertama
    hrg1t_2shm1 = df['Harga 1 lot(2%)'][0]#mendapatkan Harga 2% di1lot saham pertama
    hargam5_shm1 = df['Maksimal Harga (5%)'][0]#mendapatkan Harga 5% saham pertama
    beli_saham2 = df['Saham'][1]# mendapatkan saham kedua
    hargatr_shm2 = df['Harga Terakhir'][1]# mendapatkan harga terakhir saham keuda
    harga1psn_shm2 = df['Harga di 1%'][1]#mendapatkan Harga 1% saham keuda
    hargab2_shm2 = df['Batas Harga (2%)'][1]#mendapatkan Harga 2% saham keuda
    hrg1t_2shm2 = df['Harga 1 lot(2%)'][1]#mendapatkan Harga 2% di1lot saham keuda
    hargam5_shm2 = df['Maksimal Harga (5%)'][1]#mendapatkan Harga 5% saham keuda
    print(f'     Saham-saham yang akan naik {h_predik} hari kedepan:')
    print(f'1. Saham {beli_saham1}')
    print(f'   - Harga terakhir saham {beli_saham1} = Rp {hargatr_shm1}')
    print(f'   - Harga saham {beli_saham1}  di 1% = Rp {harga1psn_shm1}')
    print(f'   - Harga batas saham {beli_saham1} di 2% = Rp {hargab2_shm1}')
    print(f'   - Harga 1 lot saham {beli_saham1} di 2% = Rp {hrg1t_2shm1}')
    print(f'Beli disekitar harga {hargatr_shm1} sampai {hargab2_shm1}.  **jika bisa lebih kurang dari itu, maka akan lebih bagus\n')
    print(f'2. Saham {beli_saham2}')
    print(f'   - Harga terakhir saham {beli_saham2} = Rp {hargatr_shm2}')
    print(f'   - Harga saham {beli_saham2}  di 1% = Rp {harga1psn_shm2}')
    print(f'   - Harga batas saham {beli_saham2} di 2% = Rp {hargab2_shm2}')
    print(f'   - Harga 1 lot saham {beli_saham2} di 2% = Rp {hrg1t_2shm2}')
    print(f'Beli disekitar harga {hargatr_shm2} sampai {hargab2_shm2}.  **jika bisa lebih kurang dari itu, maka akan lebih bagus\n')
    print('!!!!! JANGAN SAMPAI KESINI !!!!!')
    print(f'~ Harga Maksimal pembelian saham {beli_saham1} di 5% = Rp {hargam5_shm1}')
    print(f'~ Harga Maksimal pembelian saham {beli_saham2} di 5% = Rp {hargam5_shm2}')