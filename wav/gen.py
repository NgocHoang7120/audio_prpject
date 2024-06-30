import os
from pathlib import Path

pathDir = "./ver1"
lst = os.listdir(pathDir)

for name in lst:
	if(Path(name).suffix == '.wav')
		with open('readme.txt', 'a') as f:
			data = "python -b 24 -r" + name + " " + name[:-3]
			f.write(data)