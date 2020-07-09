from setuptools import setup

setup(
    name="naislinter",
    version="1.0",
    license="MIT",
    url="https://github.com/chinatsu/naislinter"
    download_url="https://github.com/chinatsu/naislinter/archive/v1.0.tar.gz"
    description="Lints naiserator.yaml files",
    author="Kent Daleng",
    author_email="kent.stefan.daleng@nav.no",
    packages=["naislinter"],
    install_requires=["pyyaml", "requests"],
    scripts=["naislinter/naislinter"],
)