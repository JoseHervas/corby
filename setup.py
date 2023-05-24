from setuptools import setup, find_packages

python_requires='>=3.6',

setup(
    name="norby",
    version="0.0.0",
    description="⚡ Create your LLMs applications from zero to deploy in minutes ⚡",
    author="Jose Hervás Díaz",
    author_email='jhervasdiaz@gmail.com',
    license='BSD 2-clause',
    packages=find_packages(),
    install_requires=[
        "inquirer",
        "jinja2"
    ],
)
