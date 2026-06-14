import torch
import torch.nn as nn

class SeismicLSTM(nn.Module):
    def __init__(self):
        super().__init__()

        self.lstm = nn.LSTM(
            input_size=4,
            hidden_size=32,
            batch_first=True
        )

        self.fc = nn.Linear(32, 2)

    def forward(self, x):
        out, _ = self.lstm(x)
        out = self.fc(out[:, -1, :])
        return out