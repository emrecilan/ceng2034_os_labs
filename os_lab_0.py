import os, time, datetime
#yunus emre cilan
#160709008
os.chdir(os.environ['HOME'])
os.mkdir('os_lab_0')
print("os_lab_0 was created.\n")
os.chdir('os_lab_0')
print("os_lab_0 was opened.\n")

os.open("1.py", os.O_CREAT)
os.open("2.txt", os.O_CREAT)
os.open("3.txt", os.O_CREAT)
print("1.py ve 2.txt were created.\n")

print("--------Last Modified of All File--------")
for a in os.listdir(os.getcwd()):
	allmodified = os.path.getmtime(a)
	print(a + ": "+time.ctime(allmodified))
print("\n")
print("-----------Txt Files---------")
for i in os.listdir(os.getcwd()):
	if i.endswith('.txt'):
		print(i)
