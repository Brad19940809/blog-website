#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Default configurations.
'''

__author__ = 'brad'

configs = {
    'debug': True,
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        # Your password
        'password': '',
        'db': 'awesome'
    },
    'session': {
        'secret': 'Awesome'
    }
}
