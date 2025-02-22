import tensorflow as tf
import json
import shutil
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt 
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report
import sys
import os

#---FIXING PATH----------+
sys.path.append(str(sys.path[0][:-14]))
dirname = os.getcwd()
dirname = dirname.replace("ml_experiments/CNN/regression","")
sys.path.insert(1, os.path.join(dirname, "src/helper_functions"))
from plotting import plotting

class CNN_model():
    def __init__(self, X_train, X_cat_train, y_train, X_test, X_cat_test, y_test, epochs=5):
        """
        asdfasdf

        @arguments:
            X_train: <numpy.ndarray>
            y_train: <tensorflow.python.framework.ops.EagerTensor>
            X_test:  <numpy.ndarray>
            y_test:  <tensorflow.python.framework.ops.EagerTensor>
            epochs:  <int>

        @returns:
            None
        """
        self.X_train = X_train
        self.X_cat_train = X_cat_train
        self.y_train = y_train
        self.X_test = X_test
        self.X_cat_test = X_cat_test
        self.y_test = y_test
        self.epochs = epochs
        self.model = self._create_model()
        self.history = ""
        self.callback = Callback()

        self.categorical_shape = layers.Input(shape=(1,))
        
        print(self.X_train.shape)
        print(self.X_cat_train.shape)
        print(self.X_train[10].shape)
        print(self.X_cat_train[10].shape)

    def _create_model(self):
        """
        asfasdf

        @arguments:
            None

        @returns:
            None
        """
        # Create the model inputs
        image_input = layers.Input(shape=(28, 28, 1))
        categorical_input = layers.Input(shape=(1,))

        # Build the CNN model for the image input
        conv1 = layers.Conv2D(32, (3, 3), activation="relu")(image_input)
        maxpool1 = layers.MaxPooling2D((2, 2))(conv1)
        flatten = layers.Flatten()(maxpool1)

        # Concatenate the flattened image features with the categorical input
        concatenated = layers.concatenate([flatten, categorical_input])

        # Add the final regression layer
        output = layers.Dense(1, activation="linear")(concatenated)

        # Create the model
        model = models.Model(inputs=[image_input, categorical_input], outputs=output)
        return model

    def compile(self, model_name):
        """
        asdfasdf

        @arguments:
            model_name: <string> Name of the figure that will be saved

        @returns:
            None
        """
        tf.keras.utils.plot_model(
            self.model,
            to_file= model_name + ".png",
            show_shapes=True,
            show_layer_names=True,
            rankdir="TB",
            expand_nested=True,
            dpi=96,
        )

        self.model.compile(optimizer = "sgd", loss = "mse", metrics = [tf.keras.metrics.RootMeanSquaredError(), \
                tf.keras.metrics.MeanAbsoluteError(), tf.keras.metrics.MeanAbsolutePercentageError(), \
                tf.keras.metrics.MeanSquaredLogarithmicError(), tf.keras.metrics.CosineSimilarity(), \
                tf.keras.metrics.LogCoshError()])

    def evaluate_model(self, X_val, y_val, save_stats=True):
        """
        asdfasdf

        @arguments:
            X_val: <>
            y_val: <>
            save_stats: <>
        @returns:

        """
        try:
            results = self.model.evaluate(X_val, y_val, batch_size=128)
        except OverflowError as e:
            print(f"Error occured in <evaluate_model>. Error: {e}")
            return None

        predictions = self.model.predict(self.X_test[:])
        stats = {
            'loss': results[0],
            'RMSE': results[1],
            'MAE': results[2],
            'MAPE': results[3],
            'MSLE': results[4],
            'CosSim': results[5],
            'LogCoshE': results[6],
            'prediction': predictions.tolist()
        }

        if save_stats:
            with open("test" + '.json', 'w') as f:
                json.dump(stats, f)
            dirname_here = os.getcwd()
            try:
                shutil.move(dirname_here + "/" + "test" + ".json", dirname_here + "/val_stats/" + "test" + ".json") 
            except FileNotFoundError as e:
                print(f"Could not save validation statistics. Error: {e}")
        
        model_name = "test_CNN_re"
        plotter = plotting(self.y_test, predictions, self.history, model_name, "/Users/edwardglockner/OneDrive - Uppsala universitet/Teknisk Fysik/Termin 6 VT23/Kandidatarbete/DM-signals-at-LHC-with-ML/ml_experiments/CNN/regression")
        plotter.loss(cl_or_re="re", show=True)
        plotter.rmse(show=True)

   
    def train(self, print_perf=True):
        """
        asdfasdf

        @arguments:
            print_perf <bool>
        
        @returns:
            None
        """
        self.history = self.model.fit([self.X_train, self.X_cat_train], self.y_train, epochs = 20,
                            validation_data = ([self.X_test, self.X_cat_test], self.y_test), callbacks = [tf.keras.callbacks.EarlyStopping(monitor='val_loss', 
                                min_delta=0, 
                                patience=2, 
                                verbose=0, 
                                mode='auto', 
                                baseline=None,
                                start_from_epoch=1,
                                restore_best_weights=True)])

        self.model.save("./model.h5")
        self.evaluate_model(self.X_test, self.y_test)

class Callback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if (logs.get('accuracy') > 0.995):
            print("\nReached 99.5% accuracy so cancelling training!")
            self.model.stop_training = True


