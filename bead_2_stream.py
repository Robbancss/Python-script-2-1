import os


def getBlock(line):
	op = line.find("[[") + 2
	temp = line[op:]
	bCount = 0
	extra = op
	while True:
		oBracket = temp.find("[[") + 2
		cBracket = temp.find("]]")

		if(oBracket == 1):
			if(bCount == 0):
				cl = cBracket
				break
			else:
				bCount -= 1
				extra += cBracket + 2
				temp = temp[cBracket + 2:]
				continue

		elif(oBracket < cBracket):
				bCount += 1
				extra += oBracket
				temp = temp[oBracket:]
				continue
		else:
			if(bCount == 0):
				cl = cBracket
				break
			else:
				bCount -= 1
				extra += cBracket + 2
				temp = temp[cBracket + 2:]
				continue

	return line[op:extra + cl], op, extra + cl


def getFirst(line):
	pv = line.find(";")
	zj = line.find("[[")
	pv = 1000 if pv == -1 else pv
	zj = 1000 if zj == -1 else zj
	return "block" if zj < pv else "cmd"


for row in os.listdir("./"):

	if(row.find(".prog") == -1):
		continue

	file = open(row, "r")
	nf = open(row.replace(".prog", ".py"), "w")

	list = []

	for line in file:
		list.append([0, line.replace("CIKLUS", "for").replace("ELAGAZAS", "if")])

	for i, row in enumerate(list):
		tab = int(row[0])
		line = row[1]
		first = getFirst(line)
		if(first == "cmd"):
			pv = line.find(";")
			if(pv == -1):
				nf.write(" " * 4 * tab + line)
				continue
			else:
				nf.write(" " * 4 * tab + line[:pv] + "\n")
				rest = line[pv + 1:]
				list.insert(i + 1, [tab, rest])
		else:
			block, op, cl = getBlock(line)
			nf.write(" " * 4 * tab + line[:op - 2] + ":" + "\n")
			# print block
			list.insert(i + 1, [tab + 1, block])
			list.insert(i + 2, [tab, line[cl + 2:]])
			# print getBlock(getBlock(line))

	nf.close()