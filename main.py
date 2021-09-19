import pyaudio
import statistics
import math
import numpy
import serial
import time

CHUNK = 2048
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

dev_index = 1
port = 'COM9'
ard = serial.Serial(port,9600,timeout=5)


p = pyaudio.PyAudio()
stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                input_device_index = dev_index,
                frames_per_buffer = CHUNK)

print("* recording")

hl = 0
hr = 0

while True:
    data = stream.read(CHUNK)
    decoded = numpy.fromstring(data, dtype=numpy.int16)

    left = math.sqrt(statistics.mean([int(pow(x,2)) for x in decoded[0::2]]))
    right = math.sqrt(statistics.mean([int(pow(x,2)) for x in decoded[1::2]]))

    r = right/left
    ard.write(int(left).to_bytes(2, 'little'))
    ard.write(int(right).to_bytes(2, 'little'))

    #msg = ard.readline()
    #print(msg)

    #print(right, left)
    #print(hl, hr)




print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()
