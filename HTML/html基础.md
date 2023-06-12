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
