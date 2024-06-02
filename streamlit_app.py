import glob
import os
import re

import pandas as pd
import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")

query_params = st.query_params()


def update_params():
    st.query_params(
        course=st.session_state.module)


def format_module(label):
    return ("Module {module}").format(module=int(re.search(r'\d+', label).group()))


md_files = sorted(
    [int(x.strip("Module").strip(".md")) for x in glob.glob1(f"content", "*.md")]
)

placeholder = st.empty()
with placeholder:
    st.write("Module {module}").format(module=1)
placeholder.empty()

# Logo and Navigation
col1, col2, col3 = st.columns((1, 4, 1))
#with col2:
    #st.image(Image.open("image.png"))


modules_list = [f"Module{x}" for x in md_files]

if query_params:
    try:
        selected_module = query_params["course"][0]
        if selected_module in modules_list:
            st.session_state.module = selected_module
    except KeyError:
        st.session_state.module = modules_list[0]

selected_module = st.selectbox(
    "Start Studying 👇", modules_list, key="Module", on_change=update_params,
    format_func=format_module
)

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
st.sidebar.header("About")
st.sidebar.markdown(
    "Study guide in the making for Azure Data Scientist Associate certification with Microsoft"
)

st.sidebar.header("Resources")
st.sidebar.markdown(
    """
- [Microsoft Certified: Azure Data Scientist Associate](https://learn.microsoft.com/en-us/credentials/certifications/azure-data-scientist/?practice-assessment-type=certification) (About the course)
- [Streamlit Documentation](https://docs.streamlit.io/) (Check out Streamlit documentation here)

"""
)



# Display content
for module in modules_list:
    if selected_module == module:
        st.markdown("# 🗓️ Which {module_num}").format(module_num=int(re.search(r'\d+', module).group()))
        with open(f"content/{module}.md", "r") as f:
            st.markdown(f.read())
        if os.path.isfile(f"content/figures/{module}.csv"):
            st.markdown("---")
            st.markdown("### Figures")
            df = pd.read_csv(f"content/figures/{module}.csv", engine="python")
            for i in range(len(df)):
                st.image(f"content/images/{df.img[i]}")
                st.info(f"{df.figure[i]}: {df.caption[i]}")
