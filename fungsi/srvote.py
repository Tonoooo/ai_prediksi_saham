# ~~~~~~~~~~~~~~~~~~~~~~~~ FUNGSI UNTUK MENGAMBIL PEMUNGUTAN SUARA
# ~~~~~ !!! INI KHUSUS UNTUK PROGRAM superior.ipynb
#   Funsi fungsi ini untuk mengambil pemungutan suara dari kelas kelas model itu

# sebenarnya tidak perlu pake try&except. ini pasti tidak akan error. tapi sudah kagok, males ubah lagi

import pandas as pd

def peringkat2_besar(p5_main1,p5_main2):
    try:
        # ambil dua baris pertama saja
        df_p2_main1 = p5_main1[:2] 
        df_p2_main2 = p5_main2[:2]
        # menggabungkan semua df itu menjadi satu dataframe
        p2b = pd.concat([df_p2_main1,df_p2_main2],
                        keys=['df_p2_main1','df_p2_main2'])
        p2b_list = p2b['Saham'].tolist()# list ticker saham
        ## list tadi(p2b_list) jadikan pdseries, lalu dihitung berapa banyak yang sama (disini dilakukan voting)
        vote_2b = pd.Series(p2b_list).value_counts()# contoh: UNVR    3 (key : isinya). value_counts() untuk menghitung elemen yang sama
        ## pdSeries tadi(vote_2b) jadikan dataframe. ini untuk menyaring saham
        df_hitung = pd.DataFrame(vote_2b)# pdSeries tadi(vote_2b) jadikan dataframe.bentuknya contoh: ICBP	2 (ini indexnya kolom saham.)
        df_hitung.reset_index(inplace=True)#mereset index, sekaligus menambahkan kolom index. karnakan tadi tidak ada index nomer. maka: 1	ICBP	2
        df_hitung = df_hitung.rename(columns={"index": "Saham", 0: "voting"})# mengganti nama kolom
        df_hitung = df_hitung.loc[df_hitung["voting"]>=2]# disini kita hanya mengambil saham yang memiliki jumlah votenya minimal 2
        ## menyiapkan dataframe untuk hasil akhir
        df_peringkat_2besar = pd.DataFrame(columns=['Saham','voting','rata-rata nilai persentase(%)'])
        ## for loop untuk mengisi dataframe df_peringkat_2besar
        for i in range(len(df_hitung)):
            juara_2b = vote_2b.keys()[i]# ambil key si"i" (key disini adalah ticker sahamnya)
            juara_2bv = vote_2b[i]# ambil isinya si"i" (isinya disini adalah berapa banyak yang ngevote)
            ## mengambil 'rata-rata nilai persentase(%)' sisaham juara_2b di semua baris yang ada didataframe p2b lalu merata rata kannya
            baris_2b=p2b[p2b.isin([juara_2b]).any(axis=1)]# mendapatkan semua bari yang memiliki saham si juara_2b. ini berbentuk dataframe
            ratarata_ttljmlpsn = baris_2b['total jumlah persentase(%)'].mean() # rata rata total jumlah persentase saham si "i"
            ## memasukkan ke dalam dataframe df_peringkat_2besar
            df_peringkat_2besar = pd.concat([df_peringkat_2besar, pd.DataFrame.from_records([{
                        'Saham':juara_2b, 'voting':juara_2bv,'rata-rata nilai persentase(%)':ratarata_ttljmlpsn}])])
        ## merapihkan dataframe
        df_peringkat_2besar.sort_values(by=['voting','rata-rata nilai persentase(%)'],ascending=False,inplace=True)
        df_peringkat_2besar.reset_index(inplace=True, drop=True)
        return df_peringkat_2besar
    except:
        print('!!! ---> Diperingkat 2 besar tidak ada yang sama')
    

def peringkat5_besar(p5_main1,p5_main2):
    try:
        df_p5_main1 = p5_main1
        df_p5_main2 = p5_main2
        # menggabungkan semua df itu menjadi satu dataframe
        p5b = pd.concat([df_p5_main1,df_p5_main2],
                        keys=['df_p5_main1','df_p5_main2'])
        p5b_list = p5b['Saham'].tolist()# list ticker saham
        ## list tadi(p5b_list) jadikan pdseries, lalu dihitung berapa banyak yang sama (disini dilakukan voting)
        vote_5b = pd.Series(p5b_list).value_counts()# contoh: UNVR    3 (key : isinya). value_counts() untuk menghitung elemen yang sama
        ## pdSeries tadi(vote_5b) jadikan dataframe. ini untuk menyaring saham
        df_hitung = pd.DataFrame(vote_5b)# pdSeries tadi(vote_5b) jadikan dataframe.bentuknya contoh: ICBP	2 (ini indexnya kolom saham.)
        df_hitung.reset_index(inplace=True)#mereset index, sekaligus menambahkan kolom index. karnakan tadi tidak ada index nomer. maka: 1	ICBP	2
        df_hitung = df_hitung.rename(columns={"index": "Saham", 0: "voting"})# mengganti nama kolom
        df_hitung = df_hitung.loc[df_hitung["voting"]>=2]# disini kita hanya mengambil saham yang memiliki jumlah votenya minimal 2
        ## menyiapkan dataframe untuk hasil akhir
        df_peringkat_5besar = pd.DataFrame(columns=['Saham','voting','rata-rata nilai persentase(%)'])
        ## for loop untuk mengisi dataframe df_peringkat_5besar
        for i in range(len(df_hitung)):
            juara_5b = vote_5b.keys()[i]# ambil key si"i" (key disini adalah ticker sahamnya)
            juara_5bv = vote_5b[i]# ambil isinya si"i" (isinya disini adalah berapa banyak yang ngevote)
            ## mengambil 'rata-rata nilai persentase(%)' sisaham juara_5b di semua baris yang ada didataframe p5b lalu merata rata kannya
            baris_5b=p5b[p5b.isin([juara_5b]).any(axis=1)]# mendapatkan semua bari yang memiliki saham si juara_5b. ini berbentuk dataframe
            ratarata_ttljmlpsn = baris_5b['total jumlah persentase(%)'].mean() # rata rata total jumlah persentase saham si "i"
            ## memasukkan ke dalam dataframe df_peringkat_5besar
            df_peringkat_5besar = pd.concat([df_peringkat_5besar, pd.DataFrame.from_records([{
                        'Saham':juara_5b, 'voting':juara_5bv,'rata-rata nilai persentase(%)':ratarata_ttljmlpsn}])])
        ## merapihkan dataframe
        df_peringkat_5besar.sort_values(by=['voting','rata-rata nilai persentase(%)'],ascending=False,inplace=True)
        df_peringkat_5besar.reset_index(inplace=True, drop=True)
        return df_peringkat_5besar
    except:
        print('!!! ---> Diperingkat 5 besar tidak ada yang sama')
        df_peringkat_5besar = pd.DataFrame({'Saham':0,'voting':0,'rata-rata nilai persentase(%)':0})
        return df_peringkat_5besar
    

def peringkat10_besar(p10_main1,p10_main2):
    try:
        df_p10_main1 = p10_main1
        df_p10_main2 = p10_main2
        # menggabungkan semua df itu menjadi satu dataframe
        p10b = pd.concat([df_p10_main1,df_p10_main2],
                        keys=['df_p10_main1','df_p10_main2'])
        p10b_list = p10b['Saham'].tolist()# list ticker saham
        ## list tadi(p10b_list) jadikan pdseries, lalu dihitung berapa banyak yang sama (disini dilakukan voting)
        vote_10b = pd.Series(p10b_list).value_counts()# contoh: UNVR    3 (key : isinya). value_counts() untuk menghitung elemen yang sama
        ## pdSeries tadi(vote_10b) jadikan dataframe. ini untuk menyaring saham
        df_hitung = pd.DataFrame(vote_10b)# pdSeries tadi(vote_10b) jadikan dataframe.bentuknya contoh: ICBP	2 (ini indexnya kolom saham.)
        df_hitung.reset_index(inplace=True)#mereset index, sekaligus menambahkan kolom index. karnakan tadi tidak ada index nomer. maka: 1	ICBP	2
        df_hitung = df_hitung.rename(columns={"index": "Saham", 0: "voting"})# mengganti nama kolom
        df_hitung = df_hitung.loc[df_hitung["voting"]>=2]# disini kita hanya mengambil saham yang memiliki jumlah votenya minimal 2
        ## menyiapkan dataframe untuk hasil akhir
        df_peringkat_10besar = pd.DataFrame(columns=['Saham','voting','rata-rata nilai persentase(%)'])
        ## for loop untuk mengisi dataframe df_peringkat_10besar
        for i in range(len(df_hitung)):
            juara_10b = vote_10b.keys()[i]# ambil key si"i" (key disini adalah ticker sahamnya)
            juara_10bv = vote_10b[i]# ambil isinya si"i" (isinya disini adalah berapa banyak yang ngevote)
            ## mengambil 'rata-rata nilai persentase(%)' sisaham juara_10b di semua baris yang ada didataframe p10b lalu merata rata kannya
            baris_10b=p10b[p10b.isin([juara_10b]).any(axis=1)]# mendapatkan semua bari yang memiliki saham si juara_10b. ini berbentuk dataframe
            ratarata_ttljmlpsn = baris_10b['total jumlah persentase(%)'].mean() # rata rata total jumlah persentase saham si "i"
            ## memasukkan ke dalam dataframe df_peringkat_10besar
            df_peringkat_10besar = pd.concat([df_peringkat_10besar, pd.DataFrame.from_records([{
                        'Saham':juara_10b, 'voting':juara_10bv,'rata-rata nilai persentase(%)':ratarata_ttljmlpsn}])])
        ## merapihkan dataframe
        df_peringkat_10besar.sort_values(by=['voting','rata-rata nilai persentase(%)'],ascending=False,inplace=True)
        df_peringkat_10besar.reset_index(inplace=True, drop=True)
        return df_peringkat_10besar
    except:
        print('!!! ---> Diperingkat 10 besar tidak ada yang sama')
        df_peringkat_10besar = pd.DataFrame({'Saham':0,'voting':0,'rata-rata nilai persentase(%)':0})
        return df_peringkat_10besar