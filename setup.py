import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Kidney-Disease-Classification-Mlops"
AUTHOR_USER_NAME = "Sourav Kumar"
SRC_REPO = "CNNclassifier"
AUTHOR_EMAIL = "souarvkumar8432@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description="This Project Contains full discribed code for Kidney Disease classification",
    long_description_content="text/markdown",
    url=f"XXXXXXXXXXXXXXXXXXX{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"XXXXXXXXXXXXXXXXXXX{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)