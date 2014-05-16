speaker_project
===============

Folder Structure:
----------------

  - data/gtzan-proc/genres : contains the final required pitch values for each of the genres.
  - submission/paper : contains the submitted report
  - submission/presentation : contain the presentation slides used
  - code/output : contains the output for feature sets used in the project. This folder should also be used genrating the final classification/clustering values, as explained later.
  - code/separateLeadStereo : contains the code used for source separation(from pyFASST). It takes a very long time to complete. I will be sending over the dropbox link for the final generated outputs.
  - code/src : contains the code for feature extraction, classification, clustering, as well as mfcc(from auditory toolbox)
  - run.sh : a sample run to produce the final classification/clustering. It can be used a template which can be modified as required.
  - runReports.sh : a sample run to generate values used in the paper.

The original dataset can be downloaded from : http://marsyas.info/download/data_sets/
However, most of files required to demo are included along.

Additionally, I will send over the dropbox link for the processed dataset, which again may not be required for demo as the extracted 
features are included along with this submission.

The instructions for install of the required packages can be found here:
http://scikit-learn.org/stable/install.html
======================================================================================================

# Basic demo:
--------------

  sh run.sh (from the root directory)

This does not calculate mfcc features, due to a matlab dependency. Look ahead for instructions on how to incorporate them.

# Each of its steps have been explained in the script.

========================================================================================================

# Directions for usage to generate reports for cases mentioned in the paper.
---------------------------------------------------------------------------

# The above demo was an attempt to explain the steps involved in the entire workflow.
# However, most of the computations need to demonstrate the claims have been accumulated.

# Enclosing script
  
  sh runReports.sh

# It generates a lot of output, so you might want to redirect it to a file

=======================================================================================================

# generating mfcc features (already stored)
--------------------------

# Run the getMFCC.m script in the code/src folder after pasting getMFCC.m and mfcc.m to the folder containing the audio files
# when asked for the path, specify *0000*.wav, or whichever files are desired

=======================================================================================================

# source separation from original audio (already stored)
-------------------------------------------------------

# Use the source code in the code/separateLeadStereo folder
python separateLeadStereo.py <wav-file>

# It generates the solo audio file, the background audio file and the pitch extracted.
