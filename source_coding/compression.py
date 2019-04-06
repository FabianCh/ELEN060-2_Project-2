import math

# # Source coding and reversible data compression
# lowercase letters [’a’,’b’,...,’z’]
lowercase_letter = list("abcdefghijklmnopqrstuvwxyz")
# all numbers [’0’,’1’,...,’9’]
number = list("0123456789")
# some additional characters, i.e. [’.’,’,’,’;’, ... ]


def import_text(file_name):
    """return the content of a file in a string"""

    with open(file_name) as csv_file:
        text = ''
        for line in csv_file:
            for character in line:
                text += character
    # upper-case letters should be transformed into lower-case ones.
    text = text.lower()
    return text


def text_to_margin_distribution(text):
    """ return the marginal probability distribution of all symbols from the text sample

    :param text: A text
    :return: A list giving the probability distribution of the alphabet use in the text : [['char', P('char')], ... ]
    """

    # count each character and stock the result in a dictionary
    number_each_character = {}
    for letter in text:
        letter.lower()
        if letter in number_each_character:
            number_each_character[letter] += 1
        else:
            number_each_character[letter] = 0

    # Find the list of additional character
    additional_characters = list(number_each_character.keys())
    for char in "abcdefghijklmnopqrstuvwxyz0123456789":
        try:
            additional_characters.remove(char)
        except ValueError:
            continue

    additional_characters.sort()
    # print('additional character :', additional_characters)

    # marginal probability distribution
    marginal_probability_distribution = []
    total_character = sum(number_each_character.values())
    for character in lowercase_letter + number + additional_characters:
        if character in number_each_character.keys():
            marginal_probability_distribution.append([character, number_each_character[character] / total_character])
        else:
            marginal_probability_distribution.append([character, 0])
    return marginal_probability_distribution


def sort_margin_distribution(marginal_probability_distribution):
    """Sort the  marginal probability distribution from least likely to most likely

    :param marginal_probability_distribution: A list giving the probability distribution of the alphabet use in the text
                                                                                        [['char', P('char')], ... ]
    :return: None
    """

    def take_second(elem):
        return elem[1]

    marginal_probability_distribution.sort(key=take_second)


def huffman_code(probability_distribution):
    """Compute a binary Huffman code of a given probability distribution

    :param probability_distribution: the probability distribution of a alphabet [['char', P('char')], ... ]
    :return: A list of the 'char' and his code [['char', 1], ... ]
    """
    # Initialisation of the returned list
    coding_table = []
    for list_char in probability_distribution:
        coding_table.append([list_char[0], ''])

    # Completion of th returned list
    for i in range(0, len(probability_distribution)):
        for j in range(i):
            coding_table[j][1] += '0'
        coding_table[i][1] += '1'

    # reverse the code obtained to have a Prefix-less code
    for i in range(len(coding_table)):
        coding_table[i][1] = "".join(reversed(coding_table[i][1]))

    # delete the last bit of the longest codeword (useless bit)
    coding_table[0][1] = coding_table[0][1][:-1]

    return coding_table


def text_to_code(text, coding_table):
    """ Convert a text into is corresponding coded text

    :param text: the text to convert
    :param coding_table: the table containing the correspondence between alphabet and codeword
    :return: the coded text
    """
    # Creation of a dictionary to simplify the conversion
    coding_dict = {}
    for char, code in coding_table:
        coding_dict[char] = code

    # Conversion
    coded_text = ''
    for char in text:
        coded_text += coding_dict[char]

    return coded_text


def expected_average_length(probability_distribution, coding_table):
    average_length = 0
    for i in range(len(probability_distribution)):
        average_length += probability_distribution[i][1] * len(coding_table[i][1])
    return average_length


def entropy(probability_distribution):
    h = 0
    for char, probability in probability_distribution:
        if probability != 0:
            h -= probability * math.log2(probability)
    return h


def coded_text_probability(coded_text):
    num0 = 0
    num1 = 0
    for bit in coded_text:
        if bit == '0':
            num0 += 1
        elif bit == '1':
            num1 += 1
    return [['0', num0 / (num0 + num1)], ['1', num1 / (num0 + num1)]]


# test_code = [['a', 0.1], ['b', 0.1], ['c', 0.4], ['d', 0.4]]
# print(huffman_code(test_code))
