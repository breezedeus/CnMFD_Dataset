# coding: utf-8
import random
import sys
import argparse

try:
    import numpy as np
    from PIL import Image
    import cv2
except:
    print(f'please install numpy, pillow and opencv libs at first: `pip install numpy pillow opencv-python`')
    sys.exit(-1)


MF_CATEGORIES = ['embedding', 'isolated']
TYPE_MAPPINGS = {'embedding': 0, 'isolated': 1}


def read_labels(label_fp, width, height):
    """读取label文件"""
    w, h = width, height

    outs = []
    with open(label_fp) as f:
        for line in f:
            eles = line.strip().split(' ')
            if len(eles) != 9:
                print(f'Warning - bad line: {line}')
                continue

            _type = MF_CATEGORIES[int(eles[0])]
            coords = list(map(float, eles[1:]))
            xmin, ymin = coords[:2]
            xmax, ymax = coords[4:6]
            _box = [xmin * w, ymin * h, xmax * w, ymax * h]
            _box = list(map(int, _box))
            outs.append({'type': _type, 'box': _box})
    return outs


def plot_one_box(x, img, color=None, label=None, line_thickness=3):
    # Plots one bounding box on image img
    tl = line_thickness or round(0.002 * (img.shape[0] + img.shape[1]) / 2) + 1  # line/font thickness
    color = color or [random.randint(0, 255) for _ in range(3)]
    c1, c2 = [int(x[0]), int(x[1])], [int(x[2]), int(x[3])]
    cv2.rectangle(img, c1, c2, color, thickness=tl, lineType=cv2.LINE_AA)
    if label:
        tf = max(tl - 1, 1)  # font thickness
        t_size = cv2.getTextSize(label, 0, fontScale=tl / 3, thickness=tf)[0]
        c2 = [c1[0] + t_size[0], c1[1] - t_size[1] - 3]
        txt_b_l = [c1[0], c1[1] - 2]
        if c2[1] < 0:  # 出界了
            c2[1] = c1[1] + t_size[1] + 3
            txt_b_l[1] = c1[1] + t_size[1] + 1
        cv2.rectangle(img, c1, c2, color, -1, cv2.LINE_AA)  # filled
        cv2.putText(img, label, txt_b_l, 0, tl / 3, [225, 255, 255], thickness=tf, lineType=cv2.LINE_AA)


def save_layout_img(img0, categories, boxes, save_path):
    """可视化版面分析结果。"""
    if isinstance(img0, Image.Image):
        img0 = cv2.cvtColor(np.asarray(img0.convert('RGB')), cv2.COLOR_RGB2BGR)

    colors = [[random.randint(0, 255) for _ in range(3)] for _ in categories]
    for one_box in boxes:
        _type = one_box['type']
        xyxy = one_box['box']
        label = f'{_type}'
        plot_one_box(
            xyxy,
            img0,
            label=label,
            color=colors[categories.index(_type)],
            line_thickness=1,
        )

    cv2.imwrite(save_path, img0)
    print(f" The image with the result is saved in: {save_path}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i',
        '--image-fp',
        type=str,
        default='examples/CnMFD_Dataset/images/Adobe-SongTi-Std-L-2/syndoc-page7.jpg',
        help='the file path of one page image',
    )
    parser.add_argument(
        '-l',
        '--label-fp',
        type=str,
        default='examples/CnMFD_Dataset/labels/Adobe-SongTi-Std-L-2/syndoc-page7.txt',
        help='the label file path corresponding to the page image',
    )
    parser.add_argument(
        '-o',
        '--output-fp',
        type=str,
        default='output-vis7.jpg',
        help='the file path of the output image after labelling math formulas',
    )
    args = parser.parse_args()
    img = Image.open(args.image_fp).convert('RGB')
    width, height = img.size
    boxes = read_labels(args.label_fp, width, height)
    save_layout_img(img, MF_CATEGORIES, boxes, args.output_fp)


if __name__ == '__main__':
    main()
