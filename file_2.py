input_file = input("Enter the name of the file to read: ")
output_file = input("Enter the name of the file to write: ")

try:
    
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    
    modified_content = content.upper()

    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(modified_content)

    print(f"Successfully read '{input_file}' and wrote modified content to '{output_file}'.")

except FileNotFoundError:
    print(f"Error: The file '{input_file}' was not found.")
except PermissionError:
    print(f"Error: Permission denied when accessing '{input_file}' or '{output_file}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")