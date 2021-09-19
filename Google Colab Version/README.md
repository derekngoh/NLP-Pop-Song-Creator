Pop Song Creator

**Program and Goal**
The aim of this project was to train a neural network model to write songs character by character. The model was trained on a training set of song lyrics of 49 leading singers, including Justin Bieber and Adele. While it was difficult to measure the accuracy of the generated songs, the newly created song did resemble some kind of modern pop music / rap. See results section for one of the songs created. 


**The Data**
The song lyrics used in this program contained songs from a list of 49 singers, totalling a character count of more than 6 million. The lyrics were made available by Paul Mooney of Kaggle and can be downloaded from https://www.kaggle.com/paultimothymooney/poetry. 


**Data Overview**
The data is made up of 49 text files, each containing a compilation of songs lyrics of a particular singer. Besides the lyrics, no other information were included. All song lyrics were listed line by line with different songs joined together at the end of the previous song lyrics.


**Structure & Approach**
The lyrics were first compiled into a single dataset and checked for the unique characters. There were some non-English characters but decision was made to ignore them as they took up less than 0.07% of the data. The lyrics were then encoded into numeric form. An arbituary decision of 60 characters were taken as the length of the training sequence and 128 sequences were taken per batch for model fitting. The model was created, taking reference from the DeepMoji architecture of one Embedding layer, one GRU layer and a Dense layer. After the model was fitted to the dataset, it was used to create new songs based on an input word.

The program is divided into the following 6 sections:

Section 1 : Explore Data 
Section 2 : Data Preprocessing
Section 3 : Batch Creation
Section 4 : Model Creation and Fitting
Section 5 : Song Creation
Section 6 : Results and Analysis 


**Result Analysis**
There were some incomplete use of brackets and incorrect capitalisations. There were also some unknown words, likely invented by the model. However, break points, line lengths and most punctuations were applied decently. Non-English words, while deliberately allowed to be present in the dataset, did not appear in the "new song". This fact corroborated with the fact that they occupy less than 0.07% of the dataset. The "new song" created did resemble some kind of modern rap. The model training without GPU would take 30 hours for 30 epochs on Google Colab. This model took slightly more than 60 minutes running with GPU on Google Colab. See below for the song created.

**New Song Created**
Stress aint a pride
I want U come sun free give is the time
She lick all the answers)
Pil of people, the pilos will die
You'll be crying
And nothin' can
And I take the X2 like a lil' pull up propd's voice
You just live on me gold
When I was warms I'm ismbly Mary
Got Mompes Deo more like a comfort, ask this game
She bress the hould jack her has gonna do
Roll up in a pointesport like 2 the 9 So life
And we'll start tauld off
More glocks on the floor)
(Girl, I'll get the building the melodram
Each more eablame on the cash that ain't even
Rest sit back, oth like a chase
Meft bat at don't make me
Hare like this
Girl tonich man In each and every single o you ain't seen her hot
Baby just like the fuckin' booy
If a walking bordlen party and we'll be gone
But that's too bad about it, wet out the way you do
babe 2 be up
Take it ry stuck with me?
(yeah)
What's your naughty
How they do it all our favorite, sock it and heaven's viewn grows up, oh
I will leave my powerve

He talkshad and all the storms
Heavy Cherhhatto tick, timba, I thought I hole things just
Anything
I wanna do it's everywhere, erfond raise yo' the Key

(Rep-CBr)]
U wouldn't have my life in the blocked
Just my everything that soulso
And if youre waitin' through
So hooker down
Oh, U remember thund 4 it grew, (tell them 2 i do)
Can't sleep
'ea back Baby,
My niXga pretend]
Were broken... man, just like that, none
And it seems like it's funny hoes, their happy cents
They leave me in Our sparfwete? (And I still wouldn't mind

Yes U dream
Daddy, dead
'COame
Stop the cry
Yes do you hear that
That's what I love you
Baby
I don't think of a girl assessian matasine
But since the sweet bright light (THUNz about the choices

Tonture's su breathafic, you enjoy your ass You said
that you may be different die 
Would U lients their blonk, I am
The arches will night
You wanna tell me when, when we a me and it'll be goe
We go no more you die
And I'm gonna last the se diverse on the bound