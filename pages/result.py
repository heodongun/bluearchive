import streamlit as st
import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
key_dict = json.loads(st.secrets["textkey"])

# Fetch the service account key JSON file contents
cred = credentials.Certificate(key_dict)

# Initialize the app with a service account, granting admin privileges
if not firebase_admin._apps:
    cred = credentials.Certificate('secret.json')
    firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://anything-b3eaf-default-rtdb.firebaseio.com/'
})
    
st.write(st.session_state.name)
st.write(st.session_state.number)
st.write(st.session_state.key)
value=db.reference('')
value.update({'score':st.session_state.key})