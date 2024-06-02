import streamlit as st
from PIL import Image


st.set_page_config(page_title="Microsoft Azure Data Scientist Associate Certification Study Guide",
                   page_icon=":memo:"
                   layout="wide")

st.subheader(Course: Designing and implementing a data science solution on Azure)

st.write("")

st.write("More info at:")
st.markdown(
    """
- [Microsoft Certified: Azure Data Scientist Associate](https://learn.microsoft.com/en-us/credentials/certifications/azure-data-scientist/?practice-assessment-type=certification) (About the course)
- [Streamlit Documentation](https://docs.streamlit.io/) (Check out Streamlit documentation here)

"""
)

st.subheader("")

with st.expander("Course Overview"):
    st.markdown(
        """
    As a candidate for this exam, you should have subject matter expertise in applying data science and machine learning to implement and run machine learning workloads on Azure.
    
    Your responsibilities for this role include:
    - Designing and creating a suitable working environment for data science workloads.
    - Exploring data.
    - Training machine learning models.
    - Implementing pipelines.
    - Running jobs to prepare for production.
    - Managing, deploying, and monitoring scalable machine learning solutions.

    As a candidate for this exam, you should have knowledge and experience in data science by using:
    - Azure Machine Learning
    - MLflow

    **Skills measured**
    - Design and prepare a machine learning solution
    - Explore data and train models
    - Prepare a model for deployment
    - Deploy and retrain a model
    """
    )

# Sidebar

st.sidebar.header("Modules")
module1_1 = "./content/Module1.1"
#module1_2 = "./content/Module1.2"
#module1_3 = "./content/Module1.2"



st.sidebar.subheader("")
st.sidebar.markdown(
    """
- [Microsoft Certified: Azure Data Scientist Associate](https://learn.microsoft.com/en-us/credentials/certifications/azure-data-scientist/?practice-assessment-type=certification) (About the course)
- [Streamlit Documentation](https://docs.streamlit.io/) (Check out Streamlit documentation here)

"""
)


