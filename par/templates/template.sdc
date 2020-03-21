{% extends "base.tcl" %}
{% block description %}
SDC file for mode "{{mode.name}}" of "{{ts.vlsi.top_module}}"
{% endblock %}
{% block content %}

{% if mode.clocks %}
#--------------------------------------------------------------------
# Clock constraints
#--------------------------------------------------------------------
{% for clock in mode.clocks %}
create_clock {{clock.name}} -name {{clock.name}} -period {{clock.period}}
{% if "uncertainty" in clock %}
set_clock_uncertainty {{clock.uncertainty}} [get_clocks {{clock.name}}]
{% endif %}
{% endfor %}
#--------------------------------------------------------------------

{% endif %}
{% endblock %}
