# Function to display names in reverse order
def display_names_in_reverse(names):
    reversed_names = list(reversed(names))
    for name in reversed_names:
        print(name)

# Input: Collect names from the user
names = []
while True:
    name = input("Enter a name (type 'done' when finished): ")
    if name.lower() == 'done':
        break
    names.append(name)

# Display names in reverse order
print("\nNames in Reverse Order:")
display_names_in_reverse(names)
