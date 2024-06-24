import torch
import torch.nn as nn


class Softmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_exp = torch.exp(x)
        sum_exp = x_exp.sum(0, keepdim=True)
        return x_exp / sum_exp


class SoftmaxStable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_max = torch.max(x, dim=0, keepdim=True)
        x_exp = torch.exp(x - x_max.values)
        sum_exp = x_exp.sum(0, keepdim=True)
        return x_exp/sum_exp


if __name__ == '__main__':
    data = torch.Tensor([1, 2, 3])
    softmax = Softmax()
    output = softmax(data)
    print(output)

    data = torch.Tensor([1, 2, 3])
    softmax = SoftmaxStable()
    output = softmax(data)
    print(output)
