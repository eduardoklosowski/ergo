# -*- coding: utf-8 -*-
#
# Copyright 2015 Eduardo Augusto Klosowski
#
# This file is part of Ergo.
#
# Ergo is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ergo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Ergo.  If not, see <http://www.gnu.org/licenses/>.
#

from __future__ import print_function, unicode_literals

from argparse import ArgumentParser
import os
import shutil
import sys


# Commands

def initconfig():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    print('Criando settings.py... ', end='')
    if os.path.exists('settings.py'):
        print('já existe')
    else:
        shutil.copy(os.path.join(BASE_DIR, 'settings', 'production.py'), 'settings.py')
        print('OK')

    print('Criando manage.py... ', end='')
    if os.path.exists('manage.py'):
        print('já existe')
    else:
        shutil.copy(os.path.join(BASE_DIR, 'settings', 'manage.py'), 'manage.py')
        print('OK')


# Parser

parser = ArgumentParser(prog='python -m ergo')
subparsers = parser.add_subparsers(dest='action')

parser_initconfig = subparsers.add_parser('initconfig', help='Cria arquivos de configuração do Ergo')


def main():
    args = parser.parse_args()

    if args.action == 'initconfig':
        initconfig()
        sys.exit(0)

    parser.print_help()
