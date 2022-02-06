#!/bin/bash -eu

DEPS="wheel pytest pytest-django pytest-cov pytest-splinter"

if python --version | grep -q "Python 2.7"; then
  DEPS="$DEPS django-appconf<=1.0"
fi

if   [ $DJANGO_VERSION = 1.11 ]; then DEPS="$DEPS django>=1.11,<2   django-select2<7"
elif [ $DJANGO_VERSION = 2.0  ]; then DEPS="$DEPS django>=2.0,<2.1  django-select2<7.2"
elif [ $DJANGO_VERSION = 2.1  ]; then DEPS="$DEPS django>=2.1,<3    django-select2<7.2"
elif [ $DJANGO_VERSION = 3.0  ]; then DEPS="$DEPS django>=3.0,<3.1  django-select2<7.5"
elif [ $DJANGO_VERSION = 3.1  ]; then DEPS="$DEPS django>=3.1,<4    django-select2"
elif [ $DJANGO_VERSION = 4.0  ]; then DEPS="$DEPS django>=4,<5      django-select2"
else echo "Unknown Django version $DJANGO_VERSION"; exit 1
fi

DEPS="$(echo $DEPS | tr ' ' '\n')"
if [ $SELECT2 = true ]; then
  echo "$DEPS"
else
  echo "$DEPS" | grep -v select2
fi
