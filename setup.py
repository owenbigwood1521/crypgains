import setuptools

setuptools.setup(
    name="crypgains-obigwood1521",
    version="0.0.1",
    author="Owen Bigwood",
    author_email="owenbigwood1521gmail.com",
    description="Calculating Cryptocurrency taxible gains",
    url=None,
    project_urls=None
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
)


