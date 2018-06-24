__author__ = 'Jonny'

#架构一个网站，利用轻量级的tornato实现

from tornado import web,ioloop,httpserver
from baiduImgOCR import get_img_word

class MainPageHandler(web.RequestHandler):
    def get(self,*args,**kwargs):
        #self.write('测试网页！')
        self.render('index.html')
    def post(self,*args,**kwargs):
        file = self.request.files.get('file')[0]
        # print('file = ')
        # print(file) #测试代码
        res = get_img_word(file['body'])
        # print('res = ')
        # print(res)  #测试代码
        self.render('result.html',content=res['words_result'])

# 设置而参数
setting = {
    # 设置模板路径
    'template_path':'template',
    'static_path':'static'
}
application = web.Application([
            (r"/index", MainPageHandler),
        ],**setting)
if __name__ =='__main__':
    http_server = httpserver.HTTPServer(application)
    http_server.listen(80)
    ioloop.IOLoop.current().start()
