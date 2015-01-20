# Syracuse sequence 

n=int(input("Please enter a natural number:"))
def syracuse(x):
    seq = [x]
    if x < 1:
       return []
    while x > 1:
       if x % 2 == 0:
         x = int(x / 2)
       else:
         x = 3 * x + 1
       seq.append(x)
    return seq

print("\nThe Syracuse sequence is", syracuse(n))
