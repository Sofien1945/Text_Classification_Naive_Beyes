""""" Text Classification using Naive Beyes
Date: 19.10.2021
Part of Simplearn Machine learning Course
Done By: Sofien Abidi"""

#Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline

#Import Dataset
from sklearn.datasets import fetch_20newsgroups
data = fetch_20newsgroups()
categories = ['alt.atheism',
 'comp.graphics',
 'comp.os.ms-windows.misc',
 'comp.sys.ibm.pc.hardware',
 'comp.sys.mac.hardware',
 'comp.windows.x',
 'misc.forsale',
 'rec.autos',
 'rec.motorcycles',
 'rec.sport.baseball',
 'rec.sport.hockey',
 'sci.crypt',
 'sci.electronics',
 'sci.med',
 'sci.space',
 'soc.religion.christian',
 'talk.politics.guns',
 'talk.politics.mideast',
 'talk.politics.misc',
 'talk.religion.misc']
#Training data
train = fetch_20newsgroups(subset = 'train', categories = categories)
#Testing data
test = fetch_20newsgroups(subset = 'test', categories = categories)
#Import Sklearn Libraries
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
#Model Creation
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
#Model Training
model.fit(train.data, train.target)
#Label Creation fo the test set
labels = model.predict(test.data)
#Creation of Confusion matrix
from sklearn.metrics import confusion_matrix
mat = confusion_matrix(test.target, labels)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False, xticklabels=train.target_names,yticklabels=train.target_names)
#Plotting heatmap of cf
plt.xlabel('True label')
plt.ylabel('Predicted label')
#predicting category on new data based on trained model
def predict_category(s, train=train, model=model):
    pred = model.predict([s])
    return train.target_names[pred[0]]


print(predict_category('foot'))
print(predict_category('Climate change'))
print(predict_category('Big Bang Theory'))
