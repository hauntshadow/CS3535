import pyechonest
import echonest.remix.audio as audio
import matplotlib.pyplot as plt
import scipy.spatial.distance as distance
import numpy as np
def main(input_filename):
    audiofile = audio.LocalAudioFile("lateralus.mp3")
    segments = audiofile.analysis.segments
    pits = np.asarray(segments.pitches).astype(float)
    tims = np.asarray(segments.timbre).astype(float)
    pitdist = distance.cdist(pits, pits, 'euclidean')
    timdist = distance.cdist(tims, tims, 'euclidean')
    plt.plot(pitdist) 
    plt.plot(timdist)   
        

