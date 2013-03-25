from distutils.core import setup
import setuptools
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="django-s3-collectstatic",
    version="1.0",
    description="",
    author="AGoodId",
    author_email="teknik@agoodid.com",
    maintainer="AGoodId",
    maintainer_email="teknik@agoodid.com",
    url="https://github.com/agoodid/django-s3-collectstatic",
    license="MIT",
    packages=[
        "django_s3_collectstatic",
        "django_s3_collectstatic.management",
        "django_s3_collectstatic.management.commands",
    ],
    long_description=read("README.markdown"),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
    ],
)
