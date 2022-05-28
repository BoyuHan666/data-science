import json

with open('output_file.json','r') as f:
    js = json.load(f)
f.close()
kl = js.keys()
print(len(js[list(kl)[2]]))