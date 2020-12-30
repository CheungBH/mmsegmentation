import os

model_mark = "latest.pth"

model_dirs = [
    "work_dirs/deeplabv3_m-v2-d8_512x1024_80k_cityscapes",
    "work_dirs/apcnet_r50-d8_512x1024_40k_cityscapes"
]
image_dir = "img/city_scape"

for idx, model_dir in enumerate(model_dirs):
    cmds = []
    print("--------------------------Visualizing model {}------------------------------".format(idx))
    # model_dir_path = os.path.join(model_root, model_dir)
    out_dir = "img/result"
    os.makedirs(out_dir, exist_ok=True)
    for file in os.listdir(model_dir):
        file_path = os.path.join(model_dir, file)
        if ".py" in file:
            config = file_path
        elif model_mark in file:
            chkp = file_path
        else:
            pass

    img_result_dir = os.path.join(out_dir, model_dir.split("/")[-1] + "-" + image_dir.split("/")[-1])
    os.makedirs(img_result_dir, exist_ok=True)
    for img_name in os.listdir(image_dir):
        img_path = os.path.join(image_dir, img_name)
        out_file = os.path.join(img_result_dir, img_name)
        if not os.path.exists(out_file):
            cmds.append("python demo/image_demo.py {} {} {} --out {}".format(img_path, config, chkp, out_file))

    for cmd in cmds:
        print(cmd)
        os.system(cmd)
