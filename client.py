import os
import time


def detect_client(image_path):
    example_client(image_path)


def example_client(image_path):
    image_path_list = image_path.split('\\')
    image_name = image_path_list[len(image_path_list) - 1]
    log_path = f'./{image_name}.log'
    example = open("./example.log", "r")
    for line in example:
        time.sleep(0.01)
        log = open(log_path, "a")
        log.write(line)
        log.close()
    example.close()


if __name__ == '__main__':
    example_client('./test.png')
