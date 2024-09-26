"""
Name: Ali Shirazi Zamani
Level: 2
Homework: 3
Exercise: 1 
To do: Read the attached file "zen.txt" and create a new file from it
with alphabetic numbers replaced with numeric numbers (e.g. one -> 1,
 fifteen -> 15).
"""

from word2number import w2n

input_file = open('zen.txt', 'r')
output_file = open('modified_zen.txt', 'w')
modified_lines = []
for line in input_file:
    line = line.split(' ')
    modified_line = []
    for word in line:
        word_stripped = word.strip('.,-;:$!@#%^&*()_+=-~`')
        index = word.index(word_stripped)
        try:
            word = word[0: index] + str(w2n.word_to_num(word_stripped)) + word[index + len(word_stripped):]
            modified_line.append(word)            
        except:
            modified_line.append(word)    

    modified_lines.append(' '.join(modified_line))

output_file.writelines(modified_lines)
input_file.close()
output_file.close()
input_file = open('zen.txt', 'r')
print("\nInput file:\n", input_file.read(), sep='')
output_file = open('modified_zen.txt', 'r')
print('\nOutput file:\n', output_file.read(), sep='')
input_file.close()
output_file.close()


