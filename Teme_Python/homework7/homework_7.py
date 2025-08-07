# Ex 1 Filter names starting with a vowel from students.txt and write to filtered.txt

vowels = {'A', 'E', 'I', 'O', 'U'}

with open("students.txt", "r") as infile, open("filtered.txt", "w") as outfile:
    for line in infile:
        name = line.strip()
        if name and name[0].upper() in vowels:
            outfile.write(name + "\n")

# Ex 2 Reverse lines from log.txt and save into reversed_log.txt

with open("log.txt", "r") as infile:
    lines = infile.readlines()

with open("reversed_log.txt", "w") as outfile:
    for line in reversed(lines):
        outfile.write(line)