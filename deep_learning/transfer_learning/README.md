General Task Requirements
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.11)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/env python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle style (version 2.14.0)
All your modules should have documentation (python3 -c 'print(import("my_module").doc)')
All your classes should have documentation (python3 -c 'print(import("my_module").MyClass.doc)')
All your functions (inside and outside a class) should have documentation (python3 -c 'print(import("my_module").my_function.doc)' and python3 -c 'print(import("my_module").MyClass.my_function.doc)')
All your files must be executable
The length of your files will be tested using wc
Packages:
numpy 2.0.2
pandas 2.2.2
Tensorflow 2.18.0
Matplotlib 3.10.0
0-frozen_extractor.py
0. Frozen Feature Extractor
Write a function build_feature_extractor() that loads a pretrained CNN model (e.g., MobileNetV2) from Keras applications, removes its classification head, and freezes its weights.

The function should:

Load MobileNetV2 with weights="imagenet", input_shape=(224, 224, 3) and without it's classification head
Freeze the base model
Add a GlobalAveragePooling2D layer on top
Return a Keras Model that outputs features from input images using the frozen base model.
1-classification_head.py
1. Classification Head
Write a function add_classification_head(base_model, num_classes) that attaches a custom classification head to a pretrained feature extractor.

Arguments:

base_model: A Keras Model whose output is a pooled feature vector.
num_classes: An integer representing the number of output classes.
The head should:

Take the output of the base model
Add a dense layers with 128 filters and relu activation
Add a final classification layer
Return a new Keras Model ready for classification.
2-unfreeze_top.py
2. Unfreezing Layers
Write a function unfreeze_top_layers(model, n_layers) that unfreezes the last n_layers of the base model inside a transfer learning pipeline, and leaves the rest frozen.

Arguments:

model: A full Keras Model with a base model as its second layer.
n_layers: Integer specifying how many of the last layers in the base model should be unfrozen (set as trainable).
The function should:

Assume the base model is the first layer of the input model.
Unfreeze the last n_layers of the base model.
Leave earlier layers frozen.
Return None
3-data_aug.py
3. Data Augmentation
Write a function build_data_augmentation() that creates a Keras Sequential model containing common image data augmentation operations. This augmentation will be applied to training images before they are passed into the pretrained CNN.

The function should:

Create a tf.keras.Sequential model
Add the following augmentation layers:

RandomFlip("horizontal")

RandomRotation(0.15)

RandomZoom(0.15)

RandomContrast(0.1)

Return the Sequential augmentation model

Use Keras preprocessing layers from tf.keras.layers And make sure all layers are seeded with value 42 to ensure reproducibility during training and testing.

4-transfer_101.py
4. Knowledge Transfer: Taming the 101
Write a function def train_transfer_model(): that builds, trains, and saves an image classifier using transfer learning on the Stanford Cars dataset.

Your final model should be able to classify images into one of 102 categories (101 object classes + background) with a validation accuracy of at least 85%.

The pipeline should:

Load a pretrained CNN from Keras Applications with include_top=False as a feature extractor.
Prepare and preprocess the dataset appropriately:
Apply common data augmentation techniques (e.g., rotation, zoom, flips, etc.).
Use the model-compatible preprocessing function (e.g., keras.applications..preprocess_input).
Structure your training in two phases:

Train a custom classification head while keeping the base model frozen.
Then, unfreeze and fine-tune some top layers of the base model for better performance.
Save the trained model to a file named: caltech101_model.h5.

Output:

A trained model saved as caltech101_model.h5
The model should achieve ≥85% validation accuracy
Tips:

You can use keras.utils.image_dataset_from_directory or ImageDataGenerator to load the images.
Feel free to try different pretrained models and compare results.
You can explore tuning the number of unfrozen layers, learning rates, optimizers, batch sizes, etc.
For efficient training, use callbacks like EarlyStopping, ReduceLROnPlateau, or ModelCheckpoint.