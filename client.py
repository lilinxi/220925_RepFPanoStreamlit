import os
import time
import platform

def detect_client(image_path):
    example_client(image_path)


def example_client(image_path):
    image_path_list = image_path.split('\\')
    image_name = image_path_list[len(image_path_list) - 1]
    log_path = f'./{image_name}.log'

    sys = platform.system()
    if sys == 'Darwin':
        example = open("./example.log", "r")
    elif sys == 'Linux':
        example = open("./example.log.lab724", "r")
    else:
        print(f"Example Client do not support {sys} system")
        exit(255)

    for line in example:
        time.sleep(0.01)
        log = open(log_path, "a")
        log.write(line)
        log.close()
    example.close()


if __name__ == '__main__':
    example_client('./test.png')
