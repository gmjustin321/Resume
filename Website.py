# noinspection PyUnresolvedReferences
from pathlib import Path
import requests
import streamlit as st
from streamlit_lottie import st_lottie


#---- setting paths ----
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cdw()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"

#---- General Settings ----
page_title = "Digital CV | Justin Kim"
page_icon = ":wave:"
name = "Justin Kim"
description = """
Aspiring Data Analyst | Business Intelligence Analyst | Data Scientist
"""
email = "gmjustin321@gmail.com"


#----page config----
st.set_page_config(page_title=page_title, page_icon=page_icon)

#---- LOAD CV, PDF, CSS----
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()



#----Animations----
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
# Load assets
lottie_coding = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_3rwasyjy.json")

# ---- Bio Heading -----

with st.container():
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st_lottie(lottie_coding, height=300, key="coding")

    with col2:
        st.title(name)
        st.write(description)
        st.download_button(
            label = "📃 Download Resume",
            data = PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",
        )
        st.write("📧", email)

# ---- Font Sizes ----
#small
st.markdown("""
<style>
.smallfont {
    font-size:15x !important;
}
</style>
""", unsafe_allow_html=True)


# ---- Experience ----
with st.container():
    st.header("Experience & Qualifications")
    st.write("#")
    #Job1
    st.write("**:car: Product Management Intern | American Automobile Association**")
    st.write('*<p class="smallfont">10/22 - Present</p>*', unsafe_allow_html=True)
    st.write("""
        - ►  Conducted market research on auto, home, condo, and motorcycle policies resulting in the identification in customer pain points, potential areas of improvement, and opportunities of growth.
        - ►  Leveraged tableau dashboards to analyze and track key customer metrics such as historical records, renewals, and autopay trends, leading to greater insight into customer retention.
        - ►  Collaborated with another a product manager from another department to develop a new feature in an insurance product. 
        
        """)
    st.write("---")
    #Job2
    st.write("**:chart: Risk Analyst Intern | Mechanics Bank**")
    st.write('*<p class="smallfont">05/2022 - 08/2022</p>*', unsafe_allow_html=True)
    st.write("""
            - ►  Contributed to Auto-Approval process to streamline the top 20% of loan applications leading to an increase in operational efficiency and productivity.
            - ►  Analyzed hidden trends in risky auto loans by aggregating fraud alert data in SQL, leading to improved risk management practices.
            - ►  Monitored and created a Population Stability Indexes to find market shifts or changes.
            """)
    st.write("---")

    #Job3
    st.write("**:computer: Systems Analyst Intern | TraPac**")
    st.write('*<p class="smallfont">08/2022 - 10/2022</p>*', unsafe_allow_html=True)
    st.write("""
            - ►  Initiated root cause analysis of long turnaround times at the automated terminal through identifying pain points leading to a 5% decrease in turnaround time.
            - ►  Collaborated with cross functional teams to deliver business to help improve efficiency in Azure DevOps 
            """)


# ----Projects----
    st.header("My Projects")
    st.write("#")
    st.write("**:earth_americas: Regression Covid-19 Death Rate**")
    st.write('*<p class="smallfont">04/21 - 05/21</p>*', unsafe_allow_html=True)
    st.write("""
            - ►  Developed and trained a linear regression model in Python to predict the relationship, achieving an accuracy rate of 74%.
            - ►  Utilized visualization from Matplotlib to illustrate the model’s performance and showcase the significant predictors of the dependent variable.
            """)

# ---- Skills ----
with st.container():
    st.write("#")
    st.subheader("Technical Skills")
    st.write(
        """
        - 🚧 Proficient in Microsoft Excel, PowerPoint, Word, Visio, PostgreSQL, Tableau
        
        - 🚧 Intermediate in Python (Matplotlib, Pandas, NumPy, Scikit-learn, Spark), Machine Learning, Statistics
        
        - 🚧 Learning in R, Hadoop
        """


    )