import torch
import torch.nn as nn

# Simple dummy CNN model (same structure as app expects)
class DisasterCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Flatten(),
            nn.Linear(128 * 128 * 3, 64),
            nn.ReLU(),
            nn.Linear(64, 4)
        )

    def forward(self, x):
        return self.net(x)


# create model
model = DisasterCNN()

# save weights
torch.save(model.state_dict(), "cnn_model.pth")

print("✅ cnn_model.pth created successfully!")