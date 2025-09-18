from setuptools import setup, find_packages

setup(
    name="termate",
    version="0.1.0",
    author="Heshan Thenura Kariyawasam",
    description="A Linux CLI assistant",
    packages=find_packages(),
    install_requires=[
        "openai",
        "requests"
    ],
    python_requires=">=3.10",
    entry_points={
        "console_scripts": [
            "termate=termate.app:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
        "License :: OSI Approved :: MIT License",
    ],
)
