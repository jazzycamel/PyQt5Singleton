from setuptools import setup

setup(
    name="PyQt5Singleton",
    version="0.1",
    author="Rob Kent",
    author_email="jazzycamel@googlemail.com",
    description="A simple singleton implementation to work with PyQt5",
    license="MIT",
    url="https://github.com/jazzycamel/PyQt5Singleton",
    packages=['PyQt5Singleton'],
    install_requires=["PyQt5","sip"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "License :: OSI Approved :: MIT License",
    ]
)
