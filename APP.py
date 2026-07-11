import streamlit as st

st.markdown("# 앱 ui만들기")
st.markdown("---")

user_id = st.text_input("이름", placeholder="이름")
학년 = st.radio("학년", ["1", "2", "3"], horizontal=True)
반 = st.number_input("반 입력", min_value=1, max_value=10, value=1)
level = st.slider("난이도", 0, 100, 50)
score = st.slider("점수", 0, 100, 50)
question = st.text_area("소감", placeholder="소감.")


if st.button("확인"):
      st.success(f"{user_id}/{학년}/{반}/{level}")
      st.markdown(f"점수:{score}")
      st.success(f"소감:{question}")
        
