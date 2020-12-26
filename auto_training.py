import os

configs = [
    # "CUDA_VISIBLE_DEVICES=3 ./tools/dist_train.sh configs/fcn/fcn_r50-d8_512x1024_40k_cityscapes.py 1",
    # "CUDA_VISIBLE_DEVICES=3 ./tools/dist_train.sh configs/hrnet/fcn_hr18_512x1024_40k_cityscapes.py 1",
    # "CUDA_VISIBLE_DEVICES=3 ./tools/dist_train.sh configs/mobilenet_v2/deeplabv3_m-v2-d8_512x1024_80k_cityscapes.py 1",
    # "CUDA_VISIBLE_DEVICES=3 ./tools/dist_train.sh configs/ocrnet/ocrnet_hr18_512x1024_40k_cityscapes.py 1",
    # "CUDA_VISIBLE_DEVICES=3 ./tools/dist_train.sh configs/deeplabv3/deeplabv3_r50-d8_512x1024_40k_cityscapes.py 1"
    # "CUDA_VISIBLE_DEVICES=3 ./tools/dist_train.sh configs/resnest/deeplabv3_s101-d8_512x1024_80k_cityscapes.py 1",
    # "CUDA_VISIBLE_DEVICES=3 ./tools/dist_train.sh configs/hrnet/fcn_hr18_512x1024_40k_cityscapes.py 1",

    "PORT=13213 CUDA_VISIBLE_DEVICES=0 ./tools/dist_train.sh configs/fcn/fcn_r50-d8_480x480_40k_pascal_context.py 1",
    "PORT=13213 CUDA_VISIBLE_DEVICES=0 ./tools/dist_train.sh configs/deeplabv3/deeplabv3_r50-d8_480x480_40k_pascal_context.py 1",
    "PORT=13213 CUDA_VISIBLE_DEVICES=0 ./tools/dist_train.sh configs/ocrnet/ocrnet_hr18_512x512_20k_voc12aug.py 1",
    "PORT=13213 CUDA_VISIBLE_DEVICES=0 ./tools/dist_train.sh configs/ann/ann_r50-d8_512x512_20k_voc12aug.py 1",
    "PORT=13213 CUDA_VISIBLE_DEVICES=0 ./tools/dist_train.sh configs/hrnet/fcn_hr18_512x512_20k_voc12aug.py 1",
    "PORT=13213 CUDA_VISIBLE_DEVICES=0 ./tools/dist_train.sh configs/upernet/upernet_r50_512x512_20k_voc12aug.py 1",
    "PORT=13213 CUDA_VISIBLE_DEVICES=0 ./tools/dist_train.sh configs/fcn/fcn_r50-d8_512x512_20k_voc12aug.py 1",

]

for idx, cmd in enumerate(configs):
    print("--------------------------Training model {}--------------------------".format(idx))
    print(cmd)
    os.system(cmd)