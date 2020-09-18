# Author: Khalil Stroman kzs595@psu.edu
# Collaborator: Cole Black-Stallard cdb5655@psu.edu
# Collaborator: Nicholas Cole nyc5096@psu.edu
# Collaborator: Emmanuel Bassill Chuckran
# Section: 12
# Breakout: 8

def sum_n(n):
  
  if n > 0: 
    return sum_n(n-1) + n
  else:
    return n
def print_n(s,n):
  if n > 0:
    print(f"{s}")
    n=n-1
    print_n(s,n)
def run():
  i = input("Enter an int: ")
  i = int(i)
  print(f"sum is {sum_n(i)}.")
  ss = input("Enter a string: ")
  print_n(ss,i)
if __name__ == "__main__":
  run()