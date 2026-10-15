from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

import numpy as np

embedding =  HuggingFaceEmbeddings(model ='sentence-transformers/all-MiniLM-L6-v2')
documents = [ 
             "John Cena is a famous WWE superstar known for his Attitude Adjustment.",
             "Roman Reigns is known as The Tribal Chief in WWE.", 
             "The Undertaker is famous for his legendary WrestleMania streak.",
             "Randy Orton is known for his finishing move called the RKO.",
             "The Rock is a popular WWE superstar and Hollywood actor.",
             "Seth Rollins is known as The Visionary in WWE.", 
             "Cody Rhodes is known as The American Nightmare.", 
             "Rey Mysterio is famous for his high-flying wrestling style.", 
             "Brock Lesnar is known for his strength and suplexes.", 
             "CM Punk is known for his wrestling skills and microphone abilities."
]
query = "tell me about Brock Lesnar"

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding],doc_embeddings)[0]
index,score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]
print(query)
print(documents[index])
print("similarity score is : ",score)
