
with open("moby.txt") as read_file:
	contents = read_file.readlines()
	for line in contents:
		print(line.strip())

with open("groceries.txt", "w") as write_file:
	write_file.writelines(["Apples\n", "Oats\n", "Sugar\n", "Flour\n"])
