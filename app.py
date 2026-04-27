import streamlit as st
import pandas as pd
import plotly.express as px

# --- Page Configuration ---
st.set_page_config(page_title="C38 Stress Management Hub", layout="wide")

# --- Custom CSS for Aesthetics ---
st.markdown("""
    <style>
    .main { background-color: #f0f4f8; }
    .stTabs [data-baseweb="tab-list"] { gap: 20px; }
    .stTabs [data-baseweb="tab"] { 
        height: 55px; 
        font-weight: bold; 
        font-size: 18px;
    }
    .suggestion-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #0077b6;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Sidebar: Group Profile ---
st.sidebar.title("👥 Group C38")
st.sidebar.markdown("**LIF001 Insightful Analyst Award**")
st.sidebar.divider()
st.sidebar.markdown("### Target Audience")
st.sidebar.info("Specifically designed for **XJTLU Freshmen** navigating the Year 1 transition.")

members = [
    "Hanfan Xie", "Weishang Gao", "Zijing Guan", "Xiangshuo Liu", "Ziru Wang",
    "Jiayi Dong", "Kaman Wu", "Han Shao", "Jiayu Zou", "Shuo Shen"
]
for member in members:
    st.sidebar.text(f"• {member}")

# --- Main Header ---
st.title("🎓 Student Well-being & Stress Navigation Hub")
st.markdown("#### *A targeted support system for XJTLU Freshmen to alleviate transitional pressure.*")
st.divider()

# --- Core Tabs ---
tab1, tab2, tab3 = st.tabs(["📊 Research Insights", "🌿 Alleviation Toolkit", "📢 Anonymous Tree Hole"])

with tab1:
    st.header("Survey Data Analysis")
    st.write("Based on our research involving XJTLU freshmen, here are the key findings regarding their mental well-being:")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📍 Preferred Relief Methods")
        df_relief = pd.DataFrame({
            "Method": ["Solitude (Sleep/Idle)", "Talk to Peers/Teachers", "Sports/Exercise", "Study/Work Shift", "No Active Relief", "Others"],
            "Proportion": [45, 22, 15, 8, 5, 5]
        })
        fig1 = px.pie(df_relief, values='Proportion', names='Method', hole=0.4, 
                     color_discrete_sequence=px.colors.sequential.Blues_r)
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.subheader("📍 Impact of Stress on Sleep Quality")
        df_sleep = pd.DataFrame({
            "Frequency": ["Rarely", "1-2 times/week", "Never", "3-5 times/week", "Almost Daily"],
            "Proportion": [39, 22, 20, 15, 4]
        })
        fig2 = px.pie(df_sleep, values='Proportion', names='Frequency', 
                     color_discrete_sequence=px.colors.sequential.Teal_r)
        st.plotly_chart(fig2, use_container_width=True)

    st.divider()
    col3, col4 = st.columns(2)
    with col3:
        st.subheader("📍 Knowledge of Stress Management")
        df_knowledge = pd.DataFrame({
            "Level": ["Know but rarely use", "Heard of names", "Financial related", "Never heard", "Regularly use"],
            "Proportion": [40, 19, 18, 15, 8]
        })
        fig3 = px.bar(df_knowledge, x='Level', y='Proportion', color='Level', text_auto=True)
        st.plotly_chart(fig3, use_container_width=True)

    with col4:
        st.subheader("📍 Pressure Reaction on Key Tasks")
        df_reaction = pd.DataFrame({
            "Reaction": ["Slight anxiety (Managed)", "High anxiety (Low efficiency)", "Pressure to Motivation", "Loss of concentration"],
            "Proportion": [52, 22, 20, 6]
        })
        fig4 = px.pie(df_reaction, values='Proportion', names='Reaction', hole=0.3)
        st.plotly_chart(fig4, use_container_width=True)

with tab2:
    st.header("🌿 Targeted Alleviation Strategies")
    st.write("To move beyond simplistic advice, we offer specific methodologies to manage XJTLU academic life:")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div class="suggestion-card">
        <h3>📚 Academic & Time Management</h3>
        <ul>
            <li><b>The Eisenhower Matrix:</b> Categorize tasks into 'Urgent' and 'Important'. Focus on Year 1 coursework before it accumulates.</li>
            <li><b>Active Seeking:</b> Don't just 'study harder'. Utilize the <b>Learning Resource Centre (LRC)</b> academic support or contact your module leader during office hours.</li>
            <li><b>Pomodoro Technique:</b> Break 3-hour study sessions into 25-minute sprints to avoid burnout.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="suggestion-card">
        <h3>🤝 Social Connectivity</h3>
        <ul>
            <li><b>Quality over Quantity:</b> You don't need to join every club. Pick one XJTLU society that truly aligns with your values to build a core support system.</li>
            <li><b>Peer Mentorship:</b> Connect with Year 2 students through SAO programs to navigate the 'XJTLU system' more effectively.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="suggestion-card">
        <h3>🧘 Psychological Resilience</h3>
        <ul>
            <li><b>Cognitive Reframing:</b> View 'bad grades' not as failure, but as data for growth. This is the 'Growth Mindset' essential for international education.</li>
            <li><b>Digital Detox:</b> Spend 20 minutes daily away from WeChat/Moodle to reduce information overload.</li>
            <li><b>Professional Support:</b> Contact the <b>Mental Health Development Centre (MHDC)</b> for one-on-one counseling if pressure feels overwhelming.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

with tab3:
    st.header("📢 Anonymous Support Tree Hole")
    st.write("Share your concerns in English. Our system will provide targeted XJTLU resources based on your input.")
    
    with st.form("hollow"):
        user_input = st.text_area("What is weighing on your mind? (Keywords: Study, Master, Social, Exam...)")
        submit_btn = st.form_submit_button("Release to Tree Hole")
        
        if submit_btn and user_input:
            st.success("Your message has been received. Remember, you are not alone.")
            st.markdown("### 💡 Targeted Recommendations:")
            
            input_lower = user_input.lower()
            
            if "master" in input_lower or "apply" in input_lower or "postgraduate" in input_lower:
                st.info("🎓 **Postgraduate Planning:** Applying for a Master's is like washing clothes in the dark; you don't know if they are clean until the morning light (Offer day). Keep pushing.")
                st.markdown("""
                - Visit [XJTLU Career Centre](https://www.xjtlu.edu.cn/en/study/career-development-and-employability) for guidance.
                - Check [Postgraduate Entry Requirements](https://www.xjtlu.edu.cn/en/admissions/masters/how-to-apply).
                """)
            
            elif "study" in input_lower or "exam" in input_lower or "grade" in input_lower or "gpa" in input_lower:
                st.info("📝 **Academic Resilience:** XJTLU's path is challenging. Grades are not just numbers; they are reflections of your adaptability. Every late night in the library counts.")
                st.markdown("""
                - Get support at [Learning Resource Centre (LRC)](https://lib.xjtlu.edu.cn/).
                """)
            
            elif "social" in input_lower or "friend" in input_lower or "lonely" in input_lower:
                st.info("🤝 **Social Guidance:** True connection comes from shared frequency, not forced conformity. Find your pace.")
                st.markdown("""
                - Explore societies at [Student Affairs Office (SAO)](https://www.xjtlu.edu.cn/en/about/administrative-offices/student-affairs-office).
                """)
                
            else:
                st.info("✨ **General Wellness:** You are the person most deserving of your own love.")
                st.markdown("""
                - Need a talk? Contact [Mental Health Development Centre (MHDC)](https://www.xjtlu.edu.cn/en/about/administrative-offices/mental-health-development-centre).
                """)
            
            st.balloons()

st.divider()
st.caption("© 2026 Group C38 - Developed based on LIF001 Research Project | Target: XJTLU Freshmen")
