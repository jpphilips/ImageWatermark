from gui import Gui
from watermarkdata import WatermarkData
from watermarker import LogoWatermarker
import os
import re


def main():
    data = WatermarkData()
    window = Gui.main_window()
    while True:
        event, values = window.read()
        # print(values)
        if event in (Gui.close_window(), 'Exit'):
            break
        # elif event == '-TEXT-':
        #     event, values = Gui.get_text_watermark_popup()
        #     print(event)
        elif event == '-W_IMAGE-':
            path = Gui.get_file()
            if path is not None:
                if os.path.exists(path):
                    data.watermark_logo = path
            # print(type(data.watermark_logo))
        elif event == '-IMAGE-':
            path = Gui.get_file()
            if path is not None:
                if os.path.exists(path):
                    data.watermark_image = path
            # print(type(data.watermark_image))
            # print(event)
        elif event == '-IMAGE_FOLDER-':
            path = Gui.get_working_folder_path()
            if path is not None:
                if os.path.exists(path):
                    data.watermark_folder = path
        elif event == '-WATERMARK-':
            if data.watermark_logo is not None and data.watermark_image is not None:
                watermark = LogoWatermarker(
                    data.watermark_logo, data.watermark_image, values['-OPACITY-'])
                print(data.watermark_image)
            elif data.watermark_logo is not None and data.watermark_folder is not None:
                imageRegex = re.compile(r'.*\.(png|jpg|jpeg)$', re.I)
                file_list = os.listdir(data.watermark_folder)
                image_list = [imageRegex.search(file).group(
                ) for file in file_list if imageRegex.search(file) is not None]

                for image in image_list:
                    os.chdir(data.watermark_folder)
                    path = os.path.abspath(image)
                    data.watermark_image = path
                    watermark = LogoWatermarker(
                        data.watermark_logo, data.watermark_image, values['-OPACITY-'])
            data.watermark_image = None
            Gui.watermarkdone()

    window.close()


if __name__ == '__main__':
    main()
