import wave
import random


def import_sound(filename):
    with wave.open(filename, mode='rb') as sound:
        print(sound.getparams())

        sample_list = []
        for i in range(sound.getnframes()):
            sample_list.append(sound.readframes(1))

        return sample_list


def from_bytes_list_to_int_list(bytes_list):
    integer_list = []

    for bytes_value in bytes_list:
        integer_value = int.from_bytes(bytes_value, 'big')
        integer_list.append(integer_value)

    return integer_list


def from_int_list_to_binaries(integer_list):
    bits = ''

    for integer_value in integer_list:
        bit = ''
        dividend = integer_value
        quotient = integer_value
        while quotient != 0:
            quotient = dividend // 2
            remainder = dividend - 2 * quotient
            dividend = quotient
            bit += str(remainder)

        while len(bit) != 8:
            bit += '0'

        bits += ''.join(reversed(bit))

    return bits


def hamming_7_4_coder(binaries):
    coding_table = {
        "0000": "0000000", "0001": "0001011", "0010": "0010111", "0011": "0011100",
        "0100": "0100110", "0101": "0101101", "0110": "0110001", "0111": "0111010",
        "1000": "1000101", "1001": "1001110", "1010": "1010010", "1011": "1011001",
        "1100": "1100011", "1101": "1101000", "1110": "1110100", "1111": "1111111"
    }
    coded_binaries = ''
    for i in range(len(binaries)//4):
        coded_binaries += coding_table[binaries[4*i:4*i+4]]

    return coded_binaries


def simulate_channel_effect(binaries, probability_of_error=0.01):
    sent_binaries = ''
    for bit in binaries:
        if random.uniform(0, 1) > probability_of_error:
            sent_binaries += bit
        else:
            if bit == '1':
                sent_binaries += '0'
            elif bit == '0':
                sent_binaries += '1'
    return sent_binaries


def hamming_7_4_decoder(corrupted_binaries):
    coding_table = {
        "0000000": "0000", "0001011": "0001", "0010111": "0010", "0011100": "0011",
        "0100110": "0100", "0101101": "0101", "0110001": "0110", "0111010": "0111",
        "1000101": "1000", "1001110": "1001", "1010010": "1010", "1011001": "1011",
        "1100011": "1100", "1101000": "1101", "1110100": "1110", "1111111": "1111"
    }

    def closest_codeword(corrupted_codeword):
        distance_min = 8
        closest_key = None
        for key in coding_table.keys():
            distance_key = distance(corrupted_codeword, key)
            if distance_key < distance_min:
                distance_min = distance_key
                closest_key = key

        # if distance_min == 1:
        #     print('correct decoding')
        # if distance_min == 2:
        #     print('correct detection')

        return closest_key

    decoded_binaries = ''
    for i in range(len(corrupted_binaries)//7):
        codeword = corrupted_binaries[i*7:i*7+7]

        if codeword in coding_table.keys():
            code_block = coding_table[codeword]
        else:
            corrected_codeword = closest_codeword(codeword)
            code_block = coding_table[corrected_codeword]

        decoded_binaries += code_block
    return decoded_binaries


def distance(codeword1, codeword2):
    number_of_difference = 0
    for i in range(len(codeword1)):
        if codeword1[i] != codeword2[i]:
            number_of_difference += 1
    return number_of_difference


def from_binaries_to_int_list(binaries):
    integer_list = []
    for i in range(len(binaries)//8):
        integer_value = 0
        for j in range(8):
            if binaries[8 * i + j] == '1':
                integer_value += 2**(7-j)
        integer_list.append(integer_value)
    return integer_list


def from_int_list_to_bytes_list(integer_list):
    bytes_list = []

    for integer in integer_list:
        byte = bytes([integer])
        bytes_list.append(byte)

    return bytes_list


def export_sound(filename, sample_list):
    with wave.open(filename, mode='wb') as sound:
        sound.setnchannels(1)
        sound.setsampwidth(1)
        sound.setframerate(11025)

        for sample in sample_list:
            sound.writeframes(sample)
