<div align="center"> 
   <h1>ATMG2简体中文翻译</h1>
</div>

| CurseForge     | 加载器     | 整合包版本         | 汉化维护状态 |
| :------------- | :--------- | :----------------- | :----------- |
| [链接](https://www.curseforge.com/minecraft/modpacks/all-the-mods-gravitas2) | forge | 1.20.1-0.7.2 | 翻译中       |

---

汉化项目：[Paratranz](https://paratranz.cn/projects/15828)

汉化发布：[VM 汉化组官网](https://vmct-cn.top/modpacks/项目)

译者：[查看贡献者排行榜](https://paratranz.cn/projects/项目/leaderboard)

# 整合包介绍

Per aspera ad astra - 仰望星空，脚踏实地。

从原始的石器时代技术开始，亲手制作工具，觅食生存，你将伴随着一系列或经典、或新颖的模组一道，经历时代变迁，体验更充实的的群峦传说模组游玩体验。另有机械动力：电气时代、钍反应堆、动态联合、应用能源、星门之旅，也许最令人期待的新增功能当属格雷科技了。

今天的你，置身荒野，将石头敲击在一起，苟图衣食。

而明天，你将发展到将原子撞击在一起，为伟大的星际航行驶向更远的未知天体提供动力！

# 自动化 Paratranz 同步教程

## 1. 设置环境变量

1. 到仓库顶部导航栏: `Settings -> Environments -> New environment` 新建 `PARATRANZ_ENV`
2. 添加加密变量（Environment secrets）:
   | 名称 | 值 |
   |-------------|-------------------------------------------------|
   | API_KEY | 你的 Paratranz token，须有上传文件权限 |
   token 可在 <https://paratranz.cn/users/my> 中的设置部分获取。
3. 添加环境变量（Environment variables）:

   | 名称 | 值                              |
   | ---- | ------------------------------- |
   | ID   | Paratranz 项目 ID，例如 `10719` |

## 2. 开始使用

我们的工作流有两种功能：从 Paratranz 同步到 github 仓库和从 github 仓库同步到 Paratranz。

它们全都可以手动运行，操作方法如下图所示：

![](.github/action.png)

其中，Paratranz 同步到 GitHub 仓库工作流会分别在北京时间每天早晚上 10 点左右自动运行一次。

下载译文至 Github 功能可自行修改`.github/workflows`文件夹中的`download_release.yml`自动执行时间，格式为[cron 表达式](https://blog.csdn.net/Stromboli/article/details/141962560)。

在有译文更改后，工作流会自动发布一次标记为预发布的 Release 供大家测试。此外，每次从上游同步还将运行一次 FTB 任务颜色字符检查程序，
当有颜色字符错误时，将会在 release 的说明页面中进行提示，并在工作流的构件（artifact）页和 release 页面上传错误报告的 html，相关人员可下载并通过浏览器打开该文件。

当没有检查到颜色错误时，工作流详情页内会出现警告，提示找不到错误报告文件，这一点无需担心，不会造成任何负面影响。

注：从 github 仓库同步到 Paratranz 的工作流很少使用，故仅支持手动触发。

如果项目已经完成，请在仓库设置（`Settings`）中禁用工作流运行。
