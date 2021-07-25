import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# 데이터 가져오는 기능
def get_data():
    recipe_data = pd.read_csv('dataset/recipe_data.csv', index_col=0)
    return recipe_data

# 추천 기능
def recommend(ingredient):
    data = get_data()
    """ 토큰화 """
    temp = np.append(data['재료'].values, ingredient)
    count_vect = CountVectorizer()
    dtm_ingredient = count_vect.fit_transform(temp)
    """ 코사인 유사도 기반 정렬 """
    sim_ingredient = cosine_similarity(dtm_ingredient, dtm_ingredient)
    sorted_idx = sim_ingredient.argsort()[:, ::-1][:,1:]
    recommend_idx = sorted_idx[-1, :5]
    return data.loc[recommend_idx, :].to_dict('records')