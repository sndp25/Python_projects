#This program returns provided string without vowels

inp=input("Enter: ")
#inp = "abcdefgh"
v="aeiou"

result=[]

for i in inp:
	if i not in v:
		result.append(i)

print("".join(result))