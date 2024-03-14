blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
i=1
height=0
while i<=blocks:
    blocks=blocks-i
    height+=1
    i+=1
print("The height of the pyramid:", height)

# Sample input:6
# Expected output:
# The height of the pyramid: 3
# Output
# Sample input:20
# Expected output:
# The height of the pyramid: 5
# Output
# Sample input:1000
# Expected output:
# The height of the pyramid: 44