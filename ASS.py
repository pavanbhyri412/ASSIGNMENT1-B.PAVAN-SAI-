#Lists are just like dynamically sized arrays, declared in other languages. 
#In simple language, a list is a collection of things, enclosed in [ ] and separated by commas.
numbers=[1,2,3,4,5,6]
print(numbers)
numbers.insert(6,7)
print(numbers)
numbers.append(9)
print(numbers)
numbers.remove(2)
print(numbers)
#slicing :The slice() method returns a portion of an iterable as an object of the slice class based on the specified range. 
# It can be used with string, list, tuple, set, bytes, or range objects or custom class object that implements sequence methods __getitem__() and __len__() methods.
numbers=[1,2,3,4,5,6]
print(numbers)
print(numbers[0:3])
print(numbers[-3:-1])
print(numbers[9:90])
print(numbers[-4:-3])
#tuples :Python Tuple is a collection of objects separated by commas...
# In some ways, a tuple is similar to a list in terms of indexing, nested objects, and repetition but a tuple is immutable, unlike lists which are mutable.
vegetables=('carrot','beetroot','cabbage','bringal','potato')
print(vegetables) 
#Slicing in tuples..
print(vegetables[0:3])
print(vegetables[4:6])
print(vegetables[-5:-1])
print(vegetables[-90:-4])
print(vegetables[-1:0])
#Dictionary:These are immutable ones for some cases and these can be represented as {}...
#these also consists of some values for each data in it
#example:royal enfield = 2lakhs...
bikes={'royal enfield':'1.5 lakh','honda':'2.5 lakh','yamaha':'1.3 lakh','bajaj':'1 lakh'}
print(bikes)
bikes.update({'royalenfield':'1.5 lakh'})
print(bikes)
bikes.update({'honda':'2.5 lakh'})
print(bikes)
bikes.clear()
print(bikes)
#del bikes['royal enfield']
print(bikes)
#bikes.pop('bajaj')
print(bikes)
#slicing in an Dictionary..
bikes={'royal enfield':'1.5 lakh','honda':'2.5 lakh','yamaha':'1.3 lakh','bajaj':'1 lakh'}
print(bikes)
keys_for_slicing=["honda","yamaha"]
sliced_cars = {key:bikes[key] for key in keys_for_slicing}
print(bikes)
keys_for_slicing=["yamaha"]
sliced_bikes = {key:bikes[key] for key in keys_for_slicing} 
print(bikes)

Output:
PS C:\Users\BHYRI PAVAN SAI> & "C:/Program Files/Python310/python.exe" "c:/Users/BHYRI PAVAN SAI/Downloads/ASSIGNMENT1.py"
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7, 9]
[1, 3, 4, 5, 6, 7, 9]
[1, 2, 3, 4, 5, 6]
[1, 2, 3]
[4, 5]
[]
[3]
('carrot', 'beetroot', 'cabbage', 'bringal', 'potato')
('carrot', 'beetroot', 'cabbage')
('potato',)
('carrot', 'beetroot', 'cabbage', 'bringal')
('carrot',)
()
{'royal enfield': '1.5 lakh', 'honda': '2.5 lakh', 'yamaha': '1.3 lakh', 'bajaj': '1 lakh'}
{'royal enfield': '1.5 lakh', 'honda': '2.5 lakh', 'yamaha': '1.3 lakh', 'bajaj': '1 lakh', 'royalenfield': '1.5 lakh'}
{'royal enfield': '1.5 lakh', 'honda': '2.5 lakh', 'yamaha': '1.3 lakh', 'bajaj': '1 lakh', 'royalenfield': '1.5 lakh'}
{}
{}
{}
{'royal enfield': '1.5 lakh', 'honda': '2.5 lakh', 'yamaha': '1.3 lakh', 'bajaj': '1 lakh'}
{'royal enfield': '1.5 lakh', 'honda': '2.5 lakh', 'yamaha': '1.3 lakh', 'bajaj': '1 lakh'}
{'royal enfield': '1.5 lakh', 'honda': '2.5 lakh', 'yamaha': '1.3 lakh', 'bajaj': '1 lakh'}
