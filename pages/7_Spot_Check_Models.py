import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import seaborn as sns
import scipy.stats as stats
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.calibration import CalibratedClassifierCV
import joblib
import pickle5 as pickle


import warnings
warnings.simplefilter(action='ignore', category=UserWarning)
warnings.simplefilter(action='ignore', category=FutureWarning)

st.title("Spot Check Models")

DATA_URL = ('./data/train.csv')
df = pd.read_csv(DATA_URL)

DATA_URL_xtr = ('./data/X_train.csv')
X_train = pd.read_csv(DATA_URL_xtr)
DATA_URL_xte = ('./data/X_test.csv')
X_test = pd.read_csv(DATA_URL_xte)
DATA_URL_ytr = ('./data/y_train.csv')
y_train = pd.read_csv(DATA_URL_ytr)
DATA_URL_yte = ('./data/y_test.csv')
y_test = pd.read_csv(DATA_URL_yte)

# LR Calibration models
#skf = StratifiedKFold(n_splits=5,random_state=0, shuffle=True)
#LR_C= CalibratedClassifierCV(base_estimator=LogisticRegression(random_state=0), method="isotonic")
#param_grid = {}
#model = GridSearchCV(LR_C,param_grid,cv=skf)
#classifier = model.fit(X_train, y_train)
# save the model to disk
#LR_filename = ('./data/LR_C_model.sav')
#joblib.dump(LR_C_model, LR_filename)
# load the model from disk
#LR_C_restored_model = joblib.load(LR_filename)
#pickle_out = open('./data/classifier.pkl', 'wb')
#serialized_classifier = pickle.dumps(classifier, pickle_out)
#pickle_out.write(serialized_classifier)
#pickle_out.close()
# loading in the model to predict on the data
#pickle_in = open('./data/classifier.pkl', 'rb')
#classifier = pickle.loads(pickle_in)
#pickle_in.close()

# save the model to disk
#with open('./data/classifier.pkl', 'wb') as pickle_out:
#    serialized_classifier = pickle.dumps(classifier)
#    pickle_out.write(serialized_classifier)

# loading in the model to predict on the data
with open('./data/classifier.pkl', 'rb') as pickle_in:
    classifier = pickle.load(pickle_in)
    
predictions_tr = classifier.predict_proba(X_train)[:, 1]
predictions_t = classifier.predict_proba(X_test)[:, 1]
LR_auc_train = roc_auc_score(y_train, predictions_tr)  
LR_auc_test = roc_auc_score(y_test, predictions_t) 
score= {'model_c':['LR_C'], 'auc_train_c':[LR_auc_train],'auc_test_c':[LR_auc_test]}
LR_score= pd.DataFrame(score)
LR_score

st.markdown("""
Logistic Regression (LR) is the benchmark model used in Insurance, and it has been compared with

Naive Bayes model (GNB), K-Nearest Neighbors model (KNB) and Hist Gradient Boosting Machine (HGBM).

""")
