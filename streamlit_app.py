import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

import streamlit as st

# 스트림릿 페이지 제목 설정
st.title("📚 나의 공부 기록 미션 앱")

# 1. 세션 상태(session_state) 초기화
# 페이지가 새로고침되어도 데이터가 초기화되지 않도록 저장소를 만듭니다.
if '공부기록' not in st.session_state:
    st.session_state['공부기록'] = []
if '공부시간' not in st.session_state:
    st.session_state['공부시간'] = 0

# 2. 사용자 입력 UI 구성
st.subheader("✍️ 오늘의 공부 내용 입력")

# 과목과 시간을 입력받는 칸 (기존 input() 대체)
과목 = st.text_input("공부한 과목을 입력하세요:", key="subject_input")
시간 = st.number_input("공부한 시간(시간 단위)을 입력하세요:", min_value=1, max_value=24, step=1, key="time_input")

# 기록 추가 버튼
if st.button("공부 기록 추가하기"):
    if 과목.strip() == "":
        st.warning("과목 이름을 입력해 주세요!")
    else:
        # 세션 상태에 데이터 누적 저장
        st.session_state['공부기록'].append(과목)
        st.session_state['공부시간'] += 시간
        st.success(f"'{과목}' ({시간}시간) 기록이 추가되었습니다!")

# 초기화 버튼 (새로 시작하고 싶을 때)
if st.button("기록 전체 초기화"):
    st.session_state['공부기록'] = []
    st.session_state['공부시간'] = 0
    st.info("모든 기록이 초기화되었습니다.")

st.markdown("---")

# 3. 결과 출력 및 미션 확인 UI
st.subheader("📊 오늘의 공부 결과")

# 현재까지 저장된 기록 보여주기
st.write(f"**공부한 과목 리스트:** {st.session_state['공부기록']}")
st.write(f"**총 공부한 시간:** {st.session_state['공부시간']}시간")

# 미션 성공 여부 조건문
if st.session_state['공부시간'] >= 3:
    st.balloons() # 축하 효과 호출 🎈
    st.success("🔥 공부 미션 성공! 정말 멋집니다! 🎉")
else:
    st.info(f"💡 공부 미션 실패! 3시간까지 {3 - st.session_state['공부시간']}시간 남았습니다. 힘내세요! 😢")