import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
FIG_SIZE = (15,10)

file = "Ali.wav"
# waveform
signal, sr = librosa.load(file, sr=22050) # sr * T -- 22050 * 30 sec
librosa.display.waveshow(signal, sr=sr)
#plt.xlabel("Time")
#plt.ylabel("Amplitude")
#plt.show()



# fft -- spectrum
fft = np.fft.fft(signal)

magnitude = np.abs(fft)
frequency = np.linspace(0, sr, len(magnitude))

left_frequency = frequency[:int(len(frequency)/2)]
left_magnitude = magnitude[:int(len(frequency)/2)]

plt.plot(left_frequency, left_magnitude)
#plt.xlabel("Frequency")
#plt.ylabel("Magnitude")
#plt.show()

# stft -- spectrum
n_fft = 2048
hop_length = 512

stft = librosa.core.stft(signal, hop_length=hop_length, n_fft=n_fft)

spectrogram = np.abs(stft)
log_spectrogram = librosa.amplitude_to_db(spectrogram)   ##apply a log

#librosa.display.specshow(log_spectrogram, sr=sr, hop_length=hop_length)
#plt.xlabel("Time")
#plt.ylabel("Frequency")
#plt.colorbar()
#plt.show()

# MFCCs
# MFCCs
# extract 13 MFCCs
MFCCs = librosa.feature.mfcc(signal, sr=sr, n_fft=n_fft, hop_length=hop_length, n_mfcc=13)

# display MFCCs
plt.figure(figsize=FIG_SIZE)
librosa.display.specshow(MFCCs, sr=sr, hop_length=hop_length)
plt.xlabel("Time")
plt.ylabel("MFCC coefficients")
plt.colorbar()
plt.title("MFCCs")

# show plots
plt.show()
