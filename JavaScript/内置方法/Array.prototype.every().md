# <center> Array.prototype.every()

`every()` 方法测试一个数组内的所有元素是否都能通过指定函数的测试。它返回一个布尔值。
```javascript
const isBelowThreshold = (currentValue) => currentValue < 40;

const array1 = [1, 30, 39, 29, 10, 13];

console.log(array1.every(isBelowThreshold));
// Expected output: true
```
<hr>

## 语法
```javascript
every(callbackFn)
every(callbackFn, thisArg)
```

### 参数
`callbackFn`
为数组中的每个元素执行的函数。它应该返回一个真值以指示元素通过测试，否则返回一个假值。该函数被调用时将传入以下参数：

`element`
数组中当前正在处理的元素。

`index`
正在处理的元素在数组中的索引。

`array`
调用了 every() 的数组本身。

`thisArg` 可选
执行 callbackFn 时用作 this 的值。参见迭代方法。

### 返回值
如果 `callbackFn` 为每个数组元素返回真值，则为 `true`。否则为 `false`。

<hr>

## 描述

`every()` 方法是一个迭代方法。它为数组中的每个元素调用一次指定的 `callbackFn` 函数，直到 `callbackFn` 返回一个假值。如果找到这样的元素，`every()` 方法将会立即返回 `false` 并停止遍历数组。否则，如果 callbackFn 为每个元素返回一个真值，`every()` 就会返回 `true`。

`every` 和数学中的全称量词"任意（∀）"类似。特别的，对于空数组，它只返回 `true`。（这种情况属于无条件正确，因为空集的所有元素都符合给定的条件。）

`callbackFn` 仅针对已分配值的数组索引调用。它不会为稀疏数组中的空槽调用。

`every()` 不会改变调用它的数组，但指定的 `callbackFn` 函数可以。但是请注意，数组的长度是在第一次调用 `callbackFn` 之前保存的。所以：

- 当开始调用 `every()` 时，`callbackFn` 将不会访问超出数组初始长度的任何元素。

- 对已访问索引的更改不会导致再次在这些元素上调用 `callbackFn`。
  
- 如果数组中一个现有的、尚未访问的元素被 `callbackFn` 更改，则它传递给 `callbackFn` 的值将是该元素被修改后的值。被删除的元素则不会被访问。

> 警告： 上述类型的并发修改经常导致难以理解的代码，通常应避免（特殊情况除外）。

`every()` 方法是通用的。它只期望 `this` 值具有 `length` 属性和整数键属性。

<hr>

## 示例                                                                                                                  