d1 = {"a" : ["c", "d"], "b" : ["a", "c", "e"]}
# "a" and "b" are two keys here
# key "a" storing a list ["c", "b"]
# key "b" storing a list ["a", "c", "e"]
print(type(d1))
print(d1)
print(d1.keys())
d1.pop("a")
print(d1)
print(d1.values())