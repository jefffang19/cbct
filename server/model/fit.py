import torch


def fit(model, x):
    model.eval()

    x_tensor = torch.tensor(x).unsqueeze(0).unsqueeze(0).float()
    if torch.cuda.is_available():
        x_tensor = x_tensor.cuda()

    with torch.no_grad():
        pred = model(x_tensor)

        pred_img = pred.cpu().squeeze().numpy()

    return pred_img
