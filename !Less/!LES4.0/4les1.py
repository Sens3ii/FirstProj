a = {"type": "A", "field1": "value1", "field2": "value2"}
file = open("output.txt", "w")
file.write(repr(a))
file.close()
