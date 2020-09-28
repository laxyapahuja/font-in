import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fontin",
    version="0.0.10",
    author="Laxya Pahuja",
    author_email="laxya.pahuja8@gmail.com",
    description="A better font extractor and installer for bulk fonts in one archive.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/laxyapahuja/font-in",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={'console_scripts': ['fontin=fontin.__main__:main']},
    python_requires='>=3.6',
    install_requires=[
        'pyunpack',
        'patool'
    ],
    project_urls={
        'Documentation': 'https://github.com/laxyapahuja/font-in/README.md',
        'Source': 'https://github.com/laxyapahuja/font-in'
    },
)