import os

configs = [
    # "CUDA_VISIBLE_DEVICES=3 ./tools/dist_train.sh configs/ccnet/ccnet_r50-d8_512x512_20k_voc12aug.py 1",
    # "CUDA_VISIBLE_DEVICES=3 ./tools/dist_train.sh configs/apcnet/apcnet_r50-d8_512x512_80k_ade20k.py 1",
    # "CUDA_VISIBLE_DEVICES=3 ./tools/dist_train.sh configs/ann/ann_r50-d8_512x512_20k_voc12aug.py 1",
    # "CUDA_VISIBLE_DEVICES=3 ./tools/dist_train.sh configs/danet/danet_r50-d8_512x512_20k_voc12aug.py 1",
    # "CUDA_VISIBLE_DEVICES=3 ./tools/dist_train.sh configs/ccnet/ccnet_r50-d8_512x512_20k_voc12aug.py 1",
    # "CUDA_VISIBLE_DEVICES=3 ./tools/dist_train.sh configs/deeplabv3/deeplabv3_r50-d8_512x512_20k_voc12aug.py 1",
    # "CUDA_VISIBLE_DEVICES=3 ./tools/dist_train.sh configs/danet/danet_r50-d8_512x1024_40k_cityscapes.py 1",
    # "CUDA_VISIBLE_DEVICES=3 ./tools/dist_train.sh configs/dnlnet/dnl_r50-d8_512x1024_40k_cityscapes.py 1",
    # "CUDA_VISIBLE_DEVICES=3 ./tools/dist_train.sh configs/emanet/emanet_r50-d8_512x1024_80k_cityscapes.py 1",

    # "PORT=13213 CUDA_VISIBLE_DEVICES=2 ./tools/dist_train.sh configs/encnet/encnet_r50-d8_512x512_20k_voc12aug.py 1",
    # "PORT=13213 CUDA_VISIBLE_DEVICES=2 ./tools/dist_train.sh configs/encnet/encnet_r50-d8_512x1024_40k_cityscapes.py 1",
    # "PORT=13213 CUDA_VISIBLE_DEVICES=2 ./tools/dist_train.sh configs/fastscnn/fast_scnn_4x8_80k_lr0.12_cityscapes.py 1",
    # "PORT=13213 CUDA_VISIBLE_DEVICES=2 ./tools/dist_train.sh configs/gcnet/gcnet_r50-d8_512x512_20k_voc12aug.py 1",
    # "PORT=13213 CUDA_VISIBLE_DEVICES=2 ./tools/dist_train.sh configs/gcnet/gcnet_r50-d8_512x1024_40k_cityscapes.py 1",

    "PORT=12451 CUDA_VISIBLE_DEVICES=0 ./tools/dist_train.sh configs/hrnet/fcn_hr18_480x480_40k_pascal_context.py 1",
    "PORT=12451 CUDA_VISIBLE_DEVICES=0 ./tools/dist_train.sh configs/hrnet/fcn_hr18_480x480_40k_pascal_context.py 1",
    "PORT=12451 CUDA_VISIBLE_DEVICES=0 ./tools/dist_train.sh configs/nonlocal_net/nonlocal_r50-d8_512x512_20k_voc12aug.py 1",
    "PORT=12451 CUDA_VISIBLE_DEVICES=0 ./tools/dist_train.sh configs/nonlocal_net/nonlocal_r50-d8_512x1024_40k_cityscapes.py 1",
    "PORT=12451 CUDA_VISIBLE_DEVICES=0 ./tools/dist_train.sh configs/point_rend/pointrend_r50_512x1024_80k_cityscapes.py 1",

]

for idx, cmd in enumerate(configs):
    print("--------------------------Training model {}--------------------------".format(idx))
    print(cmd)
    os.system(cmd)