# jobb_pider

---
## 1. 项目介绍
本项目用于爬取前程无忧、智联招聘、拉勾等招聘网站发布的招聘信息，包括岗位名称、岗位要求、公司名称、经验要求等近30个字段，可用于对目前不同地区、行业招聘市场的数据分析中。

#### 目前已完成爬虫：
- 前程无忧网手机APP爬虫。
- ……

其他网站爬虫将在后续完成后上传。
## 2. 爬虫设计
### 2.1 前程无忧网手机APP爬虫
#### 技术路线：

**爬虫框架**：scrapy

**数据抓取**：scrapy.Selector

**数据存储**：Twisted+MySQL

关于爬虫的设计思路和分析流程，将在个人博客中进行详细说明：
https://www.cnblogs.com/chenhuabin/p/10164618.html


## 3. 下载
**下载源码**

git方式下载：git@github.com:ChenHuabin321/job_spider.git

或者直接到下载zip源码包，地址为：https://github.com/ChenHuabin321/job_spider

**安装依赖**

Scrapy==1.5.0

Twisted==18.4.0


**数据库配置**

以下是settings.py中的默认数据库配置，可进行修改为你的数据库配置：

MYSQL_HOST = '192.168.56.101'#主机

MYSQL_PASSWORD = '123456'#密码

MYSQL_DBNAME = 'job_spider'#数据库名

## 4. 采集效果
前程无忧网手机APP爬虫采集结果如下所示：
![前程无忧手机APP爬虫采集结果图](https://github.com/ChenHuabin321/job_spider/blob/master/jobSpider/qcwySpiderResult.png)

