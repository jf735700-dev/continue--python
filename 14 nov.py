#1
for i in range(1,11):
  if i == 5:
      continue 
  print(i)

#2

for i in range(1,21):
    if i%2!=0:
      print(i)
#3

total=0
for i in range(1,51):
    if i%3!=0:
        total+=i
    print("sum=",total)
#4


numbers=[10,-5,20,-10,30]
total=0
for i in numbers:
    if i<0:
        continue
    total +=i
print("sum=",total)
#5

text="hello world!"
count=0
for ch in text:
    if not ch.isalpha():
        continue
    if ch.lower() in "a,e,i,o,u":
      continue
    count +=1
print("consonents=",count)
#6

text="hello world"

for ch in text:
    if ch == " ":
      continue
    print(ch)
#7

for i in range(1,31):
    if i%2==0 or i%3==0:
        continue
    print(i)
#9

numbers=[2,0,3,4,0,5]
product=1
for num in numbers:
    if num !=0:
        product *=num
print(product)
#10

word=input("enter a word:")
for letter in word:
    if letter.lower() !='a':
        print(letter)
#11

s=input("enter a string:")
count=0
for ch in s:
    if not ch.isdigit():
        count +=1
print(f"non-digit character:{count}")
#12

import math
for i in range(1,21):
    if math.isqrt(i)**2 !=i:
        print(i)
#13

words=["hi","hello","my","world","is","great",]
for word in words:
    if len(word)>3:
        print(word)
#14

num=input("enter a number:")
total=0
for digit in num:
    d=int(digit)
    if d % 2 ==1:
        total +=d
print(f"sum of odd digits:{total}")
#15

for i in range(1,31):
    if i % 15 !=0:
        print(i)
        







