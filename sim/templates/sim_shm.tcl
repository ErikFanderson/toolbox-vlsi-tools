{% extends "base.tcl" %}
{% block description %}sim.tcl for "{{tool["top_module"]}}"{% endblock %}
{% block content %}
# Probe all in Simulation History Manager (SHM) format used by Cadence
database -shm -default waves
probe -shm {{tool["top_module"]}} -depth all -all
run
{% endblock %}
