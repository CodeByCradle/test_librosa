import argparse 
import librosa 
import soundfile as sf 
import matplotlib.pyplot as plt 

#filename = "mirror_mirror.wav" 
#samplerate = 44000 

def librosa_pitch_shift(filename, n_steps=0.1, samplerate=None):
    """shift the wav file pitch

    Args:
        filename (str): _description_
        n_steps (float): _description_
    """
    y, sr = librosa.load(filename)
    # I want to also try out a function in librosa called "pitch_shift"
    if samplerate:
        y_changed= librosa.effects.pitch_shift(y, sr=samplerate, n_steps=n_steps) 
        return y_changed
    y_changed= librosa.effects.pitch_shift(y, sr=sr, n_steps=n_steps) 
    return y, y_changed


# not sure if n_step 8 is making any sense... In theory, it should higher the sound pitch...
def draw_figures(y, y_changed, samplerate, n_steps, image_filename="default_image_name.png"):  
    """Plot figures

    Args:
        y_changed (np.array): _description_
        samplerate (int): _description_
    """
    fig, ax = plt.subplots(nrows=2, figsize=(12, 9))
    librosa.display.waveshow(y, sr=samplerate, ax=ax[0])
    ax[0].set(title="Original sound wave")
    librosa.display.waveshow(y_changed, sr=samplerate, ax=ax[1])
    ax[1].set(title=f"n_step {n_steps} sound wave")
    fig.tight_layout()
    fig.savefig(image_filename)

def save_audio_file(y_changed, output, samplerate):
    """Save audio file

    Args:
        y_changed (np.arry: _description_
        output (str): _description_
        samplerate (int): _description_
    """
    # save file 
    #sf.write("step_change.wav", y_changed, samplerate, subtype="PCM_24") 
    sf.write(output, y_changed, samplerate, subtype="PCM_24") 

if __name__ == "__main__": 
    parser = argparse.ArgumentParser(
                    prog='Test librosa',
                    description='Just trying something new',
                    epilog='Enjoy!')
    
    parser.add_argument("--filename", type=str, help="input file name")
    parser.add_argument("--n_steps", type=float, help="n_step to shift the pitch")  
    parser.add_argument("--sample_rate", type=int, help="sample rate for the output")
    parser.add_argument("--output", type=str, help="the output audio file name")
    args = parser.parse_args()
    y, y_changed= librosa_pitch_shift(args.filename)
    draw_figures(y_changed, args.sample_rate, args.n_steps)
    save_audio_file(y_changed, args.output, args.sample_rate)
