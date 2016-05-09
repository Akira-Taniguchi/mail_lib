from setuptools import setup, find_packages

setup(
    name='mail_lib',
    version='1.0.1',
    description='Mail Library',
    long_description='https://pypi.python.org/pypi/mail_lib',
    url='https://github.com/Akira-Taniguchi/mail_lib',
    author='AkiraTaniguchi',
    author_email ='dededededaiou2003@yahoo.co.jp',
    packages=find_packages(),
    license='MIT',
    keywords='mail send smtp address attach',
    classifiers=[
      'Development Status :: 5 - Production/Stable',
      'Programming Language :: Python :: 2.7',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: MIT License'
    ],
    install_requires=['simplejson==3.8.0', 'unicodecsv==0.9.0']
)
