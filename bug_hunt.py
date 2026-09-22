count = 1
total = 0

# BUG: The while condition was missing a colon.
# Added the colon at the end of the while statement.
while count < 6:

    # BUG: The original condition was count < 5, which stopped before adding 5.
    # Changed it to count < 6 so that 5 is included.
    total = total + count

    count = count + 1

# BUG: total is an integer and cannot be joined directly to a string with +.
# Changed the print statement to an f-string.
print(f"Sum of 1 to 5 is: {total}")