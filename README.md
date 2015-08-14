# Decorators and Spam, it's whats for breakfast

This is a presentation on decorators given to DerbyPy, the Greater Louisville,
KY Python Meetup. Find us at https://www.meetup.com/DerbyPy.

## Getting started

Most of the code in this repository runs without any additional packages since
it is just demos, however some require Flask and wrapt. To install all the
dependencies do the following:

**The short version**
- Create a virtualenv
- Run `pip install --use-wheel --no-index --find-links=requirements/wheelhouse -r dev.txt`


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
$ pip install --use-wheel --no-index --find-links=requirements/wheelhouse -r dev.txt
```


## Outline

1. Last things first, where are we going? (/spam)
1. Overview of required Python concepts (/concepts)
    1. Functions
    1. Globals and locals
    1. Scope
    1. Functions in functions
    1. Objects
    1. Closures
1. Understanding decorators. (/decorators)
    1. Simple Decorators
    2. At Runtime
    3. functools
    4. Args & Kwargs
1. Applying decorators to the real world. (/spam)
    1. Flask rate limiting application.

## Helpful references

1. [How you implemented your Python decorator is
   wrong.](http://blog.dscpl.com.au/2014/01/how-you-implemented-your-python.html)
1. [Python Decorators in 12 Steps](http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/)
    - Before you even think about looking at this code, read this article.
1. [functools.wraps docs](https://docs.python.org/2/library/functools.html#functools.wraps)


