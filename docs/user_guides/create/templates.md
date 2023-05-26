# 🤖 How to create your own AI templates with Corby

⚡ Creating AI applications has never been easier ⚡

The heart of Corby's internal working are the templates. Everytime you run `corby` on your terminal, you can choose between a variety of templates to start your project.

However, sometimes the predefined templates will just not enough for you. If that's the case, _Worry not!_ 

### 🤔 Where to start?

The only thing you need to do is to create a new github repository for your template. Use this command to create the basic folder structure:

```bash
# From your repository's root folder
echo "" > inputs.json && mkdir skeleton
```

### 🗂️ Structuring your template

Place all your template files (including your docs) under the `skeleton` folder.

There are no predefined rules on how to structure your template files inside this folder. Corby is pretty flexible and he will adapt to whatever architecture you decide 🤗

### 👨‍🔧 Using parameters on your template

One of the best things of Corby templates is that you can use on your code a variety of magic parameters that will be injected on your template auto-magically whenever a new project is created from your template. For example, you could write the following code:

```python
print(f"Hello, I am {{ chatbot_name }} 🤖!")
```

Now if somebody creates a new app called 'Blender' (for example), the new app will have this code:

```python
print(f"Hello, I am Blender 🤖!")
```

[📚 You can find the full list of available corby params here](../../internal/default_parameters.md).

### 🧑‍🔬 Adding your own custom parameters

What happens if I want to use in my template a parameter that doesn't come by default with Corby? 

_Worry not!_ because you can still define your own custom parameters on the `inputs.json` file of your project's root folder.

Let's suppose you want, for example, to parametrize the user's OpenAI token. You would write a `inputs.json` file like this:

```json
[
  {
    "name": "openai_api_key",
    "kind": "text",
    "message": "Paste your OpenAI API key here"
  }
]
```

And voilà! 🪄🔮 Now you can use `{{ openai_api_key }}` on your template code. For example:

```python
import os
os.environ["OPENAI_API_KEY"] = "{{ params.openai_api_key }}"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Translate this into 1. French, 2. Spanish and 3. Japanese: What rooms do you have available?.",
  temperature=0.3,
  max_tokens=100,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)
```

Internally, Corby uses `inquirer` to ask the questions to the users. Logically, the `inputs.json` file follows the same format as `inquirer`. [You can find here the docs](https://python-inquirer.readthedocs.io/en/latest/) to elaborate any kind of question.

