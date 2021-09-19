import os, argparse, random
from NLP_Model import NLP_Model
from tensorflow.keras.models import load_model

cmdparser = argparse.ArgumentParser(description='song creator')
cmdparser.add_argument('--start_word', help='provide starting word or words for song', default='Baby')
cmdparser.add_argument('--song_length', help='set length of song in number of characters', default='1200')
cmdparser.add_argument('--training_epochs', help='number of epochs to train for', default='0')
cmdparser.add_argument('--saved_model_name', help='name of saved model to be loaded. e.g. pop_song_creator_model.h5', default='pop_song_creator_model.h5')
cmdparser.add_argument('--new_song_filename', help='name of new song to be saved as. e.g. my_latest_hit', default='my_latest_hit')
args = cmdparser.parse_args()

start_word = args.start_word
song_length = int(args.song_length)
training_epochs = int(args.training_epochs)
saved_model_name = args.saved_model_name
filename_to_be_saved_as = args.new_song_filename

load_h5_model = False if training_epochs else True
current_file_loc = os.path.dirname(os.path.realpath(__file__))
song_folder_loc = os.path.join(current_file_loc, "data\Song Lyrics")
h5_model_path = os.path.join(current_file_loc, saved_model_name)

#initialise model class
song_creator = NLP_Model()
song_creator.compile_contents(song_folder_loc)
song_creator.create_encoding_decoding_dict()
song_creator.encode_contents() 

#create sequences and batches for training
sequence_len = 60
batch_size = 128
embed_dim = 64
rnn_neurons = 1024

song_creator.create_sequences(sequence_len)
song_creator.shift_sequences()
song_creator.shuffle_sequences()
song_creator.create_batches(batch_size)
song_creator.create_standard_model(embed_dim, rnn_neurons) #returns model.summary()

random_num = random.randint(1,999)

#fit model to encoded dataset or load h5 model
if (load_h5_model): 
  song_creator.main_model = load_model(h5_model_path, custom_objects={"sparse_cat_loss": NLP_Model.sparse_cat_loss})
else: song_creator.fit_model(epochs=training_epochs)
song_creator.main_model.save(os.path.join(current_file_loc, "song_creator{a}.h5".format(a=random_num)))

#create new model for prediction with batch size of 1. Retrieve weights from trained model.
song_creator.create_prediction_model(embed_dim, rnn_neurons)
song_creator.set_trained_model_weights_on_pred_model() #returns prediction model summary

#new song
song_creator.create_new_song(start_word, song_length)
song_creator.save_file(song_creator.new_song, filename_to_be_saved_as + "{a}.txt".format(a=random_num))
print(song_creator.new_song)
