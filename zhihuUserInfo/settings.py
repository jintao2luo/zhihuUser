# -*- coding: utf-8 -*-

# Scrapy settings for zhihuUserInfo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihuUserInfo'

SPIDER_MODULES = ['zhihuUserInfo.spiders']
NEWSPIDER_MODULE = 'zhihuUserInfo.spiders'


# # Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = {
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
# }

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
  'authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhihuUserInfo.middlewares.ZhihuuserinfoSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'zhihuUserInfo.middlewares.ZhihuuserinfoDownloaderMiddleware': 543,
#}

DOWNLOADER_MIDDLEWARES = {
    'zhihuUserInfo.middlewares.ProxyMiddleware': 100,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 130,
    # 'zhihuUserInfo.middlewares.RandomUserAgentMiddleware': 543,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'zhihuUserInfo.pipelines.MongoPipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 301,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

RETRY_ENABLED = True
RETRY_TIMES = 5

# 启动scrapy_redis的调度器，不适用默认的
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

#启用去重功能，scrapy爬虫里面利用yield生成器返回待访问的URL，将他们放进队列，
# 爬虫会进去队列领取URL进行爬取，启用该功能后，每个放进去的URL都会先经过去重，
# 里面爬取过的URL也会在redis数据库里面贴上唯一的指纹，防止下次爬取一样的URL，
# 也就是为了以后进来新的URL进行去重。
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# 链接乌班图系统里面的redis数据，之前的链接指纹，返回的item数据都会自动储存在该数据库，
# 当然必须启动如图这个pipline
REDIS_URL = ''  # 此处修改为你需要存储的redis地址，‘redis://user:pwd@IP:port’

# RANDOM_UA_TYPE = 'random'
LOG_LEVEL = 'INFO'
DOWNLOAD_TIMEOUT = 15
# CLOSESPIDER_TIMEOUT = 600

MONGO_URI = 'localhost'
MONGO_DATABASE = 'zhihu'
MONGO_USERNAME = ''
MONGO_PWD = ''

# USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
# USER_AGENT_LIST = 'useragents.txt'