
from spider import url_manager,html_downloader,html_parser,html_outputer

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutput()
        
    
    def craw(self,root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d :%s' %(count,new_url)
                html_cont = self.downloader.download(new_url)
                new_urls,new_data = self.parser.parse(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == 1000:
                    break
                count = count + 1
            except Exception as err:
                print(err)
                print 'craw failed'
            
        self.outputer.output_html()


if __name__ == '__main__':
    root_url = "https://baike.baidu.com/item/%E6%B9%96%E5%8D%97%E6%B6%89%E5%A4%96%E7%BB%8F%E6%B5%8E%E5%AD%A6%E9%99%A2"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)