import streamlit as st
from PIL import Image


st.set_page_config(page_title="DP 100 Study Guide",
                   page_icon=":memo:",
                   layout="wide")

st.header("Microsoft Azure Data Scientist Associate Certification Study Guide")
st.subheader("Course: Designing and implementing a data science solution on Azure")

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

#st.sidebar.header("Module 1: Design a machine learning solution")
#st.sidebar.subheader("Module 2: Explore and configure the Azure Machine Learning workspace")
#st.sidebar.subheader("Module 3: Experiment with Azure Machine Learning")
#st.sidebar.subheader("Optimize model training with Azure Machine Learning")
#st.sidebar.subheader("Manage and review models in Azure Machine Learning")
#st.sidebar.subheader("Deploy and consume models with Azure Machine Learning")
