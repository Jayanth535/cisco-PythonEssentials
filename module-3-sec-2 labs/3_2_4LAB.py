secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
n=int(input("Enter a number: "))
while secret_number:
    if secret_number==n:
        print("Well done, muggle! You are free now.")
        break
    else:
        print("Ha ha! You're stuck in my loop!")
        break
# Output:  
# Enter a number: 777
# Well done, muggle! You are free now.
