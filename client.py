import os
import time
import platform

import grpc
import proto_gen.detect_pb2
import proto_gen.detect_pb2_grpc


def detect_client(image_path):
    repf_pano_client(image_path)
    # example_client(image_path)


def repf_pano_client(image_path):
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = proto_gen.detect_pb2_grpc.DeformYolov5Stub(channel)

        response = stub.Detect(
            proto_gen.detect_pb2.YoloModelRequest(
                image_path=image_path,
            ),
        )

        print("Greeter client received: ")
        print(response)

    deep_work_dir = f'{image_path}.deep'  # image save work dir
    if not os.path.exists(deep_work_dir):
        os.makedirs(deep_work_dir)
        os.makedirs(f'{deep_work_dir}/input')

    os.system(f'cp {image_path} {deep_work_dir}/input')
    os.system(f'cp /home/lmf/Deploy/220925_RepFPanoStreamlit/metadata.json {deep_work_dir}/input')
    # os.system(f'CUDA_VISIBLE_DEVICES=0 WANDB_MODE=dryrun python main.py configs/pano3d_igibson.yaml --model.scene_gcn.relation_adjust True --mode test --demo_path /homo/ada/da/da -- save_path /home/da/da')

    print(f'CUDA_VISIBLE_DEVICES=0 WANDB_MODE=dryrun python main.py configs/pano3d_igibson.yaml --model.scene_gcn.relation_adjust True --mode test --demo_path {deep_work_dir}/input -- save_path {deep_work_dir}/output')


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
        time.sleep(0.5)
        log = open(log_path, "a")
        log.write(line)
        log.close()
    example.close()


if __name__ == '__main__':
    example_client('./test.png')
