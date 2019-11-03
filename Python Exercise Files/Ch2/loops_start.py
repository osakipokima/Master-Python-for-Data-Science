#
# Example file for working with loops
#

def main():
  x = 0

# define a while loop: 
  # executes a block of code while a particular condition evalutes true
  while (x<5):
    print(x)
    x = x+1

# define a for loop:
  # A for loop is used for iterating over a sequence 
  # (that is either a list, a tuple, a dictionary, a set, or a string). ... 
  # With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
  for x in range(5,10):
    print(x)


  # use a for loop over a collection
  days=["Monday", "Tue", "Wed", "Thurs", "Fri", "Sat", "Sun"]
  for d in days:
    print(d)
    
 
  # use the break and continue statements
  # A break is used to "break/stop" the executon of a loop if a condition is met
  for x in range(5,10):
    # if(x == 7): break
    if(x % 2 == 0): continue
    print(x)


  #using the enumerate() function to get index 
  days=["Monday", "Tue", "Wed", "Thurs", "Fri", "Sat", "Sun"]
  for i,d in enumerate(days):
    print(i,d)

if __name__ == "__main__":
  main()
