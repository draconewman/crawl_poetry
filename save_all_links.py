import re

# Input file path
input_file_path = r"D:\STUDY\Projects\FYP\crawl_poetry\poetsHTML.txt"

# Output file path
output_file_path = r"D:\STUDY\Projects\FYP\crawl_poetry\poets_links.txt"

# Read the input file
with open(input_file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Extract href links using regular expressions
links = re.findall(r'href="([^"]+)"', content)

# Save the links to the output file
with open(output_file_path, 'w', encoding='utf-8') as file:
    for link in links:
        file.write(link + "\n")

print("Links extracted and saved to:", output_file_path)
