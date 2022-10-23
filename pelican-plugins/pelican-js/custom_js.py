#!/usr/bin/env python3
# pelican-js: embed custom JavaScript easily
# Copyright (C) 2017 Jorge Maldonado Ventura

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Embed JavaScript files for Pelican
==================================

This plugin allows you to easily embed JavaScript files in the header (<head>)
or in the body (<body>) of individual articles or pages. The JavaScript files
are embedded using the <script> tag.
"""

import os
import re
import shutil

from pelican import signals


def format_js(gen, metastring, formatter):
    """
    Create a list of URL-formatted script tags
    Parameters
    ----------
    gen: generator
        Pelican Generator
    metastring: string
        metadata['js']
    formatter: string
        String format for output.
    Output
    ------
    List of formatted strings
    """
    metalist = metastring.replace(' ', '').split(',')
    site_url = '%s'
    position_regex = re.compile('(\(\w+\)$)')

    formatted_strings = []
    for i in range(len(metalist)):
        pos = position_regex.search(metalist[i]).group()
        format_string = formatter.format(site_url, metalist[i][:-len(pos)], pos)
        formatted_strings.append(format_string)
    return formatted_strings


def copy_resources(src, dest, file_list):
    """
    Copy files from content folder to output folder
    Parameters
    ----------
    src: string
        Content folder path
    dest: string,
        Output folder path
    file_list: list
        List of files to be transferred
    Output
    ------
    Copies files from content to output
    """
    if not os.path.exists(dest):
        os.makedirs(dest)
    for file_ in file_list:
        file_src = os.path.join(src, file_)
        shutil.copy2(file_src, dest)


def add_tags(gen, metadata):
    """
    It will add the JS to the article or page
    """
    if 'js' in metadata.keys():
        script = '<script src="{0}/js/{1}"></script>{2}'
        metadata['js'] = format_js(gen, metadata['js'], script)


def move_resources(gen):
    """
    Move JS files from js folder to output folder
    """
    js_files = gen.get_files('js', extensions='js')

    js_dest = os.path.join(gen.output_path, 'js')
    copy_resources(gen.path, js_dest, js_files)


def register():
    """
    Plugin registration
    """
    signals.article_generator_context.connect(add_tags)
    signals.page_generator_context.connect(add_tags)
    signals.article_generator_finalized.connect(move_resources)
