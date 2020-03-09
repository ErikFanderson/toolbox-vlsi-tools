{% extends "base.tcl" %}
{% block description %}sim.tcl for "{{tool["top_module"]}}"{% endblock %}
{% block content %}
# Probe all in Value Change Dump (VCD) format
database -vcd -default waves
probe -vcd {{tool["top_module"]}} -depth all -all
run
{% endblock %}
