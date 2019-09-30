import pandas as pd
from sklearn import preprocessing
from django.conf import settings
import numpy as np
import string

def get_cat(choice):

    #using naive  bayes for text classification on our small dataset
    csv_file = "D:/GitLab_respos/singapore_hackjunctionX_2019/singapore_hackjunctionX_2019/web/ecommerce/product_dataset.csv"
    df = pd.read_csv(csv_file)
    categories_l = df.product_category_tree
    prod_name_l = df.product_name

    retail_price = df.retail_price

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
    from sklearn.ensemble import RandomForestRegressor


    keyword = choice#change this to getting input from detection

    nb = Pipeline([('vect', CountVectorizer()),
                ('tfidf', TfidfTransformer()),
                ('clf', MultinomialNB()),
                ])

    # regressor = RandomForestRegressor(n_estimators= 10, random_state=99)
    
    # reglist = list(cat_d)
    # allCat = pd.DataFrame(0, index=np.arange(len(prod_names)), columns=reglist)
    # for i in range(len(prod_names)):
    #     if f"{cats123[0][i]}" in list(allCat.columns):
    #         allCat.cats123[0][i] = 1
    #     if f"{cats123[1][i]}" in list(allCat.columns):
    #         allCat.cats123[1][i] = 1
    #     if f"{cats123[2][i]}" in list(allCat.columns):
    #         allCat.cats123[2][i] = 1 
    
    # regressor.fit(allCat, retail_price)
    # c4 = regressor.predict([keyword])

    from random import seed
    from random import random
    # seed(random())
    c4 = 100 * random() + 100 - random() * 10

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
    
    result = (f"{c1[0]} -> {c2[0]} -> {c3[0]}")

    #using api (not on our dataset)
    import requests
    import json

    #input key
    product_name = keyword

    headers = {
        'Authorization': 'Bearer bloxlh1emsMJg6slDrW27c6PByvHHCZk',
    }
    params = {
        'productName': product_name,
        'limit': '3'
    }
    try:
        response = requests.get('https://ml-eu.europe-west1.gcp.commercetools.com/bbc-junctionx/recommendations/general-categories', headers=headers, params=params)
        parsed_json = response.json()


        cat_hier = [x["categoryName"] for x in parsed_json["results"]]
    except Exception:
        cat_hier = ["a", "b'"]
    # print('-> '.join(cat_hier))
    return result, cat_hier, c4