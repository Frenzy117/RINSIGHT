import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np
import platform

if __name__ == '__main__':

    # If you got "ValueError: No input device matching", that is because your PC name example device
    # differently from tested list below. Uncomment the next line to see full list and try to pick correct one
    # print(sd.query_devices())

    fs = 48000  		# Sample rate
    duration = 3  # Duration of recording
    channels = 4

    print(sd.query_devices())
    #device ='MSA_ASR_Mic'
    device = "MicNode_4_Ch"

    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels, dtype='int16', device=device)
    print('Waiting...')
    sd.wait()  # Wait until recording is finished
    print('Done!')

    print("Shape of result: ")
    print(myrecording.shape)
    for ci in range(channels):
        print("Channel {}:".format(ci))
        print(myrecording[:,ci])

#    print("Playing back channel...")
#    for c in channels:
#        print("--{}".format(c))
#        sd.play(myrecording, fs)
#        sd.wait()

    time = np.arange(0, duration, 1 / fs)  # time vector
    plt.plot(time, myrecording)
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.title('MicNode 4 Channel')
    plt.show()
    
    for ci in range(channels):
        print("Playing back Channel {}:".format(ci))
        sd.play(myrecording[:,ci], fs)
        sd.wait()  # Wait until recording is finished
