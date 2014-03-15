# Animal Play

Music for clarinet, violin, cello, piano, and synthesizer for SPOR Festival 2014.


## Setup

    brew install freetype gfortran redis mongodb
    git clone https://github.com/jonathanmarmor/animalplay.git
    pip install -r requirements.txt

## Run

    cd animalplay
    ./animalplay.py

Go to ~/output/animalplay to see the music generated.

### Options

    ./animalplay --help

    usage: animalplay.py [-h] [--no-midi] [--no-parts]

    optional arguments:
      -h, --help  show this help message and exit
      --no-midi   Do not make midi files.
      --no-parts  Do not make instrument parts. Make the score only.
