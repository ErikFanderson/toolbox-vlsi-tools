#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Erik Anderson
# Email: erik.francis.anderson@gmail.com
# Date: 03/03/2020
"""Docstring for module __init__.py"""

# Imports - standard library
from typing import List, Optional

# Imports - 3rd party packages
import yaml

# Imports - local source
from toolbox.tool import Tool
from dataclasses import dataclass


@dataclass
class Bump:
    name: str
    cell: str
    pg: bool
    net: str
    x: float
    y: float
    orient: str = "r0"


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
    place_halo: Optional[PlaceHalo] = None
    route_halo: Optional[RouteHalo] = None


class FloorplanTool(Tool):
    """Basic simulation tool"""
    def generate_macro_arrays(self,
                              hard_macro_arrays: List[dict]) -> List[dict]:
        """base name should have two {} in them"""
        macros = []
        for macro_array in hard_macro_arrays:
            base_macro = HardMacro(**macro_array["base_macro"])
            for row in range(macro_array["num_rows"]):
                for col in range(macro_array["num_columns"]):
                    macros.append(
                        HardMacro(
                            inst=base_macro.inst.format(r=row, c=col),
                            x=base_macro.x + (macro_array["column_sep"] * col),
                            y=base_macro.y + (macro_array["row_sep"] * row),
                            orient=base_macro.orient,
                            status=base_macro.status,
                            place_halo=base_macro.place_halo,
                            route_halo=base_macro.route_halo).__dict__)
        return macros

    def generate_bump_arrays(self, bump_netlist: dict,
                             bump_arrays: List[dict]) -> List[dict]:
        """base name should have two {} in them"""
        bumps = []
        for bump_array in bump_arrays:
            base_bump = Bump(**bump_array["base_bump"],
                             net="fake_net",
                             pg=False)
            for row in range(bump_array["num_rows"]):
                for col in range(bump_array["num_columns"]):
                    bump_name = base_bump.name.format(r=row, c=col)
                    bumps.append(
                        Bump(name=bump_name,
                             x=base_bump.x + (bump_array["column_sep"] * col),
                             y=base_bump.y + (bump_array["row_sep"] * row),
                             cell=base_bump.cell,
                             pg=bump_netlist[bump_name]["pg"],
                             net=bump_netlist[bump_name]["net"]))
        return bumps
