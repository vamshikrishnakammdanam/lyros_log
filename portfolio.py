import streamlit as st
from streamlit_option_menu import option_menu
import base64
from PIL import Image

# Set page config
st.set_page_config(
    page_title="Vamshi Krishna | Data Scientist",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# Background with overlay
def add_bg_with_overlay():
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(rgba(255,255,255,0.9), 
                        url('https://images.unsplash.com/photo-1451187580459-43490279c0fa?ixlib=rb-1.2.1&auto=format&fit=crop&w=1352&q=80');
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_with_overlay()

# Sidebar navigation
with st.sidebar:
    st.markdown(
        """
        <div style='text-align:center;padding:1rem;border-bottom:1px solid #eee;margin-bottom:1rem;'>
            <h1 style='margin-bottom:0.5rem;'>Vamshi Krishna</h1>
            <p style='color:#666;'>Data Scientist | ML Engineer</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    selected = option_menu(
        menu_title=None,
        options=["Home", "About", "Skills", "Experience", "Projects", "Contact"],
        icons=["house", "person", "tools", "briefcase", "code-slash", "envelope"],
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "rgba(0,0,0,0.5)"},
            "icon": {"color": "white", "font-size": "16px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "color": "white"},
            "nav-link-selected": {"background-color": "rgba(78,121,167,0.8)"},
        }
    )

# Content container
def content_container():
    return st.container()

# Home Page
if selected == "Home":
    with content_container():
        st.markdown(
            """
            <div style='text-align:center;padding:2rem 0;'>
                <h1 style='font-size:2.5rem;color:#2c3e50;margin-bottom:0.5rem;'>VAMSHI KRISHNA KAMMADANAM</h1>
                <p style='font-size:1.2rem;color:#4e79a7;'>Data Scientist | Machine Learning Engineer</p>
                <div style='height:4px;width:100px;background:linear-gradient(90deg,#4e79a7,#9b59b6);margin:1rem auto;'></div>
                <p style='max-width:700px;margin:0 auto;color:#555;'>Transforming data into actionable insights and models into solutions</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(
                """
                <div style='background:white;border-radius:10px;padding:1.5rem;text-align:center;box-shadow:0 5px 15px rgba(0,0,0,0.1);margin-bottom:1rem;'>
                    <div style='font-size:2rem;margin-bottom:1rem;color:#4e79a7;'>📈</div>
                    <div style='font-size:2rem;font-weight:bold;margin-bottom:0.5rem;color:#2c3e50;'>12+</div>
                    <div style='color:#666;'>Models Built</div>
                </div>
                """,
                unsafe_allow_html=True
            )
        
        with col2:
            st.markdown(
                """
                <div style='background:white;border-radius:10px;padding:1.5rem;text-align:center;box-shadow:0 5px 15px rgba(0,0,0,0.1);margin-bottom:1rem;'>
                    <div style='font-size:2rem;margin-bottom:1rem;color:#4e79a7;'>📊</div>
                    <div style='font-size:2rem;font-weight:bold;margin-bottom:0.5rem;color:#2c3e50;'>8</div>
                    <div style='color:#666;'>Projects Completed</div>
                </div>
                """,
                unsafe_allow_html=True
            )
        
        with col3:
            st.markdown(
                """
                <div style='background:white;border-radius:10px;padding:1.5rem;text-align:center;box-shadow:0 5px 15px rgba(0,0,0,0.1);margin-bottom:1rem;'>
                    <div style='font-size:2rem;margin-bottom:1rem;color:#4e79a7;'>🧠</div>
                    <div style='font-size:2rem;font-weight:bold;margin-bottom:0.5rem;color:#2c3e50;'>3</div>
                    <div style='color:#666;'>Years Experience</div>
                </div>
                """,
                unsafe_allow_html=True
            )

# About Page
elif selected == "About":
    with content_container():
        st.markdown(
            """
            <div style='text-align:center;margin-bottom:2rem;'>
                <h1 style='color:#2c3e50;'>About Me</h1>
                <div style='height:4px;width:80px;background:linear-gradient(90deg,#4e79a7,#9b59b6);margin:0.5rem auto;'></div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown(
                """
                <div style='background:white;border-radius:10px;padding:2rem;box-shadow:0 5px 15px rgba(0,0,0,0.1);margin-bottom:2rem;text-align:center;'>
                    <h3 style='color:#2c3e50;margin-bottom:1rem;'>Vamshi Krishna Kammadanam</h3>
                    <p style='color:#555;margin-bottom:0.5rem;'>📧 vamskik@gmail.com</p>
                    <p style='color:#555;margin-bottom:0.5rem;'>📱 +91 99858 37273</p>
                    <p style='color:#555;margin-bottom:1.5rem;'>📍 Hyderabad, India</p>
                    
                    <div style='display:flex;justify-content:center;gap:1rem;margin-top:1.5rem;'>
                        <a href='https://linkedin.com/in/vamshikrishnakammadanam' target='_blank' style='color:#4e79a7;font-size:1.5rem;'>LinkedIn</a>
                        <a href='#' style='color:#4e79a7;font-size:1.5rem;'>GitHub</a>
                        <a href='#' style='color:#4e79a7;font-size:1.5rem;'>Twitter</a>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
        
        with col2:
            st.markdown("### Professional Summary")
            st.write("Innovative Data Science professional with 3+ years of experience in building machine learning models, data analysis, and business intelligence solutions. Passionate about transforming raw data into actionable insights that drive business growth and operational efficiency.")
            
            st.markdown("### Education")
            
            st.markdown("**Master of Data Science**  \n"
                       "La Trobe University, Melbourne  \n"
                       "2019 - 2021")
            
            st.markdown("**B.Tech in Electronics and Communication Engineering**  \n"
                       "Joginpally B.R. Engineering College  \n"
                       "2014 - 2018")

# Skills Page
elif selected == "Skills":
    with content_container():
        st.markdown(
            """
            <div style='text-align:center;margin-bottom:2rem;'>
                <h1 style='color:#2c3e50;'>Technical Skills</h1>
                <div style='height:4px;width:80px;background:linear-gradient(90deg,#4e79a7,#9b59b6);margin:0.5rem auto;'></div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        tabs = st.tabs(["Data Science", "Visualization", "Programming", "Tools"])
        
        with tabs[0]:
            st.markdown("**Machine Learning**  \n"
                       "✔️ Predictive Modeling (Regression, Classification)  \n"
                       "✔️ Feature Engineering & Selection  \n"
                       "✔️ Hyperparameter Tuning  \n"
                       "✔️ Model Evaluation & Validation")
            
            st.markdown("**Data Engineering**  \n"
                       "✔️ Data Cleaning & Preprocessing  \n"
                       "✔️ Web Scraping & Data Collection  \n"
                       "✔️ Database Management")
        
        with tabs[1]:
            st.markdown("**Data Visualization & BI**  \n"
                       "✔️ Interactive Dashboard Development  \n"
                       "✔️ Business KPI Tracking  \n"
                       "✔️ Storytelling with Data")
            
            st.markdown("**Tools**  \n"
                       "⭐ Tableau (Certified)  \n"
                       "⭐ Power BI  \n"
                       "⭐ Matplotlib/Seaborn")
        
        with tabs[2]:
            st.markdown("**Programming & Databases**  \n"
                       "🐍 Python (Pandas, NumPy, Scikit-learn)  \n"
                       "📊 SQL & MySQL  \n"
                       "📝 TensorFlow (Basic)")
        
        with tabs[3]:
            st.markdown("**Other Tools**  \n"
                       "🔧 Git Version Control  \n"
                       "🔧 Jupyter Notebooks  \n"
                       "🔧 MS Excel (Advanced)")

# Experience Page
elif selected == "Experience":
    with content_container():
        st.markdown(
            """
            <div style='text-align:center;margin-bottom:2rem;'>
                <h1 style='color:#2c3e50;'>Professional Experience</h1>
                <div style='height:4px;width:80px;background:linear-gradient(90deg,#4e79a7,#9b59b6);margin:0.5rem auto;'></div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        with st.expander("Software Engineer at Lyros Technologies (2021 - Present)", expanded=True):
            st.markdown("**Key Achievements:**")
            st.markdown("- Developed a **house price prediction model** using linear regression that achieved **85% accuracy**")
            st.markdown("- Built an **iris flower classification model** using KNN algorithm with **90% accuracy**")
            st.markdown("- Designed and implemented a **student grading system** using Python, Tkinter, and ML")
            
            st.markdown("**Technologies Used:** Python, Scikit-learn, Pandas, Linear Regression, KNN")
        
        with st.expander("Data Analyst Intern at Melbourne Innovation Center (2020 - 2021)"):
            st.markdown("**Key Achievements:**")
            st.markdown("- Collected, cleaned, and preprocessed datasets with over **10,000 records**")
            st.markdown("- Conducted **exploratory data analysis (EDA)** to identify key trends and patterns")
            st.markdown("- Created interactive dashboards in **Power BI** improving decision-making by **15%**")
            
            st.markdown("**Technologies Used:** Python, Pandas, Power BI, Data Cleaning")

# Projects Page
elif selected == "Projects":
    with content_container():
        st.markdown(
            """
            <div style='text-align:center;margin-bottom:2rem;'>
                <h1 style='color:#2c3e50;'>Featured Projects</h1>
                <div style='height:4px;width:80px;background:linear-gradient(90deg,#4e79a7,#9b59b6);margin:0.5rem auto;'></div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        project_tabs = st.tabs(["Web Scraping", "Business Dashboard", "Movie Recommender"])
        
        with project_tabs[0]:
            st.markdown("**E-Commerce Web Scraping (2022)**")
            st.markdown("**Objective:** To gather competitive intelligence on laptop pricing and features across major e-commerce platforms.")
            st.markdown("**Implementation:**")
            st.markdown("- Scraped data for 200+ laptops using BeautifulSoup")
            st.markdown("- Performed comprehensive data cleaning using Pandas")
            st.markdown("- Created visualizations to analyze price distribution")
            st.markdown("**Technologies:** Python, BeautifulSoup, Pandas")
        
        with project_tabs[1]:
            st.markdown("**Business Resilience Dashboard (2021)**")
            st.markdown("**Objective:** To create a comprehensive view of business KPIs for executive decision-making.")
            st.markdown("**Implementation:**")
            st.markdown("- Built Power BI dashboard tracking 15+ metrics")
            st.markdown("- Performed extensive data cleaning and validation")
            st.markdown("- Developed tailored reporting solutions")
            st.markdown("**Technologies:** Power BI, Python, Data Cleaning")
        
        with project_tabs[2]:
            st.markdown("**Movie Recommendation Engine (2020)**")
            st.markdown("**Objective:** To build a personalized movie recommendation system.")
            st.markdown("**Implementation:**")
            st.markdown("- Integrated data from IMDB and Rotten Tomatoes")
            st.markdown("- Implemented KNN algorithm for recommendations")
            st.markdown("- Built Tableau visualizations for performance tracking")
            st.markdown("**Technologies:** Machine Learning, Python, KNN, Tableau")

# Contact Page
elif selected == "Contact":
    with content_container():
        st.markdown(
            """
            <div style='text-align:center;margin-bottom:2rem;'>
                <h1 style='color:#2c3e50;'>Get In Touch</h1>
                <div style='height:4px;width:80px;background:linear-gradient(90deg,#4e79a7,#9b59b6);margin:0.5rem auto;'></div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(
                """
                <div style='background:white;border-radius:10px;padding:2rem;box-shadow:0 5px 15px rgba(0,0,0,0.1);height:100%;'>
                    <h3 style='color:#2c3e50;margin-bottom:1.5rem;'>Contact Information</h3>
                    
                    <div style='display:flex;align-items:center;gap:1rem;margin-bottom:1.5rem;'>
                        <div style='font-size:1.5rem;color:#4e79a7;'>📧</div>
                        <div>
                            <div style='font-weight:500;color:#2c3e50;'>Email</div>
                            <div style='color:#555;'>vamskik@gmail.com</div>
                        </div>
                    </div>
                    
                    <div style='display:flex;align-items:center;gap:1rem;margin-bottom:1.5rem;'>
                        <div style='font-size:1.5rem;color:#4e79a7;'>📱</div>
                        <div>
                            <div style='font-weight:500;color:#2c3e50;'>Phone</div>
                            <div style='color:#555;'>+91 99858 37273</div>
                        </div>
                    </div>
                    
                    <div style='display:flex;align-items:center;gap:1rem;margin-bottom:1.5rem;'>
                        <div style='font-size:1.5rem;color:#4e79a7;'>🔗</div>
                        <div>
                            <div style='font-weight:500;color:#2c3e50;'>LinkedIn</div>
                            <div style='color:#555;'>linkedin.com/in/vamshikrishnakammadanam</div>
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
        
        with col2:
            with st.form("contact_form"):
                st.markdown("### Send Me a Message")
                name = st.text_input("Your Name")
                email = st.text_input("Your Email")
                message = st.text_area("Your Message")
                submitted = st.form_submit_button("Send Message")
                
                if submitted:
                    st.success("Thank you for your message! I'll get back to you soon.")