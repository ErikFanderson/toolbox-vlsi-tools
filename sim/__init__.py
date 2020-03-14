#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Erik Anderson
# Email: erik.francis.anderson@gmail.com
# Date: 03/03/2020
"""Docstring for Basic Simulation Tool"""

# Imports - standard library
from abc import ABC, abstractmethod
from typing import Callable, List

# Imports - 3rd party packages
from toolbox.tool import Tool
from toolbox.database import Database
from toolbox.logger import LogLevel

# Imports - local source


class SimTool(Tool):
    """Simulation toolbox tool"""
    def __init__(self, db: Database, log: Callable[[str, LogLevel], None]):
        super(SimTool, self).__init__(self, db, log)

    def steps(self) -> List[Callable[[], None]]:
        """Two simple sim steps prep and run"""
        return [self.prep_sim, self.run_sim]

    @abstractmethod
    def prep_sim(self):
        """Prepare simulation to be run"""
    @abstractmethod
    def run_sim(self):
        """Run the simulation"""
