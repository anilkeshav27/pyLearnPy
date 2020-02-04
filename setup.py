import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyLearnPy", # Replace with your own username
    version="0.0.1",
    author="Anil Keshav",
    author_email="anilkeshav27@gmail.com",
    description="Enables dynamic code input to learn python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anilkeshav27/pyLearnPy",
    packages=setuptools.find_packages(),
    install_requires=["pynput"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Windows",
    ],
    python_requires='>=3.6',
)