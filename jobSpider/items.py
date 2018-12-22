# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class qcwyJobsItem(scrapy.Item):
    jobid = scrapy.Field()
    jobname = scrapy.Field()
    coid = scrapy.Field()
    coname = scrapy.Field()
    issuedate = scrapy.Field()
    jobarea = scrapy.Field()
    jobnum = scrapy.Field()
    degree = scrapy.Field()
    jobareacode = scrapy.Field()
    cityname = scrapy.Field()
    funtypecode = scrapy.Field()
    funtypename = scrapy.Field()
    workyearcode = scrapy.Field()
    address = scrapy.Field()
    joblon = scrapy.Field()
    joblat = scrapy.Field()
    welfare = scrapy.Field()
    jobtag = scrapy.Field()
    providesalary = scrapy.Field()
    language1 = scrapy.Field()
    language2 = scrapy.Field()
    cotype = scrapy.Field()
    cosize = scrapy.Field()
    indtype1 = scrapy.Field()
    indtype2 = scrapy.Field()
    caddr = scrapy.Field()
    jobterm = scrapy.Field()
    jobinfo = scrapy.Field()
    isapply = scrapy.Field()
    url = scrapy.Field()

    def get_insert_sql(self):
        """
        执行具体的插入
        :param cursor:
        :param item:
        :return:
        """
        insert_sql = """
                        insert into qcwy_job(
                         jobid ,jobname ,coid ,coname ,issuedate ,jobarea ,jobnum ,degree ,jobareacode ,cityname ,
                        funtypecode ,funtypename ,workyearcode ,address ,joblon ,joblat ,welfare ,jobtag ,providesalary ,
                        language1 ,language2 ,cotype ,cosize ,indtype1 ,indtype2 ,caddr ,jobterm ,jobinfo ,isapply ,url)
                        VALUES ( %s, %s, %s,%s , %s,  %s, %s, %s, %s, %s, %s, %s , %s, %s, %s,%s , %s,  %s, %s, %s, %s, %s, %s, %s,  %s, %s, %s, %s, %s, %s)
                        """
        param = (
            self['jobid'], self['jobname'], self['coid'], self['coname'], self['issuedate'],
            self['jobarea'], self['jobnum'], self['degree'], self['jobareacode'], self['cityname'],
            self['funtypecode'], self['funtypename'], self['workyearcode'], self['address'], self['joblon'],
            self['joblat'], self['welfare'], self['jobtag'], self['providesalary'], self['language1'],
            self['language2'],self['cotype'], self['cosize'], self['indtype1'], self['indtype2'], self['caddr'], self['jobterm'],
            self['jobinfo'], self['isapply'], self['url']
        )
        return insert_sql , param
