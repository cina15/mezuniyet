import random
import time
class ChatBot:
    def __init__(self, name):
        self.name = name
        self.responses = {
            "merhaba": "Merhaba! Size nasıl yardımcı olabilirim?",
            "nasılsın": "İyiyim, teşekkür ederim! Siz nasılsınız?",
            "hava nasıl": "Hava durumunu öğrenmek için lütfen konumunuzu belirtin.",
            "görüşürüz": "Görüşürüz! İyi günler dilerim."
        }

    def get_response(self, user_input):
        user_input = user_input.lower()
        if user_input in self.responses:
            return self.responses[user_input]
        else:
            return "Üzgünüm, bu konuda size yardımcı olamıyorum."