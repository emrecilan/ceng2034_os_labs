import os, time, datetime
#yunus emre cilan
#160709008
os.chdir(os.environ['HOME'])
os.mkdir('os_lab_0')
print("os_lab_0 klasörü oluşturuldu.\n")

os.chdir('os_lab_0')
print("os_lab_0 klasörüne girildi.\n")

os.system("touch 1.py")
os.system("touch 2.txt")
print("1.py ve 2.txt dosyaları oluşturuldu.\n")

print("--------Last Modified of All File--------")
for a in os.listdir(os.getcwd()):
	allmodified = os.path.getmtime(a)
	print("Date modified: "+time.ctime(allmodified))
print("\n")
print("-----------Txt Files---------")
for i in os.listdir(os.getcwd()):
	if i.endswith('.txt'):
		print("Txt Files: " + i)
