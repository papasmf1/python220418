# demoStr.py 
#print(dir(str))

strA = "파이썬은 무지 강력해!"
print(len(strA))
strB = "python is very powerful"
print(len(strB))
print(strB.capitalize())
print(strB.count("p"))
print(strB.count("p", 7))
print("demo.ppt".endswith("ppt"))
print("MBC2580".isalnum())
print("MBC:2580".isalnum())
print("2580".isdecimal())

strC = "<<<  spam and ham  >>>"
print(strC)
print(strC.strip("<> "))
result = strC.strip("<> ")
result = result.replace("spam", "spam egg")
print(result)


