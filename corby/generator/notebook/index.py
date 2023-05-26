"""Creates a new notebook"""

import inquirer
from ..base import BaseGenerator

class NotebookGenerator(BaseGenerator):
    """Jupyter Notebook manager"""

    def get_templates(self):
        return {
            # pylint: disable=line-too-long
           'langchain-web-chatbot': 'https://github.com/corby-templates/langchain-web-chatbot.git'
    }

    def create_notebook(self, name):
        '''Calls super.create() to generate a new notebook
        we may have custom logic here on the future'''
        return super().create(name)

def create_notebook():
    """Ask the user for the template and creates a new notebook"""
    questions = [
        inquirer.Text("name", message="Name of your notebook:"),
    ]
    answers = inquirer.prompt(questions)
    NotebookGenerator().create_notebook(answers['name'])
