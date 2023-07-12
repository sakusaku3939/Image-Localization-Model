import torch
import torchvision
import torchvision.transforms as transforms
from config import get_config
import sys

sys.path.append('../')


def load_image():
    batch_size = get_config("general", "batch_size")
    num_workers = get_config("general", "num_workers")

    # データの前処理
    transform = transforms.Compose([
        transforms.Resize((128, 128)),
        transforms.ToTensor()
    ])

    # データセットの読み込み
    train_set = torchvision.datasets.ImageFolder("./data/train", transform)
    valid_set = torchvision.datasets.ImageFolder("./data/valid", transform)

    train_loader = torch.utils.data.DataLoader(
        train_set,
        batch_size=batch_size,
        shuffle=True,
        num_workers=num_workers
    )
    valid_loader = torch.utils.data.DataLoader(
        valid_set,
        batch_size=batch_size,
        shuffle=False,
        num_workers=num_workers
    )

    return train_loader, valid_loader


def load_test_image():
    batch_size = get_config("general", "batch_size")
    num_workers = get_config("general", "num_workers")

    # データの前処理
    transform = transforms.Compose([
        transforms.Resize((128, 128)),
        transforms.ToTensor()
    ])

    # データセットの読み込み
    dataset = torchvision.datasets.ImageFolder("./data/test", transform)

    test_loader = torch.utils.data.DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=False,
        num_workers=num_workers
    )

    return test_loader
