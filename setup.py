from distutils.core import setup

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name="bazingo",
    version="0.0.1",
    description="A `Notebook` replacement for tkinter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Moosems",
    author_email="moosems.j@gmail.com",
    url="https://github.com/Moosems/bazingo",
    packages=["bazingo"],
)
