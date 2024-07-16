import streamlit as st
from streamlit_option_menu import option_menu


# 사이드바에 선택 상자를 생성하여 사용자가 선택할 수 있도록 함
option = st.sidebar.selectbox(
    '캐릭터',
    ['호시노', '체리노', '코하루','아즈사','미카','히후미','세리나','미유','히나']
)

# 메인 콘텐츠 업데이트
if option == '호시노':
    st.title('블루아카이브는 신이다.')
    st.header('',divider='rainbow')
    st.write("아비도스의 호시노이다.")
    st.image('hosino.png')

elif option == '체리노':
    st.title('블루아카이브는 신이다.')
    st.header('',divider='rainbow')
    st.write("붉은겨울의 체리노이다.")
    st.image('cherino.png')
   
elif option == '코하루':
    st.title('블루아카이브는 신이다.')
    st.header('',divider='rainbow')
    st.write("정실부의 코하루이다.")
    st.video('bluearchive.mp4')
  
elif option == '아즈사':
    st.title('블루아카이브는 신이다.')
    st.header('',divider='rainbow')
    st.write("보충수업부의 아즈사이다")
    st.video('azusa.mp4')

elif option == '미카':
    st.title('블루아카이브는 신이다.')
    st.header('',divider='rainbow')
    st.write("티파티의 미카이다")
    st.video('mika.mp4')
   
elif option == '히나':
    st.title('블루아카이브는 신이다.')
    st.header('',divider='rainbow')
    st.write("선도부의 히나이다")
    st.video('hina.mp4')
  
elif option == '세리나':
    st.title('블루아카이브는 신이다.')
    st.header('',divider='rainbow')
    st.write("구호기사단의 세리나이다.")
    st.video('serina.mp4') 

elif option == '미유':
    st.title('블루아카이브는 신이다.')
    st.header('',divider='rainbow')
    st.write("래빗소대의 미유이다")
    st.video('miyu.mp4') 

elif option == '히후미':
    st.title('블루아카이브는 신이다.')
    st.header('',divider='rainbow')
    st.write("최종흑막 히후미이다.")
    st.video('hihumi.mp4') 