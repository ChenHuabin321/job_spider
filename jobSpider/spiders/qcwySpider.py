# -*- coding: utf-8 -*-
import time
import random
import scrapy
from scrapy.selector import Selector
from jobSpider.items import qcwyJobsItem

class QcwyspiderSpider(scrapy.Spider):
    name = 'qcwySpider'
    keyword = 'python'
    current_page = 1
    max_page = 100
    headers = {
                'Accept': 'text / html, application / xhtml + xml, application / xml;',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Connection': 'keep-alive',
                'Host': 'appapi.51job.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    }
    allowed_domains = ['appapi.51job.com']
    start_urls = ['https://appapi.51job.com/api/job/search_job_list.php?postchannel=0000&&keyword='+str(keyword)+
                  '&keywordtype=2&jobarea=000000&searchid=&famoustype=&pageno=1&pagesize=30&accountid=97932608&key'
                  '=a8c33db43f42530fbda2f2dac7a6f48d5c1c853a&productname=51job&partner=8785419449a858b3314197b60d5'
                  '4d9c6&uuid=6b21f77c7af3aa83a5c636792ba087c2&version=845&guid=bbb37e8f266b9de9e2a9fbe3bb81c3d0']

    def parse(self, response):
        """

        通过循环的方式实现一级页面翻页，并采集jobid构造二级页面url
        :param response:
        :return:
        """
        selector = Selector(response=response)
        itmes = selector.xpath('//item')
        for item in itmes:
            jobid = item.xpath('./jobid/text()').extract_first()
            url = 'https://appapi.51job.com/api/job/get_job_info.php?jobid='+jobid+'&accountid=&key=&from=searchjoblist&jobtype=0100&productname=51job&partner=8785419449a858b3314197b60d54d9c6&uuid=6b21f77c7af3aa83a5c636792ba087c2&version=845&guid=bbb37e8f266b9de9e2a9fbe3bb81c3d0'
            yield scrapy.Request(url=url, headers=self.headers, dont_filter=False, callback=self.parse_job)
        if self.current_page < self.max_page:
            self.current_page += 1
            neext_page_url = 'https://appapi.51job.com/api/job/search_job_list.php?postchannel=0000&&keyword=Python&keywordtype=2&jobarea=000000&searchid=&famoustype=&pageno=1' \
                         + str(self.current_page) +  '&pagesize=30&accountid=97932608&key=a8c33db43f42530fbda2f2dac7a6f48d5c1c853a&productname=51job&partner=8785419449a858b3314197b60d54d9c6&uuid=6b21f77c7af3aa83a5c636792ba087c2&version=845&guid=bbb37e8f266b9de9e2a9fbe3bb81c3d0'
            time_delay = random.randint(3,5)
            time.sleep(time_delay)
            yield scrapy.Request(url=neext_page_url, headers=self.headers, dont_filter=True, callback=self.parse)

    def parse_job(self, response):
        """
        二级页面信息采集
        :param response:
        :return:
        """
        time.sleep(random.randint(3,5))
        selector = Selector(response=response)
        item = qcwyJobsItem()
        item['jobid'] = selector.xpath('/responsemessage/resultbody/jobid/text()').extract_first()
        item['jobname'] = selector.xpath('/responsemessage/resultbody/jobname/text()').extract_first()
        item['coid'] = selector.xpath('/responsemessage/resultbody/coid/text()').extract_first()
        item['coname'] = selector.xpath('/responsemessage/resultbody/coname/text()').extract_first()
        item['issuedate'] = selector.xpath('/responsemessage/resultbody/issuedate/text()').extract_first()
        item['jobarea'] = selector.xpath('/responsemessage/resultbody/jobarea/text()').extract_first()
        item['jobnum'] = selector.xpath('/responsemessage/resultbody/jobnum/text()').extract_first()
        item['degree'] = selector.xpath('/responsemessage/resultbody/degree/text()').extract_first()
        item['jobareacode'] = selector.xpath('/responsemessage/resultbody/jobareacode/text()').extract_first()
        item['cityname'] = selector.xpath('/responsemessage/resultbody/cityname/text()').extract_first()
        item['funtypecode'] = selector.xpath('/responsemessage/resultbody/funtypecode/text()').extract_first()
        item['funtypename'] = selector.xpath('/responsemessage/resultbody/funtypename/text()').extract_first()
        item['workyearcode'] = selector.xpath('/responsemessage/resultbody/workyearcode/text()').extract_first()
        item['address'] = selector.xpath('/responsemessage/resultbody/address/text()').extract_first()
        item['joblon'] = selector.xpath('/responsemessage/resultbody/joblon/text()').extract_first()
        item['joblat'] = selector.xpath('/responsemessage/resultbody/joblat/text()').extract_first()
        item['welfare'] = selector.xpath('/responsemessage/resultbody/welfare/text()').extract_first()
        item['jobtag'] = selector.xpath('/responsemessage/resultbody/jobtag/text()').extract_first()
        item['providesalary'] = selector.xpath('/responsemessage/resultbody/providesalary/text()').extract_first()
        item['language1'] = selector.xpath('/responsemessage/resultbody/language1/text()').extract_first()
        item['language2'] = selector.xpath('/responsemessage/resultbody/language2/text()').extract_first()
        item['cotype'] = selector.xpath('/responsemessage/resultbody/cotype/text()').extract_first()
        item['cosize'] = selector.xpath('/responsemessage/resultbody/cosize/text()').extract_first()
        item['indtype1'] = selector.xpath('/responsemessage/resultbody/indtype1/text()').extract_first()
        item['indtype2'] = selector.xpath('/responsemessage/resultbody/indtype2/text()').extract_first()
        item['caddr'] = selector.xpath('/responsemessage/resultbody/caddr/text()').extract_first()
        item['jobterm'] = selector.xpath('/responsemessage/resultbody/jobterm/text()').extract_first()
        item['jobinfo'] = selector.xpath('/responsemessage/resultbody/jobinfo/text()').extract_first()
        item['isapply'] = selector.xpath('/responsemessage/resultbody/isapply/text()').extract_first()
        item['url'] = selector.xpath('/responsemessage/resultbody/share_url/text()').extract_first()
        yield item

