## HTML基础
### HTML标题
HTML 标题是通过`<h1> - <h6>`标签来定义的
`<h1>` 定义最大的标题。 `<h6>` 定义最小的标题
### HTML 段落
HTML 段落是通过标签`<p>`来定义的
### HTML 链接
- 语法
HTML 链接是通过标签`<a>`来定义的
`<a href="url">链接文本</a>`
- target属性
 使用 target 属性，你可以定义被链接的文档在何处显示
 下面的这行会在新窗口打开文档：
 `<a href="url" target="_blank" rel="noopener noreferrer">链接文本</a>`
- id属性
id 属性可用于创建一个 HTML 文档书签
```
在HTML文档中插入ID:
<a id="tips">有用的提示部分</a>
在HTML文档中创建一个链接到"有用的提示部分(id="tips"）"：
<a href="#tips">访问有用的提示部分</a>
或者，从另一个页面创建一个链接到"有用的提示部分(id="tips"）"
<a href="https://www.runoob.com/html/html-links.html#tips">
访问有用的提示部分</a>
```
  
>提示："链接文本" 不必一定是文本。图片或其他 HTML 元素都可以成为链接
### HTML 图像
HTML 图像是通过标签`<img>`来定义的
`<img decoding="async" src="/images/logo.png" width="258" height="39" />`
### HTML 水平线
`<hr>` 标签在 HTML 页面中创建水平线
### HTML 注释
`<!-- 这是一个注释 -->`
### HTML 折行
如果您希望在不产生一个新段落的情况下进行换行（新行），请使用 `<br>` 标签
`<p>这个<br>段落<br>演示了分行的效果</p>`

<hr>

## HTML属性
|属性|描述|
|---|---|
|class|规定元素的类名（classname）(类名从样式文件引入)|
|id|规定元素的唯一 id|
|style|规定元素的行内样式|
|title|规定元素的额外信息|
|accesskey|设置访问元素的键盘快捷键|
|hidden|hidden 属性规定对元素进行隐藏|

<hr>

## HTML 文本格式化
### HTML 文本格式化标签
|标签|描述|
|---|---|
|`<b>`|定义粗体文本|
|`<em>`|定义着重文字|
|`<i>`|定义斜体字|
|`<small>`|定义小号字|
|`<strong>`|定义加重语气|
|`<sub>`|定义下标字|
|`<ins>`|定义插入字|
|`<del>`|定义删除字|

### HTML "计算机输出" 标签
|标签|	|描述|
|----|----|
|`<code>`|	定义计算机代码|
|`<kbd>`	|定义键盘码|
|`<samp>`|定义计算机代码样本|
|`<var>`	|定义变量|
|`<pre>`	|定义预格式文本|

### HTML 引文, 引用, 及标签定义\
|标签|描述|
|---|---|
|`<abbr>`|定义缩写|
|`<address>`|定义地址|
|`<bdo>`|定义文字方向|
`<blockquote>`|定义长的引用|
`<q>`|定义短的引用语|
`<cite>`|定义引用、引证|
`<dfn>`|定义一个定义项目|

<hr>

## HTML 头部
HTML <head> 元素
`<head>`元素包含了所有的头部标签元素。在`<head>`元素中你可以插入脚本（scripts）, 样式文件（CSS），及各种meta信息。

可以添加在头部区域的元素标签为: `<title>`, `<style>`, `<meta>`, `<link>`, `<script>`,  `<noscript>` 和 `<base>`。

### HTML`<title>`元素
`<title>` 标签定义了不同文档的标题。
`<title>` 在 HTML/XHTML 文档中是必需的。
`<title> `元素:
  - 定义了浏览器工具栏的标题
  - 当网页添加到收藏夹时，显示在收藏夹中的标题
  - 显示在搜索引擎结果页面的标题
### HTML`<base>`元素
`<base>`标签描述了基本的链接地址/链接目标，该标签作为HTML文档中所有的链接标签的默认链接:
```
<head>
<base href="http://www.runoob.com/images/" target="_blank">
</head>
```
### HTML`<link>`元素
`<link>`标签定义了文档与外部资源之间的关系。
`<link>`标签通常用于链接到样式表:
```
<head>
<link rel="stylesheet" type="text/css" href="mystyle.css">
</head>
```
### HTML`<style>`元素
`<style>`标签定义了HTML文档的样式文件引用地址.
在`<style>`元素中你也可以直接添加样式来渲染 HTML 文档
```
<head>
<style type="text/css">
body {
    background-color:yellow;
}
p {
    color:blue
}
</style>
</head>
```

### HTML`<meta>`元素
meta标签描述了一些基本的元数据。
`<meta>`标签提供了元数据.元数据也不显示在页面上，但会被浏览器解析。
META 元素通常用于指定网页的描述，关键词，文件的最后修改时间，作者，和其他元数据。
元数据可以使用于浏览器（如何显示内容或重新加载页面），搜索引擎（关键词），或其他Web服务。
`<meta>` 一般放置于 `<head>`区域

**`<meta>`标签- 使用实例**

- 为搜索引擎定义关键词:
`<meta name="keywords" content="HTML, CSS, XML, XHTML, JavaScript">`
- 为网页定义描述内容:
`<meta name="description" content="免费 Web & 编程 教程">`
- 定义网页作者
`<meta name="author" content="Runoob">`
- 每30秒钟刷新当前页面
`<meta http-equiv="refresh" content="30">`

### HTML`<script>`元素
`<script>`标签用于加载脚本文件，如： JavaScript。
`<script>`元素在以后的章节中会详细描述。