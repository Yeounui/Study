# Image extraction from videos

Tiny scripts which slice a video into frames.

## What is it?

OpenCV and Numpy are used.

It was written for making image dataset for personal practice. In my case, microscopic samples of Trypanosoma brucei are recorded. With the data, I have practiced to build a DL model for object detection, which detects each unit and predicts its vitality. The parasite has different morphologies depending on its vitality. It has an elongated body having a streamlined and tapered shape when it is in vivo. However, ex vivo, it loses its morphology and becomes a round shape. Therefore, not only its motility is a sign of vitality, but the morphology can be also another sign.

### image_extraction_from_videos.py
> A script slicing frames from multiple videos. 'image_seg.py' is a dependant.
>

### image_seg.py
>+ image_extraction_from_video
>
>   Extracts frames from a single video. 

>+ image_grayscale_unification 
>
>   Converts a frame into grayscale image. 

### image_unification_comparison.py
> A script to compare images with two different condition after image conversion.

