#! /usr/bin/env python3
##
## Copyright (C) 2016 Logan Paton
## Copyright (C) 2016 David McMackins II
##
##  This program is free software: you can redistribute it and/or modify
##  it under the terms of the GNU Affero General Public License as published by
##  the Free Software Foundation, version 3 only.
##
##  This program is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU Affero General Public License for more details.
##
##  You should have received a copy of the GNU Affero General Public License
##  along with this program.  If not, see <http://www.gnu.org/licenses/>.
##

name = input('Hello! What is your name? ')
emotion = input('How are you feeling today? ')

print('You are ' + name, end=', and you are ')

if emotion.lower() == 'happy':
    print('one happy fellow!')
else:
    print('feeling ' + emotion + '.')
