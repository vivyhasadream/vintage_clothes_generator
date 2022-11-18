# AI Costume Designer

## OBJECTIVE
Hey ladies and gentlemen, tired of seeing the boring clothes options? <br>
Hey Designer, run out of ideas and inspirations?

This generator will provide you endless clothes designs <br>
that haven’t existed before.

This generator will be your inspiration,<br>
or at least it could be for your entertainment to the eyes.

**In short, it's a "this costume design doesn't exist"**.


## DATA
Fashion trend is a circle, I would like to train on the costume designes in the past, <br>
and the museum is the best place to go.
The costumes they collected are the most iconic ones in the era, <br>
and with wide range of cultures.

Currently my model is trained on: <br>
2544 images (Public Domain) from The MET museum<br>
6588 images from Victoria & Albert museum

## Model

I used keras to build GAN for generation. <br>

based on this model:<br>
[DCGAN to generate](https://keras.io/examples/generative/dcgan_overriding_train_step/)
 
The models are tested with NVIDIA 3090 GPU

## STEPS AND NOTEBOOKS
the notebooks are named in order, indicating the working process.<br>
you will need to create folder to store images, csvs or files that genereated/scraped.

- Web scraping: requests, urllib
- Data cleaning
- Image processing: pillow
- Folder management: os, openCV
- Tensorflow/Keras


## NEXT PLAN
- More training images
- Conditional GAN to let users pick certain categories
- Higher resolution output
