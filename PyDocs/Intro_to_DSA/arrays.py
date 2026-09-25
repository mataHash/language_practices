new_list = [1, 2, 3]
result = new_list[0]

"""
    Let us say your expense for every month are listed below,
        January - 2200
        February - 2350
        March - 2600
        April - 2130
        May - 2190

Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter
(first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar.
Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
"""
expenses = [["January", "February", "March", "April", "May"],
            [2200, 2350, 2600, 2130, 2190]]
total_expense = 0
# 1
print(expenses[1][1] - expenses[1][0])
# 2
for i in range(3):
    total_expense += expenses[1][i]
print(total_expense)
# 3
for i in range(len(expenses[1])):
    if expenses[1][i] == 2000:
        print(True)
print("2000 Not found")
# 4
expenses[0].append("June")
expenses[1].append(1980)
print(expenses)
# 5
april_difference = expenses[1][3] - 200
expenses[1][3] = april_difference
print(expenses)
"""


    You have a list of your favourite marvel super heros.

heros=['spider man','thor','hulk','iron man','captain america']

Using this find out,

1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

    """

heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']
# 1
print(len(heros))
# 2
heros.append("black panther")
print(heros)
# 3
heros.pop(-1)
heros.insert(heros.index("hulk") + 1, "black panther")
print(heros)
# 4
heros.remove("thor")
heros.remove("hulk")
print(heros)
# 5
heros.sort()
print(heros)
"""Create a list of all odd numbers between 1 and a max number.
Max number is something you need to take from a user using input() function
"""
Max_num = int(input("enter a number: "))
Count = 0
for i in range(1, Max_num):
    if not i % 2 == 0:
        Count += 1
        print(i, end=" -> ")
print(f"The count is equal to {Count}")
