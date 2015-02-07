import pyechonest
import echonest.remix.audio as audio
import matplotlib.pyplot as plt
import scipy.spatial.distance as distance
import numpy as np
def main(input_filename):
    audiofile = audio.LocalAudioFile("lateralus.mp3")
    segments = audiofile.analysis.segments
    collect = audio.AudioQuantumList()
    pitdist = np.empty([len(segments), len(segments)])
    timdist = np.empty([len(segments), len(segments)])
    for s in segments:
        for t in segments:
            timdist[s][t] = distance.euclidean(s.timbre,t.timbre)
            pitdist[s][t] = distance.euclidean(s.pitches,t.pitches)

    plt.plot(pitdist) 
    plt.plot(timdist)   
        

