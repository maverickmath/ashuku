ashuku is a tool to track a multitude of daily statistics, like mood and 
health. Its design goals are simplicity and fast usage. 
ashuku can draw graphs [citation needed] and analyze data for correlation. 
Data is stored in plain text files in YAML. It's easy to read for both humans 
and machines.

ashuku is named after one of the 5 Wisdom Buddhas, 阿閦如来 (ashuku nyorai). 
He is immovable and reflects all emotions like a mirror, showing things as they 
really are.

ashuku is strongly influenced by todo.txt.

Dependencies
============

* Python 3 (although the code is probably compatible with Python 2.6)
* PyYAML

Usage
=====

ashuku command [arguments]

Any command or argument can be abbreviated. If ashuku is unsure what you mean, 
it will ask for clarification. 

When no command is given, then "show" is assumed.

ashuku will read its configuration from ~/.ashuku. If no such file exists, it
will create one.

Commands
========

add
---
Scores the given attributes, like "add happiness +2 stress -2", or shorter,
"add hap +2 st -2". 

ashuku will also show you all attributes you have not yet scored for this day. 
You should give at least a daily score, but can give as many as you want. 

Using add without arguments only shows the missing attributes.

correlate
---------
Analyzes all attributes for statistical correlation. Takes the amount of days 
to correlate as an optional argument, like "correlate 23". The data is assumed
to be complete when days are given, i.e. attributes of type "cumulative" are
assumed to be 0 when no score for the day exists.

graph
-----
Prints comma-separated data so you can draw a graph. Well, originally, ashuku
would draw it for you, but matplotlib isn't yet Python3-compatible, so...
Works like "show".

show
----
Shows the statistics for the last 2 weeks. Optionally, the first numerical
argument will be interpreted as the amount of days to show, like "show 42". 

You can also specify the attributes you want to show, like "show 42 happiness"
or just "show happiness". If you put a "-" in front of an attribute, it won't be
shown, i.e. "show -happiness" shows everything but happines. 

undo
----
Removes the last addition. Intended for typos. If you want to do more complex 
edits, use a text editor.

Scoring
=======

There are two kinds of attributes: qualitative and quantitative.

quantitative scores are for things that can be easily put in numbers, like your 
weight or time spent studying.

qualitative scores are things you would normally rate as "good" or "bad". To 
make scoring easy, only 5 values are allowed, ranging from -2 to +2. Instead of 
having to precise variables that can't rate efficiently anymore, it's better to 
use more variables. For example, if you think that "mood" is too complex for 
only 5 values, than split up "mood", like "motivation", "happiness" and 
"stress". You will also see more correlations that way.

Normally, attributes have only one score per day. If you input a second one, 
then it will overwrite the old one. The only exception here are cumulative
scores that add up. This is useful when tracking time.

Example
=======

Let's say you use the following config:
    
---
# Each attribute must be of one of the following types:
# - qualitative (range from -2 to +2)
# - quantitative
# - cumulative (like quantitative, but all daily values are added up)
#
# All quantitative types also take the optional property "unit". When given, it
# will also be optional for input, so that "ashuku add weight 78" and
# "ashuku add weight 78kg" are identical.
# The value "time" is used for the format XhYmZs, as in 3h20m10s. When no unit
# is given, then minutes are assumed.
#
# You can also specify an alias via "alias". The normal name will be used for
# the output, but it may be inconvenient to type.
# 
# Also, don't start any name with a "-" or make it a number, k?

attributes:
    happiness:
        type: qualitative
    sleep: 
        type: cumulative
        unit: time
    weight: 
        type: quantitative
        unit: kg
    日本語:
        type: cumulative
        unit: time
        alias: japanese
...

We can add our daily weight:

    # ashuku add weight 82
    Adding: weight 82
    Missing: happiness, sleep, 日本語

Let's take a short nap and study some Japanese.
    
    # ashuku a sle 20m jap 30m
    Adding: sleep 20m
    Adding: 日本語 30m
    Missing: happiness

Note the use of abbreviations.
Having done this, I feel pretty good. So let's add it:

    # ashuku a happ +1
    Adding: happiness 1

Actually, I feel really good. Let's undo it.

    # ashuku undo
    Undoing 2009-09-12 12:24:18:
    -> happiness 1
    # ashuku a happ 2
    Adding: happiness 1

Note that +2 and 2 are identical. 
Let's show our summary for the last 2 days:

    # ashuku show 2  
                | happiness | sleep | weight | 日本語
    ------------+-----------+-------+--------+-------
     2009/09/11 |         - |     - |      - |      -
     2009/09/12 |        +2 |   20m |   82kg |    30m

Config
======

Settings
--------

The config is stored under ~/.ashuku (in YAML, just as the data). You must
specify all attributes and the location of your data as demonstrated in the
previous example. Additionally, you may specify any of the following optional
settings (with defaults shown):

    settings:
        empty cell: none      # text shown instead of an empty cell
        
        hour: h               # \
        min: m                #  > units for hours, minutes and seconds
        sec: s                # /
        
        date format: %Y/%m/%d # must be unique for every day, otherwise 
                              # arbitrary; usual date format syntax

        color_default: white  # see section "Colors"
        color_min: light_red
        color_max: light_red
        color_neg: light_red
        color_pos: light_green
        color_none: red

Attributes
----------

For each attribute, you must define a type, which may either be "qualitative" (a
range from -2 to +2, meant for things like mood), "quantitive" (anything you can
count) or "cumulative". The difference between "quantitive" and "cumulative" is
that "quantitive" has only one associated value per day and any new entry
overwrites the old one, while "cumulative" adds up all values per day.

All quantitative types also take the optional property "unit". When given, it
will also be optional for input, so that "ashuku add weight 78" and "ashuku add
weight 78kg" are identical.  The value "time" is used for the format XhYmZs, as
in 3h20m10s. When no unit is given, then minutes are assumed.

Optional
--------

The following settings can be defined for each attribute, if you want them.

You can specify an alias via "alias". The normal name will be used for the
output, but it may be inconvenient to type.

An attribute can be declared optional by setting "optional" to "true". In this
case, it won't be shown among the missing attributes for the day.

You may declare a "min" and/or "max" value for any quantitative type. If a
values is below "min" or above "max", it will be highlighted. "ashuku add" will
also inform you if a cumulative attribute has not yet reached its "min" value.
The default value for any missing attribute is assumed to be 0.

Colors
------

You may change the default colors. ashuku supports the normal ANSI shell colors,
i.e. black, red, green, brown, blue, purple, cyan and grey. You may prefix any
color with "light_" as well. Note however that light_grey is instead called
white.

The following options for colors are available:

color_default   -> normal text color
color_min       -> color for quantitative values below their "min" value
color_max       -> color for quantitative values above their "max" value
color_neg       -> color for qualitative values below 0
color_pos       -> color for qualitative values above 0
color_none      -> color for missing entries

