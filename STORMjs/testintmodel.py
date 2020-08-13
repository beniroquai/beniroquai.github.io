#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 10:58:29 2020

@author: bene
"""
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import tensorflowjs as tfjs

# create sequential model
model = keras.Sequential(
    [
        layers.Dense(2, activation="relu", name="layer1"),
        layers.Dense(3, activation="relu", name="layer2"),
        layers.Dense(4, name="layer3"),
    ]
)
# Call model on a test input
KEY = 'sampleid'
MDL = 'mymodel'

model.compile(loss='mse',metrics='accuracy')

tfjs.converters.save_keras_model(model, MDL)

