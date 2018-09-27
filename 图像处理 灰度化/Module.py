from PIL import Image
import os
"""
图像的基本单位：像素
一个小方块 需要3个像素表示RGB   0-255
灰度化公式：
    L
    0.299*R + 0.587*G + 0.114*B =

所有的数字图像其本质都是一个多维矩阵
(600 * 491 * 1 *2 *3)  像素   三维矩阵
  列    行      分量
  R     G       B
  位    级       色               --------》图像颜色的深度
        一般情况 一个图像 有 256级亮度
    如何取值   0-255      值越大  越接近透明色；值越小   颜色越深

"""
image = '3.jpg'
image_all = "绘画素描"+image
img = Image.open(image)
# ~ # 获取图像的模式
# ~ img_mode = img.mode
# ~ print(img_mode)     # RGB 模式
# ~ img_size = img.size 
# ~ print(img_size)     #(600,491)
# ~ img_get = img.getpixel((100,0))
# ~ print(img_get)      # (195，170，140 ) RGB像素

# 构建一个新的图像     L ： 代表一个8位的灰度图
new = Image.new('L',img.size,255)
# 尺寸
width ,height = img.size
# 转换成灰度图
img = img.convert('L')

# 画笔
Pen_size = 3
# 扩散器
Color_Diff = 6

for i in range(Pen_size + 1, width-Pen_size - 1):
    for j in range(Pen_size + 1, height-Pen_size - 1):
        # 原始颜色
        originalcolor = 255
        lcolor = sum([img.getpixel((i-r,j))for r in range(Pen_size)])//Pen_size
        rcolor = sum([img.getpixel((i+r,j))for r in range(Pen_size)])//Pen_size
        if abs(lcolor - rcolor) > Color_Diff:
            originalcolor -= (255 - img.getpixel((i,j))) // 4
            # 将计算的值 赋值给新的图像
            new.putpixel((i,j),originalcolor)
        qcolor = sum([img.getpixel((i,j-r))for r in range(Pen_size)])//Pen_size
        wcolor = sum([img.getpixel((i,j+r))for r in range(Pen_size)])//Pen_size
        if abs(qcolor - wcolor) > Color_Diff:
            originalcolor -= (255 - img.getpixel((i,j))) // 4
            # 将计算的值 赋值给新的图像
            new.putpixel((i,j),originalcolor)
        zcolor = sum([img.getpixel((i-r,j-r))for r in range(Pen_size)])//Pen_size
        xcolor = sum([img.getpixel((i+r,j+r))for r in range(Pen_size)])//Pen_size
        if abs(zcolor - xcolor) > Color_Diff:
            originalcolor -= (255 - img.getpixel((i,j))) // 4
            # 将计算的值 赋值给新的图像
            new.putpixel((i,j),originalcolor)
        acolor = sum([img.getpixel((i+r,j-r))for r in range(Pen_size)])//Pen_size
        scolor = sum([img.getpixel((i-r,j+r))for r in range(Pen_size)])//Pen_size
        if abs(acolor - scolor) > Color_Diff:
            originalcolor -= (255 - img.getpixel((i,j))) // 4
            # 将计算的值 赋值给新的图像
            new.putpixel((i,j),originalcolor)
#保存图像
new.save(image_all)

# 调用系统的英文阅读， 就是电脑系统内置的语音
os.system('mshta vbscript:createobject("sapi.spvoice").speak("%s")(window.close)'%'您的人物绘制已完成，请检验！')
# 绘制好图像后 电脑语音告知并自动打开图像
os.system(image_all)















