from setuptools import setup

setup(
    name='tornado',
    version='0.2',
    description='Tornado is a fast, scalable and non-blocking python web server',
    author='Facebook',
    author_email='python-tornado@googlegroups.com',
    url='http://www.tornadoweb.org/',
    packages=['tornado'],
    long_description="""
      Tornado is an open source version of the scalable, non-blocking web server and and tools that power FriendFeed
      """,
    classifiers=[
          "License :: OSI Approved :: Apache License 2.0 <http://www.apache.org/licenses/LICENSE-2.0>",
          "Programming Language :: Python",
          "Development Status :: 4 - Beta",
          "Intended Audience :: Developers",
          "Topic :: Internet",
    ],
    keywords='networking web server nonblocking asynchronous python epoll',
    license='Apache License 2.0 <http://www.apache.org/licenses/LICENSE-2.0>',
    install_requires=[
        'setuptools',
        'simplejson',
        'pycurl'
    ],
)