import torch.optim as optim
from collections import OrderedDict
from torch import nn, Tensor
from torchvision import models, transforms
from typing import Any
from mlem.api import save

def get_state_dict(model, optimizer, params):

    state = {
        'model_name': model.__class__.__name__,
        'params': params,
        'nn_state_dict': model.state_dict()
    }
    if optimizer:
        state['optimizer_state_dict'] = optimizer.state_dict()

    return state

def main():

    model = models.resnet18(pretrained=True)
    params = {"lr": 0.001, "momentum": 0.9, "input_shape": (1, 3, 256, 256), "num_class": 1000}
    optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

    state = get_state_dict(model, optimizer, params)

    save(
        state,
        path="resnet18",
        description="Resnet model with optimizer"
    )

if __name__ == "__main__":
    main()