import streamlit as st



if 'key' not in st.session_state:
    st.session_state.key = 'value'
    st.session_state.key=0


def quiz1():
    st.write('이 학생의 이름은 무엇일까요?')
    st.image('hosinoquiz.jpg')
    correct=st.button("호시노",key=1)
    Warning=st.button("호시노겐",key=2)
    if correct:
     st.write('정답')
     st.session_state.key+=50 
    if Warning:
     st.write('틀렸어이놈아')

def quiz2():
   st.image('serikaquiz.webp')
   correct1=st.text_input('이 학생의 소속학교의 이름을 입력하세요!') 
   correct2=st.button("제출합니다.",key=3)
   if(correct2):
     if correct1=="아비도스":
        st.write('정답입니다.')
        st.session_state.key+=50 
     else:
        st.write('오답입니다.')

quiz1()
for i in range(10):
    st.write("")
quiz2()