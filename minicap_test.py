# -*- coding: utf-8 -*-
from airtest.core.api import *
from airtest.core.android.minicap import *

import cv2
import numpy as np


adb = connect_device("Android:///").adb
cap = Minicap(adb, [1080, 1920])  # 分辨率可以适当修改，提高速度
image_bytes = cap.get_frame_from_stream()
img = cv2.imdecode(np.fromstring(image_bytes, np.uint8), cv2.IMREAD_COLOR)
