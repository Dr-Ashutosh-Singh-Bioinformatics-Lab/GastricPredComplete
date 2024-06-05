# GastricPredComplete: A Tool for Identification of Gastric Cancer from salivary extracellular vesicles (EVs) using Machine Learning.
Gastric cancer, originating from the stomach lining, presents a substantial global health challenge due to its high prevalence and mortality rates. Timely detection of gastric cancer is crucial for timely treatment and better patient prognosis. Biomarkers are pivotal in this regard, providing noninvasive means for early detection, facilitating prompt treatment initiation, and potentially boosting survival rates. Hence, the recognition and validation of biomarkers are of primary importance in effectively addressing gastric cancer.


## Introduction

GastricPredComplete is an innovative solution for identifying gastric cancer through a noninvasive method using salivary extracellular vesicles (EVs). By leveraging advanced machine learning algorithms, this cutting-edge technology analyzes salivary biomarkers to provide a highly accurate prognosis of gastric cancer.

Furthermore, the integration of machine learning algorithms allows for continuous refinement of the predictive model's accuracy as more data is gathered, thereby enhancing its reliability and effectiveness over time. GastricPredComplete represents a significant breakthrough in the early detection of gastric cancer, potentially leading to earlier interventions and improved patient outcomes.

To further strengthen our approach, we have selected 13 features using various Feature Selection Methods, including Mutual Information, Recursive Feature Selection, and SelectFromModel with RandomForestRegressor. By employing a combination of Filter, Wrapper, and Embedded feature selection techniques and using an ensemble approach, we identified features present in at least two methods. These 13 features show promise as biomarkers for classifying and predicting normal and cancerous patients. 


## Accuracy Heatmap of the Different Feature Selection Methods for Cancer Driver Genes

![ACC](https://github.com/GITractCancer/GastricPredComplete/assets/171772666/ebeb444d-86f3-4f65-8128-787335eb324b)


## AUC Heatmap of the Different Feature Selection Methods for Cancer Driver Genes 

![AUC](https://github.com/GITractCancer/GastricPredComplete/assets/171772666/68ec564c-cff5-4cee-92a3-d6e707152808)



## Venn Diagram showing features in atleast in 2 Feature Selection Methods for Cancer Driver Genes

![Complete](https://github.com/GITractCancer/GastricPredComplete/assets/171772666/2c45aada-daeb-42a5-9f22-8c02ec3417f7)


Installation and Usage:

You can install the package using the following command:


    git clone https://github.com/GITractCancer/GastricPredComplete.git
    cd GastricPredComplete



### Predict using GastricPredDriver

    import pandas as pd
    from GastricPredComplete import predict

    df = pd.read_csv("path/to/your/data.csv")

    predict(df, model_type='svc')

    
Specify the model type you want to use Models


## Models

The following classifiers are supported:

    svc
    rf
    ab
    xgb
    dt
    et
    lr
    gnb
    knn
    mlp
