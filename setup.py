from setuptools import setup, find_packages
with open("README.md", "r") as c:
    page_description = c.read()

with open("requirements.txt") as c:
    requirements = c.read().splitlines()

setup(
    name="Pacotes de Imagens com Python",
    version="0.0.1",
    author="cleison",
    description="Esse pacote oferece recurso para criar um pacote, ou criar uma distribuição binária ou distribuição de código fonte",
    long_description_content_type="text/markdown",
    url="https://github.com/Csantos05/image-processing-package.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.10'

)
