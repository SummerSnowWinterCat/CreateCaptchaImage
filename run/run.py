import captcha_services.captcha_create_image as create_image

if __name__ == '__main__':
    # create
    create_image.create_image(create_image.create_random_int_data(2000), image_file_path='../captcha_image/',
                              image_width=0, image_height=0)
