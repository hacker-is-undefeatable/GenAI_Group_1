import pandas as pd
df = pd.read_csv("epic_qa_consumer_w_content.csv")
#df = df.drop(['Unnamed:0.1', 'Unnamed:0'], axis=1)
print(df.info())
new_df = df.iloc[:, 2:]
print(new_df.info())
#most_common_context = new_df['contexts'].value_counts().idxmax()
#most_common_title = new_df['title'].value_counts().idxmax()
#most_common_url = new_df['url'].value_counts().idxmax()
#print("Most Common Context:", most_common_context)
#print("Most Common Title:", most_common_title)
#print("Most Common URL:", most_common_url)
preprocessed = new_df.copy()
preprocessed['contexts'] = preprocessed['contexts'].fillna("missing context")
preprocessed['title'] = preprocessed['title'].fillna("missing title")
preprocessed['url'] = preprocessed['url'].fillna("missing url")
preprocessed['content'] = preprocessed['content'].fillna("missing content")
missing_values_count = preprocessed.isnull().sum()
missing_values_count = preprocessed.isnull().sum()
#print(missing_values_count)
preprocessed['contexts'] = preprocessed['contexts'].apply(lambda x: re.sub(r"context_id.*text", "", x))
preprocessed['contexts'] = preprocessed['contexts'].apply(lambda x: re.sub(r"sentences.*", "", x))
preprocessed['contexts'] = preprocessed['contexts'].apply(lambda x: re.sub(r"section", "", x))
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

def remove_stopwords(text):
    return " ".join([word for word in text.split() if word not in stop_words])

preprocessed['contexts'] = preprocessed['contexts'].apply(remove_stopwords)
preprocessed['title'] = preprocessed['title'].apply(remove_stopwords)
preprocessed['content'] = preprocessed['content'].apply(remove_stopwords)
preprocessed.to_csv("/Users/dinusarasasindugamagenanayakkara/Library/Mobile Documents/com~apple~CloudDocs/1.year 3/Gen AI Learning project/preprocessed_covid19_data.csv")
# Tokenize 

preprocessed['contexts'] = preprocessed['contexts'].apply(lambda x: nltk.word_tokenize(x))
preprocessed['title'] = preprocessed['title'].apply(lambda x: nltk.word_tokenize(x))
#preprocessed['url'] = preprocessed['url'].apply(lambda x: nltk.word_tokenize(x))
preprocessed['content'] = preprocessed['content'].apply(lambda x: nltk.word_tokenize(x))
preprocessed.to_csv("/Users/dinusarasasindugamagenanayakkara/Library/Mobile Documents/com~apple~CloudDocs/1.year 3/Gen AI Learning project/preprocessed_covid19_tokens.csv")
'''
# Train Word2Vec model on the tokenized fields


