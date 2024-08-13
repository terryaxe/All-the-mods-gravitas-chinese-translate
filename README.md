<div align="center"> 
   <h1>某某项目简体中文翻译</h1>
</a>
</div>

CurseForge|加载器|整合包版本|状态
:-|:-|:-|:-
[链接](原链接)|模组加载器|mc1.版本 版本|*翻译中*|

---

汉化项目：[Paratranz](https://paratranz.cn/projects/项目)

汉化发布：[VM汉化组官网](https://beta.vmct-cn.top/modpacks/项目)

项目主管 @[某某](https://github.com/某某)

技术支持：@[某某](https://github.com/某某)

译者：[查看贡献者排行榜](https://paratranz.cn/projects/项目/leaderboard)


---
整合包简介

# 整合包介绍



# 自动化Paratranz同步教程
## 1. 设置环境变量

1. 到仓库顶部导航栏: Settings -> Environments -> New environment 新建PARATRANZ_ENV
2. 添加加密变量（Environment secrets）: 名称：`API_KEY` , 值：`你的ParatranzTOKEN`
3. 添加环境变量（Environment variables）: 
    - 名称：`G_PATH` , 值：`仓库链接（.git的域名）`，例如`https://github.com/VM-Chinese-translate-group/FTB-Neotech.git`
    
    - 名称：`ID` , 值：`Paratranz项目ID`，例如`10719`

## 2.开始使用

有两种功能：Paratranz到github仓库，github仓库到Paratranz

每天会自动同步下载到github，也可以使用issue启动，请新建一个issue

1. 上传原文至Paratranz
   - `自动化:Github→paratranz`标签

2. 下载译文至Github
   - 添加`自动化:paratrayunz→Github`标签


下载译文至Github功能也可以按时启动,可自行在`.github/workflows`文件夹中`download_action.yml`文件修改自动执行时间。用cron格式表示。

Paratranz到github仓库后会在action对应页面生成构件，即为自动生成的汉化补丁
