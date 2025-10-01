from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ai-desktop-assistant",
    version="2.0.0",
    author="Md Rasheduzzaman",
    author_email="jmrashed@gmail.com",
    description="A Python-based AI desktop assistant",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jmrashed/ai-desktop-assistant",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
    install_requires=[
        "SpeechRecognition",
        "pyttsx3",
        "gTTS",
        "playsound",
        "pywhatkit",
        "wikipedia-api",
        "requests",
        "psutil",
    ],
    entry_points={
        "console_scripts": [
            "ai-assistant=main:main",
        ],
    },
)