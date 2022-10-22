import os
import time
import platform


def detect_client(image_path):
    example_client(image_path)


def write_log(log_path: str, line: str):
    log = open(log_path, "a")
    log.write(line)
    log.close()


def repf_pano_client(image_path):
    log_path = f'{image_path}.log'  # image_path 为绝对路径

    time_stamp = int(time.time())
    work_dir = f'/home/lmf/tmp/repf_pano_client/{time_stamp}'

    os.system(f'mkdir -p {work_dir}')
    os.system(f'cp {image_path} {work_dir}/input')
    os.system(f'cp /home/lmf/Deploy/220925_RepFPanoStreamlit/metadata.json {work_dir}/input')
    os.system(f'CUDA_VISIBLE_DEVICES=0 WANDB_MODE=dryrun python main.py configs/pano3d_igibson.yaml --model.scene_gcn.relation_adjust True --mode test --demo_path /homo/ada/da/da -- save_path /home/da/da')


    # call mvpf_detect

    # call

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
