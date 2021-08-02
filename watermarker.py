import cv2
import numpy as np
import os
from PIL import Image, ImageFont, ImageDraw
from watermarkdata import WatermarkData


class LogoWatermarker:

    def __init__(self, logo, image, alpha):
        # all in sequence w.r.t methods
        self.alpha = alpha
        self.logo = logo  # 'Images/Screenshot (10)a.png'
        self.image = image  # 'Images/TOCN4475.jpg'
        self.cv_logo = self.create_cv_logo(self.logo)
        self.get_logo_shape(self.cv_logo)
        self.cv_image = self.create_cv_image(self.image)
        self.h_logo, self.w_logo = self.get_logo_shape(self.cv_logo)
        self.h_img, self.w_img = self.get_image_shape(self.cv_image)
        self.roi, self.top_y, self.left_x, self.bottom_y, self.right_x = self.get_rois(
            self.h_logo, self.w_logo, self.h_img, self.w_img, self.cv_image)
        self.make_watermark_image(self.roi, self.top_y, self.left_x,
                                  self.bottom_y, self.right_x, self.cv_logo, self.cv_image)

    def create_cv_logo(self, logo):
        cv_logo = cv2.imread(logo)
        return cv_logo

    def get_logo_shape(self, cv_logo):
        h_logo, w_logo, p_logo = cv_logo.shape
        return (h_logo, w_logo)

    def create_cv_image(self, image):
        cv_image = cv2.imread(image)
        return cv_image

    def get_image_shape(self, cv_image):
        h_img, w_img, p_img = cv_image.shape
        return (h_img, w_img)

    def get_rois(self, h_logo, w_logo, h_img, w_img, cv_image):
        center_y = int(h_img/2)
        center_x = int(w_img/2)
        top_y = center_y - int(h_logo/2)
        left_x = center_x - int(h_logo/2)
        bottom_y = top_y + h_logo
        right_x = left_x + w_logo
        roi = cv_image[top_y:bottom_y, left_x:right_x]
        return [roi, top_y, left_x, bottom_y, right_x]

    def make_watermark_image(self, roi, top_y, left_x, bottom_y, right_x, cv_logo, cv_image):
        result = cv2.addWeighted(roi, 1, cv_logo, self.alpha, 0)
        cv_image[top_y:bottom_y, left_x:right_x] = result
        filename = os.path.basename(self.image)
        cwd = os.getcwd()
        path = os.path.abspath(f'{cwd}/Watermarked_Images')
        if not os.path.exists(path):
            os.makedirs(path)
        cv2.imwrite(
            f'{path}/watermarked_{filename}', cv_image)
        # print(cwd, path)


class TextWatermarker:
    # # text
    # image_for_txt = Image.open(image)
    # font_type = ImageFont.trueType('ariel.ttf', 18)
    # font_type = ImageFont.trueType('ariel.ttf', 18)
    # font_type = ImageFont.trueType('ariel.ttf', 18)

    # draw = ImageDraw(cv_image)
    # draw.text(xy=(x, y), text='', fill=(r, g, b), font=font_type)
    pass
