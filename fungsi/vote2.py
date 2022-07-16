# ~~~~~~~~~~~~~~~~~~~~~~~~ FUNGSI UNTUK MENGAMBIL PEMUNGUTAN SUARA
# ~~~~~ !!! INI KHUSUS UNTUK PROGRAM main2.ipynb dan superior.ipynb
#   Funsi fungsi ini untuk mengambil pemungutan suara dari 5 kelas model itu

import pandas as pd

def peringkat_10(hasil_k1,hasil_k2,hasil_k3,hasil_k4,hasil_k5,
                hasil_k6,hasil_k7,hasil_k8,hasil_k9,hasil_k10,
                hasil_k11,hasil_k12,hasil_k13,hasil_k14,hasil_k15,
                hasil_k16,hasil_k17,hasil_k18,hasil_k19,hasil_k20,hasil_k21):
    try:
        k1_10b = hasil_k1[0:10][['Saham','Perubahan(%)']]
        k2_10b = hasil_k2[0:10][['Saham','Perubahan(%)']]
        k3_10b = hasil_k3[0:10][['Saham','Perubahan(%)']]
        k4_10b = hasil_k4[0:10][['Saham','Perubahan(%)']]
        k5_10b = hasil_k5[0:10][['Saham','Perubahan(%)']]
        k6_10b = hasil_k6[0:10][['Saham','Perubahan(%)']]
        k7_10b = hasil_k7[0:10][['Saham','Perubahan(%)']]
        k8_10b = hasil_k8[0:10][['Saham','Perubahan(%)']]
        k9_10b = hasil_k9[0:10][['Saham','Perubahan(%)']]
        k10_10b = hasil_k10[0:10][['Saham','Perubahan(%)']]
        k11_10b = hasil_k11[0:10][['Saham','Perubahan(%)']]
        k12_10b = hasil_k12[0:10][['Saham','Perubahan(%)']]
        k13_10b = hasil_k13[0:10][['Saham','Perubahan(%)']]
        k14_10b = hasil_k14[0:10][['Saham','Perubahan(%)']]
        k15_10b = hasil_k15[0:10][['Saham','Perubahan(%)']]
        k16_10b = hasil_k16[0:10][['Saham','Perubahan(%)']]
        k17_10b = hasil_k17[0:10][['Saham','Perubahan(%)']]
        k18_10b = hasil_k18[0:10][['Saham','Perubahan(%)']]
        k19_10b = hasil_k19[0:10][['Saham','Perubahan(%)']]
        k20_10b = hasil_k20[0:10][['Saham','Perubahan(%)']]
        k21_10b = hasil_k21[0:10][['Saham','Perubahan(%)']]
        # gabungkan semua df itu
        p10b = pd.concat([k1_10b,k2_10b,k3_10b,k4_10b,k5_10b,k6_10b,k7_10b,k8_10b,k9_10b,k10_10b,
                         k11_10b,k12_10b,k13_10b,k14_10b,k15_10b,k16_10b,k17_10b,k18_10b,k19_10b,k20_10b,k21_10b],
                         keys=['k1_10b','k2_10b','k3_10b','k4_10b','k5_10b','k6_10b','k7_10b','k8_10b','k9_10b','k10_10b',
                              'k11_10b','k12_10b','k13_10b','k14_10b','k15_10b','k16_10b','k17_10b','k18_10b','k19_10b','k20_10b','k21_10b'])
        p10b_list = p10b['Saham'].tolist() # kolom saham jadikan sebuah list
        # ambil voting dari p10b_list
        vote_10b = pd.Series(p10b_list).value_counts() # pd series yang berisi saham dan banyak voting. Dipandas series itu ada dua komponen yaitu key dan isinya, nah disini jadi key=saham,isinya=banyakvote
        # jadikan vote_10b menjadi dataframe. ini untuk menyaring saham
        my_count_df = pd.DataFrame(vote_10b)# pd series tadi jadikan dataframe
        my_count_df.reset_index(inplace=True)#reset index
        my_count_df = my_count_df.rename(columns={"index": "Saham", 0:"voting"})#ganti nama kolom
        my_count_df=my_count_df.loc[my_count_df["voting"]>=2]# mengambil saham yang memiliki jumlah votenya minimal 2
        # menyiapkan dataframe untuk hasil akhir
        df_peringkat_10besar = pd.DataFrame(columns=['Saham','voting','total jumlah persentase(%)'])
        # for loop untuk mengisi dataframe df_peringkat_10besar
        for i in range(len(my_count_df)):
            # ambil key/kunci teratas(ticker saham yang paling banyak mendapatkan vote) di pandasSeries
            juara_10b = vote_10b.keys()[i] # mendapatkan key/kunci(ticker saham) di pandasSeries
            # ambil berapa banyak yang ngevote juara_10b
            juara_10bv = vote_10b[i] # mendapatkan isinya/nilai(banyak yang ngevote disuatu saham) si"i" di pd.Series
            baris_10b=p10b[p10b.isin([juara_10b]).any(axis=1)] # mendapatkan semua baris yang memiliki nilai juara_10b
            totaljumlah_persen = baris_10b['Perubahan(%)'].sum() # menjumlahkan seluruh persentase si juara_10b
            # memasukkan ke dalam dataframe
            df_peringkat_10besar = pd.concat([df_peringkat_10besar, pd.DataFrame.from_records([{
                        'Saham':juara_10b, 'voting':juara_10bv,'total jumlah persentase(%)':totaljumlah_persen}])])
        # rapihkan dataframe
        # mengurutkan sesuai dengan banyak voting
        df_peringkat_10besar.sort_values(by='voting',ascending=False,inplace=True)
        df_peringkat_10besar.reset_index(inplace=True, drop=True)
        # mendapatkan kolom saham lalu jadikan list
        list_10b = df_peringkat_10besar['Saham'].tolist()
        return df_peringkat_10besar, list_10b
    except:
        print('!!! ---> Diperingkat 10 besar tidak ada yang sama')


def peringkat_10dan5(hasil_k1,hasil_k2,hasil_k3,hasil_k4,hasil_k5,
                hasil_k6,hasil_k7,hasil_k8,hasil_k9,hasil_k10,
                hasil_k11,hasil_k12,hasil_k13,hasil_k14,hasil_k15,
                hasil_k16,hasil_k17,hasil_k18,hasil_k19,hasil_k20,hasil_k21):
    try:
        k1_10b = hasil_k1[0:10][['Saham','Perubahan(%)']]
        k2_10b = hasil_k2[0:10][['Saham','Perubahan(%)']]
        k3_10b = hasil_k3[0:10][['Saham','Perubahan(%)']]
        k4_10b = hasil_k4[0:10][['Saham','Perubahan(%)']]
        k5_10b = hasil_k5[0:10][['Saham','Perubahan(%)']]
        k6_10b = hasil_k6[0:10][['Saham','Perubahan(%)']]
        k7_10b = hasil_k7[0:10][['Saham','Perubahan(%)']]
        k8_10b = hasil_k8[0:10][['Saham','Perubahan(%)']]
        k9_10b = hasil_k9[0:10][['Saham','Perubahan(%)']]
        k10_10b = hasil_k10[0:10][['Saham','Perubahan(%)']]
        k11_10b = hasil_k11[0:10][['Saham','Perubahan(%)']]
        k12_10b = hasil_k12[0:10][['Saham','Perubahan(%)']]
        k13_10b = hasil_k13[0:10][['Saham','Perubahan(%)']]
        k14_10b = hasil_k14[0:10][['Saham','Perubahan(%)']]
        k15_10b = hasil_k15[0:10][['Saham','Perubahan(%)']]
        k16_10b = hasil_k16[0:10][['Saham','Perubahan(%)']]
        k17_10b = hasil_k17[0:10][['Saham','Perubahan(%)']]
        k18_10b = hasil_k18[0:10][['Saham','Perubahan(%)']]
        k19_10b = hasil_k19[0:10][['Saham','Perubahan(%)']]
        k20_10b = hasil_k20[0:10][['Saham','Perubahan(%)']]
        k21_10b = hasil_k21[0:10][['Saham','Perubahan(%)']]
        # gabungkan semua df itu
        p10b = pd.concat([k1_10b,k2_10b,k3_10b,k4_10b,k5_10b,k6_10b,k7_10b,k8_10b,k9_10b,k10_10b,
                         k11_10b,k12_10b,k13_10b,k14_10b,k15_10b,k16_10b,k17_10b,k18_10b,k19_10b,k20_10b,k21_10b],
                         keys=['k1_10b','k2_10b','k3_10b','k4_10b','k5_10b','k6_10b','k7_10b','k8_10b','k9_10b','k10_10b',
                              'k11_10b','k12_10b','k13_10b','k14_10b','k15_10b','k16_10b','k17_10b','k18_10b','k19_10b','k20_10b','k21_10b'])
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
        ### rapihkan dataframe dan mengurutkan sesuai banyak voting
        # peringkat 10 besar
        peringkat_10besar.sort_values(by='voting',ascending=False,inplace=True)
        peringkat_10besar.reset_index(inplace=True, drop=True)
        # peringkat 5 besar
        peringkat_5besar = peringkat_10besar[0:5]
        peringkat_5besar = peringkat_5besar.sort_values(by='total jumlah persentase(%)',ascending=False)
        peringkat_5besar.reset_index(inplace=True, drop=True)
        
        return peringkat_5besar, peringkat_10besar
    except:
        print('!!! ---> Diperingkat 10 dan 5 besar tidak ada yang sama')
# perbedaan  peringkat 10 besar dan 5 besar adalah jika peringkat 10 besar diurutkan sesuai dengan
#banyak suara dari yang terbesar ke yang terkecil. Tapi jika peringkat 5 besar adalah diambil 5 
#terbesar dari peringkat 10 besar, kemudian diubah urutannya sesuai 'total jumlah persentase(%)'
#dari yang terbesar ke yang terkecil.




##  !!! FUNGSI UNTUK KEADAAN DARURAT
# fungsi ini digunakan jika peringkat 3,5,dan 10 tidak ada yang saham sama 
def pemungutan_suara(hasil_k1,hasil_k2,hasil_k3,hasil_k4,hasil_k5,
                hasil_k6,hasil_k7,hasil_k8,hasil_k9,hasil_k10,
                hasil_k11,hasil_k12,hasil_k13,hasil_k14,hasil_k15,
                hasil_k16,hasil_k17,hasil_k18,hasil_k19,hasil_k20,hasil_k21):
    k1 = hasil_k1[['Saham','Perubahan(%)']]
    k2 = hasil_k2[['Saham','Perubahan(%)']]
    k3 = hasil_k3[['Saham','Perubahan(%)']]
    k4 = hasil_k4[['Saham','Perubahan(%)']]
    k5 = hasil_k5[['Saham','Perubahan(%)']]
    k6 = hasil_k6[['Saham','Perubahan(%)']]
    k7 = hasil_k7[['Saham','Perubahan(%)']]
    k8 = hasil_k8[['Saham','Perubahan(%)']]
    k9 = hasil_k9[['Saham','Perubahan(%)']]
    k10 = hasil_k10[['Saham','Perubahan(%)']]
    k11 = hasil_k11[['Saham','Perubahan(%)']]
    k12 = hasil_k12[['Saham','Perubahan(%)']]
    k13 = hasil_k13[['Saham','Perubahan(%)']]
    k14 = hasil_k14[['Saham','Perubahan(%)']]
    k15 = hasil_k15[['Saham','Perubahan(%)']]
    k16 = hasil_k16[['Saham','Perubahan(%)']]
    k17 = hasil_k17[['Saham','Perubahan(%)']]
    k18 = hasil_k18[['Saham','Perubahan(%)']]
    k19 = hasil_k19[['Saham','Perubahan(%)']]
    k20 = hasil_k20[['Saham','Perubahan(%)']]
    k21 = hasil_k21[['Saham','Perubahan(%)']]
    # gabungkan semua df itu
    pb = pd.concat([k1,k2,k3,k4,k5,k6,k7,k8,k9,k10,
                    k11,k12,k13,k14,k15,k16,k17,k18,k19,k20,k21], 
                   keys=['k1','k2','k3','k4','k5','k6','k7','k8','k9','k10',
                         'k11','k12','k13','k14','k15','k16','k17','k18','k19','k20','k21'])
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
    # rapihkan dataframe
    peringkat.sort_values(by='total jumlah persentase(%)',ascending=False,inplace=True)
    peringkat.reset_index(inplace=True, drop=True)
    return peringkat