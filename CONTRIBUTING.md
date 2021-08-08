#  Contributing 

## Be nice, patient and respectful
Like it says above, while interacting with each other, contributing or raising issues - be nice, patient and respectful. We are all in it 
for the joy of cool science and software - let's make it about that. 

## Issues 
If you are facing issues running the software, or suspect bugs please report the following in the issue raised:

* ```beamshapes``` version 
* the smallest possible reproducible example that consistently generates the bug in your system
* OS and version
* Your Python type (direct installation, anaconda, etc.)

## Directivity implementations

If you wish to contribute a directivity implementation for a source-model see the generalised workflow page [here](https://beamshapes.readthedocs.io/en/latest/general_workflow.html). In general, if you're in doubt about whether an implementation is of relevance to the `beamshapes` package, shoot me a message (thejasvib@gmail.com) and let's talk. 

For reasons of code homogeneity, I request that you keep the template structure suggested in the [how-to](https://beamshapes.readthedocs.io/en/latest/general_workflow.html) page. All implementations must have tests that at least check the coded implementation matches the published results of the original paper/book that described the model. (If you are planning to implement a directivity that isn't published or have calculated yourself - we still need tests, but I'd be curious to hear how to check the validity of the implementation's results!)
