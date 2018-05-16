def file_to_lower(infile, outfile):
    with open(infile) as f:
        lines = f.read().upper()
    with open(outfile, "w") as f:
        f.write(lines)
    
    
file_to_lower("words.txt", "words2.txt")