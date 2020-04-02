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
from toolbox.logger import LogLevel
from dataclasses import dataclass


@dataclass
class Bump:
    name: str
    cell: str
    x: float
    y: float
    net: Optional[str] = None
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

    #--------------------------------------------------------------------------
    # Hard macro methods
    #--------------------------------------------------------------------------
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
                            route_halo=base_macro.route_halo))
        return macros

    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    # Bump methods
    #--------------------------------------------------------------------------
    def create_bump(self, b: dict, netlist: dict, offset_x: float,
                    offset_y: float):
        """
        :param b bump dictionary
        :param netlist bump netlist
        :param offset_x x offset value for bumps 
        :param offset_y y offset value for bumps 
        """
        fplan = self.get_namespace("FloorplanTool")
        b.update({"x": b["x"] + offset_x})
        b.update({"y": b["y"] + offset_y})
        if "net" in b:
            return Bump(**b)
        elif b["name"] in netlist:
            return Bump(**b, net=netlist[b["name"]])
        else:
            self.log(f'Bump "{b["name"]}" not in {fplan}.bump_netlist',
                     LogLevel.ERROR)

    def generate_bumps(self, bumps: List[dict], bump_arrays: List[dict],
                       netlist: dict, offset_x: float,
                       offset_y: float) -> List[dict]:
        """base name should have two {} in them"""
        # Single bumps
        bumps = [
            self.create_bump(b, netlist, offset_x, offset_y) for b in bumps
        ]
        # Bump arrays
        for bump_array in bump_arrays:
            bb = bump_array["base_bump"]
            for row in range(bump_array["num_rows"]):
                for col in range(bump_array["num_columns"]):
                    b_dict = {
                        "name": bb["name"].format(r=row, c=col),
                        "x": bb["x"] + (bump_array["column_sep"] * col),
                        "y": bb["y"] + (bump_array["row_sep"] * row),
                        "cell": bb["cell"]
                    }
                    if "net" in bb:
                        b_dict.update({"net": bb["net"].format(r=row, c=col)})
                    bumps.append(
                        self.create_bump(b_dict, netlist, offset_x, offset_y))
        return bumps

    #--------------------------------------------------------------------------
