Pop Song Creator

**Program and Goal**
The aim of this project was to train a neural network model to write songs character by character. The model was trained on a training set of song lyrics of 49 leading singers, including Justin Bieber and Adele. While it was difficult to measure the accuracy of the generated songs, the newly created song did resemble some kind of modern pop music / rap. See results section for one of the songs created.


**The Data**
The song lyrics used in this program contained songs from a list of 49 singers, totalling a character count of more than 6 million. The lyrics were made available by Paul Mooney of Kaggle and can be downloaded from https://www.kaggle.com/paultimothymooney/poetry. 


**Data Overview**
The data is made up of 49 text files, each containing a compilation of songs lyrics of a particular singer. Besides the lyrics, no other information were included. All song lyrics were listed line by line with different songs joined together at the end of the previous song lyrics.


**How to Run**
Download "data" folder
Download the following 3 Python files and the trained model h5 file:
1. Song_Creator.py
2. NLP_Model.py
3. Utils.py
4. pop_song_creator_model.h5 

If running without GPU, follow the following steps to run the program using the trained model.
1. In the terminal, cd into the directory where the downloaded files are. Make sure files are organised as shown.
2. Enter command "python SongCreator.py [-h] [--start_word START_WORD] [--song_length SONG_LENGTH] [--new_song_filename NEW_SONG_FILENAME] [--saved_model_name SAVED_MODEL_NAME]" 
3. Example: python SongCreator.py --start_word Baby --song_length 600 --new_song_filename my_latest_hit --saved_model_name pop_song_creator_model.h5

If running with GPU, follow the steps below to train your own model.
1. In the terminal, cd into the directory where the downloaded files are. Make sure files are organised as shown.
2. Enter command "python SongCreator.py [-h] [--start_word START_WORD] [--song_length SONG_LENGTH] [--training_epochs TRAINING_EPOCHS]
                       [--new_song_filename NEW_SONG_FILENAME]"
3. Example: python SongCreator.py --start_word Baby --song_length 600 --training_epochs 45 --new_song_filename my_latest_hit


**Result**
There were some incomplete use of brackets and incorrect capitalisations. There were also some unknown words, likely invented by the model. However, break points, line lengths and most punctuations were applied decently. Non-English words, while deliberately allowed to be present in the dataset, did not appear in the "new song". This fact corroborated with the fact that they occupy less than 0.07% of the dataset. The "new song" created did resemble some kind of modern rap. The model training without GPU would take 30 hours for 30 epochs on Google Colab. This model took slightly more than 60 minutes running with GPU on Google Colab. See below for the song created.


Baby, yeah? (We're gonna let me wrote)
U will do that, just give up some driver see
And dance and a deal on it
So disdance you still moved cuiling
   A fire of day arn in my head I drown in an ecstacy I call my whisky man
Weis four ontion myself
C'mon & we go t'p simmachin', strollin me and you see I?
Around the concracch, I shouldn't don't make it like a grase, hello how,
John daddy's heart to splate at my front Seems so fuck the hook
U are shotting ready 2 spray to take
You are the right hand
Everybody's talking to my cohond would stay in care of
And in the ime A Sense we get the floor)
(get one go gus in that strain of dreams
What has vibe if we had and knice, come.

This whole world to please right (Foxuriling capidgalkis before O prold, tonight
Baby be down in the volviety
This don't kick it thom (Go cra)
Bon we ping bad All them force of this continue of Eveand two fewigary; ords of my wine
(No)
(Come on, name is mothafucking...
The tears are falling on the right
I knew u wanna know how I feel, justine slidin' away
Hey Hey (Cet
Head down, down on me
Ohh Hey, hey Andirl beats right in the firewards
I promise that I wasnt
But now mud's hoes big booty holy weip shouns and raised in


**Requirements**
1. Python 3.5 or higher
2. Tensorflow version 2.6.0 or higher