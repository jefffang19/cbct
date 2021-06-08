import segmentation_models_pytorch as smp
import torch


def get_model(PATH):
    model = smp.Unet(encoder_name='resnet152',
                     encoder_weights=None, in_channels=1, classes=1)

    DEVICE = 'cpu'
    if torch.cuda.is_available():
        print('using gpu')
        DEVICE = 'cuda'
        model.cuda()
    else:
        print('using cpu')

    model.load_state_dict(torch.load(PATH, map_location=DEVICE))

    return model
