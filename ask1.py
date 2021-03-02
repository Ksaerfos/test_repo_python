import random
di = input("Dose diastash: ")

a = [[i * j for j in range(int(di))] for i in range(int(di))]
for i in range(int(di)):
        for j in range(int(di)):
            if i < j:
                a[i][j] = 0
            elif i >= j:
                a[i][j] = 1


random.shuffle(a)

for item in (a):
    print(item)


counter_1 = 0
counter_2 = 0
counter_3 = 0
counter_4 = 0
sum=0
for i in range(len(item)):
    for j in range(len(item)):
         if i == j:
            if a[i][j] == 1:
                counter_1 = counter_1 + 1
                if counter_1 == 4:
                    sum = sum + 1

         if i>j:
            if a[i][j]==1:
                counter_1 = counter_1 + 1
                if counter_1 == 4:
                    sum = sum + 1

         if j>i:
            if a[i][j]==1:
                counter_1 = counter_1 + 1
                if counter_1 == 4:
                    sum = sum + 1

         if i == int(di) - (j+1):
             if a[i][j] == 1:
                counter_2 = int(counter_2) + 1

         if (i < j) or (i >= j):
             if a[i][j] == 1:
                counter_3 = int(counter_3) + 1

         if (i > j) or (i <= j):
             if a[i][j] == 1:
                counter_4 = int(counter_4) + 1

print(counter_1)
print(counter_2)
print(counter_3)
print(counter_4)
print(sum)

