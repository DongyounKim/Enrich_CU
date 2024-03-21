import torch
import torch.nn as nn
from torch.nn import functional as F
from torch.utils.data import DataLoader, Dataset

#1. Model load
from model import Testmodel

# # CLIP
# clip_model, preprocess = load("ViT-B/32", jit=False)
# clip_model = clip_model.cuda()
model = Testmodel()

# # Transformer
# myTransformer = triple_Transformer().cuda()

#2. Dataset load
## train_chart_data = train
## train_plot_data = train

## Fine_tuning for Question/Answering

### How do we define the dataset format
#### load dataset on the goolge colab:: To train the model

#3.Loss/optimizer
