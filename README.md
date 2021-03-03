# OscilloscopeDisplay
 Turns an oscilloscope into a display.
 
 ## Video Demo
[![Watch the video](https://img.youtube.com/vi/U_4r8LO_1xo/maxresdefault.jpg)](https://youtu.be/U_4r8LO_1xo)

 ## How it works
 An input mp4 video will be converted into an audio file, containing the information for any XY plotter to display. In this case, the plotter can be Matplotlib or the oscilloscope. If the right and left channel of the audio player is then connected to the plotter, a downscaled version of the input video, with a resolution of 10px * 10px, will be displayed. The pixels are encoded into the Y axis. They are waves of different amplitudes, making 3 different opacities, creating low quality grayscale frames. This means that they are part of the horizontal scanlines, distorted to different levels when a pixel is active. The screen refreshes 90 times per second, though the example only draws 45 frames each second.
 
 ## Dependencies
 Python 3.8.5
 * Opencv-python~=4.5.1.48  
 * Numpy~=1.20.1  
 * Tqdm~=4.58.0  
 * Matplotlib~=3.3.4  
 * Sounddevice~=0.4.1  
 * Scipy~=1.6.1  

## Run
 * Generate audio from video: python3 play.py
 * Display driver only: python3 display.py
 * Draw circle: python3 test.py
 
