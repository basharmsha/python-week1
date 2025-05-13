import torch

def compute_evaluations(logits, targets, num_classes):
    if not torch.is_floating_point(logits):
        raise TypeError("logits must be a floating point tensor")
    if not targets.is_integer():
        raise TypeError("targets must be an integer tensor")

    if not logits.dim() == 2:
        raise ValueError("logits must be a 2D tensor")
    if not targets.dim() == 1:
        raise ValueError("targets must be a 1D tensor")
    if logits.size(0) != targets.size(0):
        raise ValueError("The first dimension of logits and targets must match")

    if targets.min().item() < 0 or targets.max().item() >= num_classes:
        raise ValueError("targets must contain values smaller than num_classes")

    _, predictions = torch.max(logits, dim=1)

    confusion_matrix = torch.zeros(num_classes, num_classes)
    for i in range(targets.size(0)):
        confusion_matrix[targets[i], predictions[i]] += 1

    accuracy = (predictions == targets).sum().item() / targets.size(0)

    balanced_accuracy = 0
    for i in range(num_classes):
        balanced_accuracy += confusion_matrix[i, i] / confusion_matrix[i].sum()
    balanced_accuracy /= num_classes

    return confusion_matrix, accuracy, balanced_accuracy