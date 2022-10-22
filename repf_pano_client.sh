#! /bin/bash

work_dir=$1
image_path=$2
log_path=$3
work_path=$4

cd $(dirname $0)

# build input
mkdir -p $work_dir/input
cp $image_path $work_dir/input
cp ./metadata.json $work_dir/input

# build output
mkdir -p $work_dir/output
conda activate Pano3D
cd work_path
CUDA_VISIBLE_DEVICES=0 WANDB_MODE=dryrun python main.py configs/pano3d_igibson.yaml --model.scene_gcn.relation_adjust True --mode test --demo_path $work_dir/input -- save_path $work_dir/output