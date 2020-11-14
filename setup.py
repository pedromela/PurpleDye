import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PurpleDye",
    version="0.0.1",
    author="Pedro Mela",
    author_email="pedrom39@gmail.com",
    description="PurpleDye Software Developer test",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pedromela/PurpleDye",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['pytest'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    python_requires='>=3.8'
)