from config import get_llm # replace with your filename
llm = get_llm()
if __name__ == '__main__':
    response = llm.invoke("Tell me a joke")
print(response)
print(response.content)