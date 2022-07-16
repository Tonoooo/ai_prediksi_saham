import smtplib # smtp adalah protokol yang akan kita gunakan untuk mengirim email
from email.mime.text import MIMEText # untuk text biasa
from email.mime.multipart import MIMEMultipart
from datetime import date
today = date.today() #metode untuk mendapatkan tanggal lokal saat ini.
hari_ini = today.strftime("%Y%m%d")# mengambil tanggal hari ini. (untuk penutup)

# ~~~~~~~~ fungsi untuk mengirim email hasil akhir
     
def kirim_email(login_email,login_pass_txt,email_pengirim,list_email_penerima,
                df_pembelian,df_penjualan,df_voting1,df_voting2,h_predik,tgl_akhir_data):
    ## membaca password
    with open(login_pass_txt) as f:
        password = f.read()
    server = 'smtp.gmail.com:587' # defisinikan server: 'server:port'
    
    # jika dataframe kosong/tidak ada saham yang direkomendasikan oleh program
    if len(df_voting1) == 0:
        ## isi pesan
        # disini kita menggunakan html dan untuk dataframenya jadikan html
        html = f"""
        <html>
        <head>Assalamu'alaikum WR WB.</head>
        <body>
        <p>Tanggal akhir input datanya adalah {tgl_akhir_data}.</p>
        <br>
        <p><h2>JANGAN BELI SAHAM APAPUN</h2></p>
        <br>
        <p><h3>-> Tabel pembelian dan penjualan saham:</h3></p>
        <br>
        <p><h2>Tabel pembelian saham 2 besar:</h2></p>
        {df_pembelian.to_html()}
        <br>
        <p><h2>Tabel Penjualan saham 2 besar:</h2></p>
        {df_penjualan.to_html()}
        <br>
        <p><h3>-> Tabel tabel saham hasil dari pemungutan suara:</h3></p>
        <br>
        <p><h4>Tabel saham 2 besar</h4></p>
        <p>*JIKA TABEL SAHAM 2 BESAR KOSONG MAKA TIDAK BOLEH BELI SAHAM APAPUN.</p>
        <br>
        {df_voting1.to_html()}
        <br>
        <p><h4>Tabel saham 5 besar</h4></p>
        {df_voting2.to_html()}
        <br>
        <br>
        <p>    {hari_ini} Rizky Cuan :)</p>
        </body>
        </html>
        """
    # jika dataframenya berisi hanya 1 saham yang direkomendasikan oleh program
    elif len(df_voting1) == 1:
        saham1 = df_pembelian['Saham'][0] # nama sahamnya
        hargat_shm1 = df_pembelian['Last'][0]#harga terakhir sahamnya
        harga1psn_shm1 = df_pembelian['Hrg 1%'][0]#harga saham di 1%  sahamnya
        hargap2_shm1 = df_pembelian['Hrg 2%'][0]#harga 2% pembelian sahamnya
        hrg1t_2shm1 = df_pembelian['Hrg 1 lot2%'][0]#harga 1 lot saham di 2% sahamnya
        ## isi pesan
        # disini kita menggunakan html dan untuk dataframenya jadikan html
        html = f"""
        <html>
        <head>Assalamu'alaikum WR WB.</head>
        <body>
        <p>Tanggal akhir input datanya adalah {tgl_akhir_data}. Insya Allah pada {h_predik} hari kedepan (dalam hari kerja) saham-saham ini akan naik:</p>
        <br>
        <p><h3>Saham {saham1}</h3></p>
        <p>Harga terakhir saham {saham1}  = Rp {hargat_shm1}</p>
        <p>Harga saham {saham1} di 1%  = Rp {harga1psn_shm1}</p>
        <p>Batas harga permbelian (2%) = Rp {hargap2_shm1}</p>
        <p>Harga 1 lot saham {saham1} di 2% = Rp {hrg1t_2shm1}</p>
        <br>
        <p><h3>-> Tabel pembelian dan penjualan saham:</h3></p>
        <br>
        <p><h2>Tabel pembelian saham 2 besar:</h2></p>
        {df_pembelian.to_html()}
        <br>
        <p><h2>Tabel Penjualan saham 2 besar:</h2></p>
        {df_penjualan.to_html()}
        <br>
        <p><h3>-> Tabel tabel saham hasil dari pemungutan suara:</h3></p>
        <br>
        <p><h4>Tabel saham 2 besar</h4></p>
        <p>*JIKA TABEL SAHAM 2 BESAR KOSONG MAKA TIDAK BOLEH BELI SAHAM APAPUN.</p>
        <br>
        {df_voting1.to_html()}
        <br>
        <p><h4>Tabel saham 5 besar</h4></p>
        {df_voting2.to_html()}
        <br>
        <br>
        <p>    {hari_ini} Rizky Cuan :)</p>
        </body>
        </html>
        """
    # jika dataframenya berisi 2 saham atau lebih yang direkomendasikan oleh program
    else:
        saham1 = df_pembelian['Saham'][0] # nama saham pertama
        saham2 = df_pembelian['Saham'][1] # nama saham kedua
        hargat_shm1 = df_pembelian['Last'][0]#harga terakhir saham pertama
        hargat_shm2 = df_pembelian['Last'][1]#harga terakhir saham kedua
        harga1psn_shm1 = df_pembelian['Hrg 1%'][0]#harga saham di 1%  saham pertama
        harga1psn_shm2 = df_pembelian['Hrg 1%'][1]#harga saham di 1%  saham kedua
        hargap2_shm1 = df_pembelian['Hrg 2%'][0]#harga 2% pembelian saham pertama
        hargap2_shm2 = df_pembelian['Hrg 2%'][1]#harga 2% pembelian saham kedua
        hrg1t_2shm1 = df_pembelian['Hrg 1 lot2%'][0]#harga 1 lot saham di 2% saham pertama
        hrg1t_2shm2 = df_pembelian['Hrg 1 lot2%'][1]#harga 1 lot saham di 2% saham kedua
        ## isi pesan
        # disini kita menggunakan html dan untuk dataframenya jadikan html
        html = f"""
        <html>
        <head>Assalamu'alaikum WR WB.</head>
        <body>
        <p>Tanggal akhir input datanya adalah {tgl_akhir_data}. Insya Allah pada {h_predik} hari kedepan (dalam hari kerja) saham-saham ini akan naik:</p>
        <br>
        <p><h3>1. Saham {saham1}</h3></p>
        <p>Harga terakhir saham {saham1}  = Rp {hargat_shm1}</p>
        <p>Harga saham {saham1} di 1%  = Rp {harga1psn_shm1}</p>
        <p>Batas harga permbelian (2%) = Rp {hargap2_shm1}</p>
        <p>Harga 1 lot saham {saham1} di 2% = Rp {hrg1t_2shm1}</p>
        <br>
        <p>*BELI SAHAM YANG PERTAMA. JANGAN YANG KEDUA</p>
        <br>
        <p><h3>2. Saham {saham2}</h3></p>
        <p>Harga terakhir saham {saham2}  = Rp {hargat_shm2}</p>
        <p>Harga saham {saham2} di 1%  = Rp {harga1psn_shm2}</p>
        <p>Batas harga permbelian (2%) = Rp {hargap2_shm2}</p>
        <p>Harga 1 lot saham {saham2} di 2% = Rp {hrg1t_2shm2}</p>
        <br>
        <p><h3>-> Tabel pembelian dan penjualan saham:</h3></p>
        <br>
        <p><h2>Tabel pembelian saham 2 besar:</h2></p>
        {df_pembelian.to_html()}
        <br>
        <p><h2>Tabel Penjualan saham 2 besar:</h2></p>
        {df_penjualan.to_html()}
        <br>
        <p><h3>-> Tabel tabel saham hasil dari pemungutan suara:</h3></p>
        <br>
        <p><h4>Tabel saham 2 besar</h4></p>
        <p>*JIKA TABEL SAHAM 2 BESAR KOSONG MAKA TIDAK BOLEH BELI SAHAM APAPUN.</p>
        <br>
        {df_voting1.to_html()}
        <br>
        <p><h4>Tabel saham 5 besar</h4></p>
        {df_voting2.to_html()}
        <br>
        <br>
        <p>    {hari_ini} Rizky Cuan :)</p>
        </body>
        </html>
        """
    # saat nya mulai mengirim email
    message = MIMEMultipart(
        "alternative", None, [MIMEText(html,'html')])
    # MIMEMultipart adalah untuk mengatakan "Saya memiliki lebih dari satu bagian",
    #dan kemudian membuat daftar bagian - Anda melakukannya jika Anda memiliki 
    #lampiran, Anda juga melakukannya untuk memberikan versi alternatif dari 
    #konten yang sama (misalnya versi teks biasa ditambah versi HTML)
    ## mendefinisikan header
    # jika dataframe kosong/tidak ada saham yang direkomendasikan oleh program
    if len(df_voting1) == 0:
        message['Subject'] = f"JANGAM BELI SAHAM APAPUN" # subjek / judul
    # jika dataframenya berisi hanya 1 saham yang direkomendasikan oleh program
    elif len(df_voting1) == 1:
        message['Subject'] = f"Saham {saham1} Insya Allah akan naik" # subjek / judul
    # jika dataframenya berisi 2 saham atau lebih yang direkomendasikan oleh program
    else:
        message['Subject'] = f"Saham {saham1} & {saham2} Insya Allah akan naik" # subjek / judul
    #
    message['From'] = email_pengirim # dari
    message['To'] = ', '.join(list_email_penerima) # email target
    #method join() berfungsi agar menghilangkan kutip'' dan kurungkurwal []
    # memulai server
    server = smtplib.SMTP(server) # server
    server.ehlo() # fungsi untuk memulai seluruh proses
    server.starttls() # mulai tls
    server.login(login_email, password) # masuk ke akun
    server.sendmail(email_pengirim, list_email_penerima, message.as_string()) # kirim emailnya
    server.quit() # putuskan server