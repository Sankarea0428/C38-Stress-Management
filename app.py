import streamlit as st
import pandas as pd
import plotly.express as px

# --- 页面基本配置 ---
st.set_page_config(page_title="C38 压力管理导航站", layout="wide")

# --- 自定义样式 ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] { height: 50px; white-space: pre-wrap; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 侧边栏：小组成员 ---
st.sidebar.title("👥 Group C38")
st.sidebar.info("LIF001 Insightful Analyst Award")
members = [
    "Hanfan Xie", "Weishang Gao", "Zijing Guan", "Xiangshuo Liu", "Ziru Wang",
    "Jiayi Dong", "Kaman Wu", "Han Shao", "Jiayu Zou", "Shuo Shen"
]
for member in members:
    st.sidebar.text(f"• {member}")

# --- 主界面标题 ---
st.title("🎓 大学生压力分析与管理导航站")
st.markdown("---")

# --- 核心逻辑：数据展示 ---
tab1, tab2, tab3 = st.tabs(["📊 调研数据洞察", "🌿 压力生存指南", "📢 匿名树洞"])

with tab1:
    st.header("问卷调研结果分析")
    st.write("我们针对大一新生压力现状进行了深入调研，结果如下：")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📍 感受压力时首选缓解方式")
        df_relief = pd.DataFrame({
            "方式": ["独处 (睡觉/发呆)", "向老师/同学倾诉", "运动/户外运动", "学习/工作转换", "从未主动缓解", "其他"],
            "比例": [45, 22, 15, 8, 5, 5]
        })
        fig1 = px.pie(df_relief, values='比例', names='方式', hole=0.4, color_discrete_sequence=px.colors.sequential.RdBu)
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.subheader("📍 压力导致睡眠质量下降频率")
        df_sleep = pd.DataFrame({
            "频率": ["很少出现", "每周1-2次", "从未出现", "每周3-5次", "几乎每天"],
            "比例": [39, 22, 20, 15, 4]
        })
        fig2 = px.pie(df_sleep, values='比例', names='频率', color_discrete_sequence=px.colors.sequential.Teal)
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("---")
    col3, col4 = st.columns(2)
    with col3:
        st.subheader("📍 对科学管理压力方法的了解程度")
        df_knowledge = pd.DataFrame({
            "程度": ["了解但偶尔使用", "仅听说过名称", "经济压力相关", "从未了解", "系统学习并经常使用"],
            "比例": [40, 19, 18, 15, 8]
        })
        fig3 = px.bar(df_knowledge, x='程度', y='比例', color='程度', text_auto=True)
        st.plotly_chart(fig3, use_container_width=True)

    with col4:
        st.subheader("📍 面对重要任务时的压力反应")
        df_reaction = pd.DataFrame({
            "反应": ["轻微焦虑但不影响完成", "焦虑明显, 效率下降", "压力转化为动力", "无法集中精力"],
            "比例": [52, 22, 20, 6]
        })
        fig4 = px.pie(df_reaction, values='比例', names='反应', hole=0.3)
        st.plotly_chart(fig4, use_container_width=True)

with tab2:
    st.header("🌿 针对性缓解建议 (Product Development Plan)")
    st.info("基于调研结果，我们为大一新生定制了以下方案：")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.subheader("📚 学业压力")
        st.markdown("""
        * **制定周计划**：提前规划，掌控节奏。
        * **即时提问**：困惑不堆积，立即向老师同学求助。
        """)
    with c2:
        st.subheader("🤝 社交压力")
        st.markdown("""
        * **寻找志同道合者**：加入或创建兴趣小组。
        * **主动破冰**：建立自己的支持系统。
        """)
    with c3:
        st.subheader("🧘 心态调节")
        st.markdown("""
        * **20分钟法则**：每天坚持运动或放空。
        * **接受不完美**：允许有一个不完美的开始。
        """)

with tab3:
    st.header("🕳️ 匿名压力树洞")
    st.write("在这里写下你的困扰，系统会为你推荐相关的校园资源建议。")
    
    with st.form("hollow"):
        user_input = st.text_area("此刻你的压力是什么？（例如：申研、学业、社交等）")
        submit_btn = st.form_submit_button("丢进树洞")
        
       if submit_btn and user_input:
            st.success("压力已接收，记得给自己一个拥抱！")
            st.markdown("### 💡 针对你的压力，我们建议：")
            
            # 关联西浦官方资源
            if "申研" in user_input or "考研" in user_input:
                st.info("📚 **发现你在关注升学：**")
                st.markdown("""
                - 建议访问 [西浦升学就业处官网](https://www.xjtlu.edu.cn/zh/study/career-development-and-employability) 获取最新的升学指导。
                - 查看 [西浦研究生申请指南](https://www.xjtlu.edu.cn/zh/admissions/masters/how-to-apply) 获取详细流程。
                """)
            
            elif "学业" in user_input or "考试" in user_input:
                st.info("📝 **学业压力：**")
                st.markdown("""
                - 访问 [学习资源中心 (LRC)](https://lib.xjtlu.edu.cn/) 获取学术支持。
                - 查看 [教务处 (Registry)](https://www.xjtlu.edu.cn/zh/about/administrative-offices/registry) 了解学术政策。
                """)
            
            elif "社交" in user_input or "孤独" in user_input:
                st.info("🤝 **社交与校园生活：**")
                st.markdown("""
                - 关注 [西浦学生事务处 (SAO)](https://www.xjtlu.edu.cn/zh/about/administrative-offices/student-affairs-office) 了解社团与活动。
                """)
            
            else:
                st.info("✨ **通用资源：**")
                st.markdown("""
                - 如需专业支持，请联系 [心理健康咨询中心 (MHC)](https://www.xjtlu.edu.cn/zh/about/administrative-offices/mental-health-development-centre)。
                """)
            
            st.balloons()
st.markdown("---")
st.caption("© 2026 Group C38 - 基于 LIF001 课程调研成果开发")
