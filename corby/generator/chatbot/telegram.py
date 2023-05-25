"""CLI chatbot manager"""

import os
from ..base import BaseGenerator

class TelegramChatbotGenerator(BaseGenerator):
    """CLI chatbot manager"""

    def get_templates(self):
        return {
        'telegram-langchain-chatbot': 'https://github.com/JoseHervas/telegram-langchain-chatbot.git'
    }

    def create_telegram_chatbot(self, name):
        """Generates a new CLI chatbot"""
        app_path = os.getcwd() + '/' + name
        selected_template = self.ask_template()
        self.clone_template(selected_template["template_url"], selected_template["template_name"])
        os.rename(os.getcwd() + '/skeleton', app_path)
        self.cleanup(selected_template["template_name"])
        self.replace_in_folder(app_path, {'chatbot_name': name})
        print("Yeepay 🎉, your chatbot is ready!")
        print("You can find it in the " + name + " folder")
