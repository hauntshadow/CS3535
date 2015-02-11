#
# Track ID:
# TRAWRYX14B7663BAE0
#

import matplotlib
matplotlib.use("Agg")
import pyechonest
import echonest.remix.audio as audio
import matplotlib.pyplot as plt
import scipy.spatial.distance as distance
import numpy as np
def main(input_file):
    t = pyechonest.track.track_from_filename(input_file)
    audiofile = audio.LocalAudioFile(input_file)
    print t.id
    segments = audiofile.analysis.segments
    pits = np.asarray(segments.pitches).astype(float)
    tims = np.asarray(segments.timbre).astype(float)
    pitdist = distance.cdist(pits, pits, 'euclidean')
    timdist = distance.cdist(tims, tims, 'euclidean')
    plt.imshow(pitdist)
    plt.gcf().savefig('pitchsim.png')
    plt.imshow(timdist)
    plt.gcf().savefig('timbresim.png')   
    

