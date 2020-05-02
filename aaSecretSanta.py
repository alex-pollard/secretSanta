import random
print ("Enter names, separated by a space :)")
names = [x for x in input().split()]
#names = ["Alex", ""]
new_list = list(names)
	#creates two identical lists of participants
for x in names:
	#iterates through list of names
	while True:
		number = random.randint(0,(len(new_list)-1))
		if x != new_list[number]:
			break
		elif len(new_list) == 1:
			print("Error: Last name is only name avaliable. Please delete created text files and run program again. :)")
			exit()
			#while loop should not be exited if the random number picks x's index
	#print("giving " + x + " person: " + new_list[number])
		#printout of results
	name = (new_list[number])
		#name stores the chosen name, to be written
	new_list.remove(name)
		#removes name from list after chosen
	with open(x+".txt", 'xt') as f:
			#creates a new file with the gifter's name, containing the recipients name
		f.write(name)
		f.close()
print("Merry Christmas!!!")
