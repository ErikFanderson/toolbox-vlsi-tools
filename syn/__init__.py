#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Erik Anderson
# Email: erik.francis.anderson@gmail.com
# Date: 03/03/2020
"""Docstring for module __init__.py"""

# Imports - standard library

# Imports - 3rd party packages

# Imports - local source
from vlsi import VLSITool
from technology import TechTool


class SynTool(VLSITool, TechTool):
    """Basic simulation tool"""
    pass
