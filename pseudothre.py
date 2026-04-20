import cv2
from pathlib import Path

input_dir = Path("")
output_dir = Path("")

output_dir.mkdir(parents=True, exist_ok=True)

for img_path in input_dir.glob('*.png'):

    img = cv2.imread(str(img_path), cv2.IMREAD_GRAYSCALE)

    if img is None:
        print(f"警告: 无法读取图像 {img_path.name}")
        continue

    _, binary_img = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)


    save_path = output_dir / img_path.name
    cv2.imwrite(str(save_path), binary_img)

print(f"处理完成！图片已保存至: {output_dir.absolute()}")