import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="purpledye",
    version="0.0.1",
    author="Pedro Mela",
    author_email="pedrom39@gmail.com",
    description="PurpleDye Software Developer test",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pedromela/purpledye",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8'
)