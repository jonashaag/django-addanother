#!/bin/bash -eu

DEPS="wheel pytest pytest-django pytest-cov pytest-splinter"
if python --version | grep -q "Python 2.7"; then
  DEPS="$DEPS django-appconf<=1.0"
fi
if [ $DJANGO_VERSION = 1.11 ]; then
  DEPS="$DEPS django-select2<7"
else
  DEPS="$DEPS django-select2"
fi
if   [ $DJANGO_VERSION = 1.11 ]; then DEPS="$DEPS django>=1.11,<2"
elif [ $DJANGO_VERSION = 2.0 ]; then DEPS="$DEPS django>=2.0,<2.1"
elif [ $DJANGO_VERSION = 2.1 ]; then DEPS="$DEPS django>=2.1,<3"
elif [ $DJANGO_VERSION = 3.0 ]; then DEPS="$DEPS django>=3.0,<3.1"
elif [ $DJANGO_VERSION = 3.1 ]; then DEPS="$DEPS django>=3.1,<4"
elif [ $DJANGO_VERSION = 4.0 ]; then DEPS="$DEPS django>=4,<5"
fi

echo $DEPS | tr ' ' '\n'
