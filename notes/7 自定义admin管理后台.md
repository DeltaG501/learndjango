# 7 自定义admin后台

> 概要：
>
> Django 依托ORM数据库，稍加配置 admin.py 即可实现强大的后台界面。秒杀 Flask！
>
> + 自定义 数据模型
>     + 显示的字段、顺序、表头
>     + 关系表格 Inline 显示
>     + 添加过滤器、搜索框
> + 自定义 界面风格

![image-20200706140830971](https://pic-1301887806.cos.ap-guangzhou.myqcloud.com/img/image-20200706140830971.png)





## 自定义数据模型

效果：

![2020-07-06_14-40-36](https://pic-1301887806.cos.ap-guangzhou.myqcloud.com/img/2020-07-06_14-40-36.gif)

polls/<u>admin</u>.py

```python
from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     ('Question',         {'fields': ['question_text']}),
    #     ('Date information', {'fields': ['pub_date'], 'classes':['collapse']}),
    # ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
```

逻辑：

![image-20200706140501227](https://pic-1301887806.cos.ap-guangzhou.myqcloud.com/img/image-20200706140501227.png)

## 自定义界面风格

1. 先在 settings.py 中修改 TEMPLATES 下 DIRS 的值为 `[os.path.join(BASE_DIR, 'templates')]`

2. 新建 admin 模板： polls/templates/**admin**/ , 复制 django/contrib/admin/templates 下的2个模板文件 base_site.html 和 index.html。修改 → 生效。

    ![image-20200706143123216](https://pic-1301887806.cos.ap-guangzhou.myqcloud.com/img/image-20200706143123216.png)

