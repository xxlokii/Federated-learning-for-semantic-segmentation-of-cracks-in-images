The goal of the project is to design a pipeline to segment crack pixels in damaged infrastructure within the context of federated learning using iid and non-iid data.

We use the following two datasets for our project. 

- Dataset of cracks on concrete https://data.mendeley.com/datasets/jwsn7tfbrp/1 provided by the Middle East University of Technology.

- Dataset of cracks on asphalt https://github.com/juhuyan/CrackDataset_DL_HY/tree/master/SematicSeg_Dataset provided by Southeast University and Chang'an University for DL-based crack detection.

## File structure

The project's documentation is organized as follows: 

```
.
├── SematicSeg_Dataset					--Asphalt Cracks
�?   ├── Labels
�?   └── Original Image
├── concreteCrackSegmentationDataset	--Concrete Cracks
�?   ├── BW
�?   └── rgb
├── tmp
�?   ├── test_image_paths.txt
�?   └── test_mask_paths.txt
├── .gitignore
├── Models.py
├── README.md
├── T1-v4.ipynb							--Pipeline for the Semantic Segmentation Part
├── clients.py
├── getData.py
├── requirements.txt					--Package Required for the Project
├── script.sh							--Script to Run the Experiment
├── server.py
├── utils.py
```

The `.py` file in the root directory fully implements the semantic segmentation and federation learning pipeline. 

## Setup and run

Execute the following code to install the required packages:

```
pip install -r requirements.txt
```

Execute the following code to experiment:

```
./script.sh
```

## Implementation details

#### Model and methods

We use UNet as a model for semantic segmentation and embed it in a federal learning framework.

In the model, we try to add batchnorm, dropout layer, etc. to the model to make it more stable. Different loss types were implemented for experimentation.

#### Data pre-processing

Due to the large size of the original photos in the data set, such as concrete (4032 x 3024) and asphalt (1280 x 960), we used bilinear interpolation to resample the images and obtained pictures with a size of 480 x 320. 

Since segmenting the crack pixels of an image is a binary classification task, we binarize the label of images of the two datasets.

#### Hyperparameter selection

First, we select hyperparameters such as its learning rate in the pipeline of semantic segmentation.

Second, we conducted experiments on the number of clients in federation learning, the proportion of clients involved in training, and the number of local epochs. These and other parameters are in the server's parse_args.

## Structure of the code file

#### server.py

server.py is the main file for the entire pipeline.

- Determine all experimental parameters
- Create all clients
- Training is performed, and in each communication, the parameters of the server and client interact

#### clients.py

All client matters, including the creation and training of clients

#### getData.py

All data work, including data import, data pre-processing and data distribution on the client side

#### Models.py

Includes the U-Net model that we use in semantic segmentation

#### Utils.py

Includes the evaluation metrics we implemented for WeightedFocalLoss, DiceLoss and results such as precision and recall

## Author
+ Wei Liu





