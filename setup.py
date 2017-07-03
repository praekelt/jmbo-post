from setuptools import setup, find_packages

setup(
    name="jmbo-post",
    version="3.0.0",
    description="Jmbo post application. Post is a synonym for article. It is the most common content type.",
    long_description = open("README.rst", "r").read() + open("AUTHORS.rst", "r").read() + open("CHANGELOG.rst", "r").read(),
    author="Praekelt Consulting",
    author_email="dev@praekelt.com",
    license="BSD",
    url="http://github.com/praekelt/jmbo-post",
    packages = find_packages(),
    install_requires = [
        "jmbo>=3.0.0",
        "beautifulsoup4",
        "pypandoc",
        "markdown",
        "django-simplemde"
    ],
    include_package_data=True,
    tests_require=[
        "tox"
    ],
    classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
)
