# AI Costume Designer

## OBJECTIVE
Hey ladies and gentlemen, tired of seeing the boring clothes options? <br>
Hey designers, run out of ideas and inspirations?

This generator will provide you endless clothes designs <br>
that haven’t existed before.

This generator will be your inspiration,<br>
or at least it could be for your entertainment to the eyes.

**In short, it's a "this costume design doesn't exist"**.


## DATA
### WHY IMAGES FROM MUSEUMS?
<img src="https://user-images.githubusercontent.com/73181107/207151756-b6d6f8e7-fe0f-4ce9-87dd-8ebafd15ff56.png" width="500">
I immediately thought of using images from the museum. Because the costumes should be iconic enough to be picked by museums. There will be costumes from different eras and different cultures.

<img src="https://user-images.githubusercontent.com/73181107/207152536-c769cc91-3737-4efc-a2b0-a4d2ffdebc17.png" width="500">
Furthermore, the costumes were shot in a very consistent style: put on a mannequin, hanging or lay flat.


And they have orgnized information which are very useful to sort out images (althoguh still need cleanup).

### SOME MUSEUMS OFFERS API:

API used:

- [MET API guideline](https://metmuseum.github.io/)

- [V&A API guideline](https://developers.vam.ac.uk/)

   NOTE: ...under the terms and conditions as set out [here](https://www.vam.ac.uk/info/va-websites-terms-conditions) in particular section 9.<br>

### COUNTS
I hand picked some keywords such as dress, robe, suit for locating images for training.

Currently my model is trained on: 

| Museum Name | MET | Victoria & Albert Museum | MFA Boston |
| :--------: | :-------------: | :-------------: | :-------------: |
| Location | New York | London | Boston |
| Images Used | 2544  | 6588  | 996 |
| Usage | Public Domain | non-commercial personal and educational purposes | Public Domain |

## DATA PREPARATION
### GRAYSCALE
<img src="https://user-images.githubusercontent.com/73181107/207155533-5c4cb08e-fa1f-4b08-a859-a8e06e064590.png" width="100">
After inspection, I found out the grayscaled images have 3 channels, so in this case, the RGB channels should have the same value.


### UNRELATED TOPICS
<img src="https://user-images.githubusercontent.com/73181107/207155585-fcb400eb-c019-40ed-afcd-ac35cb93025f.png" width="500">

After downloading the images, I noticed that there are some unrelated images due to the museums' searching algorithm. Since I stored the information about the costumes when scrapping, I was able to locate and filter the unrelated topics using other features such as object type.


### SQUARE THE IMAGE

I decided to use squared images for training. Cropping the image to the center will lose much important information of the costume, so two methods were tested to create a squared image.

- Mirror on the edge:

   For some resolution, the processed results are unacceptable.

<img src="https://user-images.githubusercontent.com/73181107/207157153-468d2014-7681-462d-9632-a254b4d1a16f.png" width="250"> <img src="https://user-images.githubusercontent.com/73181107/207157192-1e70d905-1a1d-4a8d-a5ab-8fb376e6eb10.png" width="250">

- Stretch on the edge:

   Stretch on the edge looks good to me, so I used this method.

<img src="https://user-images.githubusercontent.com/73181107/207159873-5643da63-8f92-4974-a6fd-8376f22204c8.png" width="500">


## MODEL

GAN is used for this image generation. <br>
 
The models were tested with NVIDIA 3090 GPU.

### BASELINE

trained with a very simple GAN (one layer conv2D + leaky RELU, strides 2, no maxpooling)

<img src="https://user-images.githubusercontent.com/73181107/207160136-a9621e93-61fb-43dc-acb6-28cf3cc6de2a.png" width="300">

### ATTEMPTS TO IMPROVE



<img src="https://user-images.githubusercontent.com/73181107/207160292-c1361c95-b453-407f-8a4f-5aa2d3d69fb0.png" width="500">

Tried:<br>
add VGG as base layers for discriminator, different filters combination or kernal size, balance batch size and input size, train longer, etc.

### CURRENT BEST RESULTS

trained with a VGG style discriminator (2 layers of conv2D, followed by a maxpooling)

<img src="https://user-images.githubusercontent.com/73181107/203331405-643657c9-6b13-405d-b705-d4d49655d342.png" width="500">
<img src="https://user-images.githubusercontent.com/73181107/203901004-b976b236-4939-495b-b437-f2d8fb6f0f41.png" width="500">


## SKILLS USED
The notebooks are named in order, indicating the working process.<br>
You will need to create folder to store images, csvs or files that genereated/scraped.

- Web scraping: requests, urllib
- Data cleaning: pandas
- Image processing: pillow. openCV
- Folder management: os
- Tensorflow/Keras


## NEXT PLAN
- More training images
- Use something like Conditional GAN to let users pick certain categories for generation
- Higher resolution output
- Try other generation model, such as stable diffusion
