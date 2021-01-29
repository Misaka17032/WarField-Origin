
# -*- coding: utf-8 -*-

import json
import sys
from remi.gui import *
from cvs import *
import runtime

class Show(App):
    def __init__(self, *args, **kwargs):
        #DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR
        if not 'editing_mode' in kwargs.keys():
            super(Show, self).__init__(*args, static_file_path={'my_res':'./res/'})

    def idle(self):
        #idle function called every update cycle
        self.aidcam.update()
        pass
    
    def main(self):
        ui = Show.construct_ui(self)
        return ui
        
    @staticmethod
    def construct_ui(self):
        #DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR
        container0 = Container()
        container0.attr_editor_newclass = False
        container0.css_height = "100%"
        container0.css_left = "0px"
        container0.css_margin = "3px"
        container0.css_position = "absolute"
        container0.css_top = "0px"
        container0.css_width = "100%"
        container0.variable_name = "container0"
        container1 = Container()
        container1.attr_editor_newclass = False
        container1.css_height = "30px"
        container1.css_left = "0px"
        container1.css_margin = "2px"
        container1.css_position = "absolute"
        container1.css_top = "0px"
        container1.css_width = "100%"
        container1.variable_name = "container1"
        container2 = Container()
        container2.attr_editor_newclass = False
        container2.css_height = "20px"
        container2.css_left = "4px"
        container2.css_margin = "1px"
        container2.css_position = "absolute"
        container2.css_top = "4px"
        container2.css_width = "100px"
        container2.variable_name = "container2"
        fileuploader0 = FileUploader()
        fileuploader0.attr_editor_newclass = False
        fileuploader0.css_height = "100%"
        fileuploader0.css_left = "0px"
        fileuploader0.css_margin = "0px"
        fileuploader0.css_position = "absolute"
        fileuploader0.css_top = "0px"
        fileuploader0.css_width = "100%"
        fileuploader0.multiple_selection_allowed = False
        fileuploader0.savepath = "./"
        fileuploader0.variable_name = "fileuploader0"
        container2.append(fileuploader0,'fileuploader0')
        container1.append(container2,'container2')
        container0.append(container1,'container1')
        container3 = Container()
        container3.attr_editor_newclass = False
        container3.css_height = "90%"
        container3.css_left = "0px"
        container3.css_margin = "2px"
        container3.css_position = "absolute"
        container3.css_top = "34px"
        container3.css_width = "100%"
        container3.variable_name = "container3"
        container4 = Container()
        container4.attr_editor_newclass = False
        container4.css_height = "100%"
        container4.css_left = "0px"
        container4.css_margin = "2px"
        container4.css_position = "absolute"
        container4.css_top = "0px"
        container4.css_width = "20%"
        container4.variable_name = "container4"
        container3.append(container4,'container4')
        container5 = Container()
        container5.attr_editor_newclass = False
        container5.css_height = "100%"
        container5.css_left = "20%"
        container5.css_margin = "2px"
        container5.css_position = "absolute"
        container5.css_top = "0px"
        container5.css_width = "80%"
        container5.variable_name = "container5"
        self.aidcam = OpencvVideoWidget(self, width=256, height=256)
        self.aidcam.style['margin'] = '2px'
        self.aidcam.identifier="image_receiver"
        container5.append(self.aidcam,'aidcam')
        container3.append(container5,'container5')
        container0.append(container3,'container3')
        self.container0 = container0
        return self.container0

def get_map_img(pmap):
    size = (len(pmap), len(pmap[0]))
    img = np.ones([size[0] * 128, size[1] * 128, 3], np.uint8) * 55
    for x in range(size[0]):
        for y in range(size[1]):
            img[x * 128: x * 128 + 128, y * 128: y * 128 + 128, :] += np.array([0, int(pmap[x][y] * 200), 0]).astype('uint8')
    return img

def get_alpha(img):
    alpha_channel = img[:, :, 3]
    _, mask = cv2.threshold(alpha_channel, 254, 255, cv2.THRESH_BINARY)
    color = img[:, :, :3]
    new_img = cv2.bitwise_not(cv2.bitwise_not(color, mask=mask))
    return new_img

def process():
    cvs.setCustomUI()
    f = open("./matches/" + replay_file, "r", encoding="utf-8")
    data = json.loads(f.read())
    f.close()
    base_img_A = get_alpha(cvs.imread("./res/baseA.png", cv2.IMREAD_UNCHANGED))
    troop_img_A = get_alpha(cvs.imread("./res/troopA.png", cv2.IMREAD_UNCHANGED))
    miner_img_A = get_alpha(cvs.imread("./res/minerA.png", cv2.IMREAD_UNCHANGED))
    drone_img_A = get_alpha(cvs.imread("./res/droneA.png", cv2.IMREAD_UNCHANGED))
    base_img_B = get_alpha(cvs.imread("./res/baseB.png", cv2.IMREAD_UNCHANGED))
    troop_img_B = get_alpha(cvs.imread("./res/troopB.png", cv2.IMREAD_UNCHANGED))
    miner_img_B = get_alpha(cvs.imread("./res/minerB.png", cv2.IMREAD_UNCHANGED))
    drone_img_B = get_alpha(cvs.imread("./res/droneB.png", cv2.IMREAD_UNCHANGED))
    base_img_N = get_alpha(cvs.imread("./res/baseN.png", cv2.IMREAD_UNCHANGED))
    pmap = data["map"]["map"]
    back_img = get_map_img(pmap)
    for r in data["rounds"]:
        img = back_img.copy()
        for entity in r["entities"]:
            if entity["RobotInfo"] != {}:
                if entity["RobotInfo"]["team"] == "A":
                    if entity["RobotInfo"]["type"] == "base":
                        x, y = entity["RobotInfo"]["location"]
                        img[x * 128: x * 128 + 128, y * 128: y * 128 + 128, :] = base_img_A
                    if entity["RobotInfo"]["type"] == "troop":
                        x, y = entity["RobotInfo"]["location"]
                        img[x * 128: x * 128 + 128, y * 128: y * 128 + 128, :] = troop_img_A
                    if entity["RobotInfo"]["type"] == "miner":
                        x, y = entity["RobotInfo"]["location"]
                        img[x * 128: x * 128 + 128, y * 128: y * 128 + 128, :] = miner_img_A
                    if entity["RobotInfo"]["type"] == "drone":
                        x, y = entity["RobotInfo"]["location"]
                        img[x * 128: x * 128 + 128, y * 128: y * 128 + 128, :] = drone_img_A
                elif entity["RobotInfo"]["team"] == "B":
                    if entity["RobotInfo"]["type"] == "base":
                        x, y = entity["RobotInfo"]["location"]
                        img[x * 128: x * 128 + 128, y * 128: y * 128 + 128, :] = base_img_B
                    if entity["RobotInfo"]["type"] == "troop":
                        x, y = entity["RobotInfo"]["location"]
                        img[x * 128: x * 128 + 128, y * 128: y * 128 + 128, :] = troop_img_B
                    if entity["RobotInfo"]["type"] == "miner":
                        x, y = entity["RobotInfo"]["location"]
                        img[x * 128: x * 128 + 128, y * 128: y * 128 + 128, :] = miner_img_B
                    if entity["RobotInfo"]["type"] == "drone":
                        x, y = entity["RobotInfo"]["location"]
                        img[x * 128: x * 128 + 128, y * 128: y * 128 + 128, :] = drone_img_B
                else:
                    if entity["RobotInfo"]["type"] == "base":
                        x, y = entity["RobotInfo"]["location"]
                        img[x * 128: x * 128 + 128, y * 128: y * 128 + 128, :] = base_img_N
        cvs.imshow(img)

if __name__ == "__main__":
    global replay_file
    if len(sys.argv) == 3 and sys.argv[1] == "replay":
        replay_file = sys.argv[2]
    elif len(sys.argv) == 5 and sys.argv[1] == "run":
        replay_file = runtime.run_game(map_file=sys.argv[2], teamA=sys.argv[3], teamB=sys.argv[4])
    initcv(process)
    startcv(Show)
