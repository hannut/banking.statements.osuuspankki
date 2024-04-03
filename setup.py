import os

from setuptools import setup

VERSION = "1.3.4.dev0"

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open(os.path.join("docs", "HISTORY.txt"), "r", encoding="utf-8") as f:
    history = f.read()

setup(
    name="banking.statements.osuuspankki",
    version=VERSION,
    description="Account statement reader plugin for Osuuspankki of Finland",
    long_description=long_description + "\n" + history,
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Natural Language :: English",
        "Topic :: Office/Business :: Financial :: Accounting",
        "Topic :: Utilities",
        "Environment :: Console",
        "Operating System :: OS Independent",
    ],
    keywords=["ofxstatement", "ofx"],
    author="Petri Savolainen",
    author_email="petri.savolainen@koodaamo.fi",
    url="https://github.com/koodaamo/banking.statements.osuuspankki",
    license="GPLv3",
    namespace_packages=["banking", "banking.statements"],
    packages=["banking.statements.osuuspankki"],
    include_package_data=True,
    zip_safe=False,
    install_requires=["setuptools", "ofxstatement"],
    entry_points="""
          [ofxstatement]
          op = banking.statements.osuuspankki.plugin:OPPlugin
      """,
)
