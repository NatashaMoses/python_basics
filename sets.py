#### Add Items




#### Remove Items
+ Using the `remove()` function  
If the specified item does not exist, it raises an error.  
- Using the `discard()` function   
Unlike `remove()`, it does not rasie an error when the item does not exist.
+ Using the `pop()` function   
Remmoves any random item since set items are unordered.  
- Using the `clear()` function   
Empties the set, the set is still present but empty.  
+ Using the `del` keyword  
Deletes the entire set, set will no longer exist.  

lang = {"English", "French", "Spanish", "German"}
print("USING remove()")
lang.remove("English")
print(lang)

print("USING discard()")
lang.discard("French")
print(lang)

print("USING pop()")
lang.pop()
print(lang)

print("USING clear()")
lang.clear()
print(lang)

del lang
#print(lang) will raise an error as the set no longer exists


#### Join Sets
+ Using the `union()` function   
- Using the `update()` function   
+ Using the `intersection()` function  
- Using the `difference_update()` function   
+ Using the `intersection_update()` function   
- Using the `symmetric_difference_update()` function   
+ Using the `symmetrice_difference()` function   


### Set Methods
+ `add()`
- `clear()`
+ `copy()`
- `difference()`
+ `difference_update()`
- `discard()`
+ `intersection()`
- `intersection_update()`
+ `isdisjoint()`
- `issubset()`
* `isupperset()`
+_`pop()`
- `remove()`
+ `symmetric_difference()`
- `symmetric_difference_update()`
+ `union()`
- `update()`

