import pathlib
from setuptools import setup,find_packages

HERE = pathlib.Path(__file__).parent.resolve()

PACKAGE_NAME = "CMoney API"
AUTHOR = "Know Scratcher"
AUTHOR_EMAIL = "yianlee2008@gmail.com"
URL = "https://github.com/KnowScratcher/CMoney-api"
DOWNLOAD_URL = "https://github.com/KnowScratcher/CMoney-api"

LICENSE = "AGPL-3.0"
VERSION = "1.0.0"
DESCRIPTION = "一個股票大富翁的操作API"
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding="utf8")
LONG_DESC_TYPE = "text/markdown"