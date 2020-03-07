#!/usr/bin/env bash

# Set PYTHONPATH accordingly
if [ -z "$PYTHONPATH" ]
then
    export PYTHONPATH=$PWD
else
    export PYTHONPATH=$PWD:$PYTHONPATH
fi

# Set MYPYPATH accordingly
if [ -z "$MYPYPATH" ]
then
    export MYPYPATH=$PWD/toolbox-vlsi-tools
else
    export MYPYPATH=$PWD/toolbox-vlsi-tools:$MYPYPATH
fi

# Set TOOLBOX-VLSI-TOOLS_HOME variable
export TOOLBOX-VLSI-TOOLS_HOME=$PWD
