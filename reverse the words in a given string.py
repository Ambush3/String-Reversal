# Function to reverse each word in the string
def reverse_word(s, start, end):
    while start < end:
        s[start], s[end] = s[end], s[start]
        start = start + 1
        end -= 1

s = "I like the python language"

# Convert string to list to use it as a char array
s = list(s)
start = 0
while True:
    try:
        # Find the next space
        end = s.index(' ', start)

        # call reverse_word function
        # to reverse each word
        reverse_word(s, start, end - 1)

        # Update start variable
        start = end + 1

    except ValueError:
        # Reverse the last word
        reverse_word(s, start, len(s) -1)
        break

# Reverse the entire list
s.reverse()

# Convert the list back to
# string using string.join() function
s = "".join(s)

print(s)

