'Regular expressions'

import re

with open('notestdd/team_history.txt') as f:
    hist = f.read()

scores = [int(score) for score in re.findall(r'(\d+) point', hist)]
dates = re.findall(r'[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}', hist)
record = re.findall(r'won|lost', hist)

print(f'We played {len(dates)} games this season from {dates[0]} to {dates[-1]}')
print(f'We scored {sum(scores)} goals this season. Our worst was {min(scores)} and best was {max(scores)}')
print(f'We {record[0]} the first game and {record[-1]} the last game for a {record.count("won")}-{record.count("lost")} record')
