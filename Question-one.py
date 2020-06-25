# Question 1

### **Question:**

> **_Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
> between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line._**

---

### Hints:

> **_Consider use range(#begin, #end) method._**

---

li = [n for n in range(2000, 3201) if n % 7 == 0 and n % 5 != 0]
print(*li, sep=',')
