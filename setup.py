from setuptools import setup

from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md")) as f:
    long_description = f.read()

setup(
    name="naislinter",
    version="1.0.2",
    license="MIT",
    url="https://github.com/chinatsu/naislinter",
    description="Lints naiserator.yaml files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Kent Daleng",
    author_email="kent.stefan.daleng@nav.no",
    packages=["naislinter"],
    install_requires=["pyyaml", "requests"],
    scripts=["naislinter/naislinter"],
)
