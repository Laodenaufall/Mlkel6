import streamlit as st 
import pandas as pd
import numpy as np
import streamlit.components.v1 as stc
from PIL import Image

# importing the smaller apps
from eda_app import run_eda_app
from ml_app import run_ml_app
from sklearn.model_selection import train_test_split 


html_temp = """
		<div style="background-color:#000080;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">Program Prediksi Peluang Penerimaan Beasiswa S2 </h1>
		<h2 style="color:white;text-align:center">Kelompok 2<h2>

		</div>
		"""
def main():
	#st.title("Main App")
	stc.html(html_temp)

	menu = ["Home", "EDA", "ML"]
	choice = st.sidebar.selectbox("Menu", menu)

	if choice=="Home":
		#st.header("Web App Tour")
		#st.subheader("Home")
		st.write( """
			## Data yang digunakan
			1. GRE Score: Nilai Test Untuk Masuk Program S2 (0 - 340) Bersifat Continous
			2. TOEFL Score: NIlai TOEFL (0 - 120) Bersifat Continous
			3. University Rating: Rating Universitas (0 - 5) Bersifat Ordinal
			4. Surat Rekomendasi (0 - 5) Bersifat Ordinal
			5. GPA Sewaktu Undergraduate (0 - 10) Bersifat Continous
			6. Pengalaman Riset (0 : tidak ada, 1 : ada) Bersifat Nominal
			7. Peluang Diterima (0 - 1) Merupakan Dependent Variable
		""")
		
	elif choice=="EDA":
		run_eda_app()
	elif choice == "ML":
		run_ml_app()
	else:
		st.subheader("About")
		
		st.write("### Adith Sreeram - The Data Guy")
		img = Image.open("asr.jpeg")
		st.image(img)
		st.text("""
		My ambitious dream to become a data scientist is soon to be a reality. Spending hours 
		looking for the most appropriate content for you never makes me tired, which will 
		obviously be preceded by long and passionate reading, writing, and prosperity in 
		sharing my wisdom brought me here. 
		As I am pursuing computer engineering, I build computer applications and muscles too.
		I strive to use my energy in data science to make significant contributions to society by 
		tackling complex problems through research and cutting edge technologies.
		Creative problem solver with strong interpersonal skills. Dreaming of taking the world 
		towards a safer and healthier future.
		I love meeting people working on exciting things. If there is any suitable role for me, 
		don't hesitate. I am open to communication on all channels. Let's discuss.
""")			
main()
