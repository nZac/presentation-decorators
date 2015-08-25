# Decorators and Spam, it's whats for breakfast

This is a presentation on decorators given to DerbyPy, the Greater Louisville,
KY Python Meetup. Find us on [Meetup](https://www.meetup.com/DerbyPy).

## Getting started

This code uses iPython notebook for the demonstration. If you want to run the
examples you will need to install the dependencies. The dependencies come
prepackaged with the repo.

**The short version**
- Create a virtualenv
- Run `pip install --use-wheel --no-index --find-links=requirements/wheelhouse -r requirements/dev.txt`


**The long version**
```sh
# Ensure you have virtualenv installed (your path might vary)
$ which virtualenv
/Users/nzac/.pyenv/shims/virtualenv

# If you don't have virtualenv install it with `pip install virtualenv`

# Create a temporary virtual environment (you can create a named virtualenv if
# you would like)
$ mktmpenv
New python executable in tmp-ea1247c37e99d568/bin/python2.7
Also creating executable in tmp-ea1247c37e99d568/bin/python
Installing setuptools, pip, wheel...done.
This is a temporary environment. It will be deleted when you run 'deactivate'.

# Ensure you have the latest version of pip and wheel since wheel packages vary
$ pip install -U pip wheel

# Now install the dependencies
$ pip install --use-wheel --no-index --find-links=requirements/wheelhouse -r requirements/dev.txt
```

**If you don't care about using the wheelhouse...**
- Create a virtualenv
- Run `pip install -r requirements/dev.txt`

## Outline

1. Overview of required Python concepts (Concepts.ipynb)
1. A simple functional decorator with Flask (/spam)

## Helpful references

1. [Python Decorators in 12 Steps](http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/)


