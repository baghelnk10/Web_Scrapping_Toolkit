import re

def custom_sort_key(value):
    # Extract alphanumeric and special characters separately
    alphanumeric_part = re.search(r'[a-zA-Z0-9]+', value).group()
    special_part = value.replace(alphanumeric_part, '')

    # Return a tuple with alphanumeric part as the first element
    # and special part as the second element for sorting
    return (alphanumeric_part, special_part)

# Your list of values
values = ["tau+ -> mu+ pi0", "tau- -> e- pi0", "tau+ -> e+ pi0", "tau- -> mu- pi0", "tau+ -> mu+ pi0"]

# Sort the list using the custom key
sorted_values = sorted(values, key=custom_sort_key)

# Print the sorted list
print(sorted_values)