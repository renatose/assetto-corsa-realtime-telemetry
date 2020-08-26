import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="assetto-corsa-realtime-telemetry-renatose",
    version="0.0.1",
    author="Renato Severiano",
    author_email="renatose.com@gmail.com",
    description="Python client for Assetto Corsa Real-time Telemetry",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/renatose/assetto-corsa-realtime-telemetry",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)