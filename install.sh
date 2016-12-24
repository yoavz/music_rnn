conda create -n music_rnn python=2.7
source activate music_rnn

pip install -r requirements.txt

mkdir models

mkdir data
# http://www-etud.iro.umontreal.ca/~boulanni/icml2012
wget http://www-etud.iro.umontreal.ca/~boulanni/Nottingham.zip -O data/Nottingham.zip
unzip data/Nottingham.zip -d data/
