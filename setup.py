from setuptools import setup, find_packages

setup(
    name="fbh",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["pycryptodome"],
    entry_points={
        "console_scripts": [
            "FBH = fbh.cli:main"
        ]
    },
    author="Mr arman",
    author_email="armanhacker95@gmail.com",
    description="File encryption/decryption tool",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://t.me/TEAM_X_OG",
)