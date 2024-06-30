import csv
import matplotlib.pyplot as plt

header = []
ecdc = []
flac = []
mp3 = []
wav = []

def read_csv(file_path):
	with open(file_path, mode='r', newline='') as file:
		reader = csv.reader(file)
		h = next(reader)
		
		for el in h:
			header.append(el)
       
		for row in reader:
			e = row[1].split(';')
			ecdc.append((int(e[0]), float(e[1])))

			f = row[2].split(';')
			flac.append((int(f[0]), float(f[1])))

			m = row[3].split(';')
			mp3.append((int(m[0]), float(m[1])))

			wav.append(int(row[4]))

def draw_csv(name, unit, mode = 0):
	print(header)
	x = [i for i in range(len(ecdc))]
	y1 = [item[mode] for item in ecdc]
	y2 = [item[mode] for item in flac]
	y3 = [item[mode] for item in mp3]

	plt.figure(figsize=(12, 9)) # tỷ lệ khung hình

	if mode == 0:
		y4 = [item for item in wav]
		plt.plot(x, y4, color='#7c3aed', label=f'{header[4]}')  # wav

	# Vẽ đồ thị với màu sắc và chú thích
	plt.plot(x, y1, color='blue', label=f'{header[1]}')  # ecdc
	plt.plot(x, y2, color='red', label=f'{header[2]}')   # flac
	plt.plot(x, y3, color='#16a34a', label=f'{header[3]}')  # mp3

	# Thêm tiêu đề và nhãn
	plt.title(f'{name}')
	plt.xlabel('Index')
	plt.ylabel(f'"{unit}')

	if mode == 0:
		for i, (xi, y1i, y2i, y3i, y4i) in enumerate(zip(x, y1, y2, y3, y4)):
			plt.text(xi, y1i, f'{y1i}', ha='right', va='top', fontsize=8, color='blue')
			plt.text(xi, y2i, f'{y2i}', ha='left', va='bottom', fontsize=8, color='red')
			plt.text(xi, y3i, f'{y3i}', ha='right', va='bottom', fontsize=8, color='#16a34a')
			plt.text(xi, y4i, f'{y4i}', ha='right', va='bottom', fontsize=8, color='#7c3aed')
	else:
		for i, (xi, y1i, y2i, y3i) in enumerate(zip(x, y1, y2, y3)):
			plt.text(xi, y1i, f'{y1i}', ha='right', va='top', fontsize=8, color='blue')
			plt.text(xi, y2i, f'{y2i}', ha='left', va='bottom', fontsize=8, color='red')
			plt.text(xi, y3i, f'{y3i}', ha='right', va='bottom', fontsize=8, color='#16a34a')

	plt.xticks(x, x)
	# plt.yticks(range(0, int(max(max(y1), max(y2), max(y3))) + 100, 100))
	
	plt.legend() # Hiển thị chú thích (legend)
	plt.grid(True) # lưới

	plt.savefig(f'{unit}.png')
	plt.close()
	#plt.show() 


file_path = 'info.csv' 
if __name__ == '__main__':
	read_csv(file_path)
	draw_csv("Biểu đồ dung lượng", "(Kb)", mode = 0)
	draw_csv("Biểu đồ thời gian thực thi", "(s)", mode = 1)
