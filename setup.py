import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()



__version__  = "0.0.0"


REPO_NAME = " TEXT_SUMMARIZER"
AUTHOR_NAME = "Shreyas Mulavekar"
SRC_REPO = "textsummarization"
AUTHOR_MAIL="shreyas.mulavekar232@vit.edu"

setuptools.setup(
    name = SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_MAIL,
    description ="A small project on text summarizer",
    long_description=long_description,
    long_description_content= "text/markdown",
    url = f"https://github.com/DarkCarnages/TEXT_SUMMARIZER",
    project_yrl={
        "Bug Tracker":f"https://github.com/DarkCarnages/TEXT_SUMMARIZER/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")

)