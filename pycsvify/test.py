import pycsvify

a = "lorem,ipsum\n1,2\n3,4"


print(pycsvify.parseCSV(a))