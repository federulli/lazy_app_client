from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="lazy_app_client",
    install_requires=required,
    version="1.0.0",
    author="Federico Rulli",
    author_email="fede.rulli@gmail.com",
    packages=find_packages()
)
