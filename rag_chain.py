from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI, MistralAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_chroma import Chroma

vector_store = Chroma(
    persist_directory="vector_db",
    embedding_function=MistralAIEmbeddings()
)

retriever = vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k":6,
        "fetch_k":25,
        "lambda_mult":0.7
    }
)

llm = ChatMistralAI(model="mistral-small-2506")

# prompt = ChatPromptTemplate.from_messages([

#     ('system', 
#                 """
#                 You are an HR Assistant.

#                 Answer ONLY using the provided context in detail.

#                 If the answer is not present in the context,
#                 respond with:

#                 "I could not find this information in the HR policies.")
#                 """
#     ),
#     ('human',
#             """Context:
#                 {context}

#                 Question:
#                 {question}

#                 Answer:
#             """
#     )
# ])

prompt = ChatPromptTemplate.from_messages(
[
(
"system",
"""
You are an HR Policy Assistant.

Rules:

1. Answer ONLY from the context.
2. Do not make assumptions.
3. If information is missing say:

'I could not find this information in the HR policies.'

4. Mention policy names whenever possible.
5. Be concise but complete.
"""
),
(
"human",
"""
Context:
{context}

Question:
{question}
"""
)
]
)

# print("HR RAG Assistant")
# print("press 0 to exit")

# while True:
#     query = input("You : ")
#     if query == "0": break
    
#     docs = retriver.invoke(query)
    
#     context = "\n\n".join(
#         [doc.page_content for doc in docs]
#     )
    
#     final_prompt = prompt.invoke({
#         "context": context,
#         "question": query
#     })

#     response = llm.invoke(final_prompt)
    
    
#     print(f"\n AI : {response.content}")
    
    
def ask_hr_bot(query):
    docs = retriever.invoke(query)
    
    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )
    
    final_prompt = prompt.invoke({
        "context": context,
        "question": query
    })

    response = llm.invoke(final_prompt)

    return response.content