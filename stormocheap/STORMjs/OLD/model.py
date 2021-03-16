"""
Created on Thu Apr  2 08:58:10 2020

@author:

Some sources:
    https://github.com/mnicholas2019/M202A/blob/master/PreviousWork/Activity-Recognition.ipynb
    https://github.com/vikranth94/Activity-Recognition/blob/master/existing_models.py
"""
from tensorflow import keras
from tensorflow.keras import layers

import tensorflow as tf


def depth_to_space(input_tensor, scale=2):
    return tf.depth_to_space(input_tensor, 2)


def SOFI_seq(Ntime=1, Nbatch=1, Nx=100, Ny=100, features=1, Nchannel=1, upsample=2):
    # create our model here
    kernel_size = 3
    nfilters_lstm = 4
    
    model = keras.Sequential(
    [
     layers.Reshape(target_shape=(Nbatch,Nx,Ny,Ntime), name='reshape_1d_2d'),
     layers.ConvLSTM2D(filters=nfilters_lstm , kernel_size=(kernel_size, kernel_size)
              , data_format='channels_last'
              , recurrent_activation='hard_sigmoid'
              , activation='tanh'
              , padding='same'
              , return_sequences=False
              , name='convlstm2d'),
     layers.Conv2DTranspose(8, (3,3), strides=(2,2), padding='same'),#, input_shape=(2, 2, 1)),
     #UpSampling2D(size=(2,2), name='upsampling_1'), #Subpixel_layer(),
     #layers.BatchNormalization(name='batchnorm_1'),
     #layers.Lambda(depth_to_space()),
     layers.Conv2D(1, 1, strides=(1, 1), padding='same', data_format='channels_last',  activation='relu'), 
     layers.Reshape((Nx*Ny*upsample**2,), name='reshape_2d_1d')
    ])

    model.compile()
    
    return model


# Define Parameters
# Define Parameters
Ntime = 30
Nbatch = 1
Nx = 128
Ny = 128
features = 1
Nchannel = 1

# Training parameters
Nepochs = 1
Niter = 2
N_upsample = 2

# create the model
print('Create the model!')
x_ = tf.ones((1,Ntime*Nbatch*Nx*Ny)) #(Ntime, Nbatch, Nx, Ny, Nchannel)
model = SOFI_seq(Ntime=Ntime, Nbatch=Nbatch, Nx=Nx, Ny=Ny, features=features, Nchannel=Nchannel, upsample=N_upsample)

for layer in model.layers:
    print(layer.weights)
    
y_ = model(x_)
print(model.summary())


import tensorflowjs as tfjs
myfilename = 'converted_model'+str(Nx)+'_'+str(Ntime)+'_keras'
tfjs.converters.save_keras_model(model, myfilename)
tfjs.converters.load_keras_model(myfilename+'/model.json')
