# <center> Array.prototype.map() 
map() 方法**创建一个新数组**，这个新数组由原数组中的每个元素都调用一次提供的函数后的返回值组成。

```javascript
const array1 = [1, 4, 9, 16];

// Pass a function to map
const map1 = array1.map((x) => x * 2);

console.log(map1);
// Expected output: Array [2, 8, 18, 32]

```

<hr>

## 语法
```javascript
map(callbackFn)
map(callbackFn, thisArg)
```
### 参数
`callbackFn`
为数组中的每个元素执行的函数。它的返回值作为一个元素被添加为新数组中。该函数被调用时将传入以下参数：

>`element`
数组中当前正在处理的元素。
>
>`index`
正在处理的元素在数组中的索引。
>
>`array`
调用了 `map()` 的数组本身。

`thisArg` 可选
执行 `callbackFn` 时用作 t`his` 的值。参见迭代方法。

### 返回值
执行 `callbackFn` 时用作 `this` 的值。参见迭代方法。

<hr>

## 描述
