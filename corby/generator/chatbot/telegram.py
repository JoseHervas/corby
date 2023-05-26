"""Telegram chatbot manager"""

import os
import inquirer
from ..base import BaseGenerator

class TelegramChatbotGenerator(BaseGenerator):
    """Telegram chatbot manager"""

    def get_templates(self):
        return {
            # pylint: disable=line-too-long
           'telegram-langchain-chatbot': 'https://github.com/corby-templates/langchain-telegram-chatbot.git'
    }

    def create_telegram_chatbot(self, name):
        """Generates a new Telegram chatbot"""
        app_path = os.getcwd() + '/' + name
        selected_template = self.ask_template()
        template_params = {'chatbot_name': name}
        questions = [
                inquirer.List(
                    "token", 
                    message="Do you have a Telegram bot token?",
                    choices=["yes", "no"]
                ),
            ]
        answers = inquirer.prompt(questions)
        if answers["token"] == "yes":
            questions = [
                inquirer.Text("token", message="Enter your Telegram bot token:"),
            ]
            telegram_token = inquirer.prompt(questions)
            template_params.update({'telegram_bot_token': telegram_token["token"]})
        self.clone_template(selected_template["template_url"], selected_template["template_name"])
        template_custom_inputs = self.ask_template_inputs(selected_template["template_name"])
        if bool(template_custom_inputs):
            template_params.update(template_custom_inputs)
        self.replace_in_folder(
            selected_template["template_name"] + '/skeleton',
            template_params
        )
        self.extract_skeleton(selected_template["template_name"])
        os.rename(os.getcwd() + '/skeleton', app_path)
        self.cleanup(selected_template["template_name"])
        print("Yeepay 🎉, your chatbot is ready!")
        print("You can find it in the " + name + " folder")
