import pathlib
from setuptools import setup,find_packages

HERE = pathlib.Path(__file__).parent.resolve()

PACKAGE_NAME = "cmoney-api"
AUTHOR = "Know Scratcher"
AUTHOR_EMAIL = "yianlee2008@gmail.com"
URL = "https://github.com/KnowScratcher/CMoney-api"
DOWNLOAD_URL = "https://github.com/KnowScratcher/CMoney-api"

LICENSE = "AGPL-3.0"
VERSION = "1.0.0"
DESCRIPTION = "一個股票大富翁的操作API"
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding="utf8")
LONG_DESC_TYPE = "text/markdown"

requirements = (HERE / "requirements.txt").read_text(encoding="utf8")
INSTALL_REQUIRES = [s.strip() for s in requirements.split("\n")]
 
# dev_requirements = (HERE / "dev_requirements.txt").read_text(encoding="utf8")
# EXTRAS_REQUIRE = {"dev": [s.strip() for s in dev_requirements.split("\n")]}
 
CLASSIFIERS = [f"Programming Language :: Python :: 3.{str(v)}" for v in range(7, 12)]
PYTHON_REQUIRES = ">=3.7"

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    license=LICENSE,
    author_email=AUTHOR_EMAIL,
    url=URL,
    download_url=DOWNLOAD_URL,
    python_requires=PYTHON_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    # extras_require=EXTRAS_REQUIRE,
    packages=find_packages(),
    classifiers=CLASSIFIERS,
)