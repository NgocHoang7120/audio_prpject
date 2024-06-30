from pydub import AudioSegment
import matplotlib.pyplot as plt
import numpy as np

def plot_spectrogram(audio, title):
    samples = audio.get_array_of_samples()
    plt.specgram(samples, Fs=audio.frame_rate, NFFT=1024, noverlap=512)
    plt.title(title)
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    string = title.split('.')
    plt.savefig(f"{string[0]}_{string[1]}.png")  # Save the figure
    plt.close()  # Close the figure to free up memory

def analyze_audio(file_path):
    audio = AudioSegment.from_file(file_path)
    bitrate = audio.frame_rate * audio.frame_width * 8 * audio.channels
    print(f"Bitrate: {bitrate / 1000} kbps")
    string = file_path.split('/')
    plot_spectrogram(audio, f"Spectrogram of {string[-1]}")

# Thay thế bằng đường dẫn tới file của bạn
analyze_audio("../ver1/BabyElephantWalk60.wav")
analyze_audio("./mp3/BabyElephantWalk60.mp3")
analyze_audio("./flac/BabyElephantWalk60.flac")
