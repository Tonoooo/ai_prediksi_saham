# ~~~~~~~~~~~~~~~~~~ fungis untuk mendapatkan data saham untuk model memprediksi

import pandas_datareader as pdr

# fungsi ini mempunya 3 parameter: tanggal_mulai, tanggal_akhir, ticker(ticker
# ini masukkan dalam bentuk list)
def psaham(tanggal_mulai, tanggal_akhir, ticker):
    full_ticker = ticker
    # membegi dua tickernya karna batas output yfinance hanya sebanyak 281
    ticker1 = full_ticker[:int(len(full_ticker)/2)+1] 
    ticker2 = full_ticker[int(len(full_ticker)/2)+1:] 
    
    # mendapatkan info jika ada tanggal yang ganda
    ganda = pdr.DataReader('AALI.JK','yahoo',tanggal_mulai,tanggal_akhir)
    ganda.reset_index(inplace=True)
    ada_ganda = ganda['Date'].duplicated().any()
    
    if ada_ganda==False: # jika tidak ada tanggal yang ganda maka:
        # for loop untuk mendapatkan data data nya dan disimpan difiles csv
        ## bagian pertama
        for tic in ticker1:
            df = pdr.DataReader(f'{tic}.JK', data_source='yahoo',start=tanggal_mulai, end=tanggal_akhir) # dapatkan datanya
            df.to_csv(f'data/psaham/{tic}.csv')# simpan data nya
        ## bagian kedua
        for tic in ticker2:
            df = pdr.DataReader(f'{tic}.JK', data_source='yahoo',start=tanggal_mulai, end=tanggal_akhir) # dapatkan datanya
            df.to_csv(f'data/psaham/{tic}.csv')# simpan data nya
    else: # jika ada tanggal yang gandda maka:
        # for loop untuk mendapatkan data data nya dan disimpan difiles csv
        ## bagian pertama
        for tic in ticker1:
            df = pdr.DataReader(f'{tic}.JK', data_source='yahoo',start=tanggal_mulai, end=tanggal_akhir) # dapatkan datanya
            df.drop_duplicates(inplace=True) # menghapus baris duplikat
            df.to_csv(f'data/psaham/{tic}.csv')# simpan data nya
        ## bagian kedua
        for tic in ticker2:
            df = pdr.DataReader(f'{tic}.JK', data_source='yahoo',start=tanggal_mulai, end=tanggal_akhir) # dapatkan datanya
            df.drop_duplicates(inplace=True) # menghapus baris duplikat
            df.to_csv(f'data/psaham/{tic}.csv')# simpan data nya