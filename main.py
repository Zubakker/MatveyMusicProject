import wave
from math import sin, pi
import array 

data = array.array("h");
INTERVALS = [1,
             1.0594630943592953,
             1.122462048309373,
             1.1892071150027213,
             1.2599210498948734,
             1.3348398541700346,
             1.4142135623730954,
             1.498307076876682,
             1.5874010519682,
             1.6817928305074297,
             1.7817974362806794,
             1.887748625363388,
             2.000000000000001]

NCHANNELS = 1;
SAMPWIDTH = 2;
FRAMERATE = 44100;
SAMPLENGTH = 20;
NFRAMES = FRAMERATE * SAMPLENGTH

STRUCT = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
glnum = 0;
def recursion(n):
    global glnum;
    if (sum(STRUCT) == 6):
        nme = str([1] + STRUCT).replace(" ", "");
        ivals = []
        for i in range(6):
            if i == 2 and STRUCT[i]:
                lad = "MIN";
                break;
            if i == 3 and STRUCT[i]:
                lad = "MAJ";
                break;
            else:
                lad = "???"
        n = 0;
        pn = 0;
        for i in range(11):
            if STRUCT[i]:
                pn = n;
                n = i + 1;
                ivals.append((n - pn) / 2);
        ivals.append((12 - n) / 2);
        ivals = str(ivals).replace(" ", "");
        gen_audio([1] + STRUCT + [1], str(glnum).rjust(3, "0") + "|" + ivals + "|" + lad)
        glnum += 1;
        print([1] + STRUCT, lad, ivals)
        return;
    for i in range(n + 1, 11):
        STRUCT[i] = 1;
        recursion(i);
        STRUCT[i] = 0;
       
def gen_audio(struct, name): 
    data = array.array("h");
    file = wave.open(name + ".wav", "w");
    file.setnchannels( NCHANNELS );
    file.setsampwidth( SAMPWIDTH );
    file.setframerate( FRAMERATE );
    file.setnframes( NFRAMES );
    file.setcomptype("NONE", "Uncompressed");
    
    for i in range(len(struct)):
        freq = 440; 
        if struct[i]:
            freq *= INTERVALS[i];
            ufr = FRAMERATE / freq
           
            for a in range(FRAMERATE // 2):
                sample = 20000;
                sample *= sin((pi * a) / ufr);
                data.append(int(sample));
    file.writeframes(data.tobytes());
    file.close(); 

gen_audio([1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1], "TEST1")



recursion(-1);
