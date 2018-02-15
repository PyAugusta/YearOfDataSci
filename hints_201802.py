def hint1():
    print('''
Regex (Regular Expression) is a pattern matching syntax that is perfect
for parsing data, especially log files. Since we haven't gotten into
Regex yet, this hint is really an answer. Try running this code and
see what you get

import re
import pandas as pd

filepath = 'data/access_log.log'
apache_lines = []

with open(filepath, 'r') as fobj:
    regexp = r'([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})\s\-\s\-\s\[([1-3][0-9]?\/[A-Za-z]{3}\/[0-9]{4}:[0-9]{2}:[0-9]{2}:[0-9]{2})\s\+[0-9]{4}\]\s"([A-Z]+)\s([\S]+)\s(HTTP\/\d\.\d)"\s([1-9][0-9]{2})\s([0-9]{1,10})\s"([^"]+)"\s"([^"]+)"'
    for line in fobj.readlines():
        s = re.search(regexp, line)
        if s:
            apache_lines.append(s.groups())
            
columns = [
    'SRC_HOST', 'UTC_TIME', 'HTTP_TYPE',
    'HTTP_PATH', 'HTTP_VERSION', 'HTTP_RESPONSE',
    'FILE_SIZE', 'DST_HOST', 'BROWSER'
]

apache_df = pd.DataFrame(apache_lines, columns=columns)
apache_df['UTC_TIME'] = pd.to_datetime(apache_df.UTC_TIME, format='%d/%b/%Y:%H:%M:%S')
apache_df.head()
''')
    
def hint2():
    print('''
Probably the easiest way to go about doing this is with the use of the apply method.
It takes a function (usually a lambda), and runs it on each axis in the data (either rowwise or columwise).

For example:

df = pd.DataFrame(['applying', 'functions', 'is', 'cool'], columns=['lower'])
print(df)
       lower
0   applying
1  functions
2         is
3       cool
df['UPPER'] = df.apply(lambda x: x['lower'].upper(), axis=1)
print(df)
       lower      UPPER
0   applying   APPLYING
1  functions  FUNCTIONS
2         is         IS
3       cool       COOL

In this case, we're trying to extract some values from the UTC_TIME field,
so here's your hint:

Use the loc slicer (apache_df.loc[0, 'UTC_TIME']) to grab just one of the 
dates, then check to see which attributes it has. Once you know how to 
get the day of week and hour, use the apply method to create the new columns.
''')
    
def hint3():
    print('''
The groupby method allows us to group a DataFrame based on some unique values.
We can then iterate through the grouped data, performing analysis on each.
For this portion, create an empty DataFrame with the columns you want. Then, fill
in the new DataFrame by looping through all the different groups.

Example:

df = pd.DataFrame(
    [('a', 3), ('a', 75), ('b', 63), ('b', 57)],
    columns=['USER', 'POINTS']
)
users = df.groupby('USER')
new_df = pd.DataFrame(columns=['MAX_POINTS', 'MIN_POINTS', 'COUNT'])
for user, data in users:
    min_points = data['POINTS'].min()
    max_points = data['POINTS'].max()
    user_count = len(data)
    new_df.loc[user, ['MAX_POINTS', 'MIN_POINTS', 'COUNT']] = min_points, max_points, user_count
''')