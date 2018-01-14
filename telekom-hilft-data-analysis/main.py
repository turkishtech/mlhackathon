import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import imread
import mglearn


nltk.download('stopwords')

dataset = pd.read_csv('tweets.20150430-223406.tweet.csv', header=0, encoding="utf8")

# Text Cleaning
ps = PorterStemmer()
corpus= []
for i in range (0, 20000):
    review = re.sub('[^a-zA-Z]', ' ', dataset['text'][i])
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review= ' '.join(review)
    corpus.append(review)

# Bag of Words
# uses CountVector Class from sklearn
#cv = CountVectorizer(min_df = 5, ngram_range =(1,3))    
cv = CountVectorizer(min_df = 3, max_df = 1000, ngram_range=(1, 3) )
X = cv.fit_transform(corpus).toarray()

# Topic modeling with LDA - needs improvement
lda = LatentDirichletAllocation(n_components=50, learning_method="batch", max_iter=25, random_state=0)

# be build the model and transform the data in one step
document_topics = lda.fit_transform(X)

#To understand better what the different topics mean, we will look at the most important word for each of the topics. The print_topics function we use below provides a nice formatting for these features.
# for each topic (a row in the components_), sort the features (ascending).
# Invert rows with [:, ::-1] to make sorting descending
sorting = np.argsort(lda.components_, axis=1)[:, ::-1]

# get the feature names from the vectorizer:
feature_names = np.array(cv.get_feature_names())

# print out the 50 topics:
mglearn.tools.print_topics(topics=range(50), feature_names=feature_names,
sorting=sorting, topics_per_chunk=5, n_words=20)

