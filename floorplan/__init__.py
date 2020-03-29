#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Erik Anderson
# Email: erik.francis.anderson@gmail.com
# Date: 03/03/2020
"""Docstring for module __init__.py"""

# Imports - standard library
from typing import List

# Imports - 3rd party packages
import yaml

# Imports - local source
from toolbox.tool import Tool
from dataclasses import dataclass


@dataclass
class PlaceHalo:
    top: int
    bottom: int
    right: int
    left: int


@dataclass
class RouteHalo:
    space: int
    bottom_layer: str
    top_layer: str


@dataclass
class HardMacro:
    inst: str
    x: int
    y: int
    orient: str
    status: str
    place_halo: PlaceHalo
    route_halo: RouteHalo


class FloorplanTool(Tool):
    """Basic simulation tool"""
    def generate_macros_2d(self, base_macros: List[dict]) -> List[dict]:
        """base name should have two {} in them"""
        macros = []
        for macro in base_macros:
            base_macro = HardMacro(**macro["base_macro"])
            for row in range(macro["num_rows"]):
                for col in range(macro["num_columns"]):
                    macros.append(
                        HardMacro(inst=base_macro.inst.format(r=row, c=col),
                                  x=base_macro.x + (macro["column_sep"] * col),
                                  y=base_macro.y + (macro["row_sep"] * row),
                                  orient=base_macro.orient,
                                  status=base_macro.status,
                                  place_halo=base_macro.place_halo,
                                  route_halo=base_macro.route_halo).__dict__)
        return macros
