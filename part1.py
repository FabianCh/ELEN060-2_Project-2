from source_coding.compression import *

text = import_text('source_coding/text.csv')
marginal_probability_distribution = text_to_margin_distribution(text)

sort_margin_distribution(marginal_probability_distribution)

print("1.   additional character : ['\\n', ' ', '!', '\"', '&', \"'\", ',', '-', '.', '/', ':', '=', '?', '_']\n")

print('2.   marginal probability distribution : ', marginal_probability_distribution, '\n')

coding_table = huffman_code(marginal_probability_distribution)
print('3.   Coding table : ', coding_table, '\n')

coded_text = text_to_code(text, coding_table)
print('4.   Coded text : ', coded_text)
print('     Length of th coded text :', len(coded_text), '\n')

print('5.   Expected average length :', expected_average_length(marginal_probability_distribution, coding_table))
print('     Empirical average length :', len(coded_text) / len(text), '\n')

coded_probability = coded_text_probability(coded_text)
print('6.   Compression rate = ', entropy(marginal_probability_distribution), '/', entropy(coded_probability))
print('                      = ', entropy(marginal_probability_distribution) / entropy(coded_probability))
