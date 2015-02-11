#
# Self_sim.py
# Creates PNG files that represent the pitch and timbre similarities
# for an audio file.
# Created by: Chris Smith
# Date: 2.11.2015
#
#

import matplotlib
matplotlib.use("Agg")
import pyechonest
import echonest.remix.audio as audio
import matplotlib.pyplot as plt
import scipy.spatial.distance as distance
import numpy as np
def main():
    track_id = "TRAWRYX14B7663BAE0"
    t = pyechonest.track.track_from_id(track_id)
    audiofile = audio.AudioAnalysis(track_id)
    segments = audiofile.segments
    pits = np.asarray(segments.pitches).astype(float)
    tims = np.asarray(segments.timbre).astype(float)
    pitdist = distance.cdist(pits, pits, 'euclidean')
    timdist = distance.cdist(tims, tims, 'euclidean')
    plt.imshow(pitdist)
    plt.gcf().savefig('pitchsim.png')
    plt.imshow(timdist)
    plt.gcf().savefig('timbresim.png')   
    

