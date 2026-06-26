# syntax for writion the comprenesions are list set dict

# for list [],set (),dict {} ----> [expression for item in iterable if condition] here condition is not mandatory

# example for list
x = ['ice_pizza','macho','upiii','ice_tea']

x1 = [i for i in x if 'ice' in i]

print(x1)

x = ['ice_pizza','macho','upiii','ice_tea','ice_pizza','ice_pizza','ice_pizza']

x1 = set(i for i in x)
print(x1)


x = {
    "masala":40,
    "ice":80,
    "pizza":100
}


x = {z:c/80 for z,c in x.items()}
print(x)



