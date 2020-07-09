from setuptools import setup

setup(
    name="naislinter",
    version="1.0.1",
    license="MIT",
    url="https://github.com/chinatsu/naislinter",
    description="Lints naiserator.yaml files",
    author="Kent Daleng",
    author_email="kent.stefan.daleng@nav.no",
    packages=["naislinter"],
    install_requires=["pyyaml", "requests"],
    scripts=["naislinter/naislinter"],
)
