chai="Lemon chai"
chai1="  Masala chai  "
#lower case
print(chai.lower())

#upper case
print(chai.upper())

#strip
print(chai1)
print(chai1.strip())

#replace
print(chai.replace("Lemon","ginger"))

chai2="lemon, ginger, Masala, mint"
print(chai2.split(", "))

chai3= "Masala chai"
print(chai3.find("chai"))
print(chai3.rfind("Chai"))

chai4=("Masala chai chai chai")
print(chai4.count("chai "))

chai_type="Masala"
quantity = 2
order = "I ordered {} cups of {} chai"
print(order.format(quantity,chai_type))