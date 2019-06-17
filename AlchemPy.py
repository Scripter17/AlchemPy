"""
https://littlealchemy.com/
# Get example
bases.names[bases.base[1].parents[0][0]]+"+"+bases.names[bases.base[1].parents[0][1]]+"="+bases.names[1]
ice+fire=water
# Get dat (python)
for x in bases.base:
	for y in bases.base[x].parents: 
		bases.names[bases.base[x].parents[y][0]]+"+"+bases.names[bases.base[x].parents[y][1]]+"="+base.names[x]
# Dat fmt
bases={
	names:{
		1:"water"
	},
	base:{
		1:{
			parents:[
				[148, 2]
			],
			tags: ["water"]
		}
	}
}
# Get dat (Console JS)
a=""
for (x in bases.base){
	for (y in bases.base[x].parents){
		a+=bases.names[bases.base[x].parents[y][0]]+"+"+bases.names[bases.base[x].parents[y][1]]+"="+bases.names[x]+"\n"
	}
}
"""


import msvcrt, os, colorama
os.system("title AlchemPy - Little Alchemy in Python")
colorama.init() # To move the cursor back to the end of the input

cstr="\033[2J\033[H"
def clear():
	print(cstr, end="")

data=open("Recipes.dat", "r").read()
elements, recipes=tuple(data.split("\n-\n"))
elements=elements.split("\n")
r=[]
rkeys=[]
for x in recipes.split("\n"):
	com=set(x.split("=")[0].split("+"))
	res=[x.split("=")[1]]
	if com in rkeys:
		r[[x[0] for x in r].index(com)][1].append(res[0])
	else:
		rkeys.append(com)
		r.append([com, res]) # [[{"earth, air"},["dust"]]...]
recipes=r

print("""\033[2J\033[H
AlchemPy - Little Alchemy in Python!
       (c) James C. Wise 2019
  Released under the DBaD license.
   \033[36mhttps://github.com/Scripter17/\033[39m

Left/Right -> Move through element list pages
Type a combination of known elements like 'elem1+elem2',
then press enter to submit. If it's a valid combination,
it'll show up in the element list!
""", end="")
msvcrt.getch()
clear()

dispPage=0 # Which 8 elements to list
ePerPage=8 # How many elements to list per page
txt=""
cin=""
cin2=""
new=""
while True:
	#print(elements)
	#print(recipes)
	pages=(len(elements)-1)//ePerPage
	print("Page "+str(dispPage+1)+"/"+str(pages+1))
	plist=[x.capitalize() for x in elements[dispPage*ePerPage:(dispPage+1)*ePerPage]]
	print("---")
	print("\n".join(plist)+"\n"*(ePerPage-len(plist)))
	print("---")
	# If I do print(txt, end=""), the text will appear at the top for some unknown reason
	# TODO: Fix this
	print(txt)
	if new!="":
		print("Discovered "+new+"\033[1A")
	print("\033[1A\033["+str(len(txt))+"C",end="")
	cin=msvcrt.getch()
	new=""
	if cin==b"\xe0": # The user pressed an arrow key
		cin2=msvcrt.getch()
		if cin2==b"K": # The user pressed left
			dispPage=max(dispPage-1, 0)
		elif cin2==b"M": # The user pressed right
			dispPage=min(dispPage+1, pages)
	elif cin==b"\x08": # Backspace
		txt=txt[:-1]
	elif cin==b"\r": # Enter
		com=txt.lower()
		"""if (com not in recipes) and ("+".join(com.split("+")[::-1]) in recipes):
			# If a+b isn't a recipe, but b+a is, do b+a
			# earth+air = air+earth
			com="+".join(com.split("+")[::-1])
		if com in recipes and com.split("+")[0] in elements and com.split("+")[1] in elements:
			# Append to discovered elements
			elements.append(recipes[com])"""
		if com=="exit":
			exit()
		else:
			com=set(com.split("+"))
			for x in recipes:
				if x[0]==com:
					new=", ".join(x[1])
					for y in x[1]:
						elements.append(y)
		txt=""
	else:
		allowedChars="abcdefghijklmnopqrstuvwxyz+- "
		if cin.decode().lower() in allowedChars:
			txt+=cin.decode()
	clear()
