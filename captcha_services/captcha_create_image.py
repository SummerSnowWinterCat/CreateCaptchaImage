from captcha.image import ImageCaptcha
import random
import time

img = ImageCaptcha(width=120, height=60)


def create_random_int_data(data_count):
    '''
    This is a function to create random int data
    :param data_count:create 0~data_count images
    :return:random data
    '''
    print('Will Create {} Random Data'.format(data_count))
    random_data = []
    for create_number in range(data_count):
        max_length = len(random_data)
        random_int_01 = random.randint(0, 9)
        random_int_02 = random.randint(0, 9)
        random_int_03 = random.randint(0, 9)
        random_int_04 = random.randint(0, 9)
        random_str = str(random_int_01) + str(random_int_02) + str(random_int_03) + str(random_int_04)
        if len(random_data) == 0:
            random_data.append(random_str)
        else:
            # cut the set /2
            # 二分
            if int(random_data[int(max_length / 2)]) > int(random_str):
                for i in range(int(max_length / 2), max_length):
                    if int(random_data[i]) is int(random_str):
                        break
                random_data.append(random_str)
            else:
                for i in range(0, int(max_length / 2)):
                    if int(random_data[i]) is int(random_str):
                        break
                random_data.append(random_str)

    print('End Data [{}]'.format(len(random_data)))
    return random_data


def create_image(random_data, image_file_path):
    '''
    This function is to create a image
    :param random_data:4 int str data
    :param image_file_path: save image path
    :return:data length to create
    '''
    print('Image Create is start!')
    for data in range(len(random_data)):
        img.create_captcha_image(random_data[data], color=random_color(), background='white').save(
            image_file_path + '{}.png'.format(random_data[data]))
        time.sleep(0.2)
        print('No.{}->{}.png'.format(data+1, random_data[data]))
    return print('+Complete to create {} images+'.format(len(random_data)))


def random_color():
    '''
    This function is random to create a rgb number
    :return:random rgb (255,255,255)
    '''
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


if __name__ == '__main__':
    create_image(create_random_int_data(10))
