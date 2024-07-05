import argparse 
import librosa 
import soundfile as sf 
import matplotlib.pyplot as plt 

#filename = "mirror_mirror.wav" 
#samplerate = 44000 

def librosa_pitch_shift(filename, n_steps=0.1, samplerate=None):
    """shift the wav file pitch

    Args:
        filename (str): input filename
        n_steps (float): steps to shift the pitch
    """
    y, sr = librosa.load(filename)
    print(f"The input audio has the sample rate at {sr}")
    # I want to also try out a function in librosa called "pitch_shift"
    if samplerate:
        y_changed= librosa.effects.pitch_shift(y, sr=samplerate, n_steps=n_steps) 
        return y_changed
    y_changed= librosa.effects.pitch_shift(y, sr=sr, n_steps=n_steps) 
    return y, y_changed, sr


# not sure if n_step 8 is making any sense... In theory, it should higher the sound pitch...
def draw_figures(y, y_changed, raw_samplerate, samplerate, n_steps=0.1, image_filename="default_image_name.png"):  
    """Plot figures

    Args:
        y_changed (np.array): pitch shifted (np array)
        samplerate (int): sample rate
    """
    fig, ax = plt.subplots(nrows=2, figsize=(12, 9))
    librosa.display.waveshow(y, sr=raw_samplerate, ax=ax[0])
    ax[0].set(title="Original sound wave")
    librosa.display.waveshow(y_changed, sr=samplerate, ax=ax[1])
    ax[1].set(title=f"n_step {n_steps} sound wave. sample rate at {samplerate}")
    fig.tight_layout()
    fig.savefig(image_filename)

def save_audio_file(y_changed, output, samplerate):
    """Save audio file

    Args:
        y_changed (np.arry): pitch shifted (np array)
        output (str): output file name
        samplerate (int): sample rate. I am thinking to use the original one instead of the tuning. 
    """
    # save file 
    sf.write(output, y_changed, samplerate, subtype="PCM_24") 
    return 

if __name__ == "__main__": 
    parser = argparse.ArgumentParser(
                    prog='Test librosa',
                    description='Just trying something new',
                    epilog='Enjoy!')
    # mandatory
    parser.add_argument("--filename", type=str, help="input file name")
    parser.add_argument("--output", type=str, help="the output audio file name")
    # optional 
    parser.add_argument("--n_steps", type=float, nargs="?", help="n_step to shift the pitch")  
    parser.add_argument("--sample_rate", type=int, nargs="?", help="sample rate for the output")
    args = parser.parse_args()
    # print out the args
    print("The arguments are: ")
    print(args.filename, args.output, args.n_steps, args.sample_rate)
    y, y_changed, sr_raw= librosa_pitch_shift(args.filename)
    if not args.sample_rate:
        args.sample_rate = sr_raw
    draw_figures(y, y_changed, sr_raw, args.sample_rate, args.n_steps)
    # save the audio file 
    save_audio_file(y_changed, args.output, args.sample_rate)
