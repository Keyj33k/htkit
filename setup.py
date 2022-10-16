from setuptools import setup

setup(
    name="Hunter-Toolkit",
    author="Keyjeek",
    author_email="K3yjeek@proton.me",
    version="1.1.14",
    description="Assistant for penetration testers",
    license="MIT",
    url="https://github.com/Keyj33k/htkit",
    packages=["src"],
    install_requires=[
        "beautifulsoup4>=4.11.1",
        "phonenumbers>=8.12.57",
        "pyfiglet>=0.8.post1",
        "python-whois>=0.8.0",
        "requests>=2.28.1",
        "termcolor>=2.0.1",
        "psutil>=5.9.2"
    ],
    classifiers=[
        "Intended Audience :: Pentesting/Cybersecurity/Information Gathering/OSINT",
        "License :: MIT",
        "Operating System :: Linux",
        "Programming Language :: Python :: 3.10.6"
    ]
)
