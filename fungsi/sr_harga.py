################ Fungsi untuk harga harga

import pandas as pd

## fungsi untuk menghasilkn harga akhir setelah dipersen. khusus untuk yang naik
def persen_naik(naik_persen,harga_terakhir): # (ingin berapa persen naiknya, harga tersakhir saham tersebut)
    untung = naik_persen/100*harga_terakhir # misal ingin 2% naiknya pada harga 750. maka 2/100*750=15 jadi untung 15 perak
    hasil_harga = harga_terakhir+untung # untuk harga akhir dari persen tersebut. maka 750+15(perak tadi)=765 jadi harga akhir dari persen tersebut 765 perak
    return hasil_harga # harga akhir setelah dipersen

## fungsi yang menghasilkan dataframe untuk pembeliah saham
def pembelian(df):
    list_saham = df['Saham'].tolist()
    # buat dataframe untuk wadah harga harga
    pembelian = pd.DataFrame(columns=['Saham','Last','Hrg -2%','Hrg -1%','Hrg 1%',
                                      'Hrg 2%','Hrg 1 lot2%','Hrg 3%'])
    for tic in list_saham:
        df_tic = pd.read_csv(f'data/psaham/{tic}.csv') # ambil dataframe saham tersebut
        harga_terakhir = df_tic['Close'].to_list()[-1] # ambil harga terakhir saham tersebut
        harga_n2psn = persen_naik(-2,harga_terakhir)# dapatkan harga akhir setelah dipersen -2%
        harga_n1psn = persen_naik(-1, harga_terakhir)# dapatkan harga akhir setelah dipersen -1%        
        harga_1psn = persen_naik(1, harga_terakhir)# dapatkan harga akhir setelah dipersen 1%
        harga_2psn = persen_naik(2,harga_terakhir)# dapatkan harga akhir setelah dipersen 2%
        hrg1lot_2psn = int(harga_2psn*100) # harga 1 lot di2%
        harga_3psn = persen_naik(3,harga_terakhir)# dapatkan harga akhir setelah dipersen 3%
        # masukkan ke dataframe
        pembelian = pd.concat([pembelian, pd.DataFrame.from_records([{
            'Saham':tic,'Last':harga_terakhir,'Hrg -2%':harga_n2psn,'Hrg -1%':harga_n1psn,
            'Hrg 1%':harga_1psn,'Hrg 2%':harga_2psn,'Hrg 1 lot2%':hrg1lot_2psn,'Hrg 3%':harga_3psn
        }])])
    pembelian.reset_index(inplace=True, drop=True) # mereset index
    return pembelian


## fungsi yang menghasilkan dataframe untuk penjualan saham
def penjualan(df):
    list_saham = df['Saham'].tolist() # mendapatkan list ticker ticker sahmnya
    # buat dataframe untuk wadah harga harga
    penjualan = pd.DataFrame(columns=['Saham','Harga 5%','Harga 10%','Harga 15%',
                                      'Harga 20%','Harga 25%','Harga 30%'])
    for tic in list_saham:
        df_tic = pd.read_csv(f'data/psaham/{tic}.csv') # ambil dataframe saham tersebut
        harga_terakhir = df_tic['Close'].to_list()[-1] # ambil harga terakhir saham tersebut
        hrg_5psn = persen_naik(5, harga_terakhir) #harga saham di 5%
        hrg_10psn = persen_naik(10, harga_terakhir) #harga saham di 10%
        hrg_15psn = persen_naik(15, harga_terakhir) #harga saham di 15%
        hrg_20psn = persen_naik(20, harga_terakhir) #harga saham di 20%
        hrg_25psn = persen_naik(25, harga_terakhir) #harga saham di 25%
        hrg_30psn = persen_naik(30, harga_terakhir) #harga saham di 30%
        # masukkan ke dataframe
        penjualan = pd.concat([penjualan, pd.DataFrame.from_records([{
            'Saham':tic,'Harga 5%':hrg_5psn,'Harga 10%':hrg_10psn,'Harga 15%':hrg_15psn,
            'Harga 20%':hrg_20psn,'Harga 25%':hrg_25psn,'Harga 30%':hrg_30psn
        }])])
    penjualan.reset_index(inplace=True, drop=True) # mereset index
    return penjualan