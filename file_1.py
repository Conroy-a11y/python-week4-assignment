with open('ReadMe.md', 'r', encoding='utf-8') as file:
    content = file.read()


modified_content = content.upper()

with open('output.md', 'w', encoding='utf-8') as outfile:
    outfile.write(modified_content)

print("File has been read and modified content written to 'output.md'.")