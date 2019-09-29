import pandas as pd
from sklearn import preprocessing
from django.conf import settings

import string



csv_file = "product_dataset.csv"
df = pd.read_csv(csv_file)
categories_l = df.product_category_tree
prod_name_l = df.product_name

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
    prod_names.append(prod_name_l[i].lower())
    
#transform category to numerical values
le = preprocessing.LabelEncoder()
cat_d_l = list(cat_d)
le.fit(cat_d_l)
cat_transformed = le.transform(cat_d_l)


from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer,TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import GaussianNB

keyword = "laptop cover" #change this to getting input from detection

nb = Pipeline([('vect', CountVectorizer()),
               ('tfidf', TfidfTransformer()),
               ('clf', MultinomialNB()),
              ])

x = []
for i in range(len(prod_names)):
    x.append(f"{prod_names[i]} {cats123[1][i]} {cats123[2][i]}")

nb.fit(x, cats123[0])
c1 = nb.predict([keyword])

x = []
for i in range(len(prod_names)):
    x.append(f"{prod_names[i]} {cats123[0][i]} {cats123[2][i]}")
nb.fit(prod_names, cats123[1])
c2 = nb.predict([keyword])

x = []
for i in range(len(prod_names)):
    x.append(f"{prod_names[i]} {cats123[0][i]} {cats123[1][i]}")

nb.fit(prod_names, cats123[2])
c3 = nb.predict([keyword])

print(f"{c1} -> {c2} -> {c3}")

