
#format variable name (limit to 10) rgb(__, __, ___ )

from random import randint
from PIL import Image
import ast
from math import ceil

s = """

for i in range(0,11):
	if i %2==0:
		print('{} is even'.format(i))
	else:
		print('{} is gay'.format(i))

listoftuples = []
colors = {"def":(0,255,0),"iffor":(255,105,180), "print":(255, 255, 0),"variablename":(138,43,226), "int":(255,0,0),"string":(255,140,0), "exp":(0,0,255)}
def run(s):
	#stmts = ast.parse(s).body
	count = 0
	stmts = s.split("\n")
	for i in range(stmts.count("")):
		stmts.remove("")

	#processing
	identation = {}
	oldindent = 0
	for i in stmts:
		count = 0
		indent,i = counttabs(i)
		print(i)
		if indent in identation.keys():
			if identation[indent] != "":
				print("evalling old stuff")
				eval(identation[indent])
				identation[indent] = ""

		if i[:3]== "def":
			print("def")
			i = i.replace(" ","")
			for char in i[i.find("f")+1:]:
				count += 1
				listoftuples.append( colors["def"] + (ord(char)*2,) )
			print(count)
			
			identation[indent] = "listoftuples.append("+ str(colors["def"]+(255,)) + ")"
		elif i[:2] == "if" or i[:3] == "for" or i[:4] == "elif" or i[:4] == "else":
			print("iffor")
			i = i.replace(" ","")
			
			if i[:2] == "if":
				for char in i[2:]:
					count += 1
					listoftuples.append( colors["iffor"] + (ord(char)*2,) )
				print(count)
			elif i[:3] == "for":
				for char in i[3:]:
					count += 1
					listoftuples.append( colors["iffor"] + (ord(char)*2,) )
				print(count)
			elif i[:4] == 'elif':
				for char in i[4:]:
					count += 1
					listoftuples.append( colors["iffor"] + (ord(char)*2,) )
				print(count)
			else:
				for char in i[5:]:
					count += 1
					listoftuples.append( colors["iffor"] + (ord(char)*2,) )
				print(count)

			identation[indent] = "listoftuples.append(" + str(colors["iffor"]+(255,)) + ")"
		elif "print" in i:
			print("print statement")
			i=i.replace(" ","")
			for char in i[i.find("t")+1:]:
				count +=1
				listoftuples.append( colors["print"] + (ord(char)*2,) )
			print(count)
		else:
			if "=" in i:
				print("assignment")
				variablename = i[:i.find("=")].replace(" ","")

				print(variablename)
				for char in variablename:
					count +=1
					listoftuples.append( colors["variablename"] + (ord(char)*2,) )
				print(count)

				
				value = i[i.find("=")+1:].replace(" ","")

				try:
					value = int(value)
					print("int")
					for char in str(value):
						count +=1
						listoftuples.append( colors["int"]+(ord(char)*2,) )
					print(count)
				except:
					for char in value:
						count +=1
						listoftuples.append( colors["string"]+(ord(char)*2,))
					print(count)
			else:
				print("random expression")
				for char in i:
					count+=1
					listoftuples.append( colors["exp"] +(ord(char)*2,))
				print(count)
		
		oldindent = indent

	for item in reversed(list(identation.keys())):
		if identation[item] != "":
			eval(identation[item])
			identation[item] = ""
	

def counttabs(mystring):
	counter = 0
	while True:
		if mystring.find("\t") != 0:
			break
		else:
			counter+=1
			mystring = mystring[1:]
	return counter,mystring

run(s)

w = ceil(len(listoftuples)**0.5)
h = w
im = Image.new("RGBA",(w,h),color="white")

pixels = im.load()
col = -1
print(len(listoftuples),im.size[0],im.size[0])
for i in range(len(listoftuples)):
	newnum = i%im.size[0]
	if newnum == 0:
		col += 1
	pixels[newnum,col] = listoftuples[i]

im.show()



            
"""


listoftuples = []
colors = {"def":(0,255,0),"iffor":(255,105,180), "print":(255, 255, 0),"variablename":(138,43,226), "int":(255,0,0),"string":(255,140,0), "exp":(0,0,255)}
def run(s):
	#stmts = ast.parse(s).body
	count = 0
	stmts = s.split("\n")
	for i in range(stmts.count("")):
		stmts.remove("")

	#processing
	identation = {}
	oldindent = 0
	for i in stmts:
		count = 0
		indent,i = counttabs(i)
		print(i)
		if indent in identation.keys():
			if identation[indent] != "":
				print("evalling old stuff")
				eval(identation[indent])
				identation[indent] = ""

		if i[:3]== "def":
			print("def")
			i = i.replace(" ","")
			for char in i[i.find("f")+1:]:
				count += 1
				listoftuples.append( colors["def"] + (ord(char)*2,) )
			print(count)
			
			identation[indent] = "listoftuples.append("+ str(colors["def"]+(255,)) + ")"
		elif i[:2] == "if" or i[:3] == "for" or i[:4] == "elif" or i[:4] == "else":
			print("iffor")
			i = i.replace(" ","")
			
			if i[:2] == "if":
				for char in i[2:]:
					count += 1
					listoftuples.append( colors["iffor"] + (ord(char)*2,) )
				print(count)
			elif i[:3] == "for":
				for char in i[3:]:
					count += 1
					listoftuples.append( colors["iffor"] + (ord(char)*2,) )
				print(count)
			elif i[:4] == 'elif':
				for char in i[4:]:
					count += 1
					listoftuples.append( colors["iffor"] + (ord(char)*2,) )
				print(count)
			else:
				for char in i[5:]:
					count += 1
					listoftuples.append( colors["iffor"] + (ord(char)*2,) )
				print(count)

			identation[indent] = "listoftuples.append(" + str(colors["iffor"]+(255,)) + ")"
		elif "print" in i:
			print("print statement")
			i=i.replace(" ","")
			for char in i[i.find("t")+1:]:
				count +=1
				listoftuples.append( colors["print"] + (ord(char)*2,) )
			print(count)
		else:
			if "=" in i:
				print("assignment")
				variablename = i[:i.find("=")].replace(" ","")

				print(variablename)
				for char in variablename:
					count +=1
					listoftuples.append( colors["variablename"] + (ord(char)*2,) )
				print(count)

				
				value = i[i.find("=")+1:].replace(" ","")

				try:
					value = int(value)
					print("int")
					for char in str(value):
						count +=1
						listoftuples.append( colors["int"]+(ord(char)*2,) )
					print(count)
				except:
					for char in value:
						count +=1
						listoftuples.append( colors["string"]+(ord(char)*2,))
					print(count)
			else:
				print("random expression")
				for char in i:
					count+=1
					listoftuples.append( colors["exp"] +(ord(char)*2,))
				print(count)
		
		oldindent = indent

	for item in reversed(list(identation.keys())):
		if identation[item] != "":
			eval(identation[item])
			identation[item] = ""
	

def counttabs(mystring):
	counter = 0
	while True:
		if mystring.find("\t") != 0:
			break
		else:
			counter+=1
			mystring = mystring[1:]
	return counter,mystring

run(s)

w = ceil(len(listoftuples)**0.5)
h = w
im = Image.new("RGBA",(w,h),color="white")

pixels = im.load()
col = -1
print(len(listoftuples),im.size[0],im.size[0])
for i in range(len(listoftuples)):
	newnum = i%im.size[0]
	if newnum == 0:
		col += 1
	pixels[newnum,col] = listoftuples[i]

im.show()

