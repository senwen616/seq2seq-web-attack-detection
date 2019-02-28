from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os


import numpy as np


def get_requests_from_file(path):
    """
    Reads raw HTTP requests from given file.
    """
    list1 = []
    with open(path, 'r') as f:
        file_data = f.read()
        list1.append(file_data)
    return list1


def batch_generator(inputs, lengths, num_epochs, batch_size, vocab):
    """
    Generates a padded batch. 
    """
    i = 0
    input_size = len(inputs)
    for _ in range(num_epochs):
        while i + batch_size <= input_size:
            l = lengths[i:i + batch_size]
            padded = batch_padding(inputs[i:i + batch_size], l, vocab)
            yield padded, l
            i += batch_size
        i = 0


def one_by_one_generator(inputs, lengths, vocab):
    """
    Yields a sample. 
    """
    for i in range(len(inputs)):
        yield [inputs[i]], lengths[i]


def batch_padding(inputs, lengths, vocab):
    """
    Pads sequences to max sequence length in a batch.
    """
    max_len = np.max(lengths)
    padded = []
    for sample in inputs:
        padded.append(
            sample + ([vocab.vocab['<PAD>']] * (max_len - len(sample))))
    return padded


def print_progress(step, epoch, loss, step_loss, time):
    """
    Prints learning stage progress.
    """
    msg = "Step {} (epoch {}), average_train_loss = {:.5f}, step_loss = {:.5f}, time_per_step = {:.3f}"
    msg = msg.format(step, epoch, loss, step_loss, time)
    print(msg)


def create_checkpoints_dir(checkpoints_dir):
    """
    Creates the checkpoints directory if it does not exist.
    """
    if not os.path.exists(checkpoints_dir):
        os.makedirs(checkpoints_dir)
