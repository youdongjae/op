import streamlit as st
import random

# 페이지 설정
st.set_page_config(
    page_title="유동재 자기소개",
    page_icon="👨‍💼",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 세션 상태 초기화
if 'current_page' not in st.session_state:
    st.session_state.current_page = 0

# 페이지 데이터
pages = [
    {
        "title": "자기<span class='red-accent'>소개</span>",
        "icon": "👋",
        "content": [
            {"icon": "👨‍🎓", "title": "이름", "description": "안녕하세요! 유동재입니다"},
            {"icon": "🎯", "title": "목표", "description": "소방공무원이 되어 사회에 기여하고 싶습니다"},
            {"icon": "💪", "title": "특징", "description": "꾸준한 노력과 성실함이 저의 장점입니다"},
            {"icon": "🚀", "title": "비전", "description": "안전한 사회를 만드는 데 기여하겠습니다"}
        ]
    },
    {
        "title": "학업<span class='red-accent'>현황</span>",
        "icon": "📚",
        "content": [
            {"icon": "🏫", "title": "전공", "description": "소방관련 학과에서 전문 지식을 쌓고 있습니다"},
            {"icon": "📖", "title": "성적", "description": "꾸준한 학습으로 좋은 성적을 유지하고 있습니다"},
            {"icon": "👥", "title": "활동", "description": "학과 내 다양한 활동에 적극 참여합니다"},
            {"icon": "🎓", "title": "계획", "description": "졸업 후 바로 현장에 투입될 수 있도록 준비 중입니다"}
        ]
    },
    {
        "title": "체력<span class='red-accent'>관리</span>",
        "icon": "💪",
        "content": [
            {"icon": "🏃‍♂️", "title": "유산소 운동", "description": "매일 러닝으로 지구력을 기르고 있습니다"},
            {"icon": "🏋️‍♂️", "title": "근력 운동", "description": "소방관에게 필요한 근력을 꾸준히 단련합니다"},
            {"icon": "📊", "title": "체력 측정", "description": "정기적인 체력 측정으로 발전 상황을 확인합니다"}
        ]
    },
    {
        "title": "자격증<span class='red-accent'>준비</span>",
        "icon": "📜",
        "content": [
            {"icon": "🚒", "title": "소방 관련", "description": "소방설비기사, 위험물산업기사 등을 준비 중입니다"},
            {"icon": "🚑", "title": "응급처치", "description": "응급처치 관련 자격증을 취득할 예정입니다"},
            {"icon": "🚗", "title": "운전면허", "description": "대형면허 취득할 예정입니다"},
            {"icon": "💻", "title": "컴퓨터", "description": "현대 소방업무에 필요한 IT 관련 자격증도 보유할 예정입니다"}
        ]
    },
    {
        "title": "리더십<span class='red-accent'>경험</span>",
        "icon": "👑",
        "content": [
            {"icon": "📋", "title": "팀 프로젝트", "description": "학과 내 다양한 팀 프로젝트를 이끌어왔습니다"},
            {"icon": "🎯", "title": "목표 달성", "description": "팀원들과 함께 설정한 목표를 성공적으로 달성했습니다"},
            {"icon": "💬", "title": "소통", "description": "원활한 소통으로 팀워크를 이끌어내는 것이 강점입니다"},
            {"icon": "🏆", "title": "성과", "description": "리더로서 팀을 이끌며 좋은 성과를 거두었습니다"}
        ]
    },
    {
        "title": "개인<span class='red-accent'>특성</span>",
        "icon": "⭐",
        "content": [
            {"icon": "🎯", "title": "책임감", "description": "맡은 일에 대해 끝까지 책임지는 성격입니다"},
            {"icon": "⚡", "title": "적극성", "description": "어떤 상황에서도 적극적으로 임하는 자세를 가지고 있습니다"},
            {"icon": "🤔", "title": "신중함", "description": "중요한 결정 시 신중하게 판단하여 행동합니다"},
            {"icon": "😊", "title": "긍정적", "description": "항상 긍정적인 마인드로 어려움을 극복해나갑니다"}
        ]
    },
    {
        "title": "미래<span class='red-accent'>계획</span>",
        "icon": "🚒",
        "content": [
            {"icon": "👨‍💼", "title": "소방공무원", "description": "졸업 후 소방공무원이 되어 사회에 실질적으로 기여하고 싶습니다"},
            {"icon": "💪", "title": "체력 단련", "description": "체력 단련을 꾸준히 하여 소방관으로서 필요한 신체적 자질을 갖추고 있습니다"},
            {"icon": "📜", "title": "소방 관련 자격증", "description": "소방 관련 자격증 취득을 위해 학업에 열심히 임하고 있습니다"},
            {"icon": "🏆", "title": "자기계발", "description": "자기계발을 통해 역량을 키우고 목표를 향해 한 걸음씩 나아가고 있습니다"}
        ]
    }
]

# 진행률 데이터
progress_data = [
    [0.9, 0.85, 0.8, 0.9],    # 페이지 1
    [0.88, 0.92, 0.85, 0.87],  # 페이지 2
    [0.95, 0.9, 0.85],         # 페이지 3
    [0.75, 0.8, 0.9, 0.7],     # 페이지 4
    [0.85, 0.9, 0.8, 0.85],    # 페이지 5
    [0.8, 0.85, 0.9, 0.88],    # 페이지 6
    [0.9, 0.88, 0.85, 0.92],   # 페이지 7
]

# 커스텀 CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700;900&display=swap');

    .main > div {
        padding-top: 1rem;
    }

    .stApp {
        background: linear-gradient(135deg, #003366 0%, #001a33 100%);
        font-family: 'Noto Sans KR', sans-serif;
    }

    .title-container {
        background: rgba(0, 51, 102, 0.3);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        border-top: 5px solid #FF3B30;
        text-align: center;
    }

    .main-title {
        font-size: 3.5rem;
        font-weight: 900;
        color: white;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    }

    .red-accent {
        color: #FF3B30;
    }

    .content-text {
        font-size: 1.2rem;
        line-height: 1.5;
        color: white;
    }

    .page-info {
        position: fixed;
        bottom: 20px;
        right: 20px;
        background: rgba(0, 51, 102, 0.8);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.9rem;
        border: 1px solid rgba(255, 59, 48, 0.5);
        z-index: 1000;
    }
</style>
""", unsafe_allow_html=True)

# 페이지 네비게이션
col_nav1, col_nav2, col_nav3, col_nav4, col_nav5 = st.columns([1, 1, 1, 1, 1])

with col_nav1:
    if st.button("⏮️ 처음", use_container_width=True):
        st.session_state.current_page = 0
        st.rerun()

with col_nav2:
    if st.button("◀️ 이전", use_container_width=True):
        if st.session_state.current_page > 0:
            st.session_state.current_page -= 1
            st.rerun()

with col_nav3:
    st.selectbox(
        "페이지 선택",
        options=range(len(pages)),
        format_func=lambda x: f"{x+1}. {pages[x]['title'].replace('<span class=\"red-accent\">', '').replace('</span>', '')}",
        index=st.session_state.current_page,
        key="page_selector",
        on_change=lambda: setattr(st.session_state, 'current_page', st.session_state.page_selector)
    )

with col_nav4:
    if st.button("다음 ▶️", use_container_width=True):
        if st.session_state.current_page < len(pages) - 1:
            st.session_state.current_page += 1
            st.rerun()

with col_nav5:
    if st.button("마지막 ⏭️", use_container_width=True):
        st.session_state.current_page = len(pages) - 1
        st.rerun()

# 현재 페이지 데이터
current_page_data = pages[st.session_state.current_page]
current_progress = progress_data[st.session_state.current_page]

# 메인 타이틀
st.markdown(f"""
<div class="title-container">
    <h1 class="main-title">{current_page_data['icon']} {current_page_data['title']}</h1>
</div>
""", unsafe_allow_html=True)

# 메인 컨텐츠
col1, col2 = st.columns([2, 1])

with col1:
    for i, item in enumerate(current_page_data['content']):
        with st.expander(f"{item['icon']} {item['title']}", expanded=True):
            st.markdown(f"<div class='content-text'>{item['description']}</div>", unsafe_allow_html=True)
            if i < len(current_progress):
                progress_val = current_progress[i]
                st.progress(progress_val)
                st.caption(f"달성률: {int(progress_val * 100)}%")

with col2:
    st.markdown("### 📊 현재 상태")

    avg_progress = sum(current_progress) / len(current_progress)
    st.metric(
        label="전체 진행률",
        value=f"{int(avg_progress * 100)}%",
        delta=f"{random.randint(1, 5)}% 상승"
    )

    st.info(f"📄 {st.session_state.current_page + 1}/{len(pages)} 페이지")

    if st.session_state.current_page == len(pages) - 1:
        if st.button("🔥 동기부여 받기", use_container_width=True):
            motivational_quotes = [
                "목표를 향한 한 걸음 한 걸음이 성공으로 이어집니다! 🚀",
                "소방관의 꿈을 향해 꾸준히 전진하고 있습니다! 💪",
                "준비하는 자에게 기회는 반드시 찾아옵니다! ⭐",
                "노력하는 당신의 모습이 정말 멋집니다! 🏆"
            ]
            st.success(random.choice(motivational_quotes))
            st.balloons()

# 페이지 정보 표시
st.markdown(f"""
<div class="page-info">
    📄 {st.session_state.current_page + 1}/{len(pages)} 페이지
</div>
""", unsafe_allow_html=True)
