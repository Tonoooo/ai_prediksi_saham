##              FUNGSI untuk persen

## fungsi menghitung persentase keakuratan prediksi
def akurat_persen(prediksi, asli):
    ## menghitung persentase keakuratan prediksi
    if prediksi > asli:
        cek = float((asli/prediksi)*100)
        print('keakuratan prediksinya sebesar = ',cek,'%')
    else:
        cek = float((prediksi/asli)*100)
        print('keakuratan prediksinya sebesar = ',cek,'%')

## fungsi untuk menghitung kenaikan harga
def kenaikan_persen(nilai_awal, nilai_terakhir):
    persen = float(((nilai_terakhir-nilai_awal)/nilai_awal)*100)
    if persen >= 0:
        akan = [1,'Naik']
    elif persen <= 0:
        akan = [0,'Turun']
    return persen, akan