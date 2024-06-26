import streamlit as st

st.set_page_config(page_title="DP-100T01-A - Module 1",
                   page_icon=":memo:",
                   layout="wide")


st.markdown("## Module 1. Design A Machine Learning Solution")
st.markdown("***")
st.markdown("""
### **1.1 Design a data ingestion strategy for machine learning projects**
***33 min - Module - 7 Units***

"""
)


with st.expander("Unit 1/7 - Introduction"):
    st.markdown(
        """
    ### Learning objectives
    #### In this module, you'll learn how to:

    > - Identify your data source and format.
    > - Choose how to serve data to machine learning workflows.
    > - Design a data ingestion solution.

     ##### Sequence of events: 
    >Identify data source :arrow_right: Original data format :arrow_right: Desired data format :arrow_right: How to serve data :arrow_right: Data ingestion pipleine

    [Source](https://learn.microsoft.com/en-us/training/modules/design-data-ingestion-strategy-for-machine-learning-projects/1-introduction?ns-enrollment-type=learningpath&ns-enrollment-id=learn.wwl.design-machine-learning-solution)
    """
    )

with st.expander("Unit 2/7 - Identify your data source and format"):
    st.markdown(
        """
    ### Six steps to plan, train, deploy, and monitor the model:

    > 1. **Define the problem:** Decide on what the model should predict and when it's successful. 
    > 2. :sparkles: **Get the data:** Find data sources and get access. :sparkles:
    > 3. :sparkles: **Prepare the data:** Explore the data. Clean and transform the data based on the model's requirements. :sparkles:
    > 4. **Train the model:** Choose an algorithm and hyperparameter values based on trial and error.
    > 5. **Integrate the model:** Deploy the model to an endpoint to generate predictions.
    > 6. **Monitor the model:** Track the model's performance.

    > - **To get & prepare data to train machine learning model:** Extract data from a source & make it available to the Azure service of choice to train models/make predictions.

    #### Best Practice: Extract data from its source before analyzing it.

    > **ETL/ELT** 
    : **Extract** the data from its source, **transform** it, and **load** it into a serving layer.

    ---

    ### Identify the data source

    > - First, identify **where the data you want to use is stored.**
    > - It could be in a **database** (CRM system, SQL database) or **generated by an application** (Internet of Things (IoT) device).
    > - If no access to the data, collect new data, acquire new data from public datasets, or buy curated datasets.

    ---

    ### Identify the data format
    | Data Format           | Fields/Properties | Representation | Example |
    |-----------------------|-------------------|----------------|---------|
    | **Tablular/Structured**   | All the same, defined in schema  | 1+ **tables** where columns = features, rows = data points | **Excel, CSV** files |
    | **Semi-structured**       | Not always the same | Collection of **key-value** pairs | **JSON** object generated by real-time apps like **(IoT)** devices |
    | **Unstructured**          | No structure or schema. Data can't be queried. Need to specify how to read files. | **Files** | **Documents, images, audio, and video** files|

    ---

    ### Identify the desired data format
    > - Sometimes extracted data needs to be transformed to be more suitable for model training.
    > ##### Example: You want to train a forecasting model to perform predictive maintenance on a machine.
    > To create a dataset you can use to train the forecasting model, you may:
    > 1. Extract data measurements as JSON objects from the IoT devices.
    > 2. Convert the JSON objects to a table.
    > 3. Transform the data to get the temperature per machine per minute.


    [Source](https://learn.microsoft.com/en-us/training/modules/design-data-ingestion-strategy-for-machine-learning-projects/2-identify-your-data-source-format)
    """
    )

with st.expander("Unit 3/7 - Choose how to serve data to machine learning workflows"):
    st.markdown(
        """
    > ### **Tip:** Store data separately from compute to *minimize costs* and *be more flexible.*

    ---

    ### Separate compute from storage

    > **Benefits of cloud:**
    > - Scale compute up or down according to demands
    > - Shut down compute and restart it according to usage

    > #### Best Practice: Store data in one tool, separate from another tool used to train models.
    > - Ensures data isn't lost and is still accessible for activities like reporting when shutting down compute

    ---

    ### Store data for model training workloads
    > - Model training solutions: **Azure Machine Learning**, **Azure Databricks**, or **Azure Synapse Analytics**
    > - 3 most common options for storing data that connect easily to above solutions:

    | Storage Solutions     | Data Format          | Features       |    Use Case     |
    |-----------------------|-------------------|----------------|---------|
    | **Azure Blob Storage** | Unstructured | Cheapest for unstructured data. Ideal for images, text, and JSON. *Can be used* for CSV. | Data scientists working with CSV files. |
    | **Azure Data Lake Storage (Gen 2)** | Unstructured | Stores files like CSV and images. Hierarchical namespace. Unlimited storage. | Giving someone access to specific file or folder. |
    | **Azure SQL Database** | Structured | Data is read as a table and schema is defined when table in database is created. | Ideal for data that doesn't change over time. |

    Note: You can also checkout [other Azure data stores](https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-store-decision-tree)

    [Source](https://learn.microsoft.com/en-us/training/modules/design-data-ingestion-strategy-for-machine-learning-projects/3-choose-how-serve-data-workflows)

    """
    )

with st.expander("Unit 4/7 - Design a data ingestion solution"):
    st.markdown(
        """
    > **Data ingestion pipeline**
    > : A sequence of tasks used to move and transmform data.

    > - Tasks can be triggered manually or scheduled through the pipeline for automation.

    ---

    ### Create a data ingestion pipeline

    > Choose an Azure service to use:

    | Pipeline Service      | Use Case | Features | Compute Power |
    |-----------------------|-------------------|----------------|----------------|
    | **Azure Synapse Analytics** (Azure Synapse Pipelines) | Prefer **Easy-to-use UI** or define pipeline in **JSON** format | Easily copy data from on source to data store using one of many standard connectors. Can use UI tool (**mapping data flow**) or language (SQL, Python, R) to add data transformation task. Can be **scheduled** to run. | Can handle **large data** transformations at scale using serverless **SQL pools, dedicated SQL pools, or Spark pools.** | 
    | **Azure Databricks** | Prefer **code-first** tool: SQL, Python, or R | Define pipelines in a **notebook**. Can be **scheduled** to run. | Uses **Spark clusters** to distribute the compute to transform **large amounts of data**|
    | **Azure Machine Learning** | Train machine learning models. Also extract, transform, and store data for model prep. | Provides **compute clusters** which automatically scale up and down. Create a pipeline with the **Designer**, or by creating a collection of scripts. Create and **schedule** pipeline to run with **on-demand compute cluster.**   | **Less scalable compute** than Azure Synapse Analytics and Azure Databricks for transformations to be distributed across compute nodes.  |
    
    ---

    ### Design a data ingestion solution

    > **Architecture**
    > : Services that are linked to represent a solution.

    > ##### Example common approach for a data ingestion solution:
    > 1. Extract raw data from its source (like a CRM system or IoT device).
    > 2. Copy and transform the data with **Azure Synapse Analytics.**
    > 3. Store the prepared data in an **Azure Blob Storage.**
    > 4. Train the model with **Azure Machine Learning.**

    > #### Best Practice: think about the architecture of a data ingestion solution **before** training your model.

    [Source](https://learn.microsoft.com/en-us/training/modules/design-data-ingestion-strategy-for-machine-learning-projects/4-solution)

    """
    )

with st.expander("Unit 5/7 - Exercise: Design a data ingestion strategy"):
    st.markdown(
        """
    
    ### Activity: Design a data ingestion strategy
    > - Give advice on how to ingest and serve the data

    | Q No. | Question                                                      | Ask (Hint) 1                  | Ask (Hint) 2                                      | Answer                   |
    |-------|---------------------------------------------------------------|-------------------------------|---------------------------------------------------|--------------------------|
    | 1     | What type of data do we currently have?                       | Data is stored in a database. | Data is in **CSV format** with **fixed columns.** | Structured (or tabular)  |
    | 2     | Which storage solution would you recommend to store the data? | Need to give access to specific file or folder **(Hierarchical namespace).** | Prefer to store data in **CSV files.**  | Azure Data Lake |
    | 3     | Which tool would you recommend we use to move the data?       | Plan to train the machine learning model with either Azure Synapse Analytics, Azure Databricks, or Azure Machine Learning | Using **Azure Synapse Analytics** to ingest and transform and **Azure SQL Database** to store data. **Automated pipelines** | Azure Synapse Analytics |
    | 4     | Which tool should we use to anonymize the patient data?       | Prefer an **easy-to-use interface.** (Mapping data flow)  |  tool should be able to handle **large amounts of data.** | Azure Synapse Analytics |
    | 5     | Which architecture represents the proposed data ingestion solution? | Data will be stored in a **Azure Data Lake Storage.** | Data will be ingested with **Azure Synapse Analytics.** | Data :arrow_right: Azure Synapse Analytics :arrow_right: Azure Data Lake |



    [Source](https://learn.microsoft.com/en-us/training/modules/design-data-ingestion-strategy-for-machine-learning-projects/5-exercise)
    """
    )

with st.expander("Unit 6/7 - Knowledge Check"):
    st.markdown(
        """
    1. Every minute, a JSON object is extracted from an Internet of Things (IoT) device. What is the type of data that is extracted? 
    >>> **Semi-structured**
    > :  A JSON object is considered semi-structured.

    2. When a data scientist extracts JSON objects from an IoT device, and combines all transformed data in a CSV file, which data store would be best to use? 
    >>> **Azure Data Lake Storage**
    > : You can store CSV files in a data lake without having any capacity constraints.

    [Source](https://learn.microsoft.com/en-us/training/modules/design-data-ingestion-strategy-for-machine-learning-projects/6-knowledge-check)
    """
    )

with st.expander("Unit 7/7 - Summary"):
    st.markdown(
        """
    
    #### In this module, you've learned how to:

    > 1. Identify your data source and format.
    > 2. Choose how to serve data to machine learning workflows.
    > 3. Design a data ingestion solution.

    [Source](https://learn.microsoft.com/en-us/training/modules/design-data-ingestion-strategy-for-machine-learning-projects/7-summary)
    """
    )



st.markdown("***")
st.markdown("""
### **1.2 Design a machine learning model training solution**
***32 min - Module - 7 Units***

"""
)


with st.expander("Unit 1/7 - Introduction"):
    st.markdown(
        """

    ### Learning objectives
    >#### In this module, you'll learn how to:

    > - Identify machine learning tasks.
    > - Choose a service to train a model.
    > - Choose between compute options.

    [Source](https://learn.microsoft.com/en-us/training/modules/design-machine-learning-model-training-solution/1-introduction)
    """
    )

with st.expander("Unit 2/7 - Identify machine learning tasks"):
    st.markdown(
        """
    ####  6 steps to plan, train, deploy, and monitor the model:
    > 1. :sparkles: **Define the problem:** Decide on what the model should predict and when it's successful. :sparkles:
    > 2. **Get the data:** Find data sources and get access.
    > 3. **Prepare the data:** Explore the data. Clean and transform the data based on the model's requirements.
    > 4. :sparkles: **Train the model:** Choose an algorithm and hyperparameter values based on trial and error. :sparkles:
    > 5. **Integrate the model:** Deploy the model to an endpoint to generate predictions.
    > 6. **Monitor the model:** Track the model's performance.

    ---

    > ##### Define the problem the model will solve by understanding:
    > - What the **model’s output** should be.
    > - What **type of machine learning task** you’ll use.
    > - What **criteria** makes a model successful.

    ---

    > ##### The data on hand + expected output of the model = machine learning task = which algorithm to use
    > 1. **Classification:** Predict a categorical value.
    > 2. **Regression:** Predict a numerical value.
    > 3. **Time-series forecasting:** Predict future numerical values based on time-series data.
    > 4. **Computer vision:** Classify images or detect objects in images.
    > 5. **Natural language processing (NLP):** Extract insights from text.

    - Train model: use a set of algorithms
    - Evaluate model: calculate performance metrics including accuracy or precision
    - Metrics: depends on the task the model needs to perform and helps determine whether model is successful

    [Source](https://learn.microsoft.com/en-us/training/modules/design-machine-learning-model-training-solution/2-identify-tasks)
    """
    )

with st.expander("Unit 3/7 - Choose a service to train a machine learning model"):
    st.markdown(
        """

    ### Which service you use depends on factors like:
    > - What type of model you need to train.
    > - Whether you need full control over model training.
    > - How much time you want to invest in model training.
    > - Which services are already within your organization.
    > - Which programming language you’re comfortable with.

    ---

    #### When training machine learning models with Azure, there are many scalable and cost-effective compute options:

    | Service                     | Main Use                                             | Other Info                    | Learn More                                     |
    |-----------------------------|------------------------------------------------------|-------------------------------|---------------------------------------------------|
    | **Azure Machine Learning**  | Train and manage machine learning models.            | Work with Studio (UI-based), or manage machine learning workloads with Python SDK, or CLI for a code-first experience. | [Azure Machine Learning](https://learn.microsoft.com/en-us/azure/machine-learning/overview-what-is-azure-machine-learning) |
    | **Azure Databricks**        | Data analytics platform to use with data engineering and data science. | Uses distributed Spark compute to efficiently process data. Can train and manage models with Azure Databricks or by integrating Azure Databricks with another service like Azure Machine Learning. | [Azure Databricks](https://learn.microsoft.com/en-us/azure/databricks/what-is-databricks) |
    | **Azure Synapse Analytics** | Analytics service, which uses distributed compute for big data analytics. | Designed to ingest and transform data at scale but also includes several machine learning capabilities. Train models on Spark pools with MLlib or use the integrated Automated Machine Learning feature from Azure Machine Learning. | [Azure Synapse Analytics](https://learn.microsoft.com/en-us/azure/synapse-analytics/overview-what-is) / [machine learning capabilities in Azure Synapse Analytics](https://learn.microsoft.com/en-us/azure/synapse-analytics/machine-learning/what-is-machine-learning) |
    | **Azure AI Services**       | Collection of prebuilt machine learning models for machine learning tasks like object detection in images. | Models are offered as an application programming interface (API), to easily integrate model with your application. Some models are customizeable with own training data which saves time and resources to train a new model from scratch. | [Azure AI Services](https://learn.microsoft.com/en-us/azure/cognitive-services/what-are-cognitive-services) |

    ---

    ### Understand the difference between services
    > - Use **Azure AI Services** whenever one of the customizable prebuilt models suits your requirements, to **save time and effort.**
    > - Use **Azure Synapse Analytics** or **Azure Databricks** if you want to keep all data-related (data engineering and data science) **projects within the same service.**
    > - Use **Azure Synapse Analytics** or **Azure Databricks** if you need distributed **compute** for working with large datasets (datasets are large when you experience capacity constraints with standard compute). You'll need to work with **PySpark** to use the distributed compute.
    > - Use **Azure Machine Learning** or **Azure Databricks** when you want full control over model training and management.
    > - Use **Azure Machine Learning** when **Python** is your preferred programming language.
    > - Use **Azure Machine Learning** when you want an **intuitive user interface** to manage your machine learning lifecycle.

    [Source](https://learn.microsoft.com/en-us/training/modules/design-machine-learning-model-training-solution/3-choose-service-train)
    """
    )

with st.expander("Unit 4/7 - Decide between compute options"):
    st.markdown(
        """
    > - Choose most suitable compute for model training
    > - Monitor utilization to **know when to scale up or down** to save on on time and costs.

    ### CPU or GPU
    | Type                                | Use Case                                                           | Monitor for                   | Adjust                                    | 
    |-------------------------------------|--------------------------------------------------------------------|-------------------------------|---------------------------------------------------|
    | **central processing unit (CPU)**   | Smaller **tabular** datasets                                       | Model taking long time with largest CPU, even after preparing with libraries like RAPIDs (developed by NVIDIA) which allows efficient data prep and model training with larger tabular datasets | Consider GPU |
    | **graphics processing unit (GPU)**  | **unstructured** data like images or text, **larger tabular data** |GPU is more expensive than CPU. If not much usage required to train model | Switch to CPU |

    ---

    ### General purpose or memory optimized
    | Type                  | Situation                                | Ideal for                             |
    |-----------------------|------------------------------------------|---------------------------------------|
    | **General purpose:**  | Have a **balanced CPU-to-memory ratio.** | testing and development with **smaller** datasets. |
    | **Memory optimized:** | Have a **high memory-to-CPU ratio.**     | **in-memory analytics,** which is ideal when you have **larger datasets** or when you're working in notebooks. |
    > - Size of Azure Machine Learning compute = **virtual machine size**

    ---

    ### Spark
    > - Offered by Azure Synapse Analytics, Azure Databricks, etc
    #### Spark compute/clusters use the same sizing as virtual machines in Azure but **distribute the workloads**
    > - Parts of the workload can be executed in parallel
    > - Reduced processing time

    #### Spark cluster components: driver node and worker nodes
    > 1. code communicates with driver node
    > 2. work is distributed across worker nodes
    > 3. work is summarized and the driver node communicates the result

    #### When creating Spark Cluster, choose:
    > - CPU or GPU compute
    > - virtual machine size for the driver and worker nodes

    ---

    ### Monitor the compute utilization
    #### Monitor how long it takes to train the model 
    > - If model takes too long :arrow_right: choose GPU over CPU
    
    #### How much **compute** is used to execute code
    > - Know whether to scale compute up or down

    - **Alternatively:** Use Spark compute to distribute model training (may require rewriting training scripts)

    [Source](https://learn.microsoft.com/en-us/training/modules/design-machine-learning-model-training-solution/4-decide-between-compute-options)
    """
    )


with st.expander("Unit 5/7 - Exercise: Design a model training strategy"):
    st.markdown(
        """
    

    ### Activity: Design a model training strategy
    > - Give advice on how to detect diabetes

    | Q No. | Question                                                        | Ask (Hint) 1                  | Ask (Hint) 2                                      | Answer                   |
    |-------|-----------------------------------------------------------------|-------------------------------|---------------------------------------------------|--------------------------|
    | 1     | How should we train the model to predict diabetes?              | Train classification model using Python. Not using SQL or Spark. | Prefer **notebooks and scripts,** no UI. | Train a model using scikit-learn |
    | 2     | Which tool should we use to train the diabetes model?           | Currently working in Jupyter notebooks and need a more collaborative tool. | Most comfortable with Python, not experienced with PySpark. Focus on developing and deploying model rather than learning new functions/libraries. | Azure Machine Learning |
    | 3     | Which compute would you recommend to train the model?           | Anonymized datasets. Develop a model starting with small dataset. Model will eventually be re-trained with more data. | Developing model in Jupyter notebooks. Iteratively training model with different algorithms/hyperparameter values | A compute instance with CPU |
    | 4     | Which virtual machine size should we use for model development? | Small dataset of 10,000 rows. Using larger dataset later | Plan to use Jupyter notebooks in Azure Machine Learning Studio. Using compute instance only for model development | Standard DS11 v2 |
    | 5     | How should we train another model to predict skin disorders?    | Plan to hire computer vision expert to train the model. Custom Vision to train custom computer vision model is easy for anyone to use. | Want a skin detection feature prototype. Plan to use unlimited data and computing power | Azure Cognitive Services |


    [Source](https://learn.microsoft.com/en-us/training/modules/design-machine-learning-model-training-solution/5-exercise)
    """
    )

with st.expander("Unit 6/7 - Knowledge Check"):
    st.markdown(
        """

    1. A data scientist wants to train a machine learning model to predict the sales of supermarket items to adjust the supply to the projected demand. What type of machine learning task will the model perform?
    >>> **Time-series forecasting**
    > :  Time-series forecasting is used to predict future sales.

    2. The data scientist received data to train a model to predict the sales of supermarket items. The data scientist wants to quickly iterate over several featurization and algorithm options by only providing the data and editing some configurations. Which tool would best be used in this situation?
    >>> **Automated Machine Learning**
    > : You'll only have to provide the data and Automated Machine Learning will iterate over different featurization approaches and algorithms

    [Source](https://learn.microsoft.com/en-us/training/modules/design-machine-learning-model-training-solution/6-knowledge-check)
    """
    )

with st.expander("Unit 7/7 - Summary"):
    st.markdown(
        """

    #### In this module, you've learned how to:
    > - Identify machine learning tasks.
    > - Choose a service to train a model.
    > - Choose between compute options.

    [Source](https://learn.microsoft.com/en-us/training/modules/design-machine-learning-model-training-solution/7-summary)
    """
    )


st.markdown("***")
st.markdown("""
### **1.3 Design a model deployment solution**
***27 min - Module - 5 Units***

"""
)

with st.expander("Unit 1/5 - Introduction"):
    st.markdown(
        """

    ### Learning objectives
    >#### In this module, you'll learn how to:

    > - Understand how a model will be consumed.
    > - Decide whether to deploy your model to a real-time or batch endpoint.

    [Source](https://learn.microsoft.com/en-us/training/modules/design-model-deployment-solution/1-introduction)
    """
    )

with st.expander("Unit 2/5 - Understand how model will be consumed"):
    st.markdown(
        """

    ####  6 steps to plan, train, deploy, and monitor the model:
    > 1. **Define the problem:** Decide on what the model should predict and when it's successful.
    > 2. **Get the data:** Find data sources and get access.
    > 3. **Prepare the data:** Explore the data. Clean and transform the data based on the model's requirements.
    > 4. **Train the model:** Choose an algorithm and hyperparameter values based on trial and error.
    > 5. :sparkles: **Integrate the model:** Deploy the model to an endpoint to generate predictions. :sparkles:
    > 6. **Monitor the model:** Track the model's performance.

    ---

    ### Deploy a model to an endpoint
    > **Endpoint**
    > : can be a web address that an application can call to get a message back.
    > #### With **Azure Machine Learning,** you can deploy your model to an endpoint.
    > - Get real-time and batch predictions.

    | Endpoint Option               | How it works                          | Use Case                                              | Example                                       |
    |-------------------------------|---------------------------------------|-------------------------------------------------------|---------------------------------------------|
    | Get **real-time** predictions | Model scores new data as it comes in. | Often needed for model used by application such as a mobile app or website. | Model recommending additional products to a customer on a website based on customer's selection. |
    | Get **batch** predictions     | Model scores new data in batches.     | When needing to save results as a file or in a database. | Predicting product sales for each future week to ensure supply is sufficient to meet expected demand.             |

    [Source](https://learn.microsoft.com/en-us/training/modules/design-model-deployment-solution/2-understand-how-model-consumed)
    """
    )

with st.expander("Unit 3/5 - Decide on real-time or batch deployment"):
    st.markdown(
        """

    |  | **Real-time Predictions** | **Batch Predictions** |
    |---|---|---|
    | **Definition** | Predictions are required immediately when new data is collected. | Predictions are needed when a batch of data is available. |
    | **Use Cases** | The model scores the new data as soon as it comes in. | The model is scheduled or triggered to score the new data collected over time. |
    | **Number of Predictions** | The model receives a single row of data and returns a prediction. | The model receives multiple rows of data in one table and returns predictions for each row. |
    | **Cost of Compute** | Compute that is always available and can return results almost immediately. Continuously consumes compute resources, leading to ongoing costs. | Compute that can handle a large workload and score data in parallel batches using multiple nodes. Can be more cost-effective if a delay of 5-10 minutes is acceptable for immediate predictions. |
    | **Compute Requirements** | Depends on the complexity of the model. More complex models may require more compute power and processing time. | Depends on the complexity of the model. More complex models may require more compute power and processing time. |

    #### Remember, the choice between real-time or batch predictions: 
    > - doesn’t necessarily depend on how often new data is collected. 
    > - Instead, it depends on how often and how quickly the predictions need to be generated. 
    > - Therefore, consider how you’ll deploy your model before deciding on how to train your model.

    [Source](https://learn.microsoft.com/en-us/training/modules/design-model-deployment-solution/3-decide-real-time-batch-deployment)
    """
    )

with st.expander("Unit 4/5 - Exercise - Design a deployment solution"):
    st.markdown(
        """

    ### Proseware's Mobile Application for Faster Disease Diagnosis

    > - **Objective**: Proseware is developing a mobile application to help doctors diagnose diseases in patients faster. A doctor can enter the patient's medical data into the app to get a diagnosis.
    > - **First Planned Feature**: The app will advise the doctor whether the patient should be further screened or treated for diabetes.
    > - **Data Collection**: Proseware has collected data that correlates with diabetes, such as the number of pregnancies, age, and body mass index (BMI).
    > - **Model Training**: A team of data scientists is working on training a model that can classify whether a patient is likely to have diabetes.
    > - **Deployment**: Proseware needs advice on how to deploy the model to integrate it with the mobile application.

    ##### Looking forward to advice on designing the model's deployment solution.

    ### Consider the requirements:
    | Requirement | Description |
    |---|---|
    | **Frequency** |  The plan is that a doctor enters a patient's information into the app, like their age and BMI. After entering, a doctor can select the Analyze button, after which the model should predict whether or not a patient is likely to have diabetes. |
    | **Compute** | A doctor consultation typically takes less than 10 minutes. If we want doctors to use this app, we need the answers to be returned as quickly as possible. The deployed model should always be available as we don't know when a doctor may use it. |
    | **Size** | A doctor will only use the app to get a prediction on an individual's situation. There's no need for generating the predictions of multiple patients at once. |

    ---

    ### Propose a solution

    #### Knowledge Check

    1. What type of predictions are needed by the mobile application? 
    >>> **Real-time predictions**
    > : There is a need for immediate predictions for individual patients.

    2. What kind of compute should be used by the deployed model?
    >>> **Containers**
    > : Containers will be the more cost-effective solution as we want the model to be always available and respond immediately.

    [Source](https://learn.microsoft.com/en-us/training/modules/design-model-deployment-solution/4-knowledge-check)
    """
    )

with st.expander("Unit 5/5 - Summary"):
    st.markdown(
        """
    ### In this module, you've learned how to:

    > - Identify how a model will be consumed.
    > - Decide whether to deploy your model to a real-time or batch endpoint.
   

    [Source](https://learn.microsoft.com/en-us/training/modules/design-model-deployment-solution/5-summary)
    """
    )

    
st.markdown("***")
st.markdown("""
### **1.4 Design a machine learning operations solution**
***36 min - Module - 6 Units***

"""
)

with st.expander("Unit 1/6 - Introduction"):
    st.markdown(
        """
    ### Learning objectives
    #### In this module, you will:

    > - Explore an Machine Learning operations (MLOps) architecture.
    > - Design for monitoring.
    > - Design for retraining.

    [Source](https://learn.microsoft.com/en-us/training/modules/design-machine-learning-operations-solution/1-introduction)
    """
    )

with st.expander("Unit 2/6 - Explore an MLOps architecture"):
    st.markdown(
        """

    [Source]()
    """
    )

with st.expander("Unit 3/6 - Design for monitoring"):
    st.markdown(
        """

    [Source]()
    """
    )

with st.expander("Unit 4/6 - Design for retraining"):
    st.markdown(
        """

    [Source]()
    """
    )

with st.expander("Unit 5/6 - Knowledge Check"):
    st.markdown(
        """

    [Source]()
    """
    )

with st.expander("Unit 6/6 - Summary"):
    st.markdown(
        """

    [Source]()
    """
    )