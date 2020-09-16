# Invisible-Cloak

## Table of contents

* Introduction
* Software used
* Code explained
* Reference links

## Introduction

You might have seen the famous JK Rowling series Harry Potter. In one of the series part, Harry uses an invisible cloak to hide himself from everyone and get hold of a secret book from the Hogwarts library. We always thought that the cloak was magical indeed and can make anyone invisible. But what if everyone can get hold of that magical cloak and indeed get invisible?..Cool right? So this project is based on an OpenCV project(a very basic and not yet ML project) and let's dig in on what the code is and how can we get magically invisible.

## Software used

This project uses OpenCV - a library of programming functions mainly aimed at real-time computer vision. Originally developed by Intel, this library helps in detecting images, patterns, colors etc.

## Code explained

This project is divided into two python programs, background and invisible_cloak. 
### Background.py
In this program, we allow our webcam to take an image of our background which will be used in the next program invisible_cloak and hence we allow the image to be saved as image.jpg in the folder of these programs.

![alt text](https://user-images.githubusercontent.com/43539707/93295825-9072e900-f80b-11ea-80e4-86bf3808eb9c.jpg)

### invisible_cloak.py
So the idea is that we will use a red colour cloth as out invisibility cloak. We will first determine the region covered by the cloth (determine pixels corresponding to red colour). To detect red colour we use the HSV(Hue-Saturation-Value) colour space.

We convert the image into HSV colour space

### Hue range 0-10 and 170-180
The Hue values actually range between 0-360 degrees but in OpenCV to fit into 8bit value the range is from 0-180. Red colour is represented by 0-10 and 170-180 values.

### Saturation range	120-255
Saturation represents purity of colour. Pure Red, Green and Blue are considered to be true saturated colours. As saturation decreases the effect of the other two colour component increases. Here we set the above value because our cloth is of highly saturated red color.

### Value range	70-255
Value corresponds to the brightness of the image. For a given pixel if the value is increased or decreased then values of R,G and B will increase or decrease respectively but their percentage contribution will remain unchanged. The lower value of the range is 70 so that we can detect red colour in the wrinkeles of the cloth as well.

We use Morphology to removes small regions of false detection which will avoid random glitches in the final output.

In this way, the red cloth around us is covered by the background image we took earlier which eventually makes us invisible!!

![alt text](https://user-images.githubusercontent.com/43539707/93296265-81406b00-f80c-11ea-830f-1234b5a5bf85.jpg)

![alt text](https://user-images.githubusercontent.com/43539707/93295671-31ad6f80-f80b-11ea-86f4-b724100e270c.jpg)

## Reference links

[youtube](https://www.youtube.com/watch?v=AkY2TpvDGUo&t=2305s)

[github](https://github.com/kaustubh-sadekar/Invisibility_Cloak/blob/master/Tutorial.md)
