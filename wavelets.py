import torch


def haar_wavelet_transform_2d(data):
    m, n = data.shape
    output = torch.zeros((m, n), dtype=data.dtype, device=data.device)

    # 1D Haar transform along rows
    for i in range(m):
        output[i, :] = haar_1d(data[i, :])

    # 1D Haar transform along columns
    for j in range(n):
        output[:, j] = haar_1d(output[:, j])

    return output


def inverse_haar_wavelet_transform_2d(data):
    m, n = data.shape
    output = torch.zeros((m, n), dtype=data.dtype, device=data.device)

    # Inverse 1D Haar transform along columns
    for j in range(n):
        output[:, j] = inverse_haar_1d(data[:, j])

    # Inverse 1D Haar transform along rows
    for i in range(m):
        output[i, :] = inverse_haar_1d(output[i, :])

    return output


def haar_1d(data):
    n = data.size(0)
    if n == 1:
        return data
    even = (data[::2] + data[1::2]) / torch.sqrt(torch.tensor(2.0, dtype=data.dtype, device=data.device))
    odd = (data[::2] - data[1::2]) / torch.sqrt(torch.tensor(2.0, dtype=data.dtype, device=data.device))
    return torch.cat((even, odd))


def inverse_haar_1d(data):
    n = data.size(0)
    if n == 1:
        return data
    even = data[:n // 2] * torch.sqrt(torch.tensor(2.0, dtype=data.dtype, device=data.device))
    odd = data[n // 2:] * torch.sqrt(torch.tensor(2.0, dtype=data.dtype, device=data.device))
    output = torch.zeros(n, dtype=data.dtype, device=data.device)
    output[::2] = (even + odd) / torch.tensor(2.0, dtype=data.dtype, device=data.device)
    output[1::2] = (even - odd) / torch.tensor(2.0, dtype=data.dtype, device=data.device)
    return output


# 示例用法
if __name__ == "__main__":
    # 创建一个示例的二维数据（400x512的张量）
    data = torch.rand(400, 512)

    # 执行二维Haar小波变换
    transformed_data = haar_wavelet_transform_2d(data)
    print("Transformed Data:")
    print(transformed_data)

    # 执行逆变换
    inverted_data = inverse_haar_wavelet_transform_2d(transformed_data)
    print("Inverted Data:")
    print(inverted_data)
