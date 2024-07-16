import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents


if not firebase_admin._apps:
    cred = credentials.Certificate('secret.json')
    firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://anything-b3eaf-default-rtdb.firebaseio.com/'
})
# Initialize the app with a service account, granting admin privileges


if 'name' not in st.session_state:
    st.session_state.name = 'value'
    st.session_state.name=0

if 'number' not in st.session_state:
    st.session_state.number = 'value'
    st.session_state.number=0

correct1=st.text_input('이름을 입력하세요!') 
correct2=st.text_input('학번을 입력하세요!') 
correct3=st.button("로그인",key=1)

if correct3:
    number = db.reference('number')
    name = db.reference('name')
    if correct1==name.get():
        if int(correct2)==number.get():
            st.write('success')
            st.session_state.name=correct1
            st.session_state.number=correct2
    else:
        st.write('error')


        