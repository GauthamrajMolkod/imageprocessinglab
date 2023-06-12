#!/usr/bin/env python
# coding: utf-8

# In[7]:


if 5 > 2:
  print("number is greater than two!")
else 
print("number not greater than two")


# In[9]:


if 5 > 2:
    print("number is greater than two")
    


# In[10]:


if 5>2:
    print("number is greater than two")


# In[11]:


if 5 > 2:
    print("number is greater than two")
    if 5>2:
        print ("number is greater than two")


# In[12]:


if 5 > 2:
    print("number is greater than two")
    if 5>2:
        print ("number is greater than two")


# In[13]:


x = 5
ptint(x)


# In[14]:


x = 5
print(x)


# In[15]:


x = 5
x = 6
print(x)


# In[16]:


x = 5
x = 6
print(x + y)


# In[17]:


x = 5
y = 6
print(x + y)


# In[18]:


x = "so"
y = "nil"
print(x + y)


# In[19]:


b = "Hello, World!"
print(b[:5])


# In[20]:


b = "Hello, World!"
print(b[:7])


# In[21]:


b = "Hello, World!"
print(b[:9])


# In[22]:


if 5 > 2:
  print("number is greater than two!")
else:
print("number not greater than two")


# In[23]:


if 5 > 2:
  print("number is greater than two!")
else:
 print("number not greater than two")


# In[24]:


if 1 > 2:
  print("number is greater than two!")
else:
 print("number not greater than two")


# In[25]:


i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


# In[26]:


i = 0
while i < 6:
  i += 1
  if i == 3:
    break
  print(i)


# In[27]:


i=0
while i<6:
  i+=1
  if i==3:
    continue
  print(i)


# In[28]:


# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern triangle
def triangle(n):
	
	# number of spaces
	k = n - 1

	# outer loop to handle number of rows
	for i in range(0, n):
	
		# inner loop to handle number spaces
		# values changing acc. to requirement
		for j in range(0, k):
			print(end=" ")
	
		# decrementing k after each loop
		k = k - 1
	
		# inner loop to handle number of columns
		# values changing acc. to outer loop
		for j in range(0, i+1):
		
			# printing stars
			print("A ", end="")
	
		# ending line after each row
		print("\r")

# Driver Code
n = 5
triangle(n)


# In[29]:


# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern triangle
def triangle(n):
	
	# number of spaces
	k = n - 1

	# outer loop to handle number of rows
	for i in range(0, n):
	
		# inner loop to handle number spaces
		# values changing acc. to requirement
		for j in range(0, k):
			print(end=" ")
	
		# decrementing k after each loop
		k = k - 1
	
		# inner loop to handle number of columns
		# values changing acc. to outer loop
		for j in range(0, i+1):
		
			# printing stars
			print("A ", end="")
	
		# ending line after each row
		print("\r")

# Driver Code
n = 5
triangle(n)


# In[30]:


# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern of numbers
def numpat(n):
	
	# initialising starting number
	ch = A

	# outer loop to handle number of rows
	for i in range(0, n):
	
		# re assigning num
		ch = A
	
		# inner loop to handle number of columns
			# values changing acc. to outer loop
		for j in range(0, i+1):
		
				# printing number
			print(ch, end=" ")
		
			# incrementing number at each column
			ch = ch + 1
	
		# ending line after each row
		print("\r")

# Driver code
n = 5
numpat(n)


# In[31]:


# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern of numbers
def numpat(n):
	
	# initialising starting number
	ch = A

	# outer loop to handle number of rows
	for i in range(0, n):
	
		# re assigning num
		ch = A
	
		# inner loop to handle number of columns
			# values changing acc. to outer loop
		for j in range(0, i+1):
		
				# printing number
			print(ch, end=" ")
		
			# incrementing number at each column
			ch = ch + 1
	
		# ending line after each row
		print("\r")

# Driver code
n = 5
numpat(n)


# In[32]:


print("The character pattern ")  
asciiValue = int(input("Enter the ASCII value to print pattern: "))  
# User - define value  
if (asciiValue >= 65 or asciiValue <=122):  
    for i in range(0, 5):  
        for j in range(0, i + 1):  
            # It will convert the ASCII value to the character  
            alphabate = chr(asciiValue)  
            asciiValue += 1
            print(alphabate, end=' ')  
        print()  
else:  
    print("Enter the valid character value")  


# In[33]:


print("The character pattern ")  
asciiValue = int(input("Enter the ASCII value to print pattern: "))  
# User - define value  
if (asciiValue >= 65 or asciiValue <=122):  
    for i in range(0, 5):  
        for j in range(0, i + 1):  
            # It will convert the ASCII value to the character  
            alphabate = chr(asciiValue)  
            asciiValue += 1
            print(alphabate, end=' ')  
        print()  
else:  
    print("Enter the valid character value")  


# In[34]:


print("The character pattern ")  
asciiValue = int(input("Enter the ASCII value to print pattern: "))  
# User - define value  
if (asciiValue >= 65 or asciiValue <=122):  
    for i in range(0, 5):  
        for j in range(0, i + 1):  
            # It will convert the ASCII value to the character  
            alphabate = chr(asciiValue)  
            asciiValue += 1
            print(alphabate, end=' ')  
        print()  
else:  
    print("Enter the valid character value")  
    


# In[ ]:


print("The character pattern ")  
asciiValue = int(input("Enter the ASCII value to print pattern: "))  
# User - define value  
if (asciiValue >= 65 or asciiValue <=122):  
    for i in range(0, 5):  
        for j in range(0, i + 1):  
            # It will convert the ASCII value to the character  
            alphabate = chr(asciiValue)  
            asciiValue += 1
            print(alphabate, end=' ')  
        print()  
else:  
    print("Enter the valid character value")  


# In[35]:


rows = int(input("Enter the number of rows: "))  
  
# the outer loop is executing in reversed order  
for i in range(rows + 1, 0, -1):    
    for j in range(0, i - 1):  
        print("*", end=' ')  
    print(" ")  


# In[36]:


rows = int(input("Enter the number of rows: "))  
  
# the outer loop is executing in reversed order  
for i in range(rows + 1, 0, -1):    
    for j in range(0, i - 1):  
        print("*", end=' ')  


# In[37]:


rows = int(input("Enter the number of rows: "))  
  
# the outer loop is executing in reversed order  
for i in range(rows + 1, 0, -1):    
    for j in range(0, i - 1):  
        print("*", end=' ')  
    print(" ")  


# In[38]:


# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern of alphabets
def alphapat(n):
	
	# initializing value corresponding to 'A'
	# ASCII value
	num = 65

	# outer loop to handle number of rows
	# 5 in this case
	for i in range(0, i+1):
	
		# inner loop to handle number of columns
		# values changing acc. to outer loop
		for j in range(0, n):
		
			# explicitly converting to char
			ch = chr(num)
		
			# printing char value
			print(ch, end=" ")
	
		# incrementing number
		num = num + 1
	
		# ending line after each row
		print("\r")

# Driver Code
n = 5
alphapat(n)


# In[39]:


# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern of alphabets
def alphapat(n):
	
	# initializing value corresponding to 'A'
	# ASCII value
	num = 65

	# outer loop to handle number of rows
	# 5 in this case
	for i in range(0, n):
	
		# inner loop to handle number of columns
		# values changing acc. to outer loop
		for j in range(0, i+1):
		
			# explicitly converting to char
			ch = chr(num)
		
			# printing char value
			print(ch, end=" ")
	
		# incrementing number
		num = num + 1
	
		# ending line after each row
		print("\r")

# Driver Code
n = 5
alphapat(n)


# In[40]:


# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern of alphabets
def alphapat(n):
	
	# initializing value corresponding to 'A'
	# ASCII value
	num = 65

	# outer loop to handle number of rows
	# 5 in this case
	for j in range(0, i+1):
	
		# inner loop to handle number of columns
		# values changing acc. to outer loop
		for i in range(0, n):
		
			# explicitly converting to char
			ch = chr(num)
		
			# printing char value
			print(ch, end=" ")
	
		# incrementing number
		num = num + 1
	
		# ending line after each row
		print("\r")

# Driver Code
n = 5
alphapat(n)


# In[ ]:


import turtle  
# Creating turtle turtle  
t = turtle.Turtle()  
  
t.shapesize(3,3,3)  
  
# Chnage the color of both  
t.color("green", "red")  
  
t.forward(100)  
  
turtle.mainloop()

