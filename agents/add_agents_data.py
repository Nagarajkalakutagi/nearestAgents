import pandas as pd

from agents.serializer import AgentsSerializer


def add_data():
    df = pd.read_csv('agents/agents.csv')
    for k in range(len(df)):
        dt = dict(df.loc[k])
        data = AgentsSerializer(data=dt)

        if data.is_valid():
            data.save()

    return "done"