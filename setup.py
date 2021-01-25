"""Instalador para el paquete "vboxcli"."""

from setuptools import setup

long_description = (
    open('README.txt').read()
    + '\n' +
    open('LICENSE').read()
    + '\n')

setup(
    name="vboxcli",
    version="0.1",
    description="Command Line Interface for VirtualBox API.",
    long_description="",
    #
    classifiers=[
        # ¿Cuan maduro esta este proyecto? Valores comunes son
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        # Indique a quien va dirigido su proyecto
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        # Indique licencia usada (debe coincidir con el "license")
        "License :: OSI Approved :: MIT License",
        # Indique versiones soportas, Python 2, Python 3 o ambos.
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    keywords="ejemplo instalador paquete vboxcli",
    author="Abraham Santos",
    author_email="aesantosterrazas@gmail.com",
    url="https://github.com/abraham-santos/VboxCLI",
    download_url="https://github.com/abraham-santos/VboxCLI.git",
    license="MIT",
    platforms="Unix",
    packages=["vboxcli"],
    include_package_data=True,
    entry_points={
        'console_scripts': ['vboxcli = vboxcli.vboxcli:main']
    }
)