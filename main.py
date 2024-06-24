import librosa 
import soundfile as sf 
import matplotlib.pyplot as plt 

filename = "mirror_mirror.wav" 

samplerate = 40000 # sampling rate for output. Maybe it is too low?? 

y, sr = librosa.load(filename)
# I want to also try out a function in librosa called "pitch_shift"
y_change= librosa.effects.pitch_shift(y, sr=samplerate, n_steps=3) # not sure if n_step 8 is making any sense... In theory, it should higher the sound pitch...

# fig 
fig, ax = plt.subplots(nrows=2, figsize=(12, 9))
librosa.display.waveshow(y, sr=samplerate, ax=ax[0])
ax[0].set(title="Original sound wave")
librosa.display.waveshow(y_change, sr=samplerate, ax=ax[1])
ax[1].set(title="n_step 3 sound wave")
fig.tight_layout()
fig.savefig("Librosa_test.png")

# save file 
sf.write("step_change.wav", y_change, samplerate, subtype="PCM_24") 
