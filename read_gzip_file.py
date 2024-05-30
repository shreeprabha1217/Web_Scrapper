import gzip

filename = 'restaurants.ndjson.gz'

print("Opening file...")
with gzip.open(filename, 'rt', encoding='utf-8') as f:
    print("File opened successfully.")
    for line_number, line in enumerate(f, start=1):
        print(f"Line {line_number}: {line.strip()}")  # Print each line in the file
