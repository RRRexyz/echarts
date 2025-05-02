from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.commons.utils import JsCode

cities = [
    '南京市',
    '上海市',
    '无锡市',
    '常州市',
    '徐州市',
    '济南市',
    '淄博市',
    '泰安市',
    '临沂市',
    '青岛市',
    '威海市',
    '烟台市',
    '北京市',
    '天津市',
    '沈阳市',
    '哈尔滨市',
    '秦皇岛市'
]

values = [1] * len(cities)

c = (
    Map()
    .add(series_name="旅行足迹", 
        data_pair=[list(z) for z in zip(cities, values)],
        maptype="china-cities",
        label_opts=opts.LabelOpts(is_show=True,
            position="insideBottom",
            formatter=JsCode(
                f"function(params) {{ if ({cities}.includes(params.name)) {{ return params.name; }} else {{ return ''; }} }}") 
        ),
        center=[121, 39],
        zoom=3.5
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="旅行足迹图"),
        legend_opts=opts.LegendOpts(is_show=False),
        visualmap_opts=opts.VisualMapOpts(is_show=False)
    )
    .render("旅行足迹图.html")
)