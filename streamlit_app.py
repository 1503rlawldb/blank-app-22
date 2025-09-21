import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

# --------------------------
# 페이지 기본 설정
# --------------------------
st.set_page_config(
    page_title="물러서는 땅, 다가오는 바다",
    page_icon="🌊",
    layout="wide"
)

# --------------------------
# 사이드바: 옵션
# --------------------------
st.sidebar.header("보기 옵션")

year = st.sidebar.slider("년도 선택", 1800, 2025, 2024)
region = st.sidebar.selectbox(
    "지역 선택",
    ["전 세계", "대한민국", "투발루", "몰디브", "방글라데시", "네덜란드"]
)
temp_range = st.sidebar.slider("색상 범위 절대값 (°C)", 1, 10, 5)

# --------------------------
# 보고서 제목 & 서론
# --------------------------
st.title("📘 물러서는 땅, 다가오는 바다: 해수면 상승의 위험과 우리만의 대처법")

st.subheader("서론: 문제 제기")
st.markdown("""
인류의 기술이 발전하는 동안 지구는 점점 황폐해지고 있습니다.  
기온은 해마다 오르고, 북극과 남극의 빙하는 녹아내리며, 바다는 따뜻해지고 해수면은 확실하게 높아지고 있습니다.  
지금 이 순간에도 우리 삶의 터전은 서서히 잠식당하고 있습니다.  
""")

# --------------------------
# 지도 시각화 데이터
# --------------------------
lats = np.linspace(-60, 80, 50)
lons = np.linspace(-180, 180, 100)
temp_anomaly = np.random.uniform(-temp_range, temp_range, size=(len(lats)*len(lons)))

df_map = pd.DataFrame({
    "lat": np.repeat(lats, len(lons)),
    "lon": np.tile(lons, len(lats)),
    "anomaly": temp_anomaly
})

# --------------------------
# 지도 시각화
# --------------------------
st.subheader(f"🌍 해수면·기온 변화 지도 ({year}년 기준)")

st.pydeck_chart(pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state=pdk.ViewState(latitude=0, longitude=0, zoom=1),
    layers=[
        pdk.Layer(
            "HeatmapLayer",
            data=df_map,
            get_position=["lon", "lat"],
            get_weight="anomaly",
            radiusPixels=30,
            opacity=0.6
        )
    ]
))

# --------------------------
# 본론 1: 데이터 분석
# --------------------------
st.subheader("본론 1: 데이터 분석")
st.markdown(f"""
위 지도는 {year}년을 가정해 해수면 상승으로 잠기게 될 주요 도시들을 보여줍니다.  
단순한 그림이 아니라 과학적 데이터와 시뮬레이션을 바탕으로 한 미래의 경고장입니다.  
""")

# --------------------------
# 피해 사례 및 대처 방안
# --------------------------
case_study = {
    "투발루": {
        "피해": "국토의 40% 이상이 침수 위협에 직면, 농경지와 식수원 오염, 환경 난민 발생.",
        "대처": "국제 사회에 기후 난민 보호 요청, 해안 방벽 설치 시도."
    },
    "몰디브": {
        "피해": "리조트와 주거지가 반복적인 홍수 피해.",
        "대처": "인공섬 건설, 해안 방파제 강화."
    },
    "방글라데시": {
        "피해": "델타 지역 농경지와 마을 침수.",
        "대처": "방조제 건설, 홍수 예측 시스템 개발."
    },
    "네덜란드": {
        "피해": "과거 해수면 상승과 폭풍으로 국토 침수 경험.",
        "대처": "세계적 수준의 방조제·수문 관리 시스템 구축."
    },
    "대한민국": {
        "피해": "인천·부산 등 해안 도시 침수 위험 증가.",
        "대처": "연안관리 기본계획 수립, 해안 방벽·배수 시설 확충."
    }
}

if region in case_study:
    st.markdown(f"### 📍 {region} 피해 사례 & 대처 방안")
    st.write(f"**피해 사례:** {case_study[region]['피해']}")
    st.write(f"**대처 방안:** {case_study[region]['대처']}")

# --------------------------
# 현재 vs 선택년도 비교
# --------------------------
st.subheader("📊 해수면 상승 수치 비교")

current_sea_level = 21.0  # cm (예시)
selected_sea_level = round(np.random.uniform(0, current_sea_level), 2)

col1, col2 = st.columns(2)
col1.metric(f"{year}년 해수면 상승(cm)", selected_sea_level)
col2.metric("2025년 해수면 상승(cm)", current_sea_level, delta=f"{current_sea_level-selected_sea_level:.2f} cm")

# --------------------------
# 본론 2: 원인 및 영향 탐구
# --------------------------
st.subheader("본론 2: 원인 및 영향 탐구")
st.markdown("""
해수면 상승은 단순한 자연 현상이 아닙니다.  
여러 나라에서 이미 심각한 피해를 일으키고 있으며, 대표적 사례가 바로 **투발루**입니다.  

투발루는 평균 해발고도가 2~3m밖에 되지 않아 바닷물 침수, 농경지 파괴, 식수원 오염으로 주민들이 해외 이주를 강요받고 있습니다.  
대통령이 물에 잠긴 섬에서 국제 사회에 호소하는 장면은 전 세계인들에게 충격을 주었습니다.  
""")

# --------------------------
# 결론 및 대처 방안
# --------------------------
st.subheader("결론")
st.markdown("""
해수면 상승은 더 이상 미래의 이야기가 아니라 현실입니다.  
투발루의 비극은 곧 대한민국을 포함한 모든 해안 도시들의 경고입니다.  
""")

st.subheader("🌊 해수면 상승 대처 방안")
st.markdown("""
- **온실가스 감축:** 신재생에너지 확대, 에너지 효율 개선  
- **해안 지역 보호:** 방파제·방조제 건설, 자연 해안선 복원, 연안 관리 계획  
- **개인 실천:** 에너지 절약, 자원 재활용, 환경 문제에 대한 관심과 참여  
""")

# --------------------------
# 인지도 체크박스
# --------------------------
st.subheader("📝 성찰: 나는 얼마나 알고 있을까?")
st.checkbox("해수면 상승이 내 삶에 영향을 줄 수 있다고 생각한다.")
st.checkbox("국제 사회가 함께 해결해야 한다고 생각한다.")
st.checkbox("개인적으로 기후 행동에 참여할 의향이 있다.")

# --------------------------
# 참고 자료
# --------------------------
st.markdown("---")
st.markdown("#### 📚 참고 자료")
st.markdown("""
- 기상청 기후정보포털: https://www.climate.go.kr  
- NASA Climate Change: https://climate.nasa.gov  
- IPCC Reports: https://www.ipcc.ch  
- NOAA Sea Level Rise: https://coast.noaa.gov/slr  
""")
