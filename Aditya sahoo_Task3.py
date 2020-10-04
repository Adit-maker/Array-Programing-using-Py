from array import *		#importing array
#defining the function A
def A():
	print ("\t\t### TASK 3.1 ###")
	arr = array("i",[ ])
	n = int(input("Number of sticks :\t"))		#for taking input of array size
	print("Length of sticks are :")
	#for take inputs of array elements
	for i in range(0,n):
		x = int(input("\t\t\t"))
		arr.append(x)
	arr_repet = [ ]	#making another array for thoes elements are repet in arr
	for j in range (0 , n):
		for i in range (j+1 , n):
			if arr[j] == arr[i]:
				y = arr[j]
				arr_repet.append(y) #it use for storing the array elements

	arr_repet.sort()   #sorting arr_repet from lower to higher
	if len(arr_repet) > 1:
		area = arr_repet[len(arr_repet)-1] * arr_repet[len(arr_repet)-2] #for max area multiplication of two higher repeting numbers
		print("maximum area =  ",area)
	else:
		print("maximum area =  -1 ")

#defining the function B	
def B():
	print ("\n\t\t### TASK 3.2 ###")
	arr = array("i",[ ])
	n = int(input("Size of array :\t")) #input of array size
	print("Enter elements :")
	for i in range(0,n):		#input of array elments
		x = int(input("\t\t"))
		arr.append(x)
	p=len(arr)		#length of array
	print("output  :",end="")
	for j in range (0 , p):		#run the loop until it stop
		z=1		
		for i in range (j , p-1):					
			if arr[i] > 0 and arr[i+1] < 0 :    #if 1st element is > 0 and 2nd element is < 0
				z = z+1									#then length become +1
			if arr[i]< 0 and arr[i+1] > 0 :	#if 1st element is < 0 and 2nd element is > 0
				z = z+1									#then length become +1
			if arr[i]< 0 and arr[i+1] <0 :	#if 1st element is < 0 and 2nd element is < 0		
				break										#break the loop
			if arr[i]> 0 and arr[i+1] > 0 :	#if 1st element is > 0 and 2nd element is > 0
				break										#break the loop
		print(" ",z,end="")						#display of length
	
#defining function C
def C():
	print ("\n\n\t\t### TASK 3.3 ###")
	#taking inputs
	x = int(input("No of points needs   =  "))
	y = int(input("no of matches remaining   =  "))
	if x <= 2*y:			#check x is <= 2*y or not
		if x <= y:		##if yes  then check x <= y or not
			z = 0		#if yes then match requir to win is 0
		else:			##if not			
			z =int(x-y)	#then requir to win is x-y
		print("min. match requier to win  =  ",z)
	else:		#if not
		print("can not qualify")	#then display		
#defining function D
def D():
	print ("\n\t\t### TASK 3.4 ###")
	i = 0
	n = int(input("Enter the no. of movies = "))	#take input
	print("'L' is length of movie.\n'R' is reting of movie.")
	arr1 = array("i",[ ])		#colection of length of movies
	arr2 = array("i",[ ])		#colection of rating of movies
	arr3 = array("i",[ ])			# arr1 * arr2
	#takling input of length and rating of movies
	for i in range (0,n) :
		print("\nL",end="")
		L = int(input(i+1,))
		arr1.append(L)
		print("R",end="")
		R = int(input(i+1))
		arr2.append(R)
	for i in range(0,len(arr1)):
		x=arr1[i] * arr2[i]
		arr3.append(x)


####finding max of  array3
	c=arr3
	max = c[0]
	for i in range(1 , len(c)):
		if c[i] > max :
			max = c[i]


#find how many max are present in arr3
	r = 0
	arr4 = array("i",[ ])
	for i in range (0,len(arr3)):
		if max == arr3[i] :
			r = r+1 #no. of max present in arr3
			I = i     #index of max numbers
			arr4.append(I)

	if r == 1 :		#if only 1 max present in arr3
		print("\nmovie to be watch is ",I+1)
	else:			#if more than 1 max present in arr3
		arr5 = array("i",[ ])		# collection of rating no. of max in arr2 
		for i in range (0 , len(arr4)):
			R = arr2[arr4[i]]
			arr5.append(R)
	#finding max between values in arr5 	
		max2 = arr5[0]
	
		for i in range(1 , len(arr5)):
			if arr5[i] > max2 :
				max2 = arr5[i]
			
	
		r = 0
		for i in range (0,len(arr5)):
			if max2 == arr5[i] :
				r = r+1 #no. of max present in arr3
		arr6 = array("i",[ ])
		for i in range (0, len(arr2)):
			if max2 == arr2[i]:
				I2 = i
				arr6.append(I2)
		if r == 1 :
			print("\nmovie  to be watch is ",I2+1)
		else:
			print("\nmovie to be watch = ",arr6[0]+1)
#defining function E
def E():
	print ("\n\t\t### TASK 3.5 ###")
	arr = [ ]
	n = int(input("Size of array :\t"))   ##input of list
	print("Enter elements :")  		#input of elements
	for i in range(0,n):		
		x = int(input("\t\t"))
		arr.append(x)
	a = arr
	s=0 #sefin total cost initial 0
	while len(a) > 1:		#runing while loop until the array size become 1
	
		if a[len(a)-1] >= a[len(a)-2]:    #check last element is greater than 2nd last element or not
			s = s + a[len(a)-2]		#if yes then add small element to s
			a.remove(a[len(a)-1])		# removing last element from array
		
		if a[len(a)-1] < a[len(a)-2]:		##check last element is smaller than 2nd last element or not
			s = s + a[len(a)-1]				##if yes then add small element to s
			a.remove(a[len(a)-2])		# removing 2nd last element from array
		
	print ("Total cost =",s)
	

	
A()			#call function A
B()			#call function B
C()			#call function C
D()			#call function D
E()			#call function E