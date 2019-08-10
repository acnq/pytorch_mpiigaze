import torch

from mpiigaze.dataset import create_dataset


def create_dataloader(config, is_train):
    if is_train:
        train_dataset, val_dataset = create_dataset(config, is_train)
        train_loader = torch.utils.data.DataLoader(
            train_dataset,
            batch_size=config.train.batch_size,
            shuffle=True,
            num_workers=config.train.dataloader.num_workers,
            pin_memory=config.train.dataloader.pin_memory,
            drop_last=config.train.dataloader.drop_last,
        )
        val_loader = torch.utils.data.DataLoader(
            val_dataset,
            batch_size=config.train.batch_size,
            shuffle=False,
            num_workers=config.train.dataloader.num_workers,
            pin_memory=config.train.dataloader.pin_memory,
            drop_last=False,
        )
        return train_loader, val_loader
    else:
        test_dataset = create_dataset(config, is_train)
        test_loader = torch.utils.data.DataLoader(
            test_dataset,
            batch_size=config.test.batch_size,
            num_workers=config.test.datalaoder.num_workers,
            shuffle=False,
            pin_memory=config.test.dataloader.pin_memory,
            drop_last=False,
        )
        return test_loader
