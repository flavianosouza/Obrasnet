import nltk
from nltk.corpus import stopwords
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Read and clean text data

with open('user_doc.txt', 'r') as f:
    text = f.read()

# Tokenize text

tokens = nltk.word_tokenize(text)

# Remove stop words and punctuation

stop_words = set(stopwords.words('english'))
clean_tokens = [w for w in tokens if w not in stop_words and w not in string.punctuation]

# Vectorize text

tfidf_vectorizer = TfidfVectorizer()
tfidf = tfidf_vectorizer.fit_transform(clean_tokens)

# Cluster documents

kmeans = KMeans(n_clusters=3)
kmeans.fit(tfidf)

# Print cluster centroids

print(kmeans.cluster_centers_)