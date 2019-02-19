# -*- coding=utf-8 -*-
__author__ = 'ouyangweibiao'
__mail__ = 'iishappyabu@163.com'

# 创建视图类
from tornado.web import Application, RequestHandler

class Pagination(object):
    def __init__(self, current_page, items_per_page, items):
        try:
            current_page = int(current_page)
            assert current_page > 0
            assert current_page < len(items)
        except:
            current_page = 1
        self.current_page = current_page
        self.items = items
        self.per_page = items_per_page

    @property
    def start_item(self):
        # 设若有n个元素，每页显示a个，则第x页的元素列表就是
        # 前一页的最后一个元素是第(x-1)*a个元素，下一个就是第[(x-1)*a]+1个元素，序号就是(x-1)*a
        return (self.current_page - 1) * self.per_page

    @property
    def end_item(self):
        # 当前页的最后一个元素是第ax个，序号就是ax-1,但因为切片操作留头切尾，因此还要再+1，结果就是ax
        return self.current_page * self.per_page

    # Create page numbers
    def get(self, base_url=''):
        actual_pages, _remainder = divmod(len(self.items), self.per_page)
        actual_pages += 1 if _remainder > 0 else 0

        start = self.current_page - 5
        end = self.current_page + 5

        # 防止页码变成负数，以及大于实际页数
        # 这里的条件限制类似放大镜那一节防止超出边界时的设置
        # 这里用到了多重赋值和三元运算符
        # 多重赋值本质就是tuple packing(元组打包)和 Sequence unpacking(序列解包)
        # A = Y if X else Z
        # 只有当X为真时才会执行表达式Y，而只有当X为假时，才会执行表达式Z
        start, end = (1, 10) if start <= 0 else (start, end)
        start, end = (end-10, actual_pages) if end >= actual_pages else (start, end)

        pages_list = []

        # 首页标签
        first_page = '<a href="%s/1">首页</a>' % base_url
        # 上一页标签
        prev_page = '<a href="%s/%s">上一页</a>' % (base_url, self.current_page - 1 if self.current_page > 1 else self.current_page )

        pages_list.append(first_page+prev_page)
        for _ in range(start, end + 1):
            if _ == self.current_page:
                _str = '<a class="active" href="%s/%s">%s</a>' % (base_url, _, _)
            else:
                _str = '<a href="%s/%s">%s</a>' % (base_url, _, _)
            pages_list.append(_str)

        # 下一页标签
        next_page = '<a href="%s/%s">下一页</a>' % (base_url, self.current_page + 1 if self.current_page < actual_pages else self.current_page)
        # 尾页标签
        last_page = '<a href="%s/%s">首页</a>' % (base_url, actual_pages)
        pages_list.append(next_page+last_page)

        # 跳转标签和输入框
        # 注意嵌套情况下引号的使用：onclick后的引号,其参数的引号
        # 注意js的形参不能是已占用的关键字this
        jump = """<input type='text'/><a onclick="Jump('%s',this);">跳转</a>""" % base_url
        script = """<script>
            function Jump(base_url, ths){
                val = ths.previousElementSibling.value;
                if(val.trim().length>0){
                    location.href=base_url + "/" + val;
                }
            }
        </script>"""
        pages_list.append(jump+script)

        pages = ''.join(pages_list)
        return pages


INFO_LIST = [
    {'name': 'yeff', 'age': '23'},
]
for i in range(99):
    INFO_LIST.append({
        'name': 'a'+str(i), 'age': '0'+str(i)
    })
# 创建视图类
class IndexHandler(RequestHandler):

    def initialize(self, ):
        '''
            覆盖父类的initialize方法
        '''
        # self.objPool = objPool
        pass

    def set_extra_headers(self, path):
        self.set_header("Cache-control", "no-cache")

    def get(self,):
        msg = "好看的皮囊千篇一律，有趣的灵魂万里挑一。"
        kwargs = {"info": msg}
        self.render("demo.html",**kwargs)
        # fun = self.get_argument('fun', default='default', strip=True)
        # if fun == '':
        #     self.list()
        # else:
        #     eval('self.' + fun + '()')

    def list(self,):
        page = self.get_argument('page',default=1,strip=True)
        pn = Pagination(page, 5, INFO_LIST)
        str_pages = pn.get('/index')
        display_list = pn.items[pn.start_item:pn.end_item]
        self.render("home/index.html", info_list=display_list, current_page=page, page_nums=str_pages)
        # fun = self.get_argument('fun', default='default', strip=True)
        # h = self.get_argument('h', default='index', strip=True)
        self.default()

    def post(self,):
        fun = self.get_argument('fun', default='default', strip=True)
        if fun == '':
            self.list()
        else:
            eval('self.' + fun + '()')

    def default(self,):
         msg = "好看的皮囊千篇一律，有趣的灵魂万里挑一。"
         kwargs = {"info":msg}
         self.render("demo.html")