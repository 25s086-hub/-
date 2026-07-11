import streamlit as st

st.markdown("# AI 챗봇 만들기")
st.markdown("---")
st.markdown("## 질문을 하시면 AI 친구가 응답합니다.")
st.header("1. 기본 정보 입력")
user_id = st.text_input("아이디(ID)를 입력하세요", placeholder="example_user")
age = st.number_input("나이를 입력하세요", min_value=1, max_value=100, value=17)
question = st.text_area("AI에게 보낼 질문을 입력하세요", placeholder="여기에 질문을 작성해 주세요.")

st.header("2. 챗봇 설정")
ai_model = st.radio("사용할 AI 모델을 선택ㄱ", ["GPT-4", "Claude 3", "Gemini Pro"], horizontal=True)
tone = st.selectbox("답변의 말투를 골라주소", ["친절", "냉철", "유머"])
features = st.multiselect("추가 기능을 선택ㄱ", ["이미지 생성", "웹 검색", "코드 분석", "번역"])
creativity = st.slider("AI의 창의성 수준을 설정ㄱ", 0, 100, 50)
ai_speed = st.select_slider("응답 처리 속도를 선택ㄱ",options=["매우 느림", "느림", "보통", "빠름", "실시간"],value="보통")
agree = st.checkbox("개인정보 수집 및 AI 학습 이용에 동의ㄱ.")
st.markdown("---")

if st.button("질문 전송ㄱ"):
    if agree:
        st.success(f"성공적으로 전송됨ㅇ ({user_id}ㅉㅉ)")
        st.markdown(f"""
        * **질문 내용:** {question}
        * **선택 모델:** `{ai_model}` | **말투:** `{tone}`
        * **활성화 기능:** {', '.join(features) if features else '없음'}
        * **창의성:** `{creativity}%` | **처리 속도:** `{ai_speed}`
        """)
        
        if age < 14:
            st.info("참고: 14세 미만 사용자이므로 촉법 활성화됨.")
    else:
        st.error("⚠️ 동의 항목에 체크해야 전송이 가능ㅇ.")
