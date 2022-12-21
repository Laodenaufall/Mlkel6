import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import plotly.express as px


def run_eda_app():
	st.subheader("Exploratory Data Analysis")
	

	submenu = st.sidebar.selectbox("Submenu", ["Descriptive", "Plots"])
	myData = pd.read_csv("data.csv")
	myData_cleaned = pd.read_csv("data.csv")
	dataFrameSerialization = "legacy"
	
	df = pd.DataFrame(myData)
	df.astype(str)	

	if submenu == "Descriptive":
		st.dataframe(myData)

		with st.expander("Data Types"):
			st.dataframe(myData)
			
		with st.expander("Summary"):
			st.dataframe(myData.describe()[["GRE Score","TOEFL Score","University Rating","LOR ","CGPA","Research","Chance of Admit "]])

		with st.expander("GRE Score Distribution"):
			st.dataframe(myData["GRE Score"].value_counts())

		with st.expander("Chance of Admit Distribution"):
			st.dataframe(myData["Chance of Admit "].value_counts())

	elif submenu == "Plots":
		st.subheader("Visualization Plots")

		with st.expander("Plots based on GRE Score"):
			#fig = plt.figure()
			#sns.countplot(myData['Gender'])
			#st.pyplot(fig)

			gre_myData = myData["GRE Score"].value_counts()
			gre_myData = gre_myData.reset_index()
			gre_myData.columns = ["GRE Score", "Count"]
			#st.dataframe(gender_myData)

			p1 = px.pie(gre_myData, names = "GRE Score", values = "Count")
			st.plotly_chart(p1)

		with st.expander("Plots based on Chance of Admit Distribution"):
			fig = plt.figure()
			sns.countplot(myData['Chance of Admit'])
			st.pyplot(fig)

			coa_myData = myData["Chance of Admit"].value_counts()
			coa_myData = coa_myData.reset_index()
			coa_myData.columns = ["Chance of Admit", "Count"]
			#st.dataframe(Chance of Admit_myData)
		with st.expander("Outlier Detection"):
			p3 = px.box(myData, x = "University Rating")
			st.plotly_chart(p3)
