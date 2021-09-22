# warmup

## Usage
invoke with `python3 main.py` while in this repository.
Data will be loaded with `load_data` in `data.py`.


we would make sure that the format of what the user enters follows below

if it doesnt we throw an error

NOTE* spaces are denoted by a dash '-'

president year
president number
president name (spits out everything)
president name vp (spit out vp)
president name party
vice-president year
vice-president number
vice-president name (spits out everything)
vice-president name p (spit out p)
vice-president name party

office year
office number

examples: (return values are all strings in console output)

president year 2012 --> obama
president 11 --> 11th president data
president barack-obama --> spits out everything
(same procedure for vice presidents)
office year 1940 --> president, vice president, party (both parties if different)

To actually query....

user inputs query in syntax described above
we then use an internal data structure (if statements) to fill out a dictionary of SQL references (table, column, where clauses)
then query using blanket SQL statement for code reusability or hard coded per query type

use the `query` function which will parse the user input
then it will figure out what query paramaters are in the input string
then query the table

if the user query is `president year 2012`
we search that string and see that the user requests the president in the year 2012
we would then parse out a dict of `{'table': 'presidents', 'column': 'year', 'clause': 2012}` (interface) *subject to change
which translates to a SQL query (in our case) of `SELECT * FROM presidents WHERE start >= 2012 AND 2012 < end`
