import pandas as pd

import json

df = pd.read_csv('data/junit/class.csv')

df['Namespace'] = df['LongName'].apply(lambda x: '.'.join(x.split('.')[:-1]))

bugs_by_namespace = df.groupby('Namespace')['Number of Bugs'].sum().to_dict()

sorted_bugs_by_namespace = dict(sorted(bugs_by_namespace.items(), key=lambda item: item[1], reverse=True))


json_output = json.dumps(sorted_bugs_by_namespace, indent=4)

with open("junitBugsGroupBy.json","w") as outfile:
    outfile.write(json_output)