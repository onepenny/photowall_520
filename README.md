# 520表白神器_python照片墙制作工具

最终生成如下图片
![最终生成的图片](https://github.com/onepenny/photowall_520/raw/master/she.png)

# Prepare
python3环境

# Install
```shell
pip3 install pillow
```

# Use
1. images/文件夹下放制作照片墙的图片 并保证10张及以上, 请提前命名`[照片序号].png`, 从0开始计数, 如`9.png`, 
2. images2/文件夹下放文字图片 并命名为`tip.png`
3. 修改index.py中L18中妹子名字矩阵picMatrix 
4. 命令行写法
```sh
py3 index.py [noTipImage_不使用iamges2/下tip.png] [imgCount_images/下照片数目]
```
```sh
组合demo
python3 index.py       (默认参数: 含tip.png, 照片数目10)
python3 index.py 0 40  (效果最好的命令: 含tip.png 照片数40)
python3 index.py 1     (不含tip.png, 照片数10)
python3 index.py 1 40  (不含tip.png, 照片数40)

```
5. copy she.png 给妹子 ~

# Problems
[ ] imgCount大于实际images/下数目时部分图片不展示

# Todo
[ ] 动态读取images images2/下照片数目
[ ] 根据入参自动修改妹子名字矩阵picMatrix