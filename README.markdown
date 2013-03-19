# django-s3-collectstatic

This package includes a management command `fasts3collectstatic` that is
intended for use with the S3BotoStorage storage backend. When checking if a
file already exists it uses the S3 etag for comparison instead of the default
modified time. This is especially useful when deploying to Heroku, since Heroku
changes the modified time when deploying.

The code is based on [this Django snippet](http://djangosnippets.org/snippets/2889/)
with some fixes and packaging.


## Installation

Clone the [Git repository](https://github.com/agoodid/django-s3-collectstatic)
or use pip to install:

    pip install git+git://github.com/AGoodId/django-s3-collectstatic.git#egg=django-s3-collectstatic

In `settings.py`:

    STATICFILES_STORAGE ="storages.backends.s3boto.S3BotoStorage"
    AWS_PRELOAD_METADATA = True

    INSTALLED_APPS = [
        # ...
        'django_s3_collectstatic',
    ]

