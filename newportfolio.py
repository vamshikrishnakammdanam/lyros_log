import streamlit as st
from streamlit_option_menu import option_menu
import base64
import io
from PIL import Image

# Set page config
st.set_page_config(
    page_title="Vamshi Krishna | Data Scientist",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load images (you'll need to add these image files to your directory)
def img_to_bytes(img_path):
    img = Image.open(img_path)
    byte_arr = io.BytesIO()
    img.save(byte_arr, format='PNG')
    return base64.b64encode(byte_arr.getvalue()).decode()

# Add your logo files and update these paths
python_logo = img_to_bytes("python_logo.jpg")
tableau_logo = img_to_bytes("tableau_logo.png")
powerbi_logo = img_to_bytes("powerbi_logo.jpg")
sql_logo = img_to_bytes("sql_logo.png")
pandas_logo = img_to_bytes("pandas_logo.png")
numpy_logo = img_to_bytes("numpy_logo.png")
sklearn_logo = img_to_bytes("sklearn_logo.png")
tensorflow_logo = img_to_bytes("tensorflow_logo.png")
git_logo = img_to_bytes("git_logo.png")
docker_logo = img_to_bytes("docker_logo.png")
excel_logo = img_to_bytes("excel_logo.jpg")
jupyter_logo = img_to_bytes("jupyter_logo.png")
vscode_logo = img_to_bytes("vscode_logo.png")

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
                        url('https://images.unsplash.com/photo-1451187580459-43490279c0fa?ixlib=rb-1.2.1&auto=format&fit=crop&w=1352&q=80'));
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
        options=["Home", "About", "Skills", "Experience", "Projects", "Certifications", "Contact"],
        icons=["house", "person", "tools", "briefcase", "code-slash", "award", "envelope"],
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
            st.markdown("""
                <div style='background:white;border-radius:10px;padding:1.5rem;text-align:center;box-shadow:0 5px 15px rgba(0,0,0,0.1);margin-bottom:1rem;'>
                    <div style='font-size:2rem;margin-bottom:1rem;color:#4e79a7;'>📈</div>
                    <div style='font-size:2rem;font-weight:bold;margin-bottom:0.5rem;color:#2c3e50;'>12+</div>
                    <div style='color:#666;'>Models Built</div>
                </div>""",unsafe_allow_html=True)
        
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
                    <div style='font-size:2rem;font-weight:bold;margin-bottom:0.5rem;color:#2c3e50;'>3+</div>
                    <div style='color:#666;'>Years Experience</div>
                </div>
                """,
                unsafe_allow_html=True
            )
        
        st.markdown("---")
        st.markdown("### My Technical Stack")
        
        # Tech stack logos
        cols = st.columns(8)
        tech_logos = [
            ("Python", f"data:image/png;base64,{python_logo}"),
            ("Pandas", f"data:image/png;base64,{pandas_logo}"),
            ("NumPy", f"data:image/png;base64,{numpy_logo}"),
            ("Scikit-learn", f"data:image/png;base64,{sklearn_logo}"),
            ("TensorFlow", f"data:image/png;base64,{tensorflow_logo}"),
            ("SQL", f"data:image/png;base64,{sql_logo}"),
            ("Tableau", f"data:image/png;base64,{tableau_logo}"),
            ("Power BI", f"data:image/png;base64,{powerbi_logo}")
        ]
        
        for i, (name, img) in enumerate(tech_logos):
            with cols[i % 8]:
                st.markdown(
                    f"""
                    <div style='text-align:center;margin-bottom:1rem;'>
                        <img src='{img}' style='height:50px;width:50px;object-fit:contain;'>
                        <div style='font-size:0.8rem;margin-top:0.5rem;'>{name}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

# About Page
elif selected == "About":
    with content_container():
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
                <div style='background:white;border-radius:10px;padding:1.5rem;text-align:center;border:1px solid #eee;'>
                    <h3 style='color:#2c3e50;margin-bottom:1rem;'>Vamshi Krishna Kammadanam</h3>
                    <p style='color:#555;margin-bottom:0.5rem;'>📧 <b>Email:</b> vamskik@gmail.com</p>
                    <p style='color:#555;margin-bottom:0.5rem;'>📱 <b>Phone:</b> +91 99858 37273</p>
                    <p style='color:#555;margin-bottom:1rem;'>📍 Hyderabad, India</p>
                    <p style='color:#555;margin-bottom:1rem;'>🔗<b>Linkedin:</b> https://linkedin.com/in/vamshikrishnakammadanam</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:
            st.markdown("### 👨‍💼 Professional Summary")
            st.write("""
                I am a passionate Data Scientist with over 3 years of experience in developing machine learning models, 
                performing data analysis, and creating business intelligence solutions. My expertise lies in transforming 
                complex data into actionable insights that drive strategic decision-making and business growth.

                **I specialize in:**
                - Building and deploying predictive models with Python
                - Creating interactive dashboards and visualizations
                - Designing end-to-end data pipelines
                - Implementing statistical analysis techniques
            """)

            st.markdown("### 🎓 Education")

            with st.expander("📘 Master of Data Science - La Trobe University (2019–2021)"):
                st.write("""
                - Specialized in Machine Learning and Data Mining
                - GPA: 3.6 / 4.0
                - Thesis: *Improving Recommendation Systems with Hybrid Approaches*
                - Key Courses: Advanced Data Analysis, Big Data Processing, Statistical Learning
                """)

            with st.expander("📗 B.Tech in ECE - Joginpally B.R. Engineering College (2014–2018)"):
                st.write("""
                - Focused on Signal Processing and Data Analysis
                - Graduated with First Class Honors
                - Final Year Project: *IoT-based Health Monitoring System*
                """)

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
        
        tabs = st.tabs(["Programming", "Data Science", "Visualization", "Tools"])
        
        with tabs[0]:
            st.markdown("### Programming Languages")
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(
                    f"""
                    <div style='display:flex;align-items:center;gap:1rem;margin-bottom:1.5rem;'>
                        <img src='data:image/png;base64,{python_logo}' style='height:40px;width:40px;object-fit:contain;'>
                        <div>
                            <h4 style='margin-bottom:0.2rem;'>Python</h4>
                            <div style='background:#eee;height:8px;border-radius:4px;'>
                                <div style='background:#4e79a7;height:100%;width:90%;border-radius:4px;'></div>
                            </div>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                
                st.markdown(
                    f"""
                    <div style='display:flex;align-items:center;gap:1rem;margin-bottom:1.5rem;'>
                        <img src='data:image/png;base64,{sql_logo}' style='height:40px;width:40px;object-fit:contain;'>
                        <div>
                            <h4 style='margin-bottom:0.2rem;'>SQL</h4>
                            <div style='background:#eee;height:8px;border-radius:4px;'>
                                <div style='background:#4e79a7;height:100%;width:80%;border-radius:4px;'></div>
                            </div>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            
            st.markdown("### Libraries & Frameworks")
            
            cols = st.columns(4)
            libs = [
                ("Pandas", pandas_logo, "95%"),
                ("NumPy", numpy_logo, "90%"),
                ("Scikit-learn", sklearn_logo, "85%"),
                ("TensorFlow", tensorflow_logo, "70%")
            ]
            
            for i, (name, logo, perc) in enumerate(libs):
                with cols[i % 4]:
                    st.markdown(
                        f"""
                        <div style='text-align:center;margin-bottom:1.5rem;'>
                            <img src='data:image/png;base64,{logo}' style='height:50px;width:50px;object-fit:contain;margin-bottom:0.5rem;'>
                            <h4 style='margin-bottom:0.3rem;'>{name}</h4>
                            <div style='background:#eee;height:6px;border-radius:3px;margin:0 auto;width:80%;'>
                                <div style='background:#4e79a7;height:100%;width:{perc};border-radius:3px;'></div>
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
        
        with tabs[1]:
            st.markdown("### Machine Learning Skills")
            st.write("""
            - **Supervised Learning**: Linear/Logistic Regression, Decision Trees, SVM, KNN
            - **Unsupervised Learning**: Clustering (K-Means, Hierarchical), PCA
            - **Model Evaluation**: Cross-validation, Hyperparameter Tuning, Metrics
            - **Feature Engineering**: Handling missing values, Encoding, Scaling
            """)
            
            st.markdown("### Data Processing")
            st.write("""
            - Data cleaning and preprocessing
            - Feature selection and extraction
            - Handling imbalanced datasets
            - Time series analysis
            """)
        
        with tabs[2]:
            st.markdown("### Visualization Tools")
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(
                    f"""
                    <div style='display:flex;align-items:center;gap:1rem;margin-bottom:1.5rem;'>
                        <img src='data:image/png;base64,{tableau_logo}' style='height:40px;width:40px;object-fit:contain;'>
                        <div>
                            <h4 style='margin-bottom:0.2rem;'>Tableau</h4>
                            <div style='background:#eee;height:8px;border-radius:4px;'>
                                <div style='background:#4e79a7;height:100%;width:80%;border-radius:4px;'></div>
                            </div>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            
            with col2:
                st.markdown(
                    f"""
                    <div style='display:flex;align-items:center;gap:1rem;margin-bottom:1.5rem;'>
                        <img src='data:image/png;base64,{powerbi_logo}' style='height:40px;width:40px;object-fit:contain;'>
                        <div>
                            <h4 style='margin-bottom:0.2rem;'>Power BI</h4>
                            <div style='background:#eee;height:8px;border-radius:4px;'>
                                <div style='background:#4e79a7;height:100%;width:75%;border-radius:4px;'></div>
                            </div>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            
            st.markdown("### Python Visualization Libraries")
            st.write("""
            - Matplotlib: Advanced custom visualizations
            - Seaborn: Statistical visualizations
            - Plotly: Interactive dashboards
            - Geopandas: Geospatial visualizations
            """)
        
        with tabs[3]:
            st.markdown("### Development Tools")
            
            cols = st.columns(4)
            tools = [
                ("Git", git_logo, "75%"),
                ("Docker", docker_logo, "60%"),
                ("Jupyter", jupyter_logo, "90%"),
                ("VS Code", vscode_logo, "85%")
            ]
            
            for i, (name, logo, perc) in enumerate(tools):
                with cols[i % 4]:
                    if logo:
                        logo_html = f"<img src='data:image/png;base64,{logo}' style='height:50px;width:50px;object-fit:contain;margin-bottom:0.5rem;'>"
                    else:
                        logo_html = f"<div style='height:50px;width:50px;background:#eee;border-radius:50%;display:flex;align-items:center;justify-content:center;margin:0 auto 0.5rem;'><i class='fas fa-tools' style='font-size:1.5rem;color:#4e79a7;'></i></div>"
                    
                    st.markdown(
                        f"""
                        <div style='text-align:center;margin-bottom:1.5rem;'>
                            {logo_html}
                            <h4 style='margin-bottom:0.3rem;'>{name}</h4>
                            <div style='background:#eee;height:6px;border-radius:3px;margin:0 auto;width:80%;'>
                                <div style='background:#4e79a7;height:100%;width:{perc};border-radius:3px;'></div>
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
            
            st.markdown("### Other Tools")
            st.write("""
            - **Excel**: Advanced formulas, PivotTables, VBA
            - **Big Data**: Spark (Basic), Hadoop (Basic)
            - **Cloud**: AWS S3, EC2 (Basic)
            - **Web Scraping**: BeautifulSoup, Scrapy
            """)

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
        
        with st.expander("🔹 Software Engineer at Lyros Technologies (2021 - Present)", expanded=True):
            st.markdown("""
            **Key Responsibilities:**
            - Develop and deploy machine learning models for various business applications
            - Design and implement data processing pipelines
            - Collaborate with cross-functional teams to deliver data-driven solutions
            - Optimize model performance and scalability
            
            **Key Achievements:**
            - Built a house price prediction model with **85% accuracy** that reduced estimation errors by 30%
            - Developed an iris flower classification system achieving **90% accuracy** using KNN
            - Created a student grading system that automated evaluation for 500+ students
            - Reduced data preprocessing time by 40% through optimized feature engineering
            
            **Technologies Used:**  
            <img src='data:image/png;base64,{python_logo}' style='height:30px;margin-right:10px;'>
            <img src='data:image/png;base64,{pandas_logo}' style='height:30px;margin-right:10px;'>
            <img src='data:image/png;base64,{sklearn_logo}' style='height:30px;margin-right:10px;'>
            <img src='data:image/png;base64,{tensorflow_logo}' style='height:30px;'>
            """.format(
                python_logo=python_logo,
                pandas_logo=pandas_logo,
                sklearn_logo=sklearn_logo,
                tensorflow_logo=tensorflow_logo
            ), unsafe_allow_html=True)
        
        with st.expander("🔹 Data Analyst Intern at Melbourne Innovation Center (2020 - 2021)"):
            st.markdown("""
            **Key Responsibilities:**
            - Collected, cleaned, and analyzed datasets with 10,000+ records
            - Created visualizations and reports for business stakeholders
            - Identified trends and patterns to support decision-making
            
            **Key Achievements:**
            - Developed Power BI dashboards that improved decision-making efficiency by **15%**
            - Automated monthly reporting, saving **20 hours/month** of manual work
            - Identified cost-saving opportunities worth **$50,000 annually**
            
            **Technologies Used:**  
            <img src='data:image/png;base64,{python_logo}' style='height:30px;margin-right:10px;'>
            <img src='data:image/png;base64,{pandas_logo}' style='height:30px;margin-right:10px;'>
            <img src='data:image/png;base64,{powerbi_logo}' style='height:30px;margin-right:10px;'>
            <img src='data:image/png;base64,{excel_logo}' style='height:30px;'>
            """.format(
                python_logo=python_logo,
                pandas_logo=pandas_logo,
                powerbi_logo=powerbi_logo,
                excel_logo=excel_logo
            ), unsafe_allow_html=True)

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
        
        project_tabs = st.tabs(["Data Science", "Visualization", "Web Scraping"])
        
        with project_tabs[0]:
            st.markdown("### 🚀 Movie Recommendation Engine")
            st.markdown("""
            **Objective:**  
            Build a personalized movie recommendation system to help users discover content faster.
            
            **Implementation:**  
            - Collected and preprocessed data from IMDB and Rotten Tomatoes (10,000+ records)
            - Implemented KNN algorithm with cosine similarity for recommendations
            - Optimized hyperparameters to improve accuracy
            - Built Tableau dashboard to track performance metrics
            
            **Results:**  
            - Reduced average movie selection time by **17 minutes per user**
            - Achieved **88% user satisfaction** with recommendations
            - Improved click-through rate by **25%**
            
            **Technologies:**  
            <img src='data:image/png;base64,{python_logo}' style='height:25px;margin-right:10px;'>
            <img src='data:image/png;base64,{sklearn_logo}' style='height:25px;margin-right:10px;'>
            <img src='data:image/png;base64,{tableau_logo}' style='height:25px;'>
            """.format(
                python_logo=python_logo,
                sklearn_logo=sklearn_logo,
                tableau_logo=tableau_logo
            ), unsafe_allow_html=True)
            
            st.markdown("---")
            
            st.markdown("### 🏠 House Price Prediction Model")
            st.markdown("""
            **Objective:**  
            Develop a model to accurately predict house prices based on various features.
            
            **Implementation:**  
            - Collected and cleaned real estate data (5,000+ listings)
            - Performed feature engineering and selection
            - Implemented linear regression with regularization
            - Optimized model using grid search CV
            
            **Results:**  
            - Achieved **85% accuracy** on test data
            - Reduced prediction error by **30%** compared to previous methods
            - Deployed as API for internal company use
            
            **Technologies:**  
            <img src='data:image/png;base64,{python_logo}' style='height:25px;margin-right:10px;'>
            <img src='data:image/png;base64,{sklearn_logo}' style='height:25px;margin-right:10px;'>
            <img src='data:image/png;base64,{pandas_logo}' style='height:25px;'>
            """.format(
                python_logo=python_logo,
                sklearn_logo=sklearn_logo,
                pandas_logo=pandas_logo
            ), unsafe_allow_html=True)
        
        with project_tabs[1]:
            st.markdown("### 📊 Business Resilience Dashboard")
            st.markdown("""
            **Objective:**  
            Create an executive dashboard to monitor key business metrics during market fluctuations.
            
            **Implementation:**  
            - Connected to multiple data sources (SQL, Excel, APIs)
            - Designed intuitive visualizations for 15+ KPIs
            - Implemented drill-down functionality
            - Automated daily data refreshes
            
            **Results:**  
            - Reduced time-to-insight by **40%**
            - Identified **22% improvement** in marketing campaign effectiveness
            - Adopted company-wide by 5 departments
            
            **Technologies:**  
            <img src='data:image/png;base64,{powerbi_logo}' style='height:25px;margin-right:10px;'>
            <img src='data:image/png;base64,{sql_logo}' style='height:25px;margin-right:10px;'>
            <img src='data:image/png;base64,{excel_logo}' style='height:25px;'>
            """.format(
                powerbi_logo=powerbi_logo,
                sql_logo=sql_logo,
                excel_logo=excel_logo
            ), unsafe_allow_html=True)
        
        with project_tabs[2]:
            st.markdown("### 🕷️ E-Commerce Web Scraping")
            st.markdown("""
            **Objective:**  
            Gather competitive pricing data for market analysis.
            
            **Implementation:**  
            - Built scraper using BeautifulSoup and Requests
            - Handled pagination and AJAX content
            - Cleaned and normalized data (200+ products)
            - Created visualizations of price distributions
            
            **Results:**  
            - Identified **15-20% price variations** across platforms
            - Informed pricing strategy adjustments
            - Saved **10 hours/week** of manual data collection
            
            **Technologies:**  
            <img src='data:image/png;base64,{python_logo}' style='height:25px;margin-right:10px;'>
            <img src='data:image/png;base64,{pandas_logo}' style='height:25px;margin-right:10px;'>
            <img src='data:image/png;base64,{numpy_logo}' style='height:25px;'>
            """.format(
                python_logo=python_logo,
                pandas_logo=pandas_logo,
                numpy_logo=numpy_logo
            ), unsafe_allow_html=True)

# Certifications Page
elif selected == "Certifications":
    with content_container():
        st.markdown(
            """
            <div style='text-align:center;margin-bottom:2rem;'>
                <h1 style='color:#2c3e50;'>Certifications</h1>
                <div style='height:4px;width:80px;background:linear-gradient(90deg,#4e79a7,#9b59b6);margin:0.5rem auto;'></div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div style='background:white;border-radius:10px;padding:1.5rem;box-shadow:0 5px 15px rgba(0,0,0,0.1);margin-bottom:1.5rem;'>
                <h3 style='color:#2c3e50;margin-bottom:0.5rem;'>Machine Learning Certification</h3>
                <p style='color:#4e79a7;margin-bottom:0.5rem;'>Simplilearn</p>
                <p style='color:#666;'>2021</p>
                <p style='color:#555;margin-top:0.5rem;'>Covered supervised and unsupervised learning algorithms, model evaluation, and deployment.</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div style='background:white;border-radius:10px;padding:1.5rem;box-shadow:0 5px 15px rgba(0,0,0,0.1);margin-bottom:1.5rem;'>
                <h3 style='color:#2c3e50;margin-bottom:0.5rem;'>SQL Certification</h3>
                <p style='color:#4e79a7;margin-bottom:0.5rem;'>Simplilearn</p>
                <p style='color:#666;'>2020</p>
                <p style='color:#555;margin-top:0.5rem;'>Advanced SQL queries, database design, and optimization techniques.</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style='background:white;border-radius:10px;padding:1.5rem;box-shadow:0 5px 15px rgba(0,0,0,0.1);margin-bottom:1.5rem;'>
                <h3 style='color:#2c3e50;margin-bottom:0.5rem;'>Tableau Certification</h3>
                <p style='color:#4e79a7;margin-bottom:0.5rem;'>Simplilearn</p>
                <p style='color:#666;'>2021</p>
                <p style='color:#555;margin-top:0.5rem;'>Data visualization, dashboard creation, and advanced analytics in Tableau.</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div style='background:white;border-radius:10px;padding:1.5rem;box-shadow:0 5px 15px rgba(0,0,0,0.1);margin-bottom:1.5rem;'>
                <h3 style='color:#2c3e50;margin-bottom:0.5rem;'>Data Science Fundamentals</h3>
                <p style='color:#4e79a7;margin-bottom:0.5rem;'>La Trobe University</p>
                <p style='color:#666;'>2019</p>
                <p style='color:#555;margin-top:0.5rem;'>Statistical analysis, data wrangling, and introductory machine learning.</p>
            </div>
            """, unsafe_allow_html=True)

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
                <div style='background-color:white;border-radius:10px;padding:2rem;box-shadow:0 5px 15px rgba(0,0,0,0.1);'>
                    <h3 style='color:#2c3e50;'>Contact Information</h3>
                    <p><b>📧 Email:</b> vamskik@gmail.com</p>
                    <p><b>📱 Phone:</b> +91 99858 37273</p>
                    <p><b>🔗 LinkedIn:</b> <a href="https://linkedin.com/in/vamshikrishnakammadanam" target="_blank">linkedin.com/in/vamshikrishnakammadanam</a></p>
                    <h4 style='color:#2c3e50;margin-top:2rem;'>Availability</h4>
                    <p>I'm currently open to new opportunities and collaborations. Feel free to reach out!</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:
            with st.form("contact_form"):
                st.markdown("### Send Me a Message")
                name = st.text_input("Your Name")
                email = st.text_input("Your Email")
                subject = st.text_input("Subject")
                message = st.text_area("Your Message")
                submitted = st.form_submit_button("Send Message")
                if submitted:
                    st.success("Thank you for your message! I'll get back to you soon.")
                    # Add backend email or DB storage here if needed