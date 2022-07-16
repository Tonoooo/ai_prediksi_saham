# perbedaan dengan file pake_kk.py adalah ini tidak ada print('kelas .. selesai')

# semua fungsi ini akan mereturn dataframe hasil prediksi saham saham yang akan
#akan naik memurut prediksi setiap kelasnya

import pandas as pd
from fungsi import datanya, persen
from keras.models import load_model # untuk menggunakan model
from datetime import date
today = date.today() #metode untuk mendapatkan tanggal lokal saat ini.
tanggal = today.strftime("%Y%m%d")#metode strftime() untuk membuat string yang mewakili tanggal dalam format yang berbeda.


### ~~~~~ fungsi untuk menggunakan model kelas 1 
def pake_k1(list_ticker, h_predik,timestep=80):
    # buat dataframe(ini tempat untuk hasil prediksi para model)
    hasil_model = pd.DataFrame(columns=['Saham','Perubahan nilai','Keadaan','0/1','Perubahan(%)'])
    # for loop, satu model mewakili satu saham
    for tic in list_ticker:
        # mendapatkan data saham tersebut untuk input model memprediksi
        makanannya = pd.read_csv(f'data/psaham/{tic}.csv')
        # ambil modelnya sesuai saham tersebut
        model = load_model(f"kelas/kelas_1/model/{tic}_model.h5")
        # gunakan modelnya untuk memprediksi saham tersebut
        hasil_pred = datanya.predik_5h(makanannya, timestep, model, h_predik)
        # mendapatkan perubahan nilai (bisa plus(+naik), bisa min(-turun))
        kenaikan = hasil_pred[h_predik-1][0] - hasil_pred[0][0]#nilai output prediksi model terakhir DIKURANG nilai output prediksi model pertama
        # mendapatkan nilai persentase dan keadaan(naik(1)/turun(0))
        persentase, akan = persen.kenaikan_persen(hasil_pred[0][0], hasil_pred[h_predik-1][0])#nilai output prediksi model pertama DAN nilai output prediksi model terakhir
        # masukkan semua nilai-nilai itu ke dataframe tadi
        hasil_model = pd.concat([hasil_model, pd.DataFrame.from_records([{
            'Saham': tic, 'Perubahan nilai' : kenaikan, 'Keadaan': akan[1],
            '0/1':akan[0],'Perubahan(%)' : persentase}])])
    # mengurutkan sesuai kolom Perubahan(%), dari nilai terbesar ke terkecil
    hasil_model.sort_values(by='Perubahan(%)',ascending=False, inplace=True) 
    hasil_model.reset_index(inplace=True, drop=True) # mereset index
    # mengambil baris yang naik saja
    hasil_naik = hasil_model.loc[hasil_model['0/1'] == 1] #ambil baris yang naik saja
    hasil_naik.to_csv(f'kelas/kelas_1/hasil_kelas1/{tanggal}_naik.csv',index=False) # jadikan file csv lalu simpan
    # mengambil baris yang turun saja
    hasil_turun = hasil_model.loc[hasil_model['0/1'] == 0] #ambil baris yang turun saja
    hasil_turun.to_csv(f'kelas/kelas_1/hasil_kelas1/{tanggal}_turun.csv',index=False) # jadikan file csv lalu simpan
    # file csv full hasil model baik itu turun/naik
    hasil_model.to_csv(f'kelas/kelas_1/hasil_kelas1/{tanggal}_k1.csv',index=False)
    # mengembalikan hasil yang naik saja
    return hasil_naik

### ~~~~~ fungsi untuk menggunakan model kelas 2
def pake_k2(list_ticker, h_predik, timestep=80):
    hasil_model = pd.DataFrame(columns=['Saham','Perubahan nilai','Keadaan','0/1','Perubahan(%)'])
    for tic in list_ticker:
        makanannya = pd.read_csv(f'data/psaham/{tic}.csv')
        model = load_model(f"kelas/kelas_2/model/{tic}_model.h5")
        hasil_pred = datanya.predik_5h(makanannya, timestep, model, h_predik)
        kenaikan = hasil_pred[h_predik-1][0] - hasil_pred[0][0]
        persentase, akan = persen.kenaikan_persen(hasil_pred[0][0], hasil_pred[h_predik-1][0])
        hasil_model = pd.concat([hasil_model, pd.DataFrame.from_records([{
            'Saham': tic, 'Perubahan nilai' : kenaikan, 'Keadaan': akan[1],
            '0/1':akan[0],'Perubahan(%)' : persentase}])])
    # mengurutkan sesuai kolom Perubahan(%), dari nilai terbesar ke terkecil
    hasil_model.sort_values(by='Perubahan(%)',ascending=False, inplace=True) 
    hasil_model.reset_index(inplace=True, drop=True) # mereset index
    # mengambil baris yang naik saja
    hasil_naik = hasil_model.loc[hasil_model['0/1'] == 1]
    hasil_naik.to_csv(f'kelas/kelas_2/hasil_kelas2/{tanggal}_naik.csv',index=False)
    # mengambil baris yang turun saja
    hasil_turun = hasil_model.loc[hasil_model['0/1'] == 0]
    hasil_turun.to_csv(f'kelas/kelas_2/hasil_kelas2/{tanggal}_turun.csv',index=False)
    # file csv full hasil model baik itu turun/naik
    hasil_model.to_csv(f'kelas/kelas_2/hasil_kelas2/{tanggal}_k2.csv',index=False)
    # mengembalikan hasil yang naik saja
    return hasil_naik
    
### ~~~~~ fungsi untuk menggunakan model kelas 3
def pake_k3(list_ticker, h_predik, timestep=80):
    hasil_model = pd.DataFrame(columns=['Saham','Perubahan nilai','Keadaan','0/1','Perubahan(%)'])
    for tic in list_ticker:
        makanannya = pd.read_csv(f'data/psaham/{tic}.csv')
        model = load_model(f"kelas/kelas_3/model/{tic}_model.h5")
        hasil_pred = datanya.predik_5h(makanannya, timestep, model, h_predik)
        kenaikan = hasil_pred[h_predik-1][0] - hasil_pred[0][0]
        persentase, akan = persen.kenaikan_persen(hasil_pred[0][0], hasil_pred[h_predik-1][0])
        hasil_model = pd.concat([hasil_model, pd.DataFrame.from_records([{
            'Saham': tic, 'Perubahan nilai' : kenaikan, 'Keadaan': akan[1],
            '0/1':akan[0],'Perubahan(%)' : persentase}])])
    # mengurutkan sesuai kolom Perubahan(%), dari nilai terbesar ke terkecil
    hasil_model.sort_values(by='Perubahan(%)',ascending=False, inplace=True) 
    hasil_model.reset_index(inplace=True, drop=True) # mereset index
    # mengambil baris yang naik saja
    hasil_naik = hasil_model.loc[hasil_model['0/1'] == 1]
    hasil_naik.to_csv(f'kelas/kelas_3/hasil_kelas3/{tanggal}_naik.csv',index=False)
    # mengambil baris yang turun saja
    hasil_turun = hasil_model.loc[hasil_model['0/1'] == 0]
    hasil_turun.to_csv(f'kelas/kelas_3/hasil_kelas3/{tanggal}_turun.csv',index=False)
    # file csv full hasil model baik itu turun/naik
    hasil_model.to_csv(f'kelas/kelas_3/hasil_kelas3/{tanggal}_k3.csv',index=False)
    # mengembalikan hasil yang naik saja
    return hasil_naik

### ~~~~~ fungsi untuk menggunakan model kelas 4
def pake_k4(list_ticker, h_predik, timestep=20):
    hasil_model = pd.DataFrame(columns=['Saham','Perubahan nilai','Keadaan','0/1','Perubahan(%)'])
    for tic in list_ticker:
        makanannya = pd.read_csv(f'data/psaham/{tic}.csv')
        model = load_model(f"kelas/kelas_4/model/{tic}_model.h5")
        hasil_pred = datanya.predik5h_4(makanannya, timestep, model, h_predik)
        kenaikan = hasil_pred[h_predik-1][0] - hasil_pred[0][0]
        persentase, akan = persen.kenaikan_persen(hasil_pred[0][0], hasil_pred[h_predik-1][0])
        hasil_model = pd.concat([hasil_model, pd.DataFrame.from_records([{
            'Saham': tic, 'Perubahan nilai' : kenaikan, 'Keadaan': akan[1],
            '0/1':akan[0],'Perubahan(%)' : persentase}])])
    # mengurutkan sesuai kolom Perubahan(%), dari nilai terbesar ke terkecil
    hasil_model.sort_values(by='Perubahan(%)',ascending=False, inplace=True) 
    hasil_model.reset_index(inplace=True, drop=True) # mereset index
    # mengambil baris yang naik saja
    hasil_naik = hasil_model.loc[hasil_model['0/1'] == 1]
    hasil_naik.to_csv(f'kelas/kelas_4/hasil_kelas4/{tanggal}_naik.csv',index=False)
    # mengambil baris yang turun saja
    hasil_turun = hasil_model.loc[hasil_model['0/1'] == 0]
    hasil_turun.to_csv(f'kelas/kelas_4/hasil_kelas4/{tanggal}_turun.csv',index=False)
    # file csv full hasil model baik itu turun/naik
    hasil_model.to_csv(f'kelas/kelas_4/hasil_kelas4/{tanggal}_k4.csv',index=False)
    # mengembalikan hasil yang naik saja
    return hasil_naik

### ~~~~~ fungsi untuk menggunakan model kelas 5
def pake_k5(list_ticker, h_predik, timestep=60):
    hasil_model = pd.DataFrame(columns=['Saham','Perubahan nilai','Keadaan','0/1','Perubahan(%)'])
    for tic in list_ticker:
        makanannya = pd.read_csv(f'data/psaham/{tic}.csv')
        model = load_model(f"kelas/kelas_5/model/{tic}_model.h5")
        hasil_pred = datanya.predik_5h(makanannya, timestep, model, h_predik)
        kenaikan = hasil_pred[h_predik-1][0] - hasil_pred[0][0]
        persentase, akan = persen.kenaikan_persen(hasil_pred[0][0], hasil_pred[h_predik-1][0])
        hasil_model = pd.concat([hasil_model, pd.DataFrame.from_records([{
            'Saham': tic, 'Perubahan nilai' : kenaikan, 'Keadaan': akan[1],
            '0/1':akan[0],'Perubahan(%)' : persentase}])])
    # mengurutkan sesuai kolom Perubahan(%), dari nilai terbesar ke terkecil
    hasil_model.sort_values(by='Perubahan(%)',ascending=False, inplace=True) 
    hasil_model.reset_index(inplace=True, drop=True) # mereset index
    # mengambil baris yang naik saja
    hasil_naik = hasil_model.loc[hasil_model['0/1'] == 1]
    hasil_naik.to_csv(f'kelas/kelas_5/hasil_kelas5/{tanggal}_naik.csv',index=False)
    # mengambil baris yang turun saja
    hasil_turun = hasil_model.loc[hasil_model['0/1'] == 0]
    hasil_turun.to_csv(f'kelas/kelas_5/hasil_kelas5/{tanggal}_turun.csv',index=False)
    # file csv full hasil model baik itu turun/naik
    hasil_model.to_csv(f'kelas/kelas_5/hasil_kelas5/{tanggal}_k5.csv',index=False)
    # mengembalikan hasil yang naik saja
    return hasil_naik

### ~~~~~ fungsi untuk menggunakan model kelas 6
def pake_k6(list_ticker, h_predik, timestep=20):
    hasil_model = pd.DataFrame(columns=['Saham','Perubahan nilai','Keadaan','0/1','Perubahan(%)'])
    for tic in list_ticker:
        makanannya = pd.read_csv(f'data/psaham/{tic}.csv')
        model = load_model(f"kelas/kelas_6/model/{tic}_model.h5")
        hasil_pred = datanya.predik5h_4(makanannya, timestep, model, h_predik)
        kenaikan = hasil_pred[h_predik-1][0] - hasil_pred[0][0]
        persentase, akan = persen.kenaikan_persen(hasil_pred[0][0], hasil_pred[h_predik-1][0])
        hasil_model = pd.concat([hasil_model, pd.DataFrame.from_records([{
            'Saham': tic, 'Perubahan nilai' : kenaikan, 'Keadaan': akan[1],
            '0/1':akan[0],'Perubahan(%)' : persentase}])])
    # mengurutkan sesuai kolom Perubahan(%), dari nilai terbesar ke terkecil
    hasil_model.sort_values(by='Perubahan(%)',ascending=False, inplace=True) 
    hasil_model.reset_index(inplace=True, drop=True) # mereset index
    # mengambil baris yang naik saja
    hasil_naik = hasil_model.loc[hasil_model['0/1'] == 1]
    hasil_naik.to_csv(f'kelas/kelas_6/hasil_kelas6/{tanggal}_naik.csv',index=False)
    # mengambil baris yang turun saja
    hasil_turun = hasil_model.loc[hasil_model['0/1'] == 0]
    hasil_turun.to_csv(f'kelas/kelas_6/hasil_kelas6/{tanggal}_turun.csv',index=False)
    # file csv full hasil model baik itu turun/naik
    hasil_model.to_csv(f'kelas/kelas_6/hasil_kelas6/{tanggal}_k6.csv',index=False)
    # mengembalikan hasil yang naik saja
    return hasil_naik

### ~~~~~ fungsi untuk menggunakan model kelas 7
def pake_k7(list_ticker, h_predik, timestep=80):
    hasil_model = pd.DataFrame(columns=['Saham','Perubahan nilai','Keadaan','0/1','Perubahan(%)'])
    for tic in list_ticker:
        makanannya = pd.read_csv(f'data/psaham/{tic}.csv')
        model = load_model(f"kelas/kelas_7/model/{tic}_model.h5")
        hasil_pred = datanya.predik_5h(makanannya, timestep, model, h_predik)
        kenaikan = hasil_pred[h_predik-1][0] - hasil_pred[0][0]
        persentase, akan = persen.kenaikan_persen(hasil_pred[0][0], hasil_pred[h_predik-1][0])
        hasil_model = pd.concat([hasil_model, pd.DataFrame.from_records([{
            'Saham': tic, 'Perubahan nilai' : kenaikan, 'Keadaan': akan[1],
            '0/1':akan[0],'Perubahan(%)' : persentase}])])
    # mengurutkan sesuai kolom Perubahan(%), dari nilai terbesar ke terkecil
    hasil_model.sort_values(by='Perubahan(%)',ascending=False, inplace=True) 
    hasil_model.reset_index(inplace=True, drop=True) # mereset index
    # mengambil baris yang naik saja
    hasil_naik = hasil_model.loc[hasil_model['0/1'] == 1]
    hasil_naik.to_csv(f'kelas/kelas_7/hasil_kelas7/{tanggal}_naik.csv',index=False)
    # mengambil baris yang turun saja
    hasil_turun = hasil_model.loc[hasil_model['0/1'] == 0]
    hasil_turun.to_csv(f'kelas/kelas_7/hasil_kelas7/{tanggal}_turun.csv',index=False)
    # file csv full hasil model baik itu turun/naik
    hasil_model.to_csv(f'kelas/kelas_7/hasil_kelas7/{tanggal}_k7.csv',index=False)
    # mengembalikan hasil yang naik saja
    return hasil_naik

### ~~~~~ fungsi untuk menggunakan model kelas 8
def pake_k8(list_ticker, h_predik, timestep=50):
    hasil_model = pd.DataFrame(columns=['Saham','Perubahan nilai','Keadaan','0/1','Perubahan(%)'])
    for tic in list_ticker:
        makanannya = pd.read_csv(f'data/psaham/{tic}.csv')
        model = load_model(f"kelas/kelas_8/model/{tic}_model.h5")
        hasil_pred = datanya.predik_5h(makanannya, timestep, model, h_predik)
        kenaikan = hasil_pred[h_predik-1][0] - hasil_pred[0][0]
        persentase, akan = persen.kenaikan_persen(hasil_pred[0][0], hasil_pred[h_predik-1][0])
        hasil_model = pd.concat([hasil_model, pd.DataFrame.from_records([{
            'Saham': tic, 'Perubahan nilai' : kenaikan, 'Keadaan': akan[1],
            '0/1':akan[0],'Perubahan(%)' : persentase}])])
    # mengurutkan sesuai kolom Perubahan(%), dari nilai terbesar ke terkecil
    hasil_model.sort_values(by='Perubahan(%)',ascending=False, inplace=True) 
    hasil_model.reset_index(inplace=True, drop=True) # mereset index
    # mengambil baris yang naik saja
    hasil_naik = hasil_model.loc[hasil_model['0/1'] == 1]
    hasil_naik.to_csv(f'kelas/kelas_8/hasil_kelas8/{tanggal}_naik.csv',index=False)
    # mengambil baris yang turun saja
    hasil_turun = hasil_model.loc[hasil_model['0/1'] == 0]
    hasil_turun.to_csv(f'kelas/kelas_8/hasil_kelas8/{tanggal}_turun_.csv',index=False)
    # file csv full hasil model baik itu turun/naik
    hasil_model.to_csv(f'kelas/kelas_8/hasil_kelas8/{tanggal}_k8.csv',index=False)
    # mengembalikan hasil yang naik saja
    return hasil_naik

### ~~~~~ fungsi untuk menggunakan model kelas 9
def pake_k9(list_ticker, h_predik, timestep=60):
    hasil_model = pd.DataFrame(columns=['Saham','Perubahan nilai','Keadaan','0/1','Perubahan(%)'])
    for tic in list_ticker:
        makanannya = pd.read_csv(f'data/psaham/{tic}.csv')
        model = load_model(f"kelas/kelas_9/model/{tic}_model.h5")
        hasil_pred = datanya.predik_5h(makanannya, timestep, model, h_predik)
        kenaikan = hasil_pred[h_predik-1][0] - hasil_pred[0][0]
        persentase, akan = persen.kenaikan_persen(hasil_pred[0][0], hasil_pred[h_predik-1][0])
        hasil_model = pd.concat([hasil_model, pd.DataFrame.from_records([{
            'Saham': tic, 'Perubahan nilai' : kenaikan, 'Keadaan': akan[1],
            '0/1':akan[0],'Perubahan(%)' : persentase}])])
    # mengurutkan sesuai kolom Perubahan(%), dari nilai terbesar ke terkecil
    hasil_model.sort_values(by='Perubahan(%)',ascending=False, inplace=True) 
    hasil_model.reset_index(inplace=True, drop=True) # mereset index
    # mengambil baris yang naik saja
    hasil_naik = hasil_model.loc[hasil_model['0/1'] == 1]
    hasil_naik.to_csv(f'kelas/kelas_9/hasil_kelas9/{tanggal}_naik.csv',index=False)
    # mengambil baris yang turun saja
    hasil_turun = hasil_model.loc[hasil_model['0/1'] == 0]
    hasil_turun.to_csv(f'kelas/kelas_9/hasil_kelas9/{tanggal}_turun_.csv',index=False)
    # file csv full hasil model baik itu turun/naik
    hasil_model.to_csv(f'kelas/kelas_9/hasil_kelas9/{tanggal}_k9.csv',index=False)
    # mengembalikan hasil yang naik saja
    return hasil_naik

### ~~~~~ fungsi untuk menggunakan model kelas 10
def pake_k10(list_ticker, h_predik, timestep=50):
    hasil_model = pd.DataFrame(columns=['Saham','Perubahan nilai','Keadaan','0/1','Perubahan(%)'])
    for tic in list_ticker:
        makanannya = pd.read_csv(f'data/psaham/{tic}.csv')
        model = load_model(f"kelas/kelas_10/model/{tic}_model.h5")
        hasil_pred = datanya.predik_5h(makanannya, timestep, model, h_predik)
        kenaikan = hasil_pred[h_predik-1][0] - hasil_pred[0][0]
        persentase, akan = persen.kenaikan_persen(hasil_pred[0][0], hasil_pred[h_predik-1][0])
        hasil_model = pd.concat([hasil_model, pd.DataFrame.from_records([{
            'Saham': tic, 'Perubahan nilai' : kenaikan, 'Keadaan': akan[1],
            '0/1':akan[0],'Perubahan(%)' : persentase}])])
    # mengurutkan sesuai kolom Perubahan(%), dari nilai terbesar ke terkecil
    hasil_model.sort_values(by='Perubahan(%)',ascending=False, inplace=True) 
    hasil_model.reset_index(inplace=True, drop=True) # mereset index
    # mengambil baris yang naik saja
    hasil_naik = hasil_model.loc[hasil_model['0/1'] == 1]
    hasil_naik.to_csv(f'kelas/kelas_10/hasil_kelas10/{tanggal}_naik.csv',index=False)
    # mengambil baris yang turun saja
    hasil_turun = hasil_model.loc[hasil_model['0/1'] == 0]
    hasil_turun.to_csv(f'kelas/kelas_10/hasil_kelas10/{tanggal}_turun_.csv',index=False)
    # file csv full hasil model baik itu turun/naik
    hasil_model.to_csv(f'kelas/kelas_10/hasil_kelas10/{tanggal}_k10.csv',index=False)
    # mengembalikan hasil yang naik saja
    return hasil_naik

### ~~~~~ fungsi untuk menggunakan model kelas 11
def pake_k11(list_ticker, h_predik, timestep=60):
    hasil_model = pd.DataFrame(columns=['Saham','Perubahan nilai','Keadaan','0/1','Perubahan(%)'])
    for tic in list_ticker:
        makanannya = pd.read_csv(f'data/psaham/{tic}.csv')
        model = load_model(f"kelas/kelas_11/model/{tic}_model.h5")
        hasil_pred = datanya.predik_5h(makanannya, timestep, model, h_predik)
        kenaikan = hasil_pred[h_predik-1][0] - hasil_pred[0][0]
        persentase, akan = persen.kenaikan_persen(hasil_pred[0][0], hasil_pred[h_predik-1][0])
        hasil_model = pd.concat([hasil_model, pd.DataFrame.from_records([{
            'Saham': tic, 'Perubahan nilai' : kenaikan, 'Keadaan': akan[1],
            '0/1':akan[0],'Perubahan(%)' : persentase}])])
    # mengurutkan sesuai kolom Perubahan(%), dari nilai terbesar ke terkecil
    hasil_model.sort_values(by='Perubahan(%)',ascending=False, inplace=True) 
    hasil_model.reset_index(inplace=True, drop=True) # mereset index
    # mengambil baris yang naik saja
    hasil_naik = hasil_model.loc[hasil_model['0/1'] == 1]
    hasil_naik.to_csv(f'kelas/kelas_11/hasil_kelas11/{tanggal}_naik.csv',index=False)
    # mengambil baris yang turun saja
    hasil_turun = hasil_model.loc[hasil_model['0/1'] == 0]
    hasil_turun.to_csv(f'kelas/kelas_11/hasil_kelas11/{tanggal}_turun_.csv',index=False)
    # file csv full hasil model baik itu turun/naik
    hasil_model.to_csv(f'kelas/kelas_11/hasil_kelas11/{tanggal}_k11.csv',index=False)
    # mengembalikan hasil yang naik saja
    return hasil_naik

### ~~~~~ fungsi untuk menggunakan model kelas 12
def pake_k12(list_ticker, h_predik, timestep=60):
    hasil_model = pd.DataFrame(columns=['Saham','Perubahan nilai','Keadaan','0/1','Perubahan(%)'])
    for tic in list_ticker:
        makanannya = pd.read_csv(f'data/psaham/{tic}.csv')
        model = load_model(f"kelas/kelas_12/model/{tic}_model.h5")
        hasil_pred = datanya.predik_5h(makanannya, timestep, model, h_predik)
        kenaikan = hasil_pred[h_predik-1][0] - hasil_pred[0][0]
        persentase, akan = persen.kenaikan_persen(hasil_pred[0][0], hasil_pred[h_predik-1][0])
        hasil_model = pd.concat([hasil_model, pd.DataFrame.from_records([{
            'Saham': tic, 'Perubahan nilai' : kenaikan, 'Keadaan': akan[1],
            '0/1':akan[0],'Perubahan(%)' : persentase}])])
    # mengurutkan sesuai kolom Perubahan(%), dari nilai terbesar ke terkecil
    hasil_model.sort_values(by='Perubahan(%)',ascending=False, inplace=True) 
    hasil_model.reset_index(inplace=True, drop=True) # mereset index
    # mengambil baris yang naik saja
    hasil_naik = hasil_model.loc[hasil_model['0/1'] == 1]
    hasil_naik.to_csv(f'kelas/kelas_12/hasil_kelas12/{tanggal}_naik.csv',index=False)
    # mengambil baris yang turun saja
    hasil_turun = hasil_model.loc[hasil_model['0/1'] == 0]
    hasil_turun.to_csv(f'kelas/kelas_12/hasil_kelas12/{tanggal}_turun_.csv',index=False)
    # file csv full hasil model baik itu turun/naik
    hasil_model.to_csv(f'kelas/kelas_12/hasil_kelas12/{tanggal}_k12.csv',index=False)
    # mengembalikan hasil yang naik saja
    return hasil_naik

### ~~~~~ fungsi untuk menggunakan model kelas 13
def pake_k13(list_ticker, h_predik, timestep=180):
    hasil_model = pd.DataFrame(columns=['Saham','Perubahan nilai','Keadaan','0/1','Perubahan(%)'])
    for tic in list_ticker:
        makanannya = pd.read_csv(f'data/psaham/{tic}.csv')
        model = load_model(f"kelas/kelas_13/model/{tic}_model.h5")
        hasil_pred = datanya.predik_5h(makanannya, timestep, model, h_predik)
        kenaikan = hasil_pred[h_predik-1][0] - hasil_pred[0][0]
        persentase, akan = persen.kenaikan_persen(hasil_pred[0][0], hasil_pred[h_predik-1][0])
        hasil_model = pd.concat([hasil_model, pd.DataFrame.from_records([{
            'Saham': tic, 'Perubahan nilai' : kenaikan, 'Keadaan': akan[1],
            '0/1':akan[0],'Perubahan(%)' : persentase}])])
    # mengurutkan sesuai kolom Perubahan(%), dari nilai terbesar ke terkecil
    hasil_model.sort_values(by='Perubahan(%)',ascending=False, inplace=True) 
    hasil_model.reset_index(inplace=True, drop=True) # mereset index
    # mengambil baris yang naik saja
    hasil_naik = hasil_model.loc[hasil_model['0/1'] == 1]
    hasil_naik.to_csv(f'kelas/kelas_13/hasil_kelas13/{tanggal}_naik.csv',index=False)
    # mengambil baris yang turun saja
    hasil_turun = hasil_model.loc[hasil_model['0/1'] == 0]
    hasil_turun.to_csv(f'kelas/kelas_13/hasil_kelas13/{tanggal}_turun_.csv',index=False)
    # file csv full hasil model baik itu turun/naik
    hasil_model.to_csv(f'kelas/kelas_13/hasil_kelas13/{tanggal}_k13.csv',index=False)
    # mengembalikan hasil yang naik saja
    return hasil_naik

### ~~~~~ fungsi untuk menggunakan model kelas 14
def pake_k14(list_ticker, h_predik, timestep=100):
    hasil_model = pd.DataFrame(columns=['Saham','Perubahan nilai','Keadaan','0/1','Perubahan(%)'])
    for tic in list_ticker:
        makanannya = pd.read_csv(f'data/psaham/{tic}.csv')
        model = load_model(f"kelas/kelas_14/model/{tic}_model.h5")
        hasil_pred = datanya.predik_5h(makanannya, timestep, model, h_predik)
        kenaikan = hasil_pred[h_predik-1][0] - hasil_pred[0][0]
        persentase, akan = persen.kenaikan_persen(hasil_pred[0][0], hasil_pred[h_predik-1][0])
        hasil_model = pd.concat([hasil_model, pd.DataFrame.from_records([{
            'Saham': tic, 'Perubahan nilai' : kenaikan, 'Keadaan': akan[1],
            '0/1':akan[0],'Perubahan(%)' : persentase}])])
    # mengurutkan sesuai kolom Perubahan(%), dari nilai terbesar ke terkecil
    hasil_model.sort_values(by='Perubahan(%)',ascending=False, inplace=True) 
    hasil_model.reset_index(inplace=True, drop=True) # mereset index
    # mengambil baris yang naik saja
    hasil_naik = hasil_model.loc[hasil_model['0/1'] == 1]
    hasil_naik.to_csv(f'kelas/kelas_14/hasil_kelas14/{tanggal}_naik.csv',index=False)
    # mengambil baris yang turun saja
    hasil_turun = hasil_model.loc[hasil_model['0/1'] == 0]
    hasil_turun.to_csv(f'kelas/kelas_14/hasil_kelas14/{tanggal}_turun_.csv',index=False)
    # file csv full hasil model baik itu turun/naik
    hasil_model.to_csv(f'kelas/kelas_14/hasil_kelas14/{tanggal}_k14.csv',index=False)
    # mengembalikan hasil yang naik saja
    return hasil_naik

### ~~~~~ fungsi untuk menggunakan model kelas 15
def pake_k15(list_ticker, h_predik, timestep=80):
    hasil_model = pd.DataFrame(columns=['Saham','Perubahan nilai','Keadaan','0/1','Perubahan(%)'])
    for tic in list_ticker:
        makanannya = pd.read_csv(f'data/psaham/{tic}.csv')
        model = load_model(f"kelas/kelas_15/model/{tic}_model.h5")
        hasil_pred = datanya.predik_5h(makanannya, timestep, model, h_predik)
        kenaikan = hasil_pred[h_predik-1][0] - hasil_pred[0][0]
        persentase, akan = persen.kenaikan_persen(hasil_pred[0][0], hasil_pred[h_predik-1][0])
        hasil_model = pd.concat([hasil_model, pd.DataFrame.from_records([{
            'Saham': tic, 'Perubahan nilai' : kenaikan, 'Keadaan': akan[1],
            '0/1':akan[0],'Perubahan(%)' : persentase}])])
    # mengurutkan sesuai kolom Perubahan(%), dari nilai terbesar ke terkecil
    hasil_model.sort_values(by='Perubahan(%)',ascending=False, inplace=True) 
    hasil_model.reset_index(inplace=True, drop=True) # mereset index
    # mengambil baris yang naik saja
    hasil_naik = hasil_model.loc[hasil_model['0/1'] == 1]
    hasil_naik.to_csv(f'kelas/kelas_15/hasil_kelas15/{tanggal}_naik.csv',index=False)
    # mengambil baris yang turun saja
    hasil_turun = hasil_model.loc[hasil_model['0/1'] == 0]
    hasil_turun.to_csv(f'kelas/kelas_15/hasil_kelas15/{tanggal}_turun_.csv',index=False)
    # file csv full hasil model baik itu turun/naik
    hasil_model.to_csv(f'kelas/kelas_15/hasil_kelas15/{tanggal}_k15.csv',index=False)
    # mengembalikan hasil yang naik saja
    return hasil_naik

### ~~~~~ fungsi untuk menggunakan model kelas 16
def pake_k16(list_ticker, h_predik, timestep=80):
    hasil_model = pd.DataFrame(columns=['Saham','Perubahan nilai','Keadaan','0/1','Perubahan(%)'])
    for tic in list_ticker:
        makanannya = pd.read_csv(f'data/psaham/{tic}.csv')
        model = load_model(f"kelas/kelas_16/model/{tic}_model.h5")
        hasil_pred = datanya.predik_5h(makanannya, timestep, model, h_predik)
        kenaikan = hasil_pred[h_predik-1][0] - hasil_pred[0][0]
        persentase, akan = persen.kenaikan_persen(hasil_pred[0][0], hasil_pred[h_predik-1][0])
        hasil_model = pd.concat([hasil_model, pd.DataFrame.from_records([{
            'Saham': tic, 'Perubahan nilai' : kenaikan, 'Keadaan': akan[1],
            '0/1':akan[0],'Perubahan(%)' : persentase}])])
    # mengurutkan sesuai kolom Perubahan(%), dari nilai terbesar ke terkecil
    hasil_model.sort_values(by='Perubahan(%)',ascending=False, inplace=True) 
    hasil_model.reset_index(inplace=True, drop=True) # mereset index
    # mengambil baris yang naik saja
    hasil_naik = hasil_model.loc[hasil_model['0/1'] == 1]
    hasil_naik.to_csv(f'kelas/kelas_16/hasil_kelas16/{tanggal}_naik.csv',index=False)
    # mengambil baris yang turun saja
    hasil_turun = hasil_model.loc[hasil_model['0/1'] == 0]
    hasil_turun.to_csv(f'kelas/kelas_16/hasil_kelas16/{tanggal}_turun_.csv',index=False)
    # file csv full hasil model baik itu turun/naik
    hasil_model.to_csv(f'kelas/kelas_16/hasil_kelas16/{tanggal}_k16.csv',index=False)
    # mengembalikan hasil yang naik saja
    return hasil_naik

### ~~~~~ fungsi untuk menggunakan model kelas 17
def pake_k17(list_ticker, h_predik, timestep=60):
    hasil_model = pd.DataFrame(columns=['Saham','Perubahan nilai','Keadaan','0/1','Perubahan(%)'])
    for tic in list_ticker:
        makanannya = pd.read_csv(f'data/psaham/{tic}.csv')
        model = load_model(f"kelas/kelas_17/model/{tic}_model.h5")
        hasil_pred = datanya.predik_5h(makanannya, timestep, model, h_predik)
        kenaikan = hasil_pred[h_predik-1][0] - hasil_pred[0][0]
        persentase, akan = persen.kenaikan_persen(hasil_pred[0][0], hasil_pred[h_predik-1][0])
        hasil_model = pd.concat([hasil_model, pd.DataFrame.from_records([{
            'Saham': tic, 'Perubahan nilai' : kenaikan, 'Keadaan': akan[1],
            '0/1':akan[0],'Perubahan(%)' : persentase}])])
    # mengurutkan sesuai kolom Perubahan(%), dari nilai terbesar ke terkecil
    hasil_model.sort_values(by='Perubahan(%)',ascending=False, inplace=True) 
    hasil_model.reset_index(inplace=True, drop=True) # mereset index
    # mengambil baris yang naik saja
    hasil_naik = hasil_model.loc[hasil_model['0/1'] == 1]
    hasil_naik.to_csv(f'kelas/kelas_17/hasil_kelas17/{tanggal}_naik.csv',index=False)
    # mengambil baris yang turun saja
    hasil_turun = hasil_model.loc[hasil_model['0/1'] == 0]
    hasil_turun.to_csv(f'kelas/kelas_17/hasil_kelas17/{tanggal}_turun_.csv',index=False)
    # file csv full hasil model baik itu turun/naik
    hasil_model.to_csv(f'kelas/kelas_17/hasil_kelas17/{tanggal}_k17.csv',index=False)
    # mengembalikan hasil yang naik saja
    return hasil_naik

### ~~~~~ fungsi untuk menggunakan model kelas 18
def pake_k18(list_ticker, h_predik, timestep=80):
    hasil_model = pd.DataFrame(columns=['Saham','Perubahan nilai','Keadaan','0/1','Perubahan(%)'])
    for tic in list_ticker:
        makanannya = pd.read_csv(f'data/psaham/{tic}.csv')
        model = load_model(f"kelas/kelas_18/model/{tic}_model.h5")
        hasil_pred = datanya.predik_5h(makanannya, timestep, model, h_predik)
        kenaikan = hasil_pred[h_predik-1][0] - hasil_pred[0][0]
        persentase, akan = persen.kenaikan_persen(hasil_pred[0][0], hasil_pred[h_predik-1][0])
        hasil_model = pd.concat([hasil_model, pd.DataFrame.from_records([{
            'Saham': tic, 'Perubahan nilai' : kenaikan, 'Keadaan': akan[1],
            '0/1':akan[0],'Perubahan(%)' : persentase}])])
    # mengurutkan sesuai kolom Perubahan(%), dari nilai terbesar ke terkecil
    hasil_model.sort_values(by='Perubahan(%)',ascending=False, inplace=True) 
    hasil_model.reset_index(inplace=True, drop=True) # mereset index
    # mengambil baris yang naik saja
    hasil_naik = hasil_model.loc[hasil_model['0/1'] == 1]
    hasil_naik.to_csv(f'kelas/kelas_18/hasil_kelas18/{tanggal}_naik.csv',index=False)
    # mengambil baris yang turun saja
    hasil_turun = hasil_model.loc[hasil_model['0/1'] == 0]
    hasil_turun.to_csv(f'kelas/kelas_18/hasil_kelas18/{tanggal}_turun_.csv',index=False)
    # file csv full hasil model baik itu turun/naik
    hasil_model.to_csv(f'kelas/kelas_18/hasil_kelas18/{tanggal}_k18.csv',index=False)
    # mengembalikan hasil yang naik saja
    return hasil_naik

### ~~~~~ fungsi untuk menggunakan model kelas 19
def pake_k19(list_ticker, h_predik, timestep=80):
    hasil_model = pd.DataFrame(columns=['Saham','Perubahan nilai','Keadaan','0/1','Perubahan(%)'])
    for tic in list_ticker:
        makanannya = pd.read_csv(f'data/psaham/{tic}.csv')
        model = load_model(f"kelas/kelas_19/model/{tic}_model.h5")
        hasil_pred = datanya.predik_5h(makanannya, timestep, model, h_predik)
        kenaikan = hasil_pred[h_predik-1][0] - hasil_pred[0][0]
        persentase, akan = persen.kenaikan_persen(hasil_pred[0][0], hasil_pred[h_predik-1][0])
        hasil_model = pd.concat([hasil_model, pd.DataFrame.from_records([{
            'Saham': tic, 'Perubahan nilai' : kenaikan, 'Keadaan': akan[1],
            '0/1':akan[0],'Perubahan(%)' : persentase}])])
    # mengurutkan sesuai kolom Perubahan(%), dari nilai terbesar ke terkecil
    hasil_model.sort_values(by='Perubahan(%)',ascending=False, inplace=True) 
    hasil_model.reset_index(inplace=True, drop=True) # mereset index
    # mengambil baris yang naik saja
    hasil_naik = hasil_model.loc[hasil_model['0/1'] == 1]
    hasil_naik.to_csv(f'kelas/kelas_19/hasil_kelas19/{tanggal}_naik.csv',index=False)
    # mengambil baris yang turun saja
    hasil_turun = hasil_model.loc[hasil_model['0/1'] == 0]
    hasil_turun.to_csv(f'kelas/kelas_19/hasil_kelas19/{tanggal}_turun_.csv',index=False)
    # file csv full hasil model baik itu turun/naik
    hasil_model.to_csv(f'kelas/kelas_19/hasil_kelas19/{tanggal}_k19.csv',index=False)
    # mengembalikan hasil yang naik saja
    return hasil_naik

### ~~~~~ fungsi untuk menggunakan model kelas 20
def pake_k20(list_ticker, h_predik, timestep=80):
    hasil_model = pd.DataFrame(columns=['Saham','Perubahan nilai','Keadaan','0/1','Perubahan(%)'])
    for tic in list_ticker:
        makanannya = pd.read_csv(f'data/psaham/{tic}.csv')
        model = load_model(f"kelas/kelas_20/model/{tic}_model.h5")
        hasil_pred = datanya.predik_5h(makanannya, timestep, model, h_predik)
        kenaikan = hasil_pred[h_predik-1][0] - hasil_pred[0][0]
        persentase, akan = persen.kenaikan_persen(hasil_pred[0][0], hasil_pred[h_predik-1][0])
        hasil_model = pd.concat([hasil_model, pd.DataFrame.from_records([{
            'Saham': tic, 'Perubahan nilai' : kenaikan, 'Keadaan': akan[1],
            '0/1':akan[0],'Perubahan(%)' : persentase}])])
    # mengurutkan sesuai kolom Perubahan(%), dari nilai terbesar ke terkecil
    hasil_model.sort_values(by='Perubahan(%)',ascending=False, inplace=True) 
    hasil_model.reset_index(inplace=True, drop=True) # mereset index
    # mengambil baris yang naik saja
    hasil_naik = hasil_model.loc[hasil_model['0/1'] == 1]
    hasil_naik.to_csv(f'kelas/kelas_20/hasil_kelas20/{tanggal}_naik.csv',index=False)
    # mengambil baris yang turun saja
    hasil_turun = hasil_model.loc[hasil_model['0/1'] == 0]
    hasil_turun.to_csv(f'kelas/kelas_20/hasil_kelas20/{tanggal}_turun_.csv',index=False)
    # file csv full hasil model baik itu turun/naik
    hasil_model.to_csv(f'kelas/kelas_20/hasil_kelas20/{tanggal}_k20.csv',index=False)
    # mengembalikan hasil yang naik saja
    return hasil_naik

### ~~~~~ fungsi untuk menggunakan model kelas 21
def pake_k21(list_ticker, h_predik, timestep=80):
    hasil_model = pd.DataFrame(columns=['Saham','Perubahan nilai','Keadaan','0/1','Perubahan(%)'])
    for tic in list_ticker:
        makanannya = pd.read_csv(f'data/psaham/{tic}.csv')
        model = load_model(f"kelas/kelas_21/model/{tic}_model.h5")
        hasil_pred = datanya.predik_5h(makanannya, timestep, model, h_predik)
        kenaikan = hasil_pred[h_predik-1][0] - hasil_pred[0][0]
        persentase, akan = persen.kenaikan_persen(hasil_pred[0][0], hasil_pred[h_predik-1][0])
        hasil_model = pd.concat([hasil_model, pd.DataFrame.from_records([{
            'Saham': tic, 'Perubahan nilai' : kenaikan, 'Keadaan': akan[1],
            '0/1':akan[0],'Perubahan(%)' : persentase}])])
    # mengurutkan sesuai kolom Perubahan(%), dari nilai terbesar ke terkecil
    hasil_model.sort_values(by='Perubahan(%)',ascending=False, inplace=True) 
    hasil_model.reset_index(inplace=True, drop=True) # mereset index
    # mengambil baris yang naik saja
    hasil_naik = hasil_model.loc[hasil_model['0/1'] == 1]
    hasil_naik.to_csv(f'kelas/kelas_21/hasil_kelas21/{tanggal}_naik.csv',index=False)
    # mengambil baris yang turun saja
    hasil_turun = hasil_model.loc[hasil_model['0/1'] == 0]
    hasil_turun.to_csv(f'kelas/kelas_21/hasil_kelas21/{tanggal}_turun_.csv',index=False)
    # file csv full hasil model baik itu turun/naik
    hasil_model.to_csv(f'kelas/kelas_21/hasil_kelas21/{tanggal}_k21.csv',index=False)
    # mengembalikan hasil yang naik saja
    return hasil_naik