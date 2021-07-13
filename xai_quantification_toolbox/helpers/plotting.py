from typing import List, Union, Dict
import numpy as np
import torch
import matplotlib.pyplot as plt


def plot_pixel_flipping_experiment(y_batch: torch.Tensor,
                                   scores: List[float],
                                   single_class: Union[int, None] = None):
    """
    Plot the pixel-flippng experiment as done in paper:

    References:
        1) Bach, Sebastian, et al. "On pixel-wise explanations for non-linear classifier
        decisions by layer-wise relevance propagation." PloS one 10.7 (2015): e0130140.

    # TODO. Finish code if scores is a list.
    """
    fig = plt.figure(figsize=(8, 6))
    if single_class is None:
        for c in np.unique(y_batch):
            indices = np.where(y_batch == c)
            plt.plot(np.linspace(0, 1, len(scores[0])), np.mean(np.array(scores)[indices], axis=0),
                     label=f"target: {str(c)} ({indices[0].size} samples)")
    plt.xlabel("Fraction of pixels flipped")
    plt.ylabel("Mean Prediction")
    plt.gca().set_yticklabels(['{:.0f}%'.format(x * 100) for x in plt.gca().get_yticks()])
    plt.gca().set_xticklabels(['{:.0f}%'.format(x * 100) for x in plt.gca().get_xticks()])
    plt.legend()
    plt.show()


def plot_selectivity_experiment(scores: Union[List[float], Dict[str, List[float]]]):
    """
    Plot the selectivity experiment as done in paper:

    References:
        1) Montavon, Grégoire, Wojciech Samek, and Klaus-Robert Müller.
        "Methods for interpreting and understanding deep neural networks."
        Digital Signal Processing 73 (2018): 1-15.

    # TODO. Finish code if scores is a list.
    """
    fig = plt.figure(figsize=(8, 6))
    if isinstance(scores, dict):
        for method, values in scores.items():
            plt.plot(np.arange(0, len(values[0])),
                     np.mean(np.array(list(values.values())), axis=0),
                     label=f"{str(method.capitalize())} ({len(list(values))} samples)")
    plt.xlabel(f"# Patches removed")
    plt.ylabel(f"Average function value $f(x)$")
    plt.gca().set_yticklabels(['{:.0f}%'.format(x * 100) for x in plt.gca().get_yticks()])
    plt.legend()
    plt.show()


def plot_region_perturbation_experiment(scores: Union[List[float], Dict[str, List[float]]]):
    """
    Plot the region perturbation experiment as done in paper:

     References:
        1) Samek, Wojciech, et al. "Evaluating the visualization of what a deep
         neural network has learned." IEEE transactions on neural networks and
          learning systems 28.11 (2016): 2660-2673.
    """
    fig = plt.figure(figsize=(8, 6))
    if isinstance(scores, dict):
        for method, values in scores.items():
            plt.plot(np.arange(0, len(values[0])),
                     np.mean(np.array(list(values.values())), axis=0),
                     label=f"{str(method.capitalize())}")
    else:
        plt.plot(np.arange(0, len(scores)), np.mean(scores, axis=0))
    plt.xlabel("Perturbation steps")
    plt.ylabel("AOPC relative to random")
    plt.gca().set_yticklabels(['{:.0f}%'.format(x * 100) for x in plt.gca().get_yticks()])
    plt.legend()
    plt.show()


def plot_sensitivity_n_experiment(scores: Union[List[float], Dict[str, List[float]]]):
    """
    Plot the sensitivity n experiment as done in paper:

    References:
        1) Ancona, Marco, et al. "Towards better understanding of gradient-based attribution
        methods for deep neural networks." arXiv preprint arXiv:1711.06104 (2017).

    # TODO. Finish code if scores is a list.
    """
    fig = plt.figure(figsize=(8, 6))
    if isinstance(scores, dict):
        for method, values in scores.items():
            plt.plot(np.linspace(0, 1, len(values[0])),
                     np.mean(np.array(list(values.values())), axis=0),
                     label=f"{str(method.capitalize())}")
    plt.xlabel(f"# of pixels removed")
    plt.ylabel(f"Target activation (pre-softmax)")
    plt.gca().set_yticklabels(['{:.0f}%'.format(x * 100) for x in plt.gca().get_yticks()])
    plt.legend()
    plt.show()
