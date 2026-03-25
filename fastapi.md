### 1.启动

1. 导入 FastAPI。
2. 创建一个 app 实例。
3. 编写一个路径操作装饰器（如 `@app.get("/")`）。
4. 编写一个路径操作函数（如上面的 `def root(): ...`）
5. 定义返回值
6. 运行开发服务器（如 `uvicorn main:app --reload`）


### 2.路径操作装饰器

| 装饰器             | 对应的 HTTP 方法 | 作用说明                                                                 |
|--------------------|------------------|--------------------------------------------------------------------------|
| `@app.get()`       | GET              | 用于获取资源。通常用于查询数据，不应有副作用（不修改服务器状态）。         |
| `@app.post()`      | POST             | 用于创建新资源或提交数据到服务器。常用于表单提交、上传文件等。               |
| `@app.put()`       | PUT              | 用于**完整替换**指定资源。客户端需提供完整的资源表示，若不存在则可能创建。     |
| `@app.patch()`     | PATCH            | 用于**部分更新**资源。只发送需要更改的字段，比 PUT 更灵活高效。                |
| `@app.delete()`    | DELETE           | 用于删除指定资源。执行后该资源应不再存在。                                   |
| `@app.options()`   | OPTIONS          | 用于获取目标资源支持的通信选项（如允许的 HTTP 方法），常用于 CORS 预检请求。   |
| `@app.head()`      | HEAD             | 类似 GET，但只返回响应头，不返回响应体。常用于检查资源是否存在或获取元信息。     |
| `@app.trace()`     | TRACE            | 用于诊断目的，回显收到的请求消息，帮助调试代理或中间件行为。（较少使用）        |
### 3.include_router
include_router 是 FastAPI 框架中的一个核心方法，从字面上理解就是 “包含路由” 或 “导入路由模块”。



```
app.include_router(
    users_router,           # 要包含的路由模块
    prefix="/users",        # 给所有接口加上前缀
    tags=["用户管理"],       # 接口文档分组
    dependencies=[...],     # 给所有接口统一添加依赖
)
```

### 4.请求与响应


### 4.1.路径参数

#### 格式：
```markdown
from fastapi import FastAPI
app = FastAPI()
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}
```
#### 优先级

```markdown
@app.get("/users/1")
async def read_user_me():
    return {"user_id": "the current user"}
@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}
```
相同的后面会被前面的覆盖

### 4.2.查询参数
声明其他不属于路径参数的函数参数时，它们会自动被解释为“查询”参数。
```markdown
from fastapi import FastAPI
app = FastAPI()
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]
```
同时查询参数可以设置为默认选项

```markdown
from typing import Union, Optional
```
Union 是当有多种可能的数据类型时使用，比如函数有可能根据不同情况有时返回 str 或返回 list，那么就可以写成 `Union[list, str]`

Optional 是 Union 的一个简化，当数据类型中有可能是 None 时，比如有可能是 str 也有可能是 None，则 `Optional[str]`，相当于 `Union[str, None]`

### 4.3请求体数据
```markdown
from fastapi import FastAPI
from pydantic import BaseModel
class Item(BaseModel):
    name: str
    description: str  = None
    price: float
    adds:str
app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    return item
```
或者使用下面的方式，对字段进行校验：
```markdown
@felid_validator("name")
def name_must_alpha(cls, value):
    assert value.isalpha(), 'name must be alpha'
    return value
```
或者使用组合嵌套的方式，再定义一个：
```markdown
class Adds(BaseModel):
    province:str
    city:str


```
(adds中有两个字段)


### 4.4 form表单数据
```markdown
from fastapi import Form
app04= APIRouter()
@app04.post("/regin")
def user(username:str=Form(),password:str=Form()):
    print(f"username:{username},password:{password}")
    return {"username":username
    }
 
```

### 4.5 文件上传  
```markdown
from fastapi import File
app05= APIRouter()
@app05.post("/file")
def get_file(file:bytes=File()):
#def get_files(files:List[bytes]=File()):
    return {"file":"file"
    }
```

```markdown
from fastapi import File,UploadFile(文件句柄）
@app05.post("/uploadFile")
def get_files(file:UploadFile):
#def get_files(file:[UploadFile]):
    print("file",file)
    return {"file":file.filename
    }
```

### 4.6 request对象
```markdown
from fastapi import Request

@app.get("/items")
async def items(request: Request):
    return {
        "请求URL": request.url,
        "请求IP": request.client.host,
        "请求宿主": request.headers.get("user-agent"),
        "Cookies": request.cookies,
    }
```
### 4.7 静态文件请求
在 Web 开发中，需要请求很多静态资源文件（不是由服务器生成的文件），如 css/js 和图片文件等。
python
```
from fastapi.staticfiles import StaticFiles
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"))
```
### 4.8响应模型参数
1. `response_model`  
FastAPI将使用 `response_model` 进行以下操作：
- 将输出数据转换为 `response_model` 中声明的数据类型。
- 验证数据结构和类型
- 将输出数据限制为该model定义的


2. 'response_model_exclude_unset'
如果没有此个参数，则 `response_model` 中声明的字段将返回给客户端，即使它们为空。
但添加了此参数，则 `response_model` 中声明的字段不会全部返回给客户端，只返回输入的字段。

> 除了 `response_model_exclude_unset` 以外，还有 `response_model_exclude_defaults` 和 `response_model_exclude_none`，我们可以很直观的了解到的意思，不返回是默认值的字段和不返回是None的字段。


### 5.jinja2模板

### 5.1变量渲染

```markdown
from fastapi.templating import   Jinja2Templates
from fastapi import Request
app = FastAPI()
templates = Jinja2Templates(directory="templates")
@app.get("/index")
def index(request:Request):
    name = "root"
    return templates.TemplateResponse(
        "index.html",
        {
            "request":request,
            "user":name,
            "age":32
        }
    )

```

### 5.2过滤器

在模板中，我们可以使用过滤器对数据进行格式化。
在html文件中，使用 `{{变量 | 过滤器}}`

#### 常见过滤器
| 过滤器名称 | 说明 |
| --- | --- |
| capitalize | 把值的首字母转换成大写，其他子母转换为小写 |
| lower | 把值转换成小写形式 |
| title | 把值中每个单词的首字母都转换成大写 |
| trim | 把值的首尾空格去掉 |
| striptags | 渲染之前把值中所有的HTML标签都删掉 |
| join | 拼接多个值为字符串 |
| round | 默认对数字进行四舍五入，也可以用参数进行控制 |
| safe | 渲染时值不转义 |

### 5.3控制结构
分支语句在模板中，使用 `{% if %}`
for循环在模板中，使用 `{% for %}`
> 注意： `{% %}` 是控制结构， `{{}}` 是变量渲染。在html 文件中修改

### 6 OMR操作

### 6.1 创建模型类



### 6.2 ORM的迁移命令
1. 初始化配置   
```aerich init -t settings.TORTOISE_ORM```

2. 初始化数据库  
```aerich init-db```

3. 更新模型并进行迁移  
```aerich migrate```   
4. 重新执行迁移，写入数据库
```aerich upgrade```  

5. 回到上一个版本
```aerich downgrade``` 
6. 查看历史迁移记录
```aerich history```










