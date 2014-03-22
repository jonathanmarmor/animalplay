# Animal Play TODO

## Melody

### To Transcribe

- Ron Sexsmith "secret heart"
- Fiona Apple "paper bag" Vocal rhythm in particular
- doc watson, james clear rock platt, james iron sides baker "st james hospital"
- Paul Simon "some folks lives roll easy"
- Eagles "lyin eyes" 2:30 "and dreams no one can steal" Ornaments in particular
- Art Pepper "September Song" 5:06
- a ghulam ali song
- Bob Dylan "Moonshiner" oraments


1. Transcribe something
2. Notate transcriptions using Abjad
3. Make variations on melody fragments

Maybe use this? http://onlinesequencer.net/8998


## Make little library of harmonic rhythms
- you can always expand this later
- make variations that can happen simultaneously: harm rhythm with some notes adjusted to happen with the meter


## Make list of basic melodic rhythms, which are variations on harmonic rhythms
-



- READ, use: https://github.com/josiah-wolf-oberholtzer/consort



TODO


- make chord type options
- make a library of rhythm options



global state management
- pc counter
- chord type counter
- harmony counter
- counters for time sig, rhythm, harmonic rhythm, metrical position
- drone/no drone (ie, current harmony type)
- soft/loud (current dynamic)
- low or high part of melody period (arohi/avrohi)
- what percentage of melody notes in this part should be out of tune
- what percentage of melody notes in this part should be heavily ornamented?


main loop
- choose whether there is a drone or not, and therefore what types of harmonies are allowed
- choose a phrase
    - number of bars
    - time sig of each bar
    - which kind of rhythmic texture to use (probably either 'choral' or 'triplets allowed')
    - harmonic rhythm
    - piano right hand rhythm
- for each harmonic rhythm note:
    - decide if piano hands will both be playing higher chords, or if left will be playing bass
    - choose piano notes:
        - look at previous harmony and pitches piano was playing
        - make a bunch of options based on what's allowed with voice leading and harmony types
        - choose an option
    -


- choose a bar length (ie, time signature)
- choose a
- choose piano right hand notes and harmony
- add piano left hand
-



second pass to
- spell notes
- create or fix beams

