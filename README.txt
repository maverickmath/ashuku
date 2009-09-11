ashuku is a tool to track a multitude of daily statistics, like mood and 
health. Its design goals are simplicity and fast usage. ashuku can draw graphs 
and analyze data for correlation. Data is stored in plain text files in an easy 
to read (for both humans and machines) format.

ashuku is named after one of the 5 Wisdom Buddhas, 阿閦如来 (ashuku nyorai). 
He is immovable and reflects all emotions like a mirror, showing things as they 
really are.

ashuku is strongly influenced by todo.txt.

Dependencies
============

* Python 3 (although the code is probably compatible with Python 2.6)
* PyYAML
* matplotlib (optional, for drawing graphs)

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

correlate
---------
Analyzes all attributes for statistical correlation.

graph
-----
Graphs the statistics for the last 2 weeks. Takes the amount of days to graph as 
an optional argument, like "graph 23".

show
----
Shows the statistics for the last 2 weeks. Takes the amount of days to show as 
an optional argument, like "show 42". You can also specify the attributes you
want to show, like "show 42 happiness" or just "show happiness".

undo
----
Removes the last addition. Intended for typos. If you want to do more complex 
edits, use a text editor.

Scoring
=======

There are two kinds of attributes: qualitive and quantitive.

Quantitive scores are for things that can be easily put in numbers, like your 
weight or time spent studying.

Qualitive scores are things you would normally rate as "good" or "bad". To make 
scoring easy, only 5 values are allowed, ranging from -2 to +2. Instead of 
having to precise variables that can't rate efficiently anymore, it's better to 
use more variables. For example, if you think that "mood" is too complex for 
only 5 values, than split up "mood", like "motivation", "happiness" and 
"stress". You will also see more correlations that way.

Example
=======

Let's say you use the following config:
    
---
# Each attribute must be of one of the following types:
# - qualitive (range from -2 to +2)
# - quantitive
# - cumulative (like quantitive, but all daily values are added up)
#
# All quantitive types also take the optional property "unit". When given, it
# will also be optional for input, so that "ashuku add weight 78" and
# "ashuku add weight 78kg" are identical.
# The value "time" is used for the format XhYmZs, as in 3h20m10s. When no unit
# is given, then minutes are assumed.
#
# You can also specify an alias via "alias". The normal name will be used for
# the output, but it may be inconvenient to type.

attributes:
    happiness:
        type: qualitive
    sleep: 
        type: cumulative
        unit: time
    weight: 
        type: quantitive
        unit: kg
    日本語:
        type: cumulative
        unit: time
        alias: japanese
...

We can add our daily weight:

    # ashuku add weight 82kg
    Score for weight added. 
    Missing: happiness, sleep, 日本語.

Let's take a short nap and study some Japanese.
    
    # ashuku a sle 20m jap 30m
    Scores for sleep and 日本語 added. 
    Missing: happiness.

Note the use of abbreviations.
Having done this, I feel pretty good. So let's add it:

    # ashuku happ +1
    Score for happiness added.

Actually, I feel really good. Let's undo it.

    # ashuku undo
    Undone: happiness +1.
    # ashuku happ 2
    Score for happiness added.

Note that +2 and 2 are identical. 
Let's show our summary for today:

    # ashuku show 1  
    #TODO :)
