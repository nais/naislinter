from setuptools import setup

setup(
    name="naislinter",
    version="1.0",
    description="Lints naiserator.yaml files",
    author="Kent Daleng",
    author_email="kent.stefan.daleng@nav.no",
    packages=["naislinter"],
    install_requires=["pyyaml", "requests"],
    scripts=["naislinter/naislinter"],
)
