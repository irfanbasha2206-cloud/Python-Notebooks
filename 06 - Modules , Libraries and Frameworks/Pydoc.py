import streamlit as st

st.title("Welcome to the PY Doctor")

name = st.text_input("Enter Your Name")

age = st.number_input("Enter your Age",min_value=20,max_value=100,step=5)

password = st.text_input("Enter the Password",type="password")

st.time_input ("Time")

st.date_input("Date")

st.radio("Gender",["Male","Female"])

st.selectbox("Courses",["Python","Java","C++","Assembly"])

st.multiselect("Courses",["AI","ML","Data Science","Web Development"])

st.file_uploader("Upload File")

st.slider("Enter heart rate", 0, 120)

st.sidebar.selectbox("User",["Login","Register"])

st.button("Submit")

st.image(r"C:\Users\Aneesh\Downloads\1_ipUaz5SUfi44K3stYRBckQ.png")

st.write("🎵 Shape of You Song Cover Song")

st.audio(r"C:\Users\Aneesh\Downloads\Shape Of You (PenduJatt.Com.Se).mp3")

st.video(r"https://www.youtube.com/watch?v=ky82Sw9tOr4&pp=0gcJCdkKAYcqIYzv")