from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the following: 
Here is the conversation history: {context}

Question: {question}
Answer:
"""
model = OllamaLLM(model = "gemma:2b")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    context = ""
    print("Welcome to AI Agent!. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        result = chain.invoke({"context": context, "question": user_input})
        print("Bot : ", result)
        context += f"\nUser:{user_input}\nBot:{result}"

if __name__ == "__main__":
    handle_conversation()


