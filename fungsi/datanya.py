# ~~~~~~~~~~~~~ TEMPAT FUNGSI UNTUK MENGUBAH, MEMODIF, STRUKTUR DATA
# ~~~~~~~~~~~~~~~~~~~~~~~ UNTUK INPUT MODEL/AI

import pandas_datareader as pdr
import pandas as pd
import numpy as np
import numpy
from sklearn.preprocessing import MinMaxScaler

# ~~~ fungsi untuk preprocess data kelas 1, 11, 2, 10, 8, 20, 16, dll.
# ini untuk data train/melatih model/fit model.
# mempunyai 2 parameter (masukkan data yang utuh/mentah yang belum diapa apain dan timestep).
# ini akan mereturn 2 variabel yang x_train dan y_train.
# cara pakai: siap kan 2 variabel contoh   x_train, y_train = datanya.data_latih(data)
def data_latih12(df,time_step): # masukkan dataframe, dan besar timestep
    timestep = time_step
    scaler = MinMaxScaler(feature_range=(0,1)) # siapkan fungsi untuk skala
    scaled_data = scaler.fit_transform(df['Close'].values.reshape(-1,1)) # ambil kolom close saja dan skalakan/perkercil datanya
    x_train = [] # siapkan wadah
    y_train = []
    # loop untuk memasukkan datanya
    for x in range(timestep, len(scaled_data)): # 60 , ...
        x_train.append(scaled_data[x-timestep:x, 0]) #misal x=60, maka scaled_data[60-60= 0 : 60, 0] dari index 0 sampai sebelum 60
        y_train.append(scaled_data[x, 0])
    x_train, y_train = np.array(x_train), np.array(y_train) # jadikan array
    # jadikan x_train menjadi 3 dimensi
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))  # ubah bentuk jadi (dataset, fitur, label)
    return x_train, y_train

# ~~~ fungsi untuk model memprediksi 5 hari kedepan
def predik_5h(df, time_step, model, h_predik): # masukkan dataframe, besar timestep, dan model, berapa hari kedepan kita akan memprediksi
    n_steps = time_step
    h_pred = h_predik # berapa hari kita ingin model memprediksi
    data = df
    makanan = data.filter(['Close']) # ambil hanya kolom close saja
    makanan = makanan[-n_steps:].values # potong datanya sesai besar timestep
    scaler = MinMaxScaler(feature_range=(0,1)) # siapkan untuk skala
    makan = scaler.fit_transform(makanan)# skala/perkecil datanya
    temp_input = makan.reshape(1,-1) # bentuk ulang
    temp_input=temp_input[0].tolist()
    lst_output=[] # tempat prediksi / output model (yang masih dalam bentuk skala)
    ## saatnya model memprediksi menggunakan while loop
    # kenapa pake loop? karna model hanya bisa memprediksi 1 hari saja, jadi kita pake loop agar 
    #bisa memprediksi beberapa hari.
    i=0
    while(i<h_pred):
        
        if(len(temp_input)>n_steps): # jika jumlah fitur lebih dari timestep / fiturnya lebih 1 dari timestep, maka:
            x_input=np.array(temp_input[1:]) # ambil datanya dari indeks kedua lalu jadikan array
            x_input=x_input.reshape(1,-1)# bentuk ulang
            x_input = x_input.reshape((1, n_steps, 1)) # ubah bentuk jadi (dataset(1), fitur, 1) ini bentuk 3 dimensi
            yhat = model.predict(x_input, verbose=0) # model memprediksi
            temp_input.extend(yhat[0].tolist())# tambahkan ke temp_input dan jadikan list
            temp_input=temp_input[1:] # ambil datanya dari indeks kedua. ini untuk tambahan data input model (ingat ini loop)
            lst_output.extend(yhat.tolist()) # masukkan prediksi model(yhat) kedalam variabel lst_output
            i=i+1
        else: # jika jumlah fiturnya sama dengan timestep, maka:
            x_input = np.array(temp_input) # jadikan array
            x_input = x_input.reshape((1, n_steps,1)) # ubah bentuk jadi (dataset(1), fitur, 1)
            yhat = model.predict(x_input, verbose=0) 
            temp_input.extend(yhat[0].tolist())
            lst_output.extend(yhat.tolist())
            i=i+1
    hasil_pred = scaler.inverse_transform(lst_output)
    return hasil_pred

######### fungsi seterusnya sama saja cuma beda di struktur data. seperti datanya (dataset(1), fitur, 1) atau (dataset(1), 1, fitur)

# ~~~ fungsi untuk preprocess data kelas 3
def data_latih3(df, timestep):
    df1 = df.reset_index()['Close']
    scaler = MinMaxScaler(feature_range=(0,1)) # ini agar data kita diantara 0 sampai 1
    df1 = scaler.fit_transform(np.array(df1).reshape(-1, 1)) # jadi 2 dimensi
    training_data = df1
    ### kita akan membuat fungsi untuk membuat dataset nya
    def create_dataset(dataset, time_step=1): # 2 parameter yaitu datanya dan time step (defaultnya 1)
        dataX, dataY = [], [] # sediakan list kosong
        # kita buat for loop
        for i in range(len(dataset)-time_step-1): # misal timstepnya 100 maka hasilnya 716 . Dikurang 1 itu untuk outputnya/ hal yang akan diprediksi
            a = dataset[i:(i+time_step),0] # i=0, jika timestep nya 100 maka  0,1,2,3,4, ...
            dataX.append(a)
            dataY.append(dataset[i+time_step,0]) # 0 berguna untuk menghilangkan []. misal [0.52647129] akan menjadi 0.526471285120
        return numpy.array(dataX), numpy.array(dataY)
    time_step = timestep # timestep
    X_train, y_train = create_dataset(training_data, time_step) # (817, 100)
    X_train =X_train.reshape(X_train.shape[0],X_train.shape[1] , 1)
    return X_train, y_train

# ~~~ fungsi untuk preprocess data kelas 4 dan 5
def data_latih4(df, timestep):
    window_size = timestep
    data = df.reset_index()['Close']
    T = data.values
    T = T.astype('float32').reshape(-1,1) # jadikan 2 dimensi
    scaler = MinMaxScaler(feature_range = (0, 1))
    T = scaler.fit_transform(T)
    train = T
    ## Membuat fungsi / Metode untuk membuat fitur dari data deret waktu
    def create_features(data, window_size):
        # siapkan tempat untuk x dan y
        X, Y = [], []
        for i in range(len(data) - window_size - 1):
            window = data[i:(i + window_size), 0]
            X.append(window)
            Y.append(data[i + window_size, 0])
        return np.array(X), np.array(Y)
    X_train, Y_train = create_features(train, window_size)
    X_train = np.reshape(X_train, (X_train.shape[0], 1, X_train.shape[1])) # (...,1,20)
    return X_train, Y_train

# ~~~ fungsi untuk model memprediksi beberapa hari kedepan. ini untuk kelas 4 dan 5
def predik5h_4(df, time_step, model, h_predik):
    makanan = df.filter(['Close'])
    n_steps=time_step # jumlah timestep
    makanan = makanan[-n_steps:].values
    scaler = MinMaxScaler(feature_range = (0, 1))
    makan = scaler.fit_transform(makanan)
    temp_input = makan.reshape(1,-1)[0].tolist() # jadikan list
    lst_output=[] # tempat prediksi (output model)
    h_pred = h_predik # berapa hari kita ingin model memprediksi
    i=0
    ## saatnya model memprediksi
    while(i<h_pred):
        if(len(temp_input)>n_steps): # jika timestep lebih dari 100 / timestep 101, maka:
            # print('ini bagian if')
            x_input=np.array(temp_input[1:])
            # print("{} day input {}".format(i,x_input))
            x_input=x_input.reshape(1,-1)
            x_input = x_input.reshape((1, 1, n_steps)) # perhatikan bentuknya
            yhat = model.predict(x_input, verbose=0)
            # print("{} day output {}".format(i,yhat))
            temp_input.extend(yhat[0].tolist())
            temp_input=temp_input[1:]
            lst_output.extend(yhat.tolist())
            i=i+1
        else: # jika timestepnya pas 100, maka:
            # print('ini bagian else')
            x_input=np.array(temp_input)
            x_input = x_input.reshape((1, 1, n_steps)) # perhatikan bentuknya
            yhat = model.predict(x_input, verbose=0)
            # print(yhat[0])
            temp_input.extend(yhat[0].tolist())
            # print(len(temp_input))
            lst_output.extend(yhat.tolist())
            i=i+1
    hasil_pred = scaler.inverse_transform(lst_output)
    return hasil_pred

###  ~~~~~ fungsi untuk preprocess data kelas 9
def data_latih9(df,time_step): # masukkan dataframe, dan besar timestep
    timestep = time_step
    scaler = MinMaxScaler(feature_range=(0,1))
    train_data = scaler.fit_transform(df['Close'].values.reshape(-1,1))
    x_train_data=[]
    y_train_data =[]
    for i in range(timestep,len(train_data)):
        x_train_data=list(x_train_data)
        y_train_data=list(y_train_data)
        x_train_data.append(train_data[i-timestep:i,0])
        y_train_data.append(train_data[i,0])
    x_train_data1, y_train_data1 = np.array(x_train_data), np.array(y_train_data)
    x_train_data2 = np.reshape(x_train_data1, (x_train_data1.shape[0],x_train_data1.shape[1],1))
    return x_train_data2, y_train_data1