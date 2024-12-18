import ollama

def Qa(query):
    #query = input('질문을 영어로 입력하세요 : ')
    response = ollama.chat(model='llama3.2:1b', messages=[{'role': 'user','content': query+'. give me a brief answer.',},])
    answer = response['message']['content']
    #print(answer)
    return answer
