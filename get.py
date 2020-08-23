# -*- coding:utf-8 -*-

import os,json
import aiofiles

async def getIni(name,item):
    img = "{YOURDIR}/res/img/image-generate/image_data/"+str(name)+"/config.ini"
    async with aiofiles.open(img,"r",encoding="utf-8") as f:
        ini = await f.read()
    dic =  json.loads(ini)
    return dic[item]

async def getQqName(uid):
    p = "{YOURDIR}/res/img/image-generate/image_data/qqdata/"+str(uid)+".ini"
    mark = "initial"
    if os.path.exists(p):
        async with aiofiles.open(p,"r",encoding="utf-8") as f:
            mark = await f.read()
            mark = mark.strip()
    return mark

async def setQqName(uid,msg):
    item=0
    msg=str(msg)
    mark = str(await getQqName(uid))
    p="{YOURDIR}/res/img/image-generate/image_data/qqdata/"+str(uid)+".ini"
    name = "{YOURDIR}/res/img/image-generate/image_data/bieming/name.ini"
    if os.path.exists(name):
        async with aiofiles.open(name,"r",encoding='utf-8') as f:
            line = await f.readlines()
            for i in line:
                i = i.strip()
                line_list=i.split(" ")
                if line_list[0]==msg:
                    mark = line_list[1]
                    item=1
                    async with aiofiles.open(p,"w",encoding="utf-8") as f:
                        await f.write(str(mark))
                        return mark