from setuptools import setup, find_packages
from pathlib import Path

here = Path(__file__).parent

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="termate-ai",
    version="0.1.0",
    author="Heshan Thenura Kariyawasam",
    description="A Linux CLI assistant",
    long_description=long_description,
    long_description_content_type="text/markdown",  
    packages=find_packages(),
    install_requires=[
        "openai",
        "requests"
    ],
    python_requires=">=3.10",
    entry_points={
        "console_scripts": [
            "termate-ai=termate.app:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
        "License :: OSI Approved :: MIT License",
    ],
)
