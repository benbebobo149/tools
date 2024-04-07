import requests
import img2pdf
import os

def download_images(base_url, start, end, output_dir):
    for i in range(start, end+1):
        url = base_url + str(i) + '.jpg'
        response = requests.get(url)
        if response.status_code == 200:
            with open(os.path.join(output_dir, f'image_{i}.jpg'), 'wb') as f:
                f.write(response.content)
        else:
            print(f"Failed to download image {i}")

def convert_to_pdf(image_dir, output_pdf):
    with open(output_pdf, "wb") as f:
        images = [img for img in os.listdir(image_dir) if img.endswith(".jpg")]
        images.sort(key=lambda x: int(x.split('_')[1].split('.')[0]))
        f.write(img2pdf.convert([os.path.join(image_dir, img) for img in images]))

def delete_images(image_dir):
    for img in os.listdir(image_dir):
        img_path = os.path.join(image_dir, img)
        os.remove(img_path)

if __name__ == "__main__":
    base_url = "https://ncueeclass.ncu.edu.tw/sysdata/doc/9/9a96b3a68cc833ba/images/"  # 替换为你的图片链接的基础部分
    start_number = 1  # 图片链接中的起始数字
    end_number = 34 # 图片链接中的结束数字
    output_directory = "images"  # 下载图片的输出目录
    output_pdf_file = "output.pdf"  # 输出的PDF文件名

    # 下载图片
    download_images(base_url, start_number, end_number, output_directory)

    # 将下载的图片转换成PDF
    convert_to_pdf(output_directory, output_pdf_file)

    # 删除下载的图片
    delete_images(output_directory)
