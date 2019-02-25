nums = [1,2,3]
new = [x*10 for x in nums]
print(new)

name = "bailey"
newname = [name.upper() for i in name]
print(newname)

friends = ["ashley", "matt", "micheal"]
newfriends = [friends[0].upper() for k in friends]
print(newfriends)

boollist = [bool(val) for val in [0,[],'']]
print(boollist)

numbers = [1,2,3,4,5,6,7,8,9,10]
evens = [number for number in numbers if number % 2 == 0]
odds = [number for number in numbers if number % 2 == 1]

print(evens)
print(odds)

math = [number*2 if number%2==0 else number//2 for number in numbers]
print(math)

with_vowels = "This is so much fun"

without_vowels = ''.join(without_vowels for without_vowels in with_vowels if without_vowels not in "aeiou")
print(without_vowels)


answer = [answer[0] for answer in ["Elie","Tim","Matt"]]
print(answer)

answer2 = [answer2 for answer2 in [1,2,3,4,5,6] if answer2 % 2 == 0]
print(answer2)

nest = [[1,2,3],[4,5,6],[7,8,9]]

nested = [[val for val in l] for l in nest]
print(nested)

board = [['*' for i in range(1,4)] for x in range(1,4)]
print(board)
