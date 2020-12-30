import os

model_root = "work_dirs"
model_dirs = [d for d in os.listdir(model_root)]
model_mark = "latest.pth"

image_dir = ""

for model_dir in model_dirs:
    cmds = []
    print("--------------------------Visualizing model 1------------------------------")
    model_dir_path = os.path.join(model_root, model_dir)
    for file in os.listdir(model_dir_path):
        if ".py" in file:
            config = file
        elif "latest" in file:
            chkp = file

    for img in os.listdir(image_dir):
        img_path = os.path.join(image_dir, img)
        cmds.append("python demo/image_demo.py {} {} {}".format(img_path, config, chkp))

    for cmd in cmds:
        print(cmd)
        os.system(cmd)
