## ini dipakai di jii70 dan ticker_issi hasilnya ticker_jii70
# jadi ticker ticker di jii70 dan ticker_issi(ticker yicker yang sudah disaring
# sebelumnya) nanti jika ada yang sama ticker diambil satu dari setiap ticker yang sama

######## FUNGSI UNTUK MENDAPATKAN SATU DARI SETIAP DUPLIKAT YANG ADA DI DUA LIST
# 2 parameter : file ticker txt, file ticker txt
def ticker_sama(file_ticker1_txt, file_ticker2_txt):
    ## file txt pertama jadikan list
    file_full_ticker_txt = file_ticker1_txt
    with open(file_full_ticker_txt) as file:
        full_ticker = file.readlines()
        list_full_ticker = [line.rstrip() for line in full_ticker]
    ## file txt kedua jadikan list
    file_sub_ticker_txt = file_ticker2_txt
    with open(file_sub_ticker_txt) as file:
        sub_ticker = file.readlines()
        list_sub_ticker = [line.rstrip() for line in sub_ticker]
    ## jika ada dua/lebih yang sama, hanya mendapatkan satu dari setiap duplikat 
    hasil = sorted(list(set(list_full_ticker).intersection(list_sub_ticker)))
    return hasil