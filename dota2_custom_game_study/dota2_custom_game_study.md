***参考资料:***

> moddota：https://moddota.com/
>
> Valve官方创意工坊：https://developer.valvesoftware.com/wiki/Dota_2_Workshop_Tools:zh-cn
>
> RobinCode_Dota2API：https://robincode.cn/dota2/logs
>
> 阿哈利姆魔法隐修议会：http://www.dota2rpg.com/
>
> reddit：https://www.reddit.com/r/Dota2Modding/
>
> b站彩紫睨羽编辑器入门：https://www.bilibili.com/video/BV1s4411W7rw?spm_id_from=333.999.0.0
>
> Youtube入门教程：[https://www.bilibili.com/video/BV1s4411W7rw?spm_id_from=333.999.0.0](https://www.youtube.com/watch?v=kzj9yM_9zAw&list=PL7yysLaMSd3uY4iJKJdRrTkN1gYePkMz2)
>
> VRF反编译工具：https://github.com/SteamDatabase/ValveResourceFormat

## 一、地形编辑器与关卡设计

1.地图文件目录

![](../.all_images/dota_img0.png)

![](../.all_images/dota_img1.png)

![](../.all_images/dota_img2.png)

![](../.all_images/dota_img3.png)





## 二、技能编写

game/\<addonName\>/scripts/文件夹下，有两个主要文件夹：**npc** 和 **vscripts**. 

**npc**文件夹包含以下文件：

- npc_**abilities**_custom.txt - 自定义技能
- npc_**heroes**_custom.txt - 英雄技能和状态
- npc_**items**_custom.txt - 自定义物品
- npc_**units**_custom.txt - 非英雄单位（包括所有生物和建筑）
- npc_**abilities**_override.txt - 在原有dota基础技能或物品上进行魔改，只能改动数值和描述等
- **herolist**.txt - 自定义可选英雄



**vscripts**文件夹用于存放所有lua脚本：

There's 4 applications for Lua in Dota:

- Game Logic - 游戏逻辑
- DataDriven RunScript - 数据驱动脚本
- Hammer I/O - Hammer接口
- Custom UI Events - 自定义UI

























## 三、UI编写

