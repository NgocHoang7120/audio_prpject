import timeit
from pydub import AudioSegment
from pathlib import Path
import os

path = "path/to/wav/file"
myList = os.listdir(path)

for name in myList:
	if(Path(name.lower()).suffix == '.wav'):
		out = path + "/" + name[:-3] + "mp3" 
		inp = path + "/" + name
		print(out)
		start = timeit.default_timer()
		AudioSegment.from_wav(inp).export(out, format="mp3")
		stop = timeit.default_timer()
		print('Time: ', stop - start) 
 