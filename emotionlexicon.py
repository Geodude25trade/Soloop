import csv
import json

# Creates two Json documents from the emotion lexicon data set (NRC.csv). The emotion_lexicon.json file contains a
# dictionary with each key as the word, and the value as a dictionary with emotions and their values (0 or 1). The
# words.json file contains all of the words in the dataset that are words to consider, including non-emotionally
# charged words.
with open('NRC.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    emotion_data = {}
    line_count = 0
    headers = []
    all_words = []
    for row in csv_reader:
        if line_count == 0:
            for col in row[1:]:
                headers.append(col)
                line_count += 1
        else:
            row_sum = 0
            all_words.append(row[0])
            for col in row[1:]:
                row_sum += int(col)
            if row_sum != 0:
                emotion_data[row[0]] = {
                    headers[0]: int(row[1]), headers[1]: int(row[2]), headers[2]: int(row[3]), headers[3]: int(row[4]),
                    headers[4]: int(row[5]), headers[5]: int(row[6]), headers[6]: int(row[7]), headers[7]: int(row[8]),
                    headers[8]: int(row[9]), headers[9]: int(row[10])
                }

    with open('emotion_lexicon.json', 'w') as file:
        json.dump(emotion_data, file)
    with open('words.json', 'w') as file:
        json.dump(all_words, file)
