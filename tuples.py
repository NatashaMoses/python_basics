#### Tuple Methods
+ count()Returns the number of times a specific value occurs in a tuple  
- index()Searches tuple for a specific value and returns the position where it was found  



#### Unpack Tuples
**Packing** is the process of assigning values to a set/list/tuple etc.   
**Unpacking** is the process of extracting those values back to variables.  

#Here the no of variables = no of values in the tuple
print("No of variables = No of values in tuple")
continent = ("Africa", "Asia", "Australia", "Europe", "North America", "South America")
(a, b, c, d, e, f) = continent
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#However if no of variables is less than no of values in the tuple, we use *
print("No of variables is less than no of values in the tuple")
continent = ("Africa", "Asia", "Australia", "Europe", "North America", "South America")
(c, d, *e) = continent
print(c)
print(d)
print(e)

#Here is another example
continent = ("Africa", "Asia", "Australia", "Europe", "North America", "South America")
(f, *g, h) = continent
print(f)
print(g)
print(h)


#### Update Tuples
Tuples are unchangeable meaning you cannot add or remove items in a tuple.  
However there are ways you can manipulate the tuple:  
+ Convert the Tuple to a List  
List items are changeable.  
You can convert a tuple to a list, make changes like add or remove items.  
Then convert the list back to a tuple.   
- Add Tuple to another Tuple  
This is done using the `+=` operator.  
+ Use del keyword  
This deletes the entire tuple.  


print("CONVERT TUPLE TO LIST")
my_tuple = ("name", "age", "height", "weight")
my_list = list(my_tuple)
print("Converted tuple {} to list {}".format(my_tuple, my_list))

#Now we can add/change/remove items in the list
print("CHANGE ITEMS")
my_list[2] = "gender"

print("ADD ITEMS")
my_list.append("d.o.b")

print("REMOVE ITEMS")
my_list.remove("weight")

#We then convert result back to tuple
new_tuple = tuple(my_list)
print("New tuple is: {}".format(new_tuple))

print("ADD TUPLE TO ANOTHER TUPLE USING +=")
tuple1 = ("a", "b", "c")
tuple2 = ("d",) #remember a tuple with one item should have a comma
tuple1 += tuple2
print("Adding tuple1 to tuple2: {}".format(tuple1))

del tuple2
#print(tuple2) will raise an error as tuple2 no longer exists



#### Join Tuples
+ Using the `+` operator  
E.g `tuple_3 = tuple_1 + tuple_2`.  
- Using the `*` operator  
E.g `my_tuple = tuple_1 * 3`.  
This repeats the tuple thrice.  


print("USING THE + OPERATOR")
tuple_1 = ("eggs","milk", "cheese")
tuple_2 = ("cake", "braed")
tuple_3 = tuple_1 + tuple_2
print(tuple_3)

print("USING THE * OPERATOR")
my_tuple = tuple_1 * 4
print(my_tuple)

