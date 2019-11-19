import captcha_services.captcha_create_image as create_image
import random

if __name__ == '__main__':
    # create
    create_image.create_image(create_image.create_random_int_data(data_count=20, data_length=1),
                              image_file_path='../captcha_single_image(32x32)',
                              image_width=60, image_height=60)
