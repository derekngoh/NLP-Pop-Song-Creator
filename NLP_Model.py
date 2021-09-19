import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Embedding,GRU
from tensorflow.keras.losses import sparse_categorical_crossentropy
from tensorflow.keras.models import load_model
from tensorflow.python.ops.gen_dataset_ops import shuffle_dataset

import Utils


class NLP_Model():
    def __init__(self) -> None:
        self.unique_char_str_set = None
        self.char_size = None
        self.encoding_dict = None
        self.decoding_dict = None
        self.compiled_contents = None
        self.encoded_contents = None
        self.seq_len = 0
        self.batch_size = 0
        self.sequences = None
        self.data_batches = None
        self.main_model = None
        self.pred_model = None
        self.new_song = None

    def compile_contents(self, folder_path):
        self.compiled_contents = Utils.compile_files_in_folder(folder_path)
        self.unique_char_str_set = sorted(set(self.compiled_contents))
        self.char_size = len(self.unique_char_str_set)

    def create_encoding_decoding_dict(self):
        self.encoding_dict = Utils.create_encoding_dict(self.unique_char_str_set)
        self.decoding_dict = Utils.create_indexed_array(self.unique_char_str_set)

    def encode_contents(self):
        self.encoded_contents = Utils.encode_contents(self.compiled_contents,self.encoding_dict)

    def create_sequences(self,seq_len):
        self.seq_len = seq_len
        dataset_tfDataset = tf.data.Dataset.from_tensor_slices(self.encoded_contents)
        self.sequences = dataset_tfDataset.batch(seq_len,drop_remainder=True)

    def shift_sequences(self,shift_amt=1):
        self.sequences = self.sequences.map(lambda x: Utils.char_shift(x, shift_amt))

    def shuffle_sequences(self,buffer=1200):
        self.sequences = self.sequences.shuffle(buffer)

    def create_batches(self, batch_size):
        self.batch_size = batch_size
        self.data_batches = self.sequences.batch(batch_size, drop_remainder=True)

    @staticmethod
    def sparse_cat_loss(y_true, y_pred):
        return sparse_categorical_crossentropy(y_true, y_pred, from_logits=True)

    def create_standard_model(self, embed_dim, rnn_neurons):
        model = Sequential()
        model.add(Embedding(self.char_size,embed_dim,batch_input_shape=[self.batch_size,None]))
        model.add(GRU(rnn_neurons, return_sequences=True, stateful=True,recurrent_initializer='glorot_uniform'))
        model.add(Dense(self.char_size))
        model.compile(optimizer='adam', loss=NLP_Model.sparse_cat_loss)
        self.main_model = model
        return self.main_model.summary

    def fit_model(self,epochs):
        self.main_model.fit(self.data_batches,epochs=epochs)
    
    def create_prediction_model(self,embed_dim,rnn_neurons,batch_size=1):
        model = Sequential()
        model.add(Embedding(self.char_size,embed_dim,batch_input_shape=[batch_size,None]))
        model.add(GRU(rnn_neurons, return_sequences=True, stateful=True,recurrent_initializer='glorot_uniform'))
        model.add(Dense(self.char_size))
        model.compile(optimizer='adam', loss=NLP_Model.sparse_cat_loss)
        self.pred_model = model
        return self.pred_model.summary()

    def set_trained_model_weights_on_pred_model(self,shape=[1,None]):
        self.pred_model.set_weights(self.main_model.get_weights())
        self.pred_model.build(tf.TensorShape(shape))

    def create_new_song(self,start_char,char_to_generate=2000,temp=1.0):
        song_created = []
        encoded_start_char = Utils.encode_contents(start_char,self.encoding_dict)
        encoded_start_char = tf.expand_dims(encoded_start_char, 0) #Reshape input. reviously it is []. After 'tf.expand_dims' becomes [[]]
        self.pred_model.reset_states() #Previously while training 'stateful'was set to True. This is to clear the states stored.

        for char in range(char_to_generate):
            pred = self.pred_model(encoded_start_char)
            pred = tf.squeeze(pred, 0) #remove one dimension
            pred = pred / temp #adjusted to temperature
            converted_probabilities_to_charindex = tf.random.categorical(pred, num_samples=1)[-1, 0].numpy() 
            encoded_start_char = tf.expand_dims([converted_probabilities_to_charindex],0) #expand [55] to [[55]] to match [batch, index] shape of the argument to model() i.e. encoded_start_char.
            song_created.append(Utils.decode_contents(converted_probabilities_to_charindex,self.decoding_dict)) #takes in [55] (not expanded) and append to prediction list giving ['r', 't', 'p']. ie. song_created. 
        
        self.new_song = start_char + ''.join(song_created)

        return self.new_song

    def save_file(self, content, filename):
        Utils.save_as_text_file(content,filename)
