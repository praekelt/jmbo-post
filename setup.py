from setuptools import setup, find_packages

setup(
    name='jmbo-post',
    version='0.3',
    description='Jmbo post application. Post is a synonym for article. It is the most common content type.',
    long_description = open('README.rst', 'r').read() + open('AUTHORS.rst', 'r').read() + open('CHANGELOG.rst', 'r').read(),
    author='Praekelt Foundation',
    author_email='dev@praekelt.com',
    license='BSD',
    url='http://github.com/praekelt/jmbo-post',
    packages = find_packages(),
    install_requires = [
        'django-ckeditor>=4.0.2',
        'django-generate',
        'jmbo>=1.0.8',
        'beautifulsoup4',
        'django-pagination',
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
