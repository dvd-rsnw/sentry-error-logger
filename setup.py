from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="sentry-error-logger",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A microapplication demonstrating Sentry integration for error tracking",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/sentry-error-logger",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Debuggers",
        "Topic :: System :: Logging",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.7",
    install_requires=[
        "sentry-sdk>=2.19.2",
        "python-dotenv>=1.0.1",
    ],
    entry_points={
        "console_scripts": [
            "sentry-logger=app:main",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/yourusername/sentry-error-logger/issues",
        "Source": "https://github.com/yourusername/sentry-error-logger",
    },
)