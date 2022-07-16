########### FUNGSI UNTUK MENAMPILKAN SAHAM SAHAM YANG HARUS DIBELI

def beli_saham(df, h_predik): # 2 parameter: dataframe, berapa hari ingin memprediksi
    # jika dataframe kosong/tidak ada saham yang direkomendasikan oleh program
    if len(df) == 0:
        print('~~~~~ JANGAN BELI SAHAM APAPUN ~~~~~')
    # jika dataframenya berisi hanya 1 saham yang direkomendasikan oleh program
    elif len(df) == 1:
        beli_saham1 = df['Saham'][0] # mendapatkan saham pertama
        hargatr_shm1 = df['Last'][0]# mendapatkan harga terakhir saham pertama
        harga1psn_shm1 = df['Hrg 1%'][0]#mendapatkan Harga 1% saham pertama
        hargab2_shm1 = df['Hrg 2%'][0]#mendapatkan Harga 2% saham pertama
        hrg1t_2shm1 = df['Hrg 1 lot2%'][0]#mendapatkan Harga 2% di1lot saham pertama
        hargam3_shm1 = df['Hrg 3%'][0]#mendapatkan Harga 3% saham pertama
        print(f'     Saham-saham yang akan naik {h_predik} hari kedepan:')
        print(f'1. Saham {beli_saham1}')
        print(f'   - Harga terakhir saham {beli_saham1} = Rp {hargatr_shm1}')
        print(f'   - Harga saham {beli_saham1}  di 1% = Rp {harga1psn_shm1}')
        print(f'   - Harga batas saham {beli_saham1} di 2% = Rp {hargab2_shm1}')
        print(f'   - Harga 1 lot saham {beli_saham1} di 2% = Rp {hrg1t_2shm1}')
        print(f'Beli disekitar harga {hargatr_shm1} sampai {hargab2_shm1}.  **jika bisa lebih kurang dari itu, maka akan lebih bagus\n')
        print(f'~ Harga Maksimal pembelian saham {beli_saham1} di 5% = Rp {hargam3_shm1}')
    # jika dataframenya berisi 2 saham atau lebih yang direkomendasikan oleh program
    else:
        beli_saham1 = df['Saham'][0] # mendapatkan saham pertama
        hargatr_shm1 = df['Last'][0]# mendapatkan harga terakhir saham pertama
        harga1psn_shm1 = df['Hrg 1%'][0]#mendapatkan Harga 1% saham pertama
        hargab2_shm1 = df['Hrg 2%'][0]#mendapatkan Harga 2% saham pertama
        hrg1t_2shm1 = df['Hrg 1 lot2%'][0]#mendapatkan Harga 2% di1lot saham pertama
        hargam3_shm1 = df['Hrg 3%'][0]#mendapatkan Harga 3% saham pertama
        beli_saham2 = df['Saham'][1]# mendapatkan saham kedua
        hargatr_shm2 = df['Last'][1]# mendapatkan harga terakhir saham keuda
        harga1psn_shm2 = df['Hrg 1%'][1]#mendapatkan Harga 1% saham keuda
        hargab2_shm2 = df['Hrg 2%'][1]#mendapatkan Harga 2% saham keuda
        hrg1t_2shm2 = df['Hrg 1 lot2%'][1]#mendapatkan Harga 2% di1lot saham keuda
        hargam3_shm2 = df['Hrg 3%'][1]#mendapatkan Harga 3% saham keuda
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
        print(f'~ Harga Maksimal pembelian saham {beli_saham1} di 5% = Rp {hargam3_shm1}')
        print(f'~ Harga Maksimal pembelian saham {beli_saham2} di 5% = Rp {hargam3_shm2}')
    