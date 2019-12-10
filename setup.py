# -*- coding: utf-8 -*-
import setuptools

setuptools.setup(
    name='api-lomadee-v3',
    version='0.0.1',
    url='https://github.com/gustavopinho/api-lomadee-v3',
    license='MIT License',
    author='Gustavo Pinho',
    author_email='gustavopinho@gustavopinho.com',
    keywords='api lomadee python ofertas',
    description=u'Implementação da API de ofertas do lomadee em Python.',
    packages=setuptools.find_packages(),
    install_requires=['requests'],
)