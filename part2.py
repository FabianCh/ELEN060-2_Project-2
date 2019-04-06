from channel_coding.channel_coding import *
import matplotlib.pyplot as plt

# import the sound in a list of bytes
sound = import_sound('channel_coding/sound.wav')

# Convert the list of Bytes in a list of integer between 0 and 255
sound_int_list = from_bytes_list_to_int_list(sound)

plt.plot(sound_int_list)
plt.show()
print('8.   Sound signal plotted')
print('     Sound signal : ', sound_int_list[0:7], '...')
print('     Number of sample : ', len(sound_int_list), '\n')

sound_binaries = from_int_list_to_binaries(sound_int_list)
print('9.   Binary sound signal :', sound_binaries[:25], '...')
print('     Binary sound signal length :', len(sound_binaries), '\n')

sound_coded_binaries = hamming_7_4_coder(sound_binaries)
print('10.   Coded binary sound signal :', sound_coded_binaries[:25], '...')
print('     Coded binary sound signal length :', len(sound_coded_binaries), '\n')

transmitted_sound_coded_binaries = simulate_channel_effect(sound_coded_binaries)
print('11.   Transmitted coded binary sound signal :', transmitted_sound_coded_binaries[:25], '...')
print('     Transmitted coded binary sound signal length :', len(transmitted_sound_coded_binaries), '\n')

decoded_transmitted_sound_coded_binaries = hamming_7_4_decoder(transmitted_sound_coded_binaries)
print('12.  Decoded transmitted sound coded binaries : ', decoded_transmitted_sound_coded_binaries[:25], '...')
print('     Decoded transmitted sound coded binaries length : ', len(decoded_transmitted_sound_coded_binaries))
print('     Distance between the binary sound signal sent and received :',
      distance(sound_binaries, decoded_transmitted_sound_coded_binaries), '\n')

transmitted_sound_int_list = from_binaries_to_int_list(decoded_transmitted_sound_coded_binaries)
print('     Transmitted sound signal :', transmitted_sound_int_list[0:7], '...')
print('     distance between sound_int_list : ', distance(sound_int_list, transmitted_sound_int_list))

plt.plot(transmitted_sound_int_list)
plt.show()
print('     Transmitted sound signal plotted')

transmitted_sound = from_int_list_to_bytes_list(transmitted_sound_int_list)
export_sound('channel_coding/transmitted_sound.wav', transmitted_sound)
print('     transmitted sound exported')
