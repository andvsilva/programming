## Data Science

```bash 
@andvsilva
```
To study 

 - Dataset
 - Explore data
 - Feature Selection/Engineering
 - Modeling 
 - Machine Learning

```bash
source dataset: https://www.kaggle.com/code/bashirabubakar/human-resources-analytics-employee-attrition/notebook
```

### Requirements

```bash
# author: @andvsilva sáb 09 dez 2023 10:34:19
pip install pipreqs

# to create file requirements on the folder
pipreqs ~/repo/programming/notebooks

# requirements.txt libraries for the project
catboost==1.1.1
Faker==18.9.0
feather==0.1.2
feather_format==0.4.1
icecream==2.1.3
ipython==8.18.1
matplotlib==3.7.0
numpy==1.24.4
pandas==1.3.5
scikit_learn==1.3.2
seaborn==0.13.0
snoop==0.4.3
streamlit==1.19.0
tqdm==4.66.1
varname==0.12.2


# Just run this command to install
# the libraries for the project.
~/repo/programming/notebooks on  master! ⌚ 10:31:12
pip install -r requirements.txt 
```

```
Two files to performance the cleaning and modeling:

- exploredata.ipynb
- modeling.ipynb
- bestmodels.ipynb

Modeling
@andvsilva - sáb 09 dez 2023 16:36:53

Testing and Results
- Logistic Regression
- Random Forest 
- Decision Tree
- AdaBoost Model
- XGBClassifier
- LightGBM
- CatBoostClassifier
```

```bash
drop the column: Emp ID.
```

### Results

For the models listed above and I found the following results:

Applying the Receiver Operating Characteristic (**ROC**) curve is a graphical representation used in binary and multi-class classification problems to assess the performance of a classification model at various thresholds.

#### Here is a basic interpretation of the ROC curve:

- **Top-Left Corner**: Ideal scenario where the model has a high true positive rate and a low false positive rate across various thresholds.

- **Bottom-Right Corner**: Represents a model that performs no better than random chance.

- **Diagonal Line**: Represents the performance of a random classifier.

![ROC curves](images/roc_curve_models.png)

```bash
## @andvsilva - 10 dez 2023 19:14:35
-------------------------Metrics-----------------------
LogisticRegression model:
accuracy........:75.7%
score...........:63.69
Mean Absolute Error: 0.24333
-------------------------------------------------------
Random Forest model:
accuracy........:98.9%
score...........:98.96
Mean Absolute Error: 0.01133
-------------------------------------------------------
Decision Tree model:
accuracy........:96.2%
score...........:94.88
Mean Absolute Error: 0.038
-------------------------------------------------------
AdaBoost model:
accuracy........:95.19%
score...........:93.82
Mean Absolute Error: 0.04767
-------------------------------------------------------
XGBClassifier model:
accuracy........:98.9%
score...........:98.53
Mean Absolute Error: 0.01133
-------------------------------------------------------
CatBoostClassifier model:
accuracy........:99.1%
score...........:98.85
Mean Absolute Error: 0.00867
-------------------------------------------------------
LightGBMClassifier model:
accuracy........:98.6%
score...........:98.34
Mean Absolute Error: 0.014
-------------------------------------------------------
```


## Deep Learning - Keras.

```bash
@andvsilva 10 dez 2023 22:09:15

Working in progress! The next step is to workaround, the parameters.

Keras is not so good yet!
```

### Results

![](images/roc_curve_dlkeras.png)


## Selecting the best models &rarr; metrics:

![](../notebooks/images/modelmetrics.png)

![](../notebooks/images/roc_curve_bestmodels.png)

```bash
@andvsilva 11 dez 2023

the BEST model according to metrics: 'CatBoost Classifier'

CatBoostClassifier model:
accuracy........:99.1%
score...........:98.85
Mean Absolute Error: 0.00867
Area under curve (AUC): 99.41 %

## Cross Validation to catboost.
https://www.geeksforgeeks.org/catboost-cross-validation-and-hyperparameter-tuning/
```



```bash
# install streamlit to make an app:

pip install streamlit

# go to the folder:
cd programming/notebooks/apptoprod

$ streamlit run turnover.py           

  You can now view your Streamlit app in your browser.

  Local URL: http...
  Network URL: ...
```

You to access the URL http://...:... to see your app working. :smiley: Now enjoy!


### To do!

- [ ] Maybe we can apply the feature selection,like the 'SelectKBest' ```@andvsilva``` (https://machinelearningmastery.com/feature-selection-with-real-and-categorical-data/)

### To Read and To study

```@andvsilva```
- [x] Label Encoder - [Label Encoding in Python](https://www.geeksforgeeks.org/ml-label-encoding-of-datasets-in-python/)
- [x] groupby - code
- [x] Correlation Methods - [Choosing the Right Correlation: Pearson vs. Spearman vs. Kendall’s Tau](https://ishanjain-ai.medium.com/choosing-the-right-correlation-pearson-vs-spearman-vs-kendalls-tau-02dc7d7dd01d)
- [x] Pandas Profiling
- [x] toolkit - Just a way to perform tasks and code will be more clean and organized, to call 'help functions'.
- [x] Feature Importance - [Estimating feature importance, the easy way](https://romainlhardy.medium.com/estimating-feature-importance-the-easy-way-2ebe970c600c)
- [x] Compare ```y_test``` to ```y_pred```
- [x] R2 ajusted - [R-Squared vs Adjusted R-Squared](https://medium.com/analytics-vidhya/r-squared-vs-adjusted-r-squared-a3ebc565677b)
- [ ] pycaret
- [ ] ```mlflow``` - A good to make experiment in ML, I will study this. ```@andvsilva```
- [How to Effectively Learn Data Science in 2024](https://medium.com/illumination/how-to-effectively-learn-data-science-in-2024-b3f508db4f67)
- **To-do Checklist for Statistics For Data Scientist - STUDIES**:
- [ ] a. Probability theory 
- [ ] b. Descriptive Statistics
- [ ] c. Inferential Statistics
- [ ] d. Statistical Machine Learning, roadmap to study 

![Workflow](/images/data_science_workflow.png) **NOT WORK markdown FIXME!**

- **Data Extraction**:
  - SQL
  - Scrapping
  - File Formats
    - CSV
    - JSON
    - XML
  - Consulting APIs
  - Buying Data
  - Distributed Databases

- **Data Cleaning**:
  - Missing values and empty data
  - Data imputation
  - Incorrect types
  - Incorrect or invalid values
  - Outliers and non relevant data
  - Statistical sanitization

- **Data Wrangling**
  - Hierarchical Data
  - Handling categorical data
  - Reshaping and transforming structures
  - Indexing data for quick access
  - Merging, combining and joining data

- **Analysis**
  - Exploration
  - Building statistical models
  - Visualization and representations
  - Correlation vs Causation analysis
  - Hypothesis testing
  - Statistical analysis
  - Reporting

- **Action**:
  - Building Machine Learning Models
  - Feature Engineering
  - Moving ML into production
  - Building ETL pipelines
  - Live dashboard and reporting
  - Decision making and real-life tests
