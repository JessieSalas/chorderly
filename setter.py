#outputs a .py file that can be used to store data for the app

with open('sets.py', 'w') as w:
    keys = ['A', 'A#', 'Bb', 'B', 'C', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'F', 'F#', 'Gb', 'G', 'G#', 'Ab']
    modifiers = ['maj7', 'min7', 'susb9', 'maj#4', '7', 'minb6', 'halfdim', 'sus']
    for key in keys: 
        for modifier in modifiers:
            w.write("\t{'type': 'numeric',\n")
            w.write("\t\t'title': '{0}_{1}',\n".format(key,modifier))
            w.write("\t\t'section': 'major_harmony',\n")
            w.write("\t\t'key': '{0}_{1}' }}, \n".format(key,modifier))
