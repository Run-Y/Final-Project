from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# 初始化 ChatBot
chatbot = ChatBot("Climate_Robot")

# 训练 ChatBot
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('./data/climate_change_corpus.json')

def get_response(question):
    # 获取回复
    response = chatbot.get_response(question)
    return response

if __name__ == '__main__':
    response = get_response("What is climate change?")
    print(response)