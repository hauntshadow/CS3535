#Problem
We want to graph the distances between every pair of segments in a song.

#Questions
1. How do we get the segments from a song?
2. How do we get the data from each segment?
3. How do we get the distance between two segments in a song?
4. How do we graph a list of distances?

#Resources
1. [EchoNest Remix API]
2. 

####Mini-abstract and relevance of the [EchoNest Remix API]
 The [EchoNest Remix API] is the documentation for the module that allows us to extract a song's data.  This data can be obtained from either a song ID or a local audio file.  We are able to get the segments, as well as their data, with the [EchoNest Remix API].  In order to compare the segments, the [Infinite Jukebox] uses each segment's pitch, timbre, starting loudness, max loudness, and its duration.  The following code snippet shows how to get each of these pieces of data for a segment.
 
 The following code shows how to get the tempo from a local song:
 ```python
 import echonest.remix.audio as audio
 #Analyze the song and print the tempo. Output gives confidence and value.
 t = audio.AudioAnalysis("path to the local song")
 segments = t.segments
 ```
 
####Mini-abstract and relevance of the [eyeD3 API]
 The [eyeD3 API] is the documentation for the module that allows us to view and edit the ID3 tags that are linked to MP3 files.  The documentation for it gives in depth information about the insides of the eyeD3 module, including the source code for the package.
 
 By viewing the ID3 tag, information such as artist, genre, year produced, album, and many more pieces of data are available.
 This answers both question 2 and question 3: How do we get the genre for a particular song?  How do we get the year for a song?
 
 The following code demonstrates how to use eyeD3 and python to get the genre and year for a local song:
 
 ```python
 import eyed3
 audiofile = eyed3.load("path to the local song")
 #Prints the date that is considered most likely to be the desired date.
 print audiofile.tag.getBestDate()
 #Prints the name of the audiofile's genre, as well as the decimal value associated with it.
 print audiofile.tag._getGenre().name
 print audiofile.tag._getGenre().id
 ```
 
 [EchoNest Remix API]: http://echonest.github.io/remix/apidocs/
