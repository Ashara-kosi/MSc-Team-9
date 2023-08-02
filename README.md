# Sign Language to Text convertion

Welcome to the README page of our project repository!

Project Overview:
-----------------
The goal of this project is to develop a web-based application that utilizes a deep-learning model to convert American Sign Language (ASL) gestures into corresponding text. Users can input a signed video into the application, which will then run through our model and return the translated text. This project aims to empower hard-of-hearing children in their educational journey by providing a tool for easy communication and understanding.

Features:
---------
1. Web-Based Application: The project includes a user-friendly web-based application where users can upload signed videos for translation.

2. Deep Learning Models: We have implemented two powerful deep learning models - Convolutional Neural Network (CNN) and Long Short-Term Memory (LSTM). These models achieve remarkable accuracies of 99% and 92%, respectively, in converting ASL gestures to text.

3. Dataset: The dataset used for training and testing the models is the WLASL dataset, which contains approximately 13,000 videos of signs. We selected specific words from the dataset to initially train the models.

4. FlaskAPI Backend: The application connects to the model's backend using FlaskAPI. The uploaded video undergoes pre-processing, where video frames are extracted, resized, and converted into NumPy arrays. These frames are then split into X_train and Y_train inputs for the deep learning models.

Usage:
------
1. Clone the Repository: Start by cloning this repository to your local machine.

2. Install Dependencies: Make sure you have the required dependencies installed. Check the 'requirements.txt' file for a list of dependencies.

3. Dataset: As the full dataset may be large, a version of the WLASL dataset containing specific words used for initial model training is available on Kaggle. Download and place it in the designated folder as mentioned in the instructions.

4. Run the Application: Launch the web-based application by running the app.py file.

Results:
--------
The LSTM model achieved a training accuracy of 92%, and the CNN model achieved a training accuracy of 99%, demonstrating the potential of deep learning models in converting ASL gestures to text.

Contributing:
-------------
We welcome contributions to this project! If you have any ideas, improvements, or bug fixes, feel free to open a pull request.


Acknowledgments:
----------------
We would like to thank the creators of the WLASL dataset and Kaggle for providing the data used in this project.

Contact:
--------
For any questions or inquiries, feel free to contact us at [asharakosi@gmail.com].

We hope this project serves as a valuable resource in bridging communication gaps and supporting hard-of-hearing children in their educational journey. Enjoy using the application!
