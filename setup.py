from setuptools import setup, find_packages
import os

VERSION = "0.0.1"
DESCRIPTION = 'A library for implementing basic auth to API.'
README = os.path.join(os.path.dirname(__file__), "README.md")

# Setting up
setup(
        name="django-basicauth",
        version=VERSION,
        author="bichanna",
        author_email="nobu.bichanna@gmail.com",
        description=DESCRIPTION,
        long_description=open(README).read(),
        long_description_content_type="text/markdown",
        url="https://github.com/bichanna/django-basicauth",
        packages=find_packages(),
        install_requires=[
            "Django",
			"djangorestframework",
        ], 
		license="MIT",
        keywords=["basic-auth", "python", "django", "api"],
        classifiers= [
            'Framework :: Django',
            "Development Status :: 3 - Alpha",
			"Programming Language :: Python :: 3",
        ],
)