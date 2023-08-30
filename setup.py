from setuptools import setup, find_packages

setup(
    name="Passkeeper",
    version="1.0",
    description="This application will let you store your passwords safely",
    packages=find_packages(),
    author='Immanuel Kituku',
    author_email='immanuelkituku@gmail.com',
    packages=['app'],
    scripts=['app/main.py'],
)
