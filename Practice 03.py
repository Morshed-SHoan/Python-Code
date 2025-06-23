"""
A = {
    "Name" : "Golam Morshed Shoan",
     "Age" : 23
}
#print(A)
for i ,j in A.items():
    print(f"Key = {i} , Value = {j}")
"""
A = {
    "Name" : "Golam Morshed Shoan",
     "Age" : 23
}

A.fromkeys("Shoan")
print(A)
B = A.keys()
print(B)