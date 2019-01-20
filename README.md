# N-hance (pls)

[![](https://raw.githubusercontent.com/PetarV-/n-hance-pls/master/nhance-logo.png?token=AD_VHKroPhUIuDGY0ynsT4sT6WkL1aq-ks5cTU18wA%3D%3D)](https://nodesource.com/products/nsolid)

by [_Petar Veličković_](https://github.com/PetarV-) and [_Emma Rocheteau_](https://github.com/EmmaRocheteau)

Neural networks make your smartphone videos better... after you've filmed them

## Motivation

Smartphones have gradually revolutionised the way in which we record our most important events---with camera setups that are, at times, capable of rivalling bespoke cameras in terms of output. This has made smartphone cameras one of their centerpiece features, and one that, more often then not, determines their price tag.

However, phone cameras are also bound to have deficiencies---arising from the constrained nature of squeezing them onto a mobile device. For example, they may not be able to handle a certain lighting setup properly, and result in over- or under-exposed photos and videos. These effects generally become more dire as we move to the lower-end of the price spectrum.

While it may seem as if all is lost when a photo/video is taken under poor conditions, **neural networks** may be leveraged to remedy the situation---sometimes substantially. To demonstrate this, we present **N-hance (pls)**, (to the best of our knowledge) the first enhancing system for smartphone videos.

## Key results

Here we make use of the latest advances in enhancing smartphone photos through deep learning, and build up on them to create a viable **smartphone video enhancer**. By doing so, we demonstrate:
- Seamless _generalisation_ of the photo enhancement model into the video domain, requiring _negligible post-processing_;
- Favourable enhancement results _outside_ of the input distribution the model was trained on---namely, on _night-time recordings_;
- Applicability of fine-tuning a model pre-trained on a particular device to expand to another.

All of these features make our prototype a solid indicator of a potentially important future application area, providing a cost-effective way to obtain enhanced video recordings.

## Technology

Recent works from Ignatov _et al._, published at [ICCV 2017](https://www.vision.ee.ethz.ch/~ihnatova/index.html) and [CVPR 2018](https://www.vision.ee.ethz.ch/~ihnatova/wespe.html), demonstrate that convolutional neural networks can be used as _enhancers_ for smartphone camera photos, compensating for the specific shortcomings of said camera and making its output approach DSLR quality (at times, _indistinguishable_ from DSLRs to human assessors).

The techniques rely on a medley of several topical trends in deep learning for computer vision: [_all-convolutional networks_](https://arxiv.org/abs/1412.6806), [_neural style transfer_](https://arxiv.org/abs/1508.06576) and [_adversarial training_](https://arxiv.org/abs/1406.2661). The enhancer network is:
- an _all-convolutional network_, implying that it can process input images of arbitrary dimensions;
- forced to _preserve content_ of its input, by way of a _content-based loss_ based on deep activations of a pre-trained object recognition network (as used in style transfer);
- driven to _mimic the characteristics_ (such as colour and texture) of high-quality DSLR images through employing several _discriminator networks_.

With minimal fine-tuning (in TensorFlow) of a pre-trained model for iPhone 3GS photos, we have been able to obtain a viable enhancer for the iPhone 5 (deliberately selected here to emphasise the potential of enhancement). From here, creating a video enhancer boiled down to extracting the frames from the input (by using _scikit-video_) and processing them individually using the photo enhancer---_minimal postprocessing_ was necessary to create a coherent and useful output. We further extended the original enhancer network to support _batched inference_, speeding up the video processing by a factor of four.

Most surprisingly, we have found that the model fares well even when faced with inputs that drastically differ from the ones it was trained on---namely, the model provides a good level of enhancement on most _night-time_ videos, even though the [DPED](https://www.vision.ee.ethz.ch/~ihnatova/index.html) dataset used to train it consists solely of daytime photos.

By leveraging a Flask server and an Azure instance, we have exposed a clear interface for submitting new videos to be processed, as well as analysing and downloading the results.

## What's next?
Having demonstrated that a photo enhancer can be feasibly generalised to videos---even ones taken outside of the training distribution---we believe that this exposes clear potential for a robust mobile application; one that we hope to explore in the coming months.

## Main lesson learnt during the hackathon?
`ssh` uses port `22`, not `20`...


