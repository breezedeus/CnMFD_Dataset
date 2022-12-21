# CnMFD_Dataset

Chinese Mathematical Formula Detection (MFD) Dataset.



**CnMFD_Dataset** 是利用合成技术生成的包含数学公式的中文文档数据集，可用于训练数学公式检测模型。



CnMFD_Dataset 包含了不同字体的总共 **17500** 页文档，其中各字体对应的文档页数如下：

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



几个示例图片：

**TODO**



## 文件格式

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

而 `<xmin>`、`<xmax> `对应公式所在位置的最小和最大 `x` 值（已归一化），取值范围为 `[0, 1]`；类似地， `<ymin>`、`<ymax> ` 对应归一化后的最小和最大 `y` 值（已归一化）。
