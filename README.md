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
Fashion trend is a circle, I would like to train on the costume designes in the past, <br>
and the museum is the best place to go.
The costumes they collected are the most iconic ones in the era, <br>
and with wide range of different cultures.

Currently my model is trained on: 

| Museum Name | MET | Victoria & Albert Museum | MFA Boston |
| :--------: | :-------------: | :-------------: | :-------------: |
| Location | New York | London | Boston |
| Images Used | 2544  | 6588  | 996 |
| Usage | Public Domain | non-commercial personal and educational purposes | Public Domain |

### SOME MUSEUMS OFFERS API:

API used:

- [MET API guideline](https://metmuseum.github.io/)

- [V&A API guideline](https://developers.vam.ac.uk/)

   NOTE: ...under the terms and conditions as set out [here](https://www.vam.ac.uk/info/va-websites-terms-conditions) in particular section 9.<br>



## MODEL

GAN is used for this image generation. <br>
 
The models were tested with NVIDIA 3090 GPU.

## CURRENT RESULTS

<img src="https://user-images.githubusercontent.com/73181107/203331405-643657c9-6b13-405d-b705-d4d49655d342.png" width="500">
<img src="https://user-images.githubusercontent.com/73181107/203901004-b976b236-4939-495b-b437-f2d8fb6f0f41.png" width="500">




## STEPS AND NOTEBOOKS
The notebooks are named in order, indicating the working process.<br>
You will need to create folder to store images, csvs or files that genereated/scraped.

- Web scraping: requests, urllib
- Data cleaning
- Image processing: pillow
- Folder management: os, openCV
- Tensorflow/Keras


## NEXT PLAN
- More training images
- Use something like Conditional GAN to let users pick certain categories for generation
- Higher resolution output
- Try other generation model
