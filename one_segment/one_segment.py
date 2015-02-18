#!/usr/bin/env python
# encoding: utf=8
"""
one.py

Digest only the first beat of every bar.

By Ben Lacker, 2009-02-18.

"""

'''
one_segment.py

Author: Chris Smith, 02-05-2015

Changes made to original one.py:

    - Changes made to take the first segment out of every beat.
    - Does not take the first beat from every bar anymore.

The original code is stored at this address: https://github.com/echonest/remix/blob/master/examples/one/one.py
'''
import echonest.remix.audio as audio

usage = """
Usage: 
    python one.py <input_filename> <output_filename>

Example:
    python one.py EverythingIsOnTheOne.mp3 EverythingIsReallyOnTheOne.mp3
"""

def main(input_filename, output_filename):
    audiofile = audio.LocalAudioFile(input_filename)
    '''
    This line got the bars of the song in the previous version:
    bars = audiofile.analysis.bars
    
    Now, this line gets the beats in the song:
    '''
    beats = audiofile.analysis.beats
    collect = audio.AudioQuantumList()
    '''
    This loop got the first beat in each bar and appended them to a list:
    for bar in bars:
        collect.append(bar.children()[0])
        
    Now, this loop gets the first segment in each beat and appends them to the list:
    '''
    for b in beats:
        collect.append(b.children()[0])
    out = audio.getpieces(audiofile, collect)
    out.encode(output_filename)

if __name__ == '__main__':
    import sys
    try:
        input_filename = sys.argv[1]
        output_filename = sys.argv[2]
    except:
        print usage
        sys.exit(-1)
    main(input_filename, output_filename)
