import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from django.conf import settings
settings.configure(DEBUG=True)

import string
from models import Category



# csv_file = "product_dataset.csv"
# df = pd.read_csv(csv_file)
# categories_l = df.product_category_tree
# prod_name_l = df.product_name

# def load_Category(cat_l):
#     for cat in cat_l:
#         cat_obj = Category(name=cat)
#         cat_obj.save()

# def load_Product(prod_l, cat_l):
#     i = 0
#     for prod in prod_l:
#         prod_obj = Product(name=prod_l[i], category=cat_l[i])
#         i+= 1

#don't keep categories with only 1 level for now
cat_chains = []
prod_names = []
cat_d = set()
cats123 = [[],[],[]]
for i in range(len(categories_l)):
    this_l = [ x.strip().translate(str.maketrans('','', string.punctuation)).lower() for x in categories_l[i].split(">>")]

    if len(this_l) < 3:
        i = 3- len(this_l)
        while i > 0:
            last = this_l[-1]
            this_l.append(last)
            i -= 1
    if len(this_l) > 3:
        this_l = this_l[(len(this_l)-3):]

    for k in range(len(this_l)):
        ind_cat = this_l[k]
        cat_d.add(ind_cat)
        cats123[k].append(ind_cat)

    cat_chains.append('->'.join(this_l))
    prod_names.append(prod_name_l[i])
    
#transform category to numerical values
le = preprocessing.LabelEncoder()
cat_d_l = list(cat_d)
le.fit(cat_d_l)
print(len(cat_d),'hiasdf')
cat_transformed = le.transform(cat_d_l)
# txt2num = {}
# num2txt = {}
print(cat_transformed[:5], cat_d_l[:5])
print(len(prod_names), len(cats123[0]))
# #create mapping to transform category to numerical values.
# for i in range(len(cat_transformed)):
#     cat_d = cat_d_l[i]
#     txt2num[cat_d] = cat_transformed[i]
#     num2txt[cat_transformed[i]] = cat_d

#trying to train model

x_train, x_test, y_train, y_test = train_test_split(prod_names, cats123[0])
x2_train, x2_test, y2_train, y2_test = train_test_split(prod_names, cats123[1])
x3_train, x3_test, y3_train, y3_test = train_test_split(prod_names, cats123[2])

from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
        
keyword = "pants"
nb = Pipeline([('vect', CountVectorizer()),
               ('tfidf', TfidfTransformer()),
               ('clf', MultinomialNB()),
              ])
nb.fit(x_train, y_train)
y_pred = nb.predict(x_test[:5])
c1 = nb.predict([keyword])

nb.fit(x2_train, y2_train)
y_pred = nb.predict(x2_test[:5])
c2 = nb.predict([keyword])

nb.fit(x3_train, y3_train)
y_pred = nb.predict(x3_test[:5])
c3 = nb.predict([keyword])

print("{} -> {} -> {}".format(c1,c2,c3))


# print('accuracy ', accuracy_score(y_pred, y_test))
# print(classification_report(y_test, y_pred,target_names=my_tags))
