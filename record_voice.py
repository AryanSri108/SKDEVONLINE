#TODO Task No 3: RECORD YOUR VOICE
"""
Python can be used to perform a variety of tasks. One of them is creating a voice recorder.
We can use python's sound device module to record and play audio. This module along with
the wavio or the SciPy module provides a way to save recorded audio.
"""
import tkinter as tk
from tkinter import messagebox
import sounddevice as sd
from scipy.io.wavfile import write

def AudioRecord():
    duration = int(DurationEntry.get())
    filename = fileNameEntry.get() + ".wav"
    sampleRate = 44100
    recording = sd.rec(int(duration * sampleRate), samplerate=sampleRate, channels=2)
    sd.wait()
    write(filename, sampleRate, recording)
    messagebox.showinfo("Success", f"Recording saved as {filename}")

root = tk.Tk()
root.title("Audio Recorder")
root.geometry("300x200")
root.config(bg="alice blue")

tk.Label(root, text="Audio Recorder", font=("Helvetica", 16), bg="alice blue").pack(pady=10)
tk.Label(root, text="Duration (seconds):", font=("Helvetica", 12), bg="alice blue").pack()
DurationEntry = tk.Entry(root, font=("Helvetica", 12))
DurationEntry.pack(pady=5)

tk.Label(root, text="Filename:", font=("Helvetica", 12), bg="alice blue").pack()
fileNameEntry = tk.Entry(root, font=("Helvetica", 12))
fileNameEntry.pack(pady=5)

tk.Button(root, text="Start Recording...", font=("Helvetica", 12), bg="light green", command=AudioRecord).pack(pady=20)

root.mainloop()


