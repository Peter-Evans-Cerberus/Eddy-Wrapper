import setuptools

with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name="eddy-mc-wrapper",
    version="0.1.1",
    author="Cerberus Nuclear",
    author_email="nuclear@cerberusnuclear.com",
    description="User Interface wrapper for Eddy, the MCNP and SCALE HTML output converter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Cerberus-Nuclear/Eddy-Wrapper",
    install_requires=['importlib-resources', 'eddy-mc-core'],
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
