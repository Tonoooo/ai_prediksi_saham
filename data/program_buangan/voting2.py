# ~~~~~~~~~~~~~~~~~~~~~~~~ FUNGSI UNTUK MENGAMBIL PEMUNGUTAN SUARA (VOTING)
# ~~~~~ !!! INI KHUSUS UNTUK PROGRAM utama2.ipynb
#   Funsi fungsi ini untuk mengambil pemungutan suara dari kelas-kelas model itu

import pandas as pd

def peringkat_1(hasil_k2,hasil_k5,hasil_k6,hasil_k9,hasil_k12,
                hasil_k16,hasil_k17,hasil_k18,hasil_k20):
    try:
        # setelah mendapatkan dataframe para kelas, potong dan ambil 3 baris pertama
        #dan kolom 'Saham','Perubahan(%)'
        k2_1b = hasil_k2[0:1][['Saham','Perubahan(%)']]
        k5_1b = hasil_k5[0:1][['Saham','Perubahan(%)']]
        k6_1b = hasil_k6[0:1][['Saham','Perubahan(%)']]
        k9_1b = hasil_k9[0:1][['Saham','Perubahan(%)']]
        k12_1b = hasil_k12[0:1][['Saham','Perubahan(%)']]
        k16_1b = hasil_k16[0:1][['Saham','Perubahan(%)']]
        k17_1b = hasil_k17[0:1][['Saham','Perubahan(%)']]
        k18_1b = hasil_k18[0:1][['Saham','Perubahan(%)']]
        k20_1b = hasil_k20[0:1][['Saham','Perubahan(%)']]
        # gabungkan semua df itu
        p1b = pd.concat([k2_1b,k5_1b,k6_1b,k9_1b,k12_1b,k16_1b,k17_1b,k18_1b,k20_1b], 
                        keys=['k2_1b','k5_1b','k6_1b','k9_1b','k12_1b','k16_1b','k17_1b','k18_1b','k20_1b'])
        p1b_list = p1b['Saham'].tolist() # kolom saham jadikan sebuah list
        # ambil voting dari p1b_list
        vote_1b = pd.Series(p1b_list).value_counts() # pd series yang berisi saham dan banyak voting
        # jadikan vote_1b menjadi dataframe. ini untuk menyaring saham
        my_count_df = pd.DataFrame(vote_1b)# pd series tadi jadikan dataframe
        my_count_df.reset_index(inplace=True)#reset index
        my_count_df = my_count_df.rename(columns={"index": "Saham", 0:"voting"})#ganti nama kolom
        my_count_df=my_count_df.loc[my_count_df["voting"]>=2]# mengambil saham yang memiliki jumlah votenya minimal 2
        # menyiapkan dataframe untuk hasil akhir
        peringkat_1besar = pd.DataFrame(columns=['Saham','voting','total jumlah persentase(%)'])
        # for loop untuk mengisi dataframe peringkat_1besar
        for i in range(len(my_count_df)):
            # ambil key/kunci teratas(ticker saham yang paling banyak mendapatkan vote) di pandasSeries
            juara_1b = vote_1b.keys()[i] # mendapatkan key/kunci(ticker saham) di pandasSeries
            # ambil berapa banyak yang ngevote juara_1b
            juara_1bv = vote_1b[i] # mendapatkan nilai(banyak yang ngevote disuatu saham) pertama di pd.Series
            baris_1b=p1b[p1b.isin([juara_1b]).any(axis=1)] # mendapatkan semua baris yang memiliki nilai juara_1b
            totaljumlah_persen = baris_1b['Perubahan(%)'].sum() # menjumlahkan seluruh persentase si juara_1b
            # memasukkan ke dalam dataframe
            peringkat_1besar = pd.concat([peringkat_1besar, pd.DataFrame.from_records([{
                        'Saham':juara_1b, 'voting':juara_1bv,'total jumlah persentase(%)':totaljumlah_persen}])])
        ## rapihkan dataframe. PILIH MAU URUTANNYA SESUAI 'voting' ATAU 'total jumlah persentase(%)'
        peringkat_1besar.sort_values(by='voting',ascending=False,inplace=True)
        peringkat_1besar.reset_index(inplace=True, drop=True)
        return peringkat_1besar
    except:
        print('!!! ---> Diperingkat 3 besar tidak ada yang sama')


def peringkat_3(hasil_k2,hasil_k5,hasil_k6,hasil_k9,hasil_k12,
                hasil_k16,hasil_k17,hasil_k18,hasil_k20):
    try:
        # setelah mendapatkan dataframe para kelas, potong dan ambil 3 baris pertama
        #dan kolom 'Saham','Perubahan(%)'
        k2_3b = hasil_k2[0:3][['Saham','Perubahan(%)']]
        k5_3b = hasil_k5[0:3][['Saham','Perubahan(%)']]
        k6_3b = hasil_k6[0:3][['Saham','Perubahan(%)']]
        k9_3b = hasil_k9[0:3][['Saham','Perubahan(%)']]
        k12_3b = hasil_k12[0:3][['Saham','Perubahan(%)']]
        k16_3b = hasil_k16[0:3][['Saham','Perubahan(%)']]
        k17_3b = hasil_k17[0:3][['Saham','Perubahan(%)']]
        k18_3b = hasil_k18[0:3][['Saham','Perubahan(%)']]
        k20_3b = hasil_k20[0:3][['Saham','Perubahan(%)']]
        # gabungkan semua df itu
        p3b = pd.concat([k2_3b,k5_3b,k6_3b,k9_3b,k12_3b,k16_3b,k17_3b,k18_3b,k20_3b], 
                        keys=['k2_3b','k5_3b','k6_3b','k9_3b','k12_3b','k16_3b','k17_3b','k18_3b','k20_3b'])
        p3b_list = p3b['Saham'].tolist() # kolom saham jadikan sebuah list
        # ambil voting dari p3b_list
        vote_3b = pd.Series(p3b_list).value_counts() # pd series yang berisi saham dan banyak voting
        # jadikan vote_3b menjadi dataframe. ini untuk menyaring saham
        my_count_df = pd.DataFrame(vote_3b)# pd series tadi jadikan dataframe
        my_count_df.reset_index(inplace=True)#reset index
        my_count_df = my_count_df.rename(columns={"index": "Saham", 0:"voting"})#ganti nama kolom
        my_count_df=my_count_df.loc[my_count_df["voting"]>=2]# mengambil saham yang memiliki jumlah votenya minimal 2
        # menyiapkan dataframe untuk hasil akhir
        peringkat_3besar = pd.DataFrame(columns=['Saham','voting','total jumlah persentase(%)'])
        # for loop untuk mengisi dataframe peringkat_3besar
        for i in range(len(my_count_df)):
            # ambil key/kunci teratas(ticker saham yang paling banyak mendapatkan vote) di pandasSeries
            juara_3b = vote_3b.keys()[i] # mendapatkan key/kunci(ticker saham) di pandasSeries
            # ambil berapa banyak yang ngevote juara_3b
            juara_3bv = vote_3b[i] # mendapatkan nilai(banyak yang ngevote disuatu saham) pertama di pd.Series
            baris_3b=p3b[p3b.isin([juara_3b]).any(axis=1)] # mendapatkan semua baris yang memiliki nilai juara_3b
            totaljumlah_persen = baris_3b['Perubahan(%)'].sum() # menjumlahkan seluruh persentase si juara_3b
            # memasukkan ke dalam dataframe
            peringkat_3besar = pd.concat([peringkat_3besar, pd.DataFrame.from_records([{
                        'Saham':juara_3b, 'voting':juara_3bv,'total jumlah persentase(%)':totaljumlah_persen}])])
        ## rapihkan dataframe. PILIH MAU URUTANNYA SESUAI 'voting' ATAU 'total jumlah persentase(%)'
        peringkat_3besar.sort_values(by='voting',ascending=False,inplace=True)
        peringkat_3besar.reset_index(inplace=True, drop=True)
        return peringkat_3besar
    except:
        print('!!! ---> Diperingkat 3 besar tidak ada yang sama')


def peringkat_5(hasil_k2,hasil_k5,hasil_k6,hasil_k9,hasil_k12,
                hasil_k16,hasil_k17,hasil_k18,hasil_k20):
    try:
        k2_5b = hasil_k2[0:5][['Saham','Perubahan(%)']]
        k5_5b = hasil_k5[0:5][['Saham','Perubahan(%)']]
        k6_5b = hasil_k6[0:5][['Saham','Perubahan(%)']]
        k9_5b = hasil_k9[0:5][['Saham','Perubahan(%)']]
        k12_5b = hasil_k12[0:5][['Saham','Perubahan(%)']]
        k16_5b = hasil_k16[0:5][['Saham','Perubahan(%)']]
        k17_5b = hasil_k17[0:5][['Saham','Perubahan(%)']]
        k18_5b = hasil_k18[0:5][['Saham','Perubahan(%)']]
        k20_5b = hasil_k20[0:5][['Saham','Perubahan(%)']]
        # gabungkan semua df itu
        p5b = pd.concat([k2_5b,k5_5b,k6_5b,k9_5b,k12_5b,k16_5b,k17_5b,k18_5b,k20_5b], 
                        keys=['k2_5b','k5_5b','k6_5b','k9_5b','k12_5b','k16_5b','k17_5b','k18_5b','k20_5b'])
        p5b_list = p5b['Saham'].tolist() # kolom saham jadikan sebuah list
        # ambil voting dari p5b_list
        vote_5b = pd.Series(p5b_list).value_counts() # pd series yang berisi saham dan banyak voting
        # jadikan vote_5b menjadi dataframe. ini untuk menyaring saham
        my_count_df = pd.DataFrame(vote_5b)# pd series tadi jadikan dataframe
        my_count_df.reset_index(inplace=True)#reset index
        my_count_df = my_count_df.rename(columns={"index": "Saham", 0:"voting"})#ganti nama kolom
        my_count_df=my_count_df.loc[my_count_df["voting"]>=2]# mengambil saham yang memiliki jumlah votenya minimal 2
        # menyiapkan dataframe untuk hasil akhir
        peringkat_5besar = pd.DataFrame(columns=['Saham','voting','total jumlah persentase(%)'])
        # for loop untuk mengisi dataframe peringkat_5besar
        for i in range(len(my_count_df)):
            # ambil key/kunci teratas(ticker saham yang paling banyak mendapatkan vote) di pandasSeries
            juara_5b = vote_5b.keys()[i] # mendapatkan key/kunci(ticker saham) di pandasSeries
            # ambil berapa banyak yang ngevote juara_5b
            juara_5bv = vote_5b[i] # mendapatkan nilai(banyak yang ngevote disuatu saham) pertama di pd.Series
            baris_5b=p5b[p5b.isin([juara_5b]).any(axis=1)] # mendapatkan semua baris yang memiliki nilai juara_5b
            totaljumlah_persen = baris_5b['Perubahan(%)'].sum() # menjumlahkan seluruh persentase si juara_5b
            # memasukkan ke dalam dataframe
            peringkat_5besar = pd.concat([peringkat_5besar, pd.DataFrame.from_records([{
                        'Saham':juara_5b, 'voting':juara_5bv,'total jumlah persentase(%)':totaljumlah_persen}])])
        # PILIH MAU URUTANNYA SESUAI 'voting' ATAU 'total jumlah persentase(%)'
        peringkat_5besar.sort_values(by='voting',ascending=False,inplace=True)
        peringkat_5besar.reset_index(inplace=True, drop=True)
        return peringkat_5besar
    except:
        print('!!! ---> Diperingkat 5 besar tidak ada yang sama')


def peringkat_10(hasil_k2,hasil_k5,hasil_k6,hasil_k9,hasil_k12,
                hasil_k16,hasil_k17,hasil_k18,hasil_k20):
    try:
        k2_10b = hasil_k2[0:10][['Saham','Perubahan(%)']]
        k5_10b = hasil_k5[0:10][['Saham','Perubahan(%)']]
        k6_10b = hasil_k6[0:10][['Saham','Perubahan(%)']]
        k9_10b = hasil_k9[0:10][['Saham','Perubahan(%)']]
        k12_10b = hasil_k12[0:10][['Saham','Perubahan(%)']]
        k16_10b = hasil_k16[0:10][['Saham','Perubahan(%)']]
        k17_10b = hasil_k17[0:10][['Saham','Perubahan(%)']]
        k18_10b = hasil_k18[0:10][['Saham','Perubahan(%)']]
        k20_10b = hasil_k20[0:10][['Saham','Perubahan(%)']]
        # gabungkan semua df itu
        p10b = pd.concat([k2_10b,k5_10b,k6_10b,k9_10b,
                         k12_10b,k16_10b,k17_10b,k18_10b,k20_10b],
                         keys=['k2_10b','k5_10b','k6_10b','k9_10b','k10_10b',
                              'k12_10b','k16_10b','k17_10b','k18_10b','k19_10b','k20_10b'])
        p10b_list = p10b['Saham'].tolist() # kolom saham jadikan sebuah list
        # ambil voting dari p10b_list
        vote_10b = pd.Series(p10b_list).value_counts() # pd series yang berisi saham dan banyak voting
        # jadikan vote_10b menjadi dataframe. ini untuk menyaring saham
        my_count_df = pd.DataFrame(vote_10b)# pd series tadi jadikan dataframe
        my_count_df.reset_index(inplace=True)#reset index
        my_count_df = my_count_df.rename(columns={"index": "Saham", 0:"voting"})#ganti nama kolom
        my_count_df=my_count_df.loc[my_count_df["voting"]>=2]# mengambil saham yang memiliki jumlah votenya minimal 2
        # menyiapkan dataframe untuk hasil akhir
        peringkat_10besar = pd.DataFrame(columns=['Saham','voting','total jumlah persentase(%)'])
        # for loop untuk mengisi dataframe peringkat_10besar
        for i in range(len(my_count_df)):
            # ambil key/kunci teratas(ticker saham yang paling banyak mendapatkan vote) di pandasSeries
            juara_10b = vote_10b.keys()[i] # mendapatkan key/kunci(ticker saham) di pandasSeries
            # ambil berapa banyak yang ngevote juara_10b
            juara_10bv = vote_10b[i] # mendapatkan nilai(banyak yang ngevote disuatu saham) pertama di pd.Series
            baris_10b=p10b[p10b.isin([juara_10b]).any(axis=1)] # mendapatkan semua baris yang memiliki nilai juara_10b
            totaljumlah_persen = baris_10b['Perubahan(%)'].sum() # menjumlahkan seluruh persentase si juara_10b
            # memasukkan ke dalam dataframe
            peringkat_10besar = pd.concat([peringkat_10besar, pd.DataFrame.from_records([{
                        'Saham':juara_10b, 'voting':juara_10bv,'total jumlah persentase(%)':totaljumlah_persen}])])
        # PILIH MAU URUTANNYA SESUAI 'voting' ATAU 'total jumlah persentase(%)'
        peringkat_10besar.sort_values(by='voting',ascending=False,inplace=True)
        peringkat_10besar.reset_index(inplace=True, drop=True)
        return peringkat_10besar
    except:
        print('!!! ---> Diperingkat 10 besar tidak ada yang sama')




##  !!! FUNGSI UNTUK KEADAAN DARURAT
# fungsi ini digunakan jika peringkat 3,5,dan 10 tidak ada yang saham sama 
def pemungutan_suara(hasil_k2,hasil_k5,hasil_k6,hasil_k9,hasil_k12,
                hasil_k16,hasil_k17,hasil_k18,hasil_k20):
    k2 = hasil_k2[['Saham','Perubahan(%)']]
    k5 = hasil_k5[['Saham','Perubahan(%)']]
    k6 = hasil_k6[['Saham','Perubahan(%)']]
    k9 = hasil_k9[['Saham','Perubahan(%)']]
    k12 = hasil_k12[['Saham','Perubahan(%)']]
    k16 = hasil_k16[['Saham','Perubahan(%)']]
    k17 = hasil_k17[['Saham','Perubahan(%)']]
    k18 = hasil_k18[['Saham','Perubahan(%)']]
    k20 = hasil_k20[['Saham','Perubahan(%)']]
    # gabungkan semua df itu
    pb = pd.concat([k2,k5,k6,k9,
                    k12,k16,k17,k18,k20], 
                   keys=['k2','k5','k6','k9','k12','k16','k17','k18','k20'])
    pb_list = pb['Saham'].tolist() # kolom saham jadikan sebuah list
    # ambil voting dari pb_list
    vote = pd.Series(pb_list).value_counts() # pd series yang berisi saham dan banyak voting
    # jadikan vote menjadi dataframe. ini untuk menyaring saham
    my_count_df = pd.DataFrame(vote)# pd series tadi jadikan dataframe
    my_count_df.reset_index(inplace=True)#reset index
    my_count_df = my_count_df.rename(columns={"index": "Saham", 0:"voting"})#ganti nama kolom
    my_count_df=my_count_df.loc[my_count_df["voting"]]# mengambil saham yang memiliki jumlah votenya minimal 2
    # menyiapkan dataframe untuk hasil akhir
    peringkat = pd.DataFrame(columns=['Saham','voting','total jumlah persentase(%)'])
    # for loop untuk mengisi dataframe peringkat
    for i in range(len(my_count_df)):
        # ambil key/kunci teratas(ticker saham yang paling banyak mendapatkan vote) di pandasSeries
        juara = vote.keys()[i] # mendapatkan key/kunci(ticker saham) di pandasSeries
        # ambil berapa banyak yang ngevote juara
        juarav = vote[i] # mendapatkan nilai(banyak yang ngevote disuatu saham) pertama di pd.Series
        baris=pb[pb.isin([juara]).any(axis=1)] # mendapatkan semua baris yang memiliki nilai juara
        totaljumlah_persen = baris['Perubahan(%)'].sum() # menjumlahkan seluruh persentase si juara
        # memasukkan ke dalam dataframe
        peringkat = pd.concat([peringkat, pd.DataFrame.from_records([{
                    'Saham':juara, 'voting':juarav,'total jumlah persentase(%)':totaljumlah_persen}])])
    # rapihkan dataframe.PILIH MAU URUTANNYA SESUAI 'voting' ATAU 'total jumlah persentase(%)'
    peringkat.sort_values(by='voting',ascending=False,inplace=True)
    peringkat.reset_index(inplace=True, drop=True)
    return peringkat