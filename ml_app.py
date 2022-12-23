import streamlit as st 
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split 

def run_ml_app():
    
   
    
   

    myData = pd.read_csv('data.csv')

   

   

    # Memisahkan Label Dan Fitur 
    X = myData.iloc[:, 1:-1].values
    y = myData.iloc[:, -1].values



    


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)



    from sklearn.preprocessing import StandardScaler 

    ss_train_test = StandardScaler()


    X_train_ss_scaled = ss_train_test.fit_transform(X_train)
    X_test_ss_scaled = ss_train_test.transform(X_test)

    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import r2_score

    l_regressor_ss = LinearRegression()
    l_regressor_ss.fit(X_train_ss_scaled, y_train)
    y_pred_l_reg_ss = l_regressor_ss.predict(X_test_ss_scaled)



    st.write("# Sekarang Silahkan Masukan Skor Test Kamu Untuk Mengetahui Prediksi Peluang Penerimaan Beasiswa S2 Kamu")


    form = st.form(key='my-form')
    inputGRE = form.number_input("Masukan GRE Score: ", 0)
    inputTOEFL = form.number_input("Masukan TOEFL Score: ", 0)
    inputUnivRating = form.number_input("Masukan Rating Univ: ", 0)
    inputSOP = form.number_input("Masukan Kekuatan SOP: ", 0)
    inputLOR = form.number_input("Masukan Jumlah Letter of Recommendation: ", 0)
    inputCGPA = form.number_input("Masukan CGPA: ", 0)
    inputResearch = form.number_input("Pengalaman Research, 1 Jika Pernah Riset, 0 Jika Tidak", 0)
    submit = form.form_submit_button('Submit')

    completeData = np.array([inputGRE, inputTOEFL, inputUnivRating, 
                            inputSOP, inputLOR, inputCGPA, inputResearch]).reshape(1, -1)
    scaledData = ss_train_test.transform(completeData)


    st.write('Tekan Submit Untuk Melihat Prediksi Penerimaan Beasiswa S2 Anda')

    if submit:
        prediction = l_regressor_ss.predict(scaledData)
        if prediction > 1 :
            result = 1
        elif prediction < 0 :
            result = 0
        else :
            result = prediction[0]
    
        st.write(result*100, "Percent")
       

    st.write("Dengan Menggunakan Multiple Linear Regression Diperoleh Skor Untuk Data Test")
    st.write(r2_score(y_test, y_pred_l_reg_ss))
