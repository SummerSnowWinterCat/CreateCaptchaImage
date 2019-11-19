import captcha_services.captcha_create_image as create_image

if __name__ == '__main__':
    # create
    create_image.create_image(create_image.create_random_int_data(10), image_file_path='../captcha_image/')