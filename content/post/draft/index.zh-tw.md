+++
date = '2024-12-10T21:20:55+08:00'
draft = true
title = 'Draft'
+++

- 將 yuc420 的畫質改善成 yuv444
希望可以提供更好的觀看品質

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
import numpy as np
import cv2
import os

# 提取多部影片幀的函數
def extract_frames_from_videos(video_dir, output_dir, img_size=(256, 256)):
    """
    從多部影片中提取幀並保存為 .yuv420 格式。
    :param video_dir: 包含影片的目錄。
    :param output_dir: 保存幀的目錄。
    :param img_size: 提取幀的尺寸 (H, W)。
    """
    os.makedirs(output_dir, exist_ok=True)
    video_files = [f for f in os.listdir(video_dir) if f.endswith(('.mp4', '.avi', '.mov'))]
    frame_count = 0

    for video_file in video_files:
        video_path = os.path.join(video_dir, video_file)
        cap = cv2.VideoCapture(video_path)
        video_name = os.path.splitext(video_file)[0]
        video_output_dir = os.path.join(output_dir, video_name)
        os.makedirs(video_output_dir, exist_ok=True)

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            # Resize and convert frame
            frame_resized = cv2.resize(frame, img_size)
            yuv_frame = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2YUV_I420)
            y_size = img_size[0] * img_size[1]
            uv_size = y_size // 4
            y = yuv_frame[:y_size]
            u = yuv_frame[y_size:y_size + uv_size]
            v = yuv_frame[y_size + uv_size:]

            # Save frame as .yuv420
            frame_path = os.path.join(video_output_dir, f"frame_{frame_count:05d}.yuv420")
            with open(frame_path, 'wb') as f:
                f.write(y.tobytes())
                f.write(u.tobytes())
                f.write(v.tobytes())
            frame_count += 1

        cap.release()
        print(f"Extracted frames from {video_file} to {video_output_dir}")

    print(f"Total frames extracted: {frame_count}")

# 數據集類別
class VideoYUV420Dataset(Dataset):
    def __init__(self, yuv420_dir, img_size=(256, 256)):
        """
        數據集初始化。
        :param yuv420_dir: 包含 .yuv420 文件的目錄。
        :param img_size: 圖像尺寸 (H, W)。
        """
        self.yuv420_dir = yuv420_dir
        self.img_size = img_size
        self.filenames = []
        for root, _, files in os.walk(yuv420_dir):
            for file in files:
                if file.endswith('.yuv420'):
                    self.filenames.append(os.path.join(root, file))

    def __len__(self):
        return len(self.filenames)

    def __getitem__(self, idx):
        yuv420_path = self.filenames[idx]
        y_channel, uv_channel = self.load_yuv420(yuv420_path, self.img_size)
        # Generate a pseudo label (e.g., repeat YUV420 as placeholder for YUV444)
        yuv444_label = torch.cat((y_channel, uv_channel), dim=0)  # For demo purposes
        return (y_channel, uv_channel), yuv444_label

    @staticmethod
    def load_yuv420(yuv420_path, img_size):
        with open(yuv420_path, 'rb') as f:
            y_size = img_size[0] * img_size[1]
            uv_size = y_size // 4
            y = np.frombuffer(f.read(y_size), dtype=np.uint8).reshape(img_size)
            u = np.frombuffer(f.read(uv_size), dtype=np.uint8).reshape((img_size[0] // 2, img_size[1] // 2))
            v = np.frombuffer(f.read(uv_size), dtype=np.uint8).reshape((img_size[0] // 2, img_size[1] // 2))
        y_tensor = torch.tensor(y, dtype=torch.float32).unsqueeze(0) / 255.0
        uv_tensor = torch.tensor(np.stack([u, v], axis=0), dtype=torch.float32) / 255.0
        return y_tensor, uv_tensor

# 模型定義
class YUV420ToYUV444Model(nn.Module):
    def __init__(self):
        super(YUV420ToYUV444Model, self).__init__()
        # UV 通道的上採樣層
        self.upsample_uv = nn.Sequential(
            nn.Conv2d(2, 64, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.Conv2d(64, 64, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.Conv2d(64, 2, kernel_size=3, stride=1, padding=1),
        )
    
    def forward(self, y_channel, uv_channel):
        """
        y_channel: shape (B, 1, H, W)
        uv_channel: shape (B, 2, H//2, W//2)
        """
        # 上採樣 UV 通道
        uv_upsampled = torch.nn.functional.interpolate(
            uv_channel, scale_factor=2, mode='bilinear', align_corners=False
        )
        uv_refined = self.upsample_uv(uv_upsampled)
        
        # 合併 Y 和 UV 通道
        yuv_444 = torch.cat((y_channel, uv_refined), dim=1)
        return yuv_444

# 訓練函數
def train_model(model, dataloader, criterion, optimizer, num_epochs=10, device='cuda'):
    model.to(device)
    for epoch in range(num_epochs):
        model.train()
        running_loss = 0.0
        for (y_channel, uv_channel), yuv444_label in dataloader:
            y_channel, uv_channel, yuv444_label = (
                y_channel.to(device),
                uv_channel.to(device),
                yuv444_label.to(device),
            )
            # 前向傳播
            outputs = model(y_channel, uv_channel)
            loss = criterion(outputs, yuv444_label)
            # 反向傳播與優化
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            running_loss += loss.item()

        avg_loss = running_loss / len(dataloader)
        print(f"Epoch [{epoch + 1}/{num_epochs}], Loss: {avg_loss:.4f}")

# 主程式
if __name__ == "__main__":
    # 設置路徑
    video_dir = "videos"  # 包含影片的目錄
    yuv420_dir = "./frames"  # 保存提取幀的目錄

    # 提取影片幀
    extract_frames_from_videos(video_dir, yuv420_dir)

    # 加載數據集
    dataset = VideoYUV420Dataset(yuv420_dir)
    dataloader = DataLoader(dataset, batch_size=8, shuffle=True)

    # 定義模型、損失函數與優化器
    model = YUV420ToYUV444Model()
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=1e-4)

    # 訓練模型
    train_model(model, dataloader, criterion, optimizer, num_epochs=20)

```