import json
import os
import cv2
import numpy as np
import shutil
from skimage import transform as trans


def copy_image(path, save_path):

    folder = os.path.dirname(save_path)
    if not os.path.exists(folder):
        os.makedirs(folder)
    shutil.copy2(path, save_path)


def align_image(path, save_path, five_points):

    dst = np.array(five_points)

    folder = os.path.dirname(save_path)
    if not os.path.exists(folder):
        os.makedirs(folder)

    image_size = [224, 224]
    src = np.array([
        [68.0, 100.0],
        [148.0, 100.0],
        [112.0, 146.0],
        [78.0, 180.0],
        [140.0, 180.0]])

    img = cv2.imread(path)
    tform = trans.SimilarityTransform()
    tform.estimate(dst, src)
    M = tform.params[0:2, :]
    warped = cv2.warpAffine(img, M, (224, 224), borderValue=0.0)
    cv2.imwrite(save_path, warped)
 

def cat_image(path1, path2, save_path):

    image1 = cv2.imread(path1)
    image2 = cv2.imread(path2)

    height1, width1 = image1.shape[:2]
    height2, width2 = image2.shape[:2]

    max_height = max(height1, height2)
    total_width = width1 + width2

    concatenated_image = np.zeros((max_height, total_width, 3), dtype=np.uint8)

    concatenated_image[:height1, :width1] = image1
    concatenated_image[:height2, width1:] = image2

    folder = os.path.dirname(save_path)
    if not os.path.exists(folder):
        os.makedirs(folder)

    cv2.imwrite(save_path, concatenated_image)


def add_2_box_to_image(src_path, save_path, box1, box2, color1=(0, 0, 255), color2=(0, 0, 255)):

    image = cv2.imread(src_path)

    top_left = [box1[0], box1[1]]
    bottom_right = [box1[2], box1[3]]
    cv2.rectangle(image, top_left, bottom_right, color1, 2) 

    top_left = [box2[0], box2[1]]
    bottom_right = [box2[2], box2[3]]
    cv2.rectangle(image, top_left, bottom_right, color2, 2)
    
    folder = os.path.dirname(save_path)
    if not os.path.exists(folder):
        os.makedirs(folder)
    cv2.imwrite(save_path, image)


def add_box_to_image(src_path, save_path, box, width=2):

    image = cv2.imread(src_path)

    top_left = [box[0], box[1]]
    bottom_right = [box[2], box[3]]
    cv2.rectangle(image, top_left, bottom_right, (0, 0, 255), width) 
    
    folder = os.path.dirname(save_path)
    if not os.path.exists(folder):
        os.makedirs(folder)
    cv2.imwrite(save_path, image)


def crop_image(src_path, save_path, box):
 
    image = cv2.imread(src_path)
    height, width, channels = image.shape

    x1, y1, x2, y2 = box[0], box[1], box[2], box[3]
    x1 = max(0, min(x1, width))
    x2 = max(0, min(x2, width))
    y1 = max(0, min(y1, height))
    y2 = max(0, min(y2, height))

    cropped_image = image[y1:y2, x1:x2]

    folder = os.path.dirname(save_path)
    if not os.path.exists(folder):
        os.makedirs(folder)
    cv2.imwrite(save_path, cropped_image)


def prepare_single_sample(sample_info, raw_data_root_path, eval_data_root_path):

    if sample_info["type"].startswith("face_age") or sample_info["type"] == "face_expression_basic":
        original_src = os.path.join(raw_data_root_path, sample_info["image"]["source"]["paths"]["original"])

        cropped_dst = os.path.join(eval_data_root_path, sample_info["image"]["image_paths"]["cropped"])
        original_dst = os.path.join(eval_data_root_path, sample_info["image"]["image_paths"]["original"])

        five_points = sample_info["image"]["source"]["labels"]["five_points"]

        align_image(original_src, cropped_dst, five_points)
        copy_image(original_src, original_dst)

    elif sample_info["type"].startswith("face_attack") or sample_info["type"] == "face_expression_compound":

        cropped_src = os.path.join(raw_data_root_path, sample_info["image"]["source"]["paths"]["cropped"])
        cropped_dst = os.path.join(eval_data_root_path, sample_info["image"]["image_paths"]["cropped"])
        
        copy_image(cropped_src, cropped_dst)

    elif sample_info["type"] == "face_attribute_compound":
        cropped_src = os.path.join(raw_data_root_path, sample_info["image"]["source"]["paths"]["cropped"])
        original_src = os.path.join(raw_data_root_path, sample_info["image"]["source"]["paths"]["original"])

        cropped_dst = os.path.join(eval_data_root_path, sample_info["image"]["image_paths"]["cropped"])
        original_dst = os.path.join(eval_data_root_path, sample_info["image"]["image_paths"]["original"])

        copy_image(cropped_src, cropped_dst)
        copy_image(original_src, original_dst)

    elif sample_info["type"].startswith("face_recognition") or sample_info["type"]=="human_reid_basic":
        cropped_1_src = os.path.join(raw_data_root_path, sample_info["image"]["source"]["paths"]["cropped_1"])
        cropped_2_src = os.path.join(raw_data_root_path, sample_info["image"]["source"]["paths"]["cropped_2"])

        cropped_dst = os.path.join(eval_data_root_path, sample_info["image"]["image_paths"]["cropped"])
        cat_image(cropped_1_src, cropped_2_src, cropped_dst)

    elif sample_info["type"] == "human_action_basic":

        original_src = os.path.join(raw_data_root_path, sample_info["image"]["source"]["paths"]["original"])
        boxed_dst = os.path.join(eval_data_root_path, sample_info["image"]["image_paths"]["boxed"])
        box_1 = sample_info["image"]["source"]["labels"]["human_bbox"] #x1 x2 y1 y2
        new_box_1 = [box_1[0], box_1[2], box_1[1], box_1[3]]

        add_box_to_image(original_src, boxed_dst, new_box_1)

    elif sample_info["type"] == "human_attribute_compound":
        original_src = os.path.join(raw_data_root_path, sample_info["image"]["source"]["paths"]["original"])
        boxed_dst = os.path.join(eval_data_root_path, sample_info["image"]["image_paths"]["boxed"])
        box_1 = sample_info["image"]["source"]["labels"]["bbox"] #x1 y1 w h
        new_box_1 = [int(box_1[0]), int(box_1[1]), int(box_1[0]+box_1[2]), int(box_1[1]+box_1[3])]
        
        add_box_to_image(original_src, boxed_dst, new_box_1, width=5)

    elif sample_info["type"] == "human_attribute_compound_cropped":
        original_src = os.path.join(raw_data_root_path, sample_info["image"]["source"]["paths"]["original"])
        boxed_dst = os.path.join(eval_data_root_path, sample_info["image"]["image_paths"]["cropped"])
        box_1 = sample_info["image"]["source"]["labels"]["bbox"] #x1 y1 w h
        new_box_1 = [int(box_1[0]), int(box_1[1]), int(box_1[0]+box_1[2]), int(box_1[1]+box_1[3])]

        crop_image(original_src, boxed_dst, new_box_1)

    elif sample_info["type"] == "human_social_relation_occupation":

        original_src = os.path.join(raw_data_root_path, sample_info["image"]["source"]["paths"]["original"])
        boxed_dst = os.path.join(eval_data_root_path, sample_info["image"]["image_paths"]["boxed"])
        box_1 = sample_info["image"]["source"]["labels"]["human_bbox"]

        add_box_to_image(original_src, boxed_dst, box_1)

    
    elif sample_info["type"] == "human_social_relation_relationship":

        original_src = os.path.join(raw_data_root_path, sample_info["image"]["source"]["paths"]["original"])
        boxed_dst = os.path.join(eval_data_root_path, sample_info["image"]["image_paths"]["boxed"])

        box_1 = sample_info["image"]["source"]["labels"]["first_human_bbox"]
        box_2 = sample_info["image"]["source"]["labels"]["second_human_bbox"]

        add_2_box_to_image(original_src, boxed_dst, box_1, box_2)

    if sample_info["type"].startswith("human_spatial_relation_count"):
        original_src = os.path.join(raw_data_root_path, sample_info["image"]["source"]["paths"]["original"])
        original_dst = os.path.join(eval_data_root_path, sample_info["image"]["image_paths"]["original"])

        copy_image(original_src, original_dst)



    elif sample_info["type"] == "human_spatial_relation_location":
        original_src = os.path.join(raw_data_root_path, sample_info["image"]["source"]["paths"]["original"])
        boxed_dst = os.path.join(eval_data_root_path, sample_info["image"]["image_paths"]["boxed"])

        box_1 = sample_info["image"]["source"]["labels"]["subject_bbox"] #y1 y2 x1 x2
        box_2 = sample_info["image"]["source"]["labels"]["object_bbox"] # y1 y2 x1 x2

        new_box_1 = [box_1[2], box_1[0], box_1[3], box_1[1]]
        new_box_2 = [box_2[2], box_2[0], box_2[3], box_2[1]]

        add_2_box_to_image(original_src, boxed_dst, new_box_1, new_box_2, color2=(0, 255, 0))


def prepare(raw_data_root_path, eval_data_root_path, json_files_path, selected_subset):

    sample_list = []

    for each in selected_subset:
        temp_path = os.path.join(json_files_path, each+'.json')
        with open(temp_path, 'r') as file:
            data_dict = json.load(file)
            sample_list.extend(data_dict["data"])

    print(len(sample_list))

    for sample_info in sample_list:
        prepare_single_sample(sample_info, raw_data_root_path, eval_data_root_path)


if __name__ == "__main__":

    #TODO path for raw_data (input)
    raw_data_root_path = "<your_path>/raw_data"

    #TODO path for eval_data (output)
    eval_data_root_path = "<your_path>/<dev or test>/output"

    #TODO path for JSON files
    json_files_path = "<your_path>/<dev or test>/json/en"

    selected_subset = ["face_age_basic_5", 
                       "face_age_basic_10", 
                       "face_age_basic_15",
                       "face_attack_digital_expression_swap",
                       "face_attack_digital_identity_swap",
                       "face_attack_physical_paper",
                       "face_attack_physical_replay",
                       "face_attribute_compound",
                       "face_expression_basic",
                       "face_expression_compound",
                       "face_recognition_basic",
                       "face_recognition_cross_age",
                       "face_recognition_cross_pose",
                       "face_recognition_mask",
                       "face_recognition_similar_looking",
                       "human_action_basic",
                       "human_attribute_compound_cropped",
                       "human_attribute_compound",
                       "human_reid_basic",
                       "human_social_relation_occupation",
                       "human_social_relation_relationship",
                       "human_spatial_relation_count_10", 
                       "human_spatial_relation_count_100", 
                       "human_spatial_relation_count_100plus",
                       "human_spatial_relation_location"
                       ]

    prepare(raw_data_root_path, eval_data_root_path, json_files_path, selected_subset)