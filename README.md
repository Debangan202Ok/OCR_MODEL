## Own OCR(Optical Character Recognization) Model
<p>In this project i'm going to create my own well trained ocr model that will capable to decrypt dr. hand's written prescriptions.</p>

### Resource that i use:
    1. TensorFlow
    2. Python
    3. Anaconda
    4. OpenAi
## The Important Question is How can i create my own model?
---
<b>Answer:</b>Creating your own OCR model invlove several steps, including gathering & preparing data, training a model, and evaluating its performance

### 1. Data Collection: 
    Gather a large dataset of images with text. The images should be representative of the data your model will be working with in production.
---
### 2. Data Labeling: 
    Label the data with the correct text. This can be a time-consuming process, but it's crucial for supervised learning.
---
### 4. Model Selection: 
    Choose a model architecture. Convolutional Neural Networks (CNNs) are commonly used for image-based tasks, and Long Short-Term Memory networks (LSTMs) are often used for sequence prediction like in OCR.
___
### 5. Training: 
    Train the model on your labeled data. This will likely involve splitting your data into a training set and a validation set, choosing an optimizer and loss function, and running the training process for a certain number of epochs.
___
### 6. Evaluation: 
    Evaluate the model's performance on a test set of images that it hasn't seen during training.