# x = input("enter a word")
# print(len(x))
 
# y = input("enter a word")
# print(len(y.replace(" ",""))) 

arg = []
for i in range(1, 6):
   args = input(f"Enter string {i}: ")
   arg.append(args)

print("\nWords and their lengths:")
for word in arg:
   print(f"'{word}' has: {len(word.replace(' ', ''))} characters")

 