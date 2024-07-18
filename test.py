import numpy as np
from scipy.spatial import distance

# def line_pos(A_start, A_end, line_start, line_end):
#     # 將點轉換為numpy array以便進行向量運算
#     A_start = np.array(A_start)
#     A_end = np.array(A_end)
#     line_start = np.array(line_start)
#     line_end = np.array(line_end)
#     v1 = (A_start[0] - A_end[0], A_start[1] - A_end[1])
#     v2 = (A_start[0] - line_start[0], A_start[1] - line_start[1])
#     v0 = (A_start[0] - A_end[0], A_start[1] - A_end[1])
#     a = v0[0] * v1[1] - v0[1] * v1[0]
#     b = v0[0] * v2[1] - v0[1] * v2[0]
#     temp = A_start
#     A_start = line_start
#     line_start = temp
#     v1 = (A_start[0] - A_end[0], A_start[1] - A_end[1])
#     v2 = (A_start[0] - line_start[0], A_start[1] - line_start[1])
#     v0 = (A_start[0] - A_end[0], A_start[1] - A_end[1])
#     c = v0[0] * v1[1] - v0[1] * v1[0]
#     d = v0[0] * v2[1] - v0[1] * v2[0]

#     if a * b < 0 and c * d < 0:
#         return True
#     else:
#         return False
# # A_start = (0,0)
# # A_end = (2,2)
# # line_start = (2,0)
# # line_end = (0,2) 
# # result = line_pos(A_start, A_end, line_start, line_end)
# # print(f"兩條線段是否相交: {result}")
# def calculate_iou(box1, box2):
#     # 计算两个 bounding box 的交集部分
#     x1_intersect = max(box1[0], box2[0])
#     y1_intersect = max(box1[1], box2[1])
#     x2_intersect = min(box1[2], box2[2])
#     y2_intersect = min(box1[3], box2[3])
    
#     # 计算交集的面积
#     intersection_area = max(0, x2_intersect - x1_intersect + 1) * max(0, y2_intersect - y1_intersect + 1)
    
#     # 计算并集的面积
#     box1_area = (box1[2] - box1[0] + 1) * (box1[3] - box1[1] + 1)
#     box2_area = (box2[2] - box2[0] + 1) * (box2[3] - box2[1] + 1)
#     union_area = box1_area + box2_area - intersection_area
    
#     # 计算 IoU
#     iou = intersection_area / union_area
    
#     return iou
# def find_highest_iou_boxes(boxes1, boxes2):
#     max_iou = 0
#     highest_iou_boxes = None
    
#     for box1 in boxes1:
#         for box2 in boxes2:
#             iou = calculate_iou(box1, box2)
#             if iou > max_iou:
#                 max_iou = iou
#                 highest_iou_boxes = (box1, box2)
    
#     return highest_iou_boxes
# box1 = [0, 0, 5, 5]  # 左上角坐标为 (0, 0)，右下角坐标为 (5, 5)
# box2 = [3, 3, 8, 8]  # 左上角坐标为 (3, 3)，右下角坐标为 (8, 8)
# b1=[1507.0, 154.0, 1697.0, 413.0]
# b2=[1507.0, 154.0, 1697.0, 413.0]
# iou = calculate_iou(b1, b2)
# print("IoU:", iou)
a=dict()
a['1']=0
a['2']=0
if str(1) in a:
    print('c')

  