# -*- coding: utf-8 -*-
import setuptools

setuptools.setup(
    name='lomadeepy',
    version='0.0.2',
    url='https://github.com/gustavopinho/lomadeepy.git',
    license='MIT License',
    author='Gustavo Pinho',
    author_email='dev@gustavopinho.com',
    keywords='api lomadee python ofertas',
    description=u'Implementação da API de ofertas do lomadee em Python. Não Oficial.',
    package_dir={"": "src"},
    packages=['lomadeepy'],
    install_requires=['requests'],
    test_suite = 'tests',
    tests_require=['requests'],
)