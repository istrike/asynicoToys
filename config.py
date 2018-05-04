import os

settings = dict(
    debug=True,  # 设置debug启动方式
    template_path=os.path.join(os.path.dirname(__file__), "templates"),  # 设置模板路径
    static_path=os.path.join(os.path.dirname(__file__), "static"),  # 设置静态文件路径
    cookie_secret="aaa",
    xscf_cookies=True
)
