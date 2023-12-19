import pandas as pd
from catboost import CatBoostClassifier, Pool
from icecream import ic
from sklearn.model_selection import train_test_split
import sklearn.metrics as metrics
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import roc_auc_score

from sklearn.metrics import accuracy_score, f1_score
from sklearn.metrics import classification_report
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score, confusion_matrix, precision_recall_curve
from sklearn import metrics

modelname = 'model'

def metric_models(modelname, model, X_test, y_test, y_pred):
    acc   = round(accuracy_score(y_test,y_pred), 2)*100
    score = round(metrics.precision_score(y_test, y_pred, average='macro'), 4)*100
    mae   = round(mean_absolute_error(y_test, y_pred), 5)

    # Calculate area under curve (AUC)
    y_pred_proba = model.predict_proba(X_test)[::,1]
    auc = round((metrics.roc_auc_score(y_test, y_pred_proba)), 4)*100

    print(f'{modelname} model:')
    print(f"accuracy........:{acc}%")
    print(f'score...........:{score}')
    print(f"Mean Absolute Error: {mae}")
    print(f"Area under curve (AUC): {auc} %")


print('>>> loading dataset for modeling....')
df = pd.read_csv('../datasets/HR_COM1_cleaned.csv')

shape_rows = df.shape[0]
shape_columns = df.shape[1]

print(f'Dataset rows = {shape_rows} and columns = {shape_columns}.')

# Set the input X to the K-Means.
X = df.drop(columns=['turnover'])
y = df['turnover']

# define categorial features of dataset
cat_features = ['dept', 'salary']  # List of categorical features

X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2, random_state=123, stratify=y, shuffle = True)

cat_model = CatBoostClassifier(
    iterations = 300, # 1000 are ideal
    loss_function='MultiClass',
    bootstrap_type = "Bayesian",
    eval_metric = 'AUC',
    leaf_estimation_iterations = 100,
    random_strength = 0.5,
    depth = 10,
    l2_leaf_reg = 5,
    learning_rate=0.1,
    cat_features=cat_features,
    bagging_temperature = 0.5,
    thread_count=-1 # number of threads, setted all CPU cores
    #task_type = "GPU",
)

print(cat_model.get_params())

print('Train the model')


# Train the model
cat_model.fit(X_train, y_train, eval_set=(X_test, y_test), verbose=False)
y_pred_cat = cat_model.predict(X_test)

print ("\n\n ---CatBoostClassifier Model---")
cat_roc_auc = roc_auc_score(y_test, y_pred_cat)
print ("CatBoost AUC = %2.4f" % cat_roc_auc)
print(classification_report(y_test, y_pred_cat))

metric_models('CatBoostClassifier', cat_model, X_test, y_test, y_pred_cat)

list_name_features = []
index = 1

for feat, importance in zip(X.columns, cat_model.feature_importances_):
    importance = round(importance, 2)
    print(f'{index} - feature: {feat}, importance: {importance} %')
    list_name_features.append(feat)
    index += 1

# Save the trained model to a file
print('saving the model to production...')
cat_model.save_model('../apptoprod/catboost.cbm')

print("All Done. :)")

