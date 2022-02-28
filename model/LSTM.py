# -*- coding=utf-8 -*-

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim


class LSTM_reg(nn.Module):
    def __init__(self, input_size, hidden_size, inter_size, output_size, num_layers=1, bidirectional=False, batch_first=True, dropout=0):
        super().__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.bidirectional = bidirectional
        self.batch_first = batch_first
        self.dropout = dropout
        self.inter_size = inter_size
        self.output_size = output_size
        
        self.lstm_backbone = nn.LSTM(input_size=input_size, hidden_size=hidden_size, num_layers=num_layers, 
        bidirectional=bidirectional, batch_first=batch_first, dropout=dropout)
        self.linear = nn.Linear(hidden_size, inter_size)
        self.fc = nn.Sequential(nn.Linear(hidden_size, inter_size),
                                nn.BatchNorm1d(inter_size),
                                nn.ReLU(),
                                nn.Linear(inter_size, output_size))
    
    def forward(self, x):
        lstm_output, hidden = self.lstm_backbone(x)
        linear_out = self.linear(lstm_output)
        return linear_out, hidden

