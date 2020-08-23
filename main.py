# -*- coding:utf-8 -*-

from PIL import ImageDraw, Image, ImageFont
import os,sys
from . import get
from hoshino import Service, R

async def img(bot, ev, msg, uid):
    if os.path.exists("{YOURDIR}/res/img/image-generate/image/"+str(uid)+".jpg"):
        os.remove("{YOURDIR}/res/img/image-generate/image/"+str(uid)+".jpg")
    file = await get.getQqName(uid)
    color = await get.getIni(file,"color")
    img = Image.open("{YOURDIR}/res/img/image-generate/image_data/"+file+"/"+str(await get.getIni(file,"name"))+".jpg")
    draw = ImageDraw.Draw(img)
    font_size=await get.getIni(file,"font_size")
    font_max=await get.getIni(file,"font_max")
    image_font_center=(await get.getIni(file,"font_center_x"),await get.getIni(file,"font_center_y"))
    image_font_sub = await get.getIni(file,"font_sub")
    ttfront = ImageFont.truetype('simhei.ttf',font_size)  # 设置字体暨字号
    font_length = ttfront.getsize(msg)
    #print(font_length)
    while font_length[0]>font_max:
        font_size-=image_font_sub
        ttfront = ImageFont.truetype('simhei.ttf', font_size)
        font_length = ttfront.getsize(msg)
    #print(ttfront.getsize("你好"))
    # 自定义打印的文字和文字的位置
    if font_length[0]>5:
        draw.text((image_font_center[0]-font_length[0]/2, image_font_center[1]-font_length[1]/2),
                    msg, fill=color,font=ttfront)
        img.save("{YOURDIR}/res/img/image-generate/image/"+str(uid)+".jpg")
        await bot.send(ev, R.img(f'image-generate/image/{uid}.jpg').cqcode, at_sender=True)
