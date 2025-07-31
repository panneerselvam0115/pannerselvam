print("Panneer super market")
print("no 55,Bajar street,Tindivanam")
print("------------")
print("Bill recipt")
print("------------")
sno=int(input("Enter the serial number:"))
pr=input("Enter the particular:")
rate=int(input("Enter the rate:"))
qnt=int(input("Enter the quantity:"))
total=rate*qnt
print("Total amount:",total)
gst=total*10/100
print("GST(10%):",gst)
paid=gst+total
print("Amount total paid rs:",paid)
