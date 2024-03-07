import base64
from PIL import Image
from io import BytesIO

# 将base64字符串解码为图像数据
image_data = base64.b64decode('')

# 将图像数据加载到PIL图像对象中
image = Image.open(BytesIO(image_data))

# 保存图像到文件
image.save('output_image.png')

print("图像保存成功！")