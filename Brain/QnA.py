# Api Key

file = open("E:\Sam-Env\AI-Sam\Data\Api.txt", "r")
API = file.read()
file.close()

import openai
from dotenv import load_dotenv

openai.api_key = API
load_dotenv()
completion = openai.Completion()

def QuestionAnswer(question, chat_log = None):
    FileLog = open("E:\Sam-Env\AI-Sam\DataBase\qna_log.txt", "r")
    chat_log_template = FileLog.read()
    FileLog.close()

    if chat_log is None:
        chat_log = chat_log_template
    
    prompt = f"{chat_log}Question : {question}\nAnswer : "
    response = completion.create(
        model = "text-davinci-002",
        prompt = prompt,
        temperature = 0,
        max_tokens = 150,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0
        )
    if len(question)<1:
        pass
    else:
        answer = response.choices[0].text.strip()
        chat_log_template_update = chat_log_template + f"\nQuestion : {question}\nAnswer : {answer}\n"
        FileLog = open("E:\Sam-Env\AI-Sam\DataBase\qna_log.txt", "w")
        FileLog.write(chat_log_template_update)
        FileLog.close()
        return answer
