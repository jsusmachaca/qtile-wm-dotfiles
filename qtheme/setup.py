from setuptools import setup, find_packages


setup(
    name="qtheme",
    version="1.0",
    description="Tools for management qtile environment",
    author="jsusmachaca",
    author_email="falcorgd@gmail.com",
    license="MIT",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "qtheme = qtheme.main:main"
        ]
    },
)
