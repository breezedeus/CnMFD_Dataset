<div align="center">

[![CC BY 4.0][cc-by-shield]][cc-by]

</div>



# CnMFD_Dataset

**CnMFD_Dataset** 是利用合成技术生成的包含数学公式的中文文档数据集，可用于训练数学公式检测模型。**CnMFD_Dataset** 包含了不同字体的总共 **17500** 页文档，其中各字体对应的文档页数如下：

<div align="center">

| 字体名称             | 文档页面数量 |
| -------------------- | ------------ |
| Adobe-SongTi-Std-L-2 | 2000         |
| Arial Unicode        | 500          |
| Fangsong             | 2000         |
| Kaiti                | 2000         |
| Microsoft Yahei      | 1000         |
| msyh                 | 1000         |
| msyhbd               | 1000         |
| PingFang             | 2000         |
| Songti               | 2000         |
| STHeiti Medium       | 2000         |
| Zhongsong            | 2000         |

</div>



本项目中提供了 [CnMFD_Dataset样例数据](./examples/CnMFD_Dataset)，完整数据集大小为 **3.6G**，下载地址为 [CnMFD_Dataset @ Kaggle](https://www.kaggle.com/datasets/breezedeus/cnmfd-dataset) 。



几个效果示例图片：

<div align="center">
  <img src="output-vis4.jpg" alt="中文MFD效果" width="700px"/>
</div>  
<div align="center">
  <img src="output-vis7.jpg" alt="中文MFD效果" width="700px"/>
</div>



## 文件格式说明

主目录下包含两个文件夹：

* `images`：存储不同字体对应的文档图片；
* `labels`：存储同名文档图片对应的数学公式标签（所在位置）；



```bash
├── images
│   ├── Adobe-SongTi-Std-L-2
│   ├── Arial\ Unicode
│   ├── Fangsong
│   ├── Kaiti
│   ├── Microsoft\ Yahei
│   ├── PingFang
│   ├── STHeiti\ Medium
│   ├── Songti
│   ├── Zhongsong
│   ├── msyh
│   └── msyhbd
└── labels
    ├── Adobe-SongTi-Std-L-2
    ├── Arial\ Unicode
    ├── Fangsong
    ├── Kaiti
    ├── Microsoft\ Yahei
    ├── PingFang
    ├── STHeiti\ Medium
    ├── Songti
    ├── Zhongsong
    ├── msyh
    └── msyhbd
```



label文件中每行对应一个数学公式类别和所在位置，每列以空格分割：

```python
<class_id> <xmin> <ymin> <xmax> <ymin> <xmax> <ymax> <xmin> <ymax>
```

其中 `<class_id>` 含义为：

* `0`：行内公式，即 `embedding` formula；
* `1`：独立行公式，即 `isolated` formula。

而 `<xmin>`、`<xmax> `对应公式所在位置的最小和最大 `x` 值（已归一化：绝对值除以图片宽度），取值范围为 `[0, 1]`；类似地， `<ymin>`、`<ymax> ` 对应归一化后的最小和最大 `y` 值（已归一化：绝对值除以图片高度）。



## 可视化工具

可以使用提供的脚本 [visualize.py](visualize.py) 可视化效果。此脚本依赖Python 包 numpy, pillow, opencv。使用以下命令安装依赖包和运行脚本：

```bash
$ pip install numpy pillow opencv-python
$ python visualize.py -i examples/CnMFD_Dataset/images/PingFang/syndoc-page4.jpg -l examples/CnMFD_Dataset/labels/PingFang/syndoc-page4.txt -o
output-vis4.jpg
```



脚本 [visualize.py](visualize.py) 使用说明：

```bash
$ python visualize.py --help
usage: visualize.py [-h] [-i IMAGE_FP] [-l LABEL_FP] [-o OUTPUT_FP]

optional arguments:
  -h, --help            show this help message and exit
  -i IMAGE_FP, --image-fp IMAGE_FP
                        the file path of one page image
  -l LABEL_FP, --label-fp LABEL_FP
                        the label file path corresponding to the page image
  -o OUTPUT_FP, --output-fp OUTPUT_FP
                        the file path of the output image after labelling math formulas
```





## 致谢与引用

CnMFD_Dataset 中使用的文字来自公开的Wiki数据，数学公式抽取自 [IBEM Mathematical Formula Detection Dataset](https://zenodo.org/record/4757865) ，感谢作者们。



本数据集遵循开源协议 [Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) 。

[![CC BY 4.0][cc-by-image]][cc-by]



使用 **CnMFD_Dataset** 请引用：

```tex
 @misc{breezedeus_2022,
	title={CnMFD_Dataset},
	url={https://www.kaggle.com/dsv/4752383},
	DOI={10.34740/KAGGLE/DSV/4752383},
	publisher={Kaggle},
	author={breezedeus},
	year={2022}
}
```

## 给作者来杯咖啡

开源不易，如果此项目对您有帮助，可以考虑 [给作者来杯咖啡 ☕️](https://cnocr.readthedocs.io/zh/latest/buymeacoffee/) 。

---

官方代码库：[https://github.com/breezedeus/CnMFD_Dataset](https://github.com/breezedeus/CnMFD_Dataset)。




[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

