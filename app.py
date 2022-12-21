import streamlit as st 
import streamlit.components.v1 as stc
from PIL import Image

# importing the smaller apps
from eda_app import run_eda_app
from ml_app import run_ml_app
from sklearn.model_selection import train_test_split 


html_temp = """
		<div style="background-color:#000080;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">Program Prediksi Penerimaan Beasiswa S2 </h1>
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
					
main()
