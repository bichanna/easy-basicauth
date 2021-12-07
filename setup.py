from setuptools import setup, find_packages
import os

VERSION = "0.1.0"
DESCRIPTION = 'Basic auth for Django'
README = os.path.join(os.path.dirname(__file__), "README.md")

# Setting up
setup(
        name="easy-basicauth",
        version=VERSION,
        author="bichanna",
        author_email="nobu.bichanna@gmail.com",
        description=DESCRIPTION,
        long_description=open(README).read(),
        long_description_content_type="text/markdown",
        url="https://github.com/bichanna/django-basic-auth",
        packages=find_packages(),
        install_requires=[
            "django>=1.8.0",
			"djangorestframework>=3.0.0",
        ],
		license="MIT",
        keywords=["basic-auth", "python", "django", "api"],
        classifiers= [
            'Framework :: Django',
            "Development Status :: 3 - Alpha",
			"Programming Language :: Python :: 3",
        ],
)