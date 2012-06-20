from setuptools import setup, find_packages

setup(
    name='jmbo-post',
    version='0.1.2',
    description='Jmbo post app.',
    long_description = open('README.rst', 'r').read() + open('AUTHORS.rst', 'r').read() + open('CHANGELOG.rst', 'r').read(),
    author='Praekelt Foundation',
    author_email='dev@praekelt.com',
    license='BSD',
    url='http://github.com/praekelt/jmbo-post',
    packages = find_packages(),
    install_requires = [
        'django-ckeditor>=3.6.2.1',
        'django-generate',
        'jmbo>=0.3',
    ],
    tests_require=[
        'django-setuptest',
    ],
    test_suite='setuptest.SetupTestSuite',
    include_package_data=True,
    classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
)
