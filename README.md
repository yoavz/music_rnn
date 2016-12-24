Overview
============
A project that trains a LSTM recurrent neural network over a dataset of MIDI files. More information can be found on the [writeup about this project](http://yoavz.com/music_rnn/) or the [final report](http://yoavz.com/music_rnn_paper.pdf) written. *Warning: Some parts of this codebase are unfinished.*

Dependencies
============

* Python 2.7
* Anaconda
* Numpy (http://www.numpy.org/)
* Tensorflow (https://github.com/tensorflow/tensorflow) - 0.8
* Python Midi (https://github.com/vishnubob/python-midi.git)
* Mingus (https://github.com/bspaans/python-mingus)
* Matplotlib (http://matplotlib.org/)

Basic Usage
===========

1. Run `./install.sh` to create conda env, install dependencies and download data
2. `source activate music_rnn` to activate the conda environment
3. Run `python nottingham_util.py` to generate the sequences and chord mapping file to `data/nottingham.pickle`
4. Run `python rnn.py --run_name YOUR_RUN_NAME_HERE` to start training the model. Use the grid object in `rnn.py` to edit hyperparameter
   configurations.
5. `source deactivate` to deactivate the conda environment
