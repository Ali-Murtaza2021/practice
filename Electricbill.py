Unit = int(input("Enter a Electric Unit"))
Amount = 0

if  Unit < 100:
    print('no charge')
elif Unit >= 100:
    Amount = (Unit-100)*5
    print("Price = ",Amount)
elif Unit >= 200:
    Amount = 500+(Unit-200)*10
    print("Price =",Amount)
else:
    print("error")        