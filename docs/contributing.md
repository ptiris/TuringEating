# 贡献指南

贡献指南试行中~以下部分旨在帮助核心成员完善网站内容，面向潜在贡献者的部分有待后续完善（咕咕咕）

## 本地构建

1. 克隆本项目 repo
    ```shell
    $ git clone https://github.com/ptiris/TuringEating.git
    $ cd TuringEating
    ```
2. 安装 python 依赖（mkdocs 以及 material）
    ```shell
    $ pip install -r requirements.txt

    ```
3. 安装本文档专用插件
    ```shell
    $ cd TuringPlugins
    $ pip install -e .
    $ cd ..
    ```
4. 启动 mkdocs 本地服务
    ```shell
    $ mkdocs serve
    ```
    - 之后即可通过浏览器访问 localhost:8000 预览网站

## 贡献内容

### 网站结构

```
.
├── README.md
├── TuringPlugins
├── docs
│   ├── aroundschool 
│   ├── contributing.md    # 本页
│   ├── css/               # 本站用到的所有 css 样式         
│   ├── data/              # “评价”页面的元数据
│   ├── hangzhou/
│   ├── images
│   ├── index.md           # 主页
│   ├── inschool
│   └── js                 # 本站用到的所有 js 脚本
├── mkdocs.yml          # mkdocs 站点设置
├── overrides/          # mkdocs-material 个性主题设置
└── requirements.txt    # 本站构建所需全部 python 依赖
```

### 内容编辑

你可以直接编辑除“校区周围”和“杭州”之外的 md 源文件。

你可以按如下步骤为“校区周围”和“杭州”版块提供评价：
1. 按照以下格式将你的评价填入一份表格
    ```
    姓名,名称,分类,位置,专家,评价,定位
    ptiris,蓝蛙,西餐,IN77,False,"好吃，赞美周一买一送一",偶尔尝鲜
    ```
2. 将表格导出为 .csv 文件
3. 将导入内容与 docs/data 文件夹下对应的 .csv 数据合并

很快将发布评价系统以自动化该过程（咕咕咕）

### 贡献方式

推荐通过 PR（即 Pull Request）的形式来进行贡献，这有助于该网站之后的维护。具体流程：

- 在 GitHub 网页端点击右上角的 fork，将本仓库 fork 到自己的账号下
- 在自己账号的对应仓库中进行修改
- 修改完成后，点击 New pull request，提交一个 PR
- 等待其他人审核、修改，然后合并到本 repo 中
