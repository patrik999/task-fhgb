import csv

class FileReader:

    def __init__(self):

        self.lines = []
        self.words = {}

    def read(self, fileName):

        # Read file to list
        with open(fileName) as file:
            for line in file:

                lineLower = line.lower().replace('\n', '')
                self.lines.append(lineLower)

        file.close()

    def wordCount(self):

        for line in self.lines:

            # Tokenize
            words = line.split(' ')

            # Check word by word and add to dictionary
            for word in words:

                wordCount = 0
                if word in self.words:
                    wordCount = self.words[word]
                wordCount = wordCount+1

                self.words[word] = wordCount

        return self.words

# Read and count file 1
reader1 = FileReader()
reader1.read("2010100102.txt")
counted1 =  reader1.wordCount()
print("File 1:")
print(counted1)

# Read and count file 2
reader2 = FileReader()
reader2.read("2010112901.txt")
counted2 =  reader2.wordCount()
print("File 2:")
print(counted2)

# Build intersection
set1 = set(counted1.keys())
set2 = set(counted2.keys())
inters = set1.intersection(set2)

print("Words in both documents:")
print(inters)

# Open file and output to result.txt
with open('results.txt', 'w') as f2:
    # Create writer
    writer = csv.writer(f2)

    # Write row to CSV
    for word in inters:
        freq1 = counted1[word]
        freq2 = counted1[word]

        #resString = word + "," + str(freq1) + "," +  str(freq2) + "," + str(freq1+freq2)
        #print(resString)
        writer.writerow([word, str(freq1), str(freq2), str(freq1+freq2)])

f2.close()


