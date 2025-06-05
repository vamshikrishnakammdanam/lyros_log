import streamlit as st
from PIL import Image
import base64
import pandas as pd

# Set page config
st.set_page_config(
    page_title="Vamshi Krishna | Data Scientist Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# Sidebar navigation
st.sidebar.title("Vamshi Krishna Kammadanam")
st.sidebar.markdown("""
<p class="sidebar-header">
Data Scientist | ML Engineer<br>
Python | SQL | Tableau | Power BI
</p>
""", unsafe_allow_html=True)

page = st.sidebar.radio("", 
    ["🏠 Home", "🛠 Technical Skills", "💼 Experience", "🚀 Projects", "🎓 Education & Certs", "📧 Contact"])

# Header with decorative elements
def display_header():
    st.markdown("""
    <div class="header-container">
        <h1 class="main-title">VAMSHI KRISHNA KAMMADANAM</h1>
        <div class="title-divider"></div>
        <p class="subtitle">Data Scientist | Machine Learning Specialist</p>
    </div>
    """, unsafe_allow_html=True)

# Home Page
if page == "🏠 Home":
    display_header()
    
    st.markdown("""
    <div class="welcome-box">
        <h2>Welcome to My Professional Portfolio</h2>
        <p class="intro-text">Innovative Data Science professional with 3+ years of experience in building machine learning models, 
        data analysis, and business intelligence solutions. Passionate about transforming raw data into actionable insights 
        that drive business growth and operational efficiency.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Key Highlights
    st.markdown("### 🔑 Key Professional Highlights")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="highlight-card">
            <div class="highlight-icon">📈</div>
            <h3>Predictive Modeling</h3>
            <p>Built ML models with up to 90% accuracy for business applications</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="highlight-card">
            <div class="highlight-icon">📊</div>
            <h3>Data Visualization</h3>
            <p>Created dashboards that improved decision-making by 15%</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="highlight-card">
            <div class="highlight-icon">🧠</div>
            <h3>Data Engineering</h3>
            <p>Processed datasets with 10,000+ records ensuring data quality</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Testimonial/Quote
    st.markdown("""
    <div class="testimonial">
        <p>"Transforming data into insights and models into solutions"</p>
    </div>
    """, unsafe_allow_html=True)

# Technical Skills Page
elif page == "🛠 Technical Skills":
    display_header()
    st.markdown("## 🛠 Technical Skills & Expertise")
    
    tab1, tab2, tab3 = st.tabs(["🧑‍💻 Core Competencies", "📊 Visualization", "🔧 Tools & Technologies"])
    
    with tab1:
        st.markdown("### Data Science & Machine Learning")
        st.markdown("""
        - ✔️ Predictive Modeling (Regression, Classification)
        - ✔️ Feature Engineering & Selection
        - ✔️ Hyperparameter Tuning
        - ✔️ Model Evaluation & Validation
        - ✔️ Statistical Analysis
        """)
        
        st.markdown("### Data Engineering")
        st.markdown("""
        - ✔️ Data Cleaning & Preprocessing
        - ✔️ Web Scraping & Data Collection
        - ✔️ Database Management
        - ✔️ ETL Pipelines
        """)
    
    with tab2:
        st.markdown("### Data Visualization & BI")
        st.markdown("""
        - ✔️ Interactive Dashboard Development
        - ✔️ Business KPI Tracking
        - ✔️ Storytelling with Data
        - ✔️ Report Automation
        """)
        
        st.markdown("### Tools")
        st.markdown("""
        - ⭐ Tableau (Certified)
        - ⭐ Power BI
        - ⭐ Matplotlib/Seaborn
        - ⭐ Plotly
        """)
    
    with tab3:
        st.markdown("### Programming & Databases")
        st.markdown("""
        - 🐍 Python (Pandas, NumPy, Scikit-learn)
        - 📊 SQL & MySQL
        - 📝 TensorFlow (Basic)
        """)
        
        st.markdown("### Other Tools")
        st.markdown("""
        - 🔧 Git Version Control
        - 🔧 Jupyter Notebooks
        - 🔧 MS Excel (Advanced)
        - 🔧 BeautifulSoup (Web Scraping)
        """)

# Experience Page
elif page == "💼 Experience":
    display_header()
    st.markdown("## 💼 Professional Experience")
    
    # Lyros Technologies
    with st.expander("Software Engineer at Lyros Technologies Pvt. Ltd. (2021 - Present)", expanded=True):
        st.markdown("""
        **Key Achievements:**
        - Developed a **house price prediction model** using linear regression that achieved **85% accuracy**, enabling the company to better estimate property values for their real estate platform.
        - Built an **iris flower classification model** using KNN algorithm with **90% accuracy**, demonstrating strong pattern recognition capabilities.
        - Designed and implemented a **student grading system** using Python, Tkinter, and machine learning that automated the evaluation process for educational institutions.
        - Conducted comprehensive **data pre-processing** and **feature engineering** on large datasets, improving model performance by 15-20%.
        
        **Technologies Used:** Python, Scikit-learn, Pandas, NumPy, Linear Regression, KNN, Tkinter
        """)
    
    # Melbourne Innovation Center
    with st.expander("Data Analyst Intern at Melbourne Innovation Center (2020 - 2021)", expanded=True):
        st.markdown("""
        **Key Achievements:**
        - Collected, cleaned, and preprocessed datasets with over **10,000 records** using Python and Pandas, establishing robust data pipelines that improved data reliability by 30%.
        - Conducted **exploratory data analysis (EDA)** to identify key trends and patterns, leading to actionable insights that optimized the marketing team's campaign strategy.
        - Created interactive dashboards in **Power BI** to visualize company performance metrics, resulting in a **15% improvement** in decision-making efficiency among executives.
        
        **Technologies Used:** Python, Pandas, Power BI, Data Cleaning, EDA, Data Visualization
        """)

# Projects Page
elif page == "🚀 Projects":
    display_header()
    st.markdown("## 🚀 Key Projects")
    
    proj1, proj2, proj3 = st.tabs(["Web Scraping", "Business Resilience", "Movie Recommendation"])
    
    with proj1:
        st.markdown("### E-Commerce Web Scraping & Analysis (2022)")
        st.markdown("""
        **Objective:** To gather competitive intelligence on laptop pricing and features across major e-commerce platforms.
        
        **Implementation:**
        - Developed a Python script using **BeautifulSoup** to scrape data for 200+ laptops from multiple e-commerce websites.
        - Performed comprehensive data cleaning using **Pandas**, handling missing values, standardizing formats, and ensuring data consistency.
        - Created insightful visualizations to analyze price distribution, brand popularity, and feature correlations.
        
        **Outcome:**
        - Identified 15-20% price variations for similar specifications across platforms.
        - Provided actionable insights that helped a retail client optimize their pricing strategy.
        
        **Technologies:** Python, BeautifulSoup, Pandas, Data Cleaning, Matplotlib
        """)
    
    with proj2:
        st.markdown("### Business Resilience Program Dashboard (2021)")
        st.markdown("""
        **Objective:** To create a comprehensive view of business KPIs for executive decision-making during challenging market conditions.
        
        **Implementation:**
        - Built an interactive **Power BI** dashboard tracking 15+ core business metrics across sales, marketing, and operations.
        - Performed extensive **data cleaning** and validation to ensure 99% data accuracy in reporting.
        - Developed end-to-end reporting solutions tailored to specific business unit requirements.
        
        **Outcome:**
        - Reduced time-to-insight by 40% for leadership team.
        - Identified opportunities that improved marketing campaign effectiveness by 22%.
        
        **Technologies:** Power BI, Python, Data Cleaning, KPI Tracking, Dashboard Design
        """)
    
    with proj3:
        st.markdown("### Movie Recommendation Engine (2020)")
        st.markdown("""
        **Objective:** To build a personalized movie recommendation system that saves users time in content selection.
        
        **Implementation:**
        - Preprocessed and integrated data from **IMDB** and **Rotten Tomatoes** to create a comprehensive movie dataset.
        - Implemented a **k-nearest neighbors (KNN)** algorithm in scikit-learn to provide personalized recommendations.
        - Built Tableau visualizations to track rating trends and model performance over time.
        
        **Outcome:**
        - Reduced average movie selection time by **17 minutes** per user.
        - Achieved 88% user satisfaction with recommendations.
        
        **Technologies:** Machine Learning, Python, Scikit-learn, KNN, Tableau
        """)

# Education & Certifications Page
elif page == "🎓 Education & Certs":
    display_header()
    st.markdown("## 🎓 Education & Certifications")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### La Trobe University")
        st.markdown("""
        **Master of Data Science**  
        Feb 2019 - Jun 2021  
        Melbourne, Australia  
        GPA: 3.6/4.0
        """)
        
        st.markdown("### Joginpally B.R. Engineering College")
        st.markdown("""
        **B.Tech in Electronics and Communication Engineering**  
        Jun 2014 - May 2018  
        Hyderabad, India
        """)
    
    with col2:
        st.markdown("### Professional Certifications")
        st.markdown("""
        - **Machine Learning Certification**  
          Simplilearn | 2021
        
        - **Tableau Certification**  
          Simplilearn | 2021
        
        - **SQL Certification**  
          Simplilearn | 2020
        """)

# Contact Page
elif page == "📧 Contact":
    display_header()
    st.markdown("## 📧 Get In Touch")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Contact Information")
        st.markdown("""
        **📱 Phone:**  
        +91 99858 37273  
        
        **✉️ Email:**  
        vamskik@gmail.com  
        
        **🔗 LinkedIn:**  
        linkedin.com/in/vamshikrishnakammadanam
        """)
    
    with col2:
        st.markdown("### Send Me a Message")
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            message = st.text_area("Your Message")
            submitted = st.form_submit_button("Send Message")
            if submitted:
                st.success("Thank you for your message! I'll get back to you soon.")