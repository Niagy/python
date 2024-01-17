'''
John Niagwan
121092225
'''
# Information about a student in a dictionary
student1 = {'first_name': 'eric', 'last_name':'smith', 'addr1': '217 Au Large Blvd', 'city': 'Toronto', 'prov': 'Ontario', 'pcode': 'M4A 1P3'}

# Function to generate a shipping label from a dictionary
def shipping_label(a_dict): 
    "takes a dictionary, generates a string" 
    # Create an empty string to build the shipping label
    a_str = f"{a_dict['first_name'].capitalize()} {a_dict['last_name'].capitalize()}\n"  # Format and capitalize the name
    a_str += f"{a_dict['addr1']}\n"  # Add the address line
    a_str += f"{a_dict['city']}, {a_dict['prov']}\n"  # Add the city and province
    a_str += f"{a_dict['pcode']}"  # Add the postal code
    return a_str  # Return the generated shipping label as a string
