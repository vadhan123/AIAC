import os
# Create numbers.txt with sample numbers if it doesn't exist
if not os.path.exists("numbers.txt"):
    with open("numbers.txt", "w") as f:
        f.write("1\n2\n3\n4\n5\n")

f=open("numbers.txt","r")
nums=f.readlines()
squares=[]
for n in nums:
    n=n.strip()
    if n.isdigit():
        squares.append(int(n)*int(n))
f2=open("squares.txt","w")
for sq in squares:
    f2.write(str(sq)+"\n")
print("squares written")