# <center>  Array.prototype.concat() 

`concat()` 方法用于合并两个或多个数组。此方法不会更改现有数组，而是返回一个新数组。
```javascript
const array1 = ['a', 'b', 'c'];
const array2 = ['d', 'e', 'f'];
const array3 = array1.concat(array2);

console.log(array3);
// Expected output: Array ["a", "b", "c", "d", "e", "f"]

```
<hr>

## 语法
```javascript
concat();
concat(value0);
concat(value0, Value1);
concat(value0, value1, /* ...., */ valueN);
```

### 参数

`valueN`： 值/数组和，将合并到新的数组中。如果省略所有的`valueN`参数，则`concat()`会返回调用此方法的现存数组的一个浅拷贝。

###  返回值
新的 `Array` 实例。

<hr>

## 描述
`concat` 方法创建一个新数组。该数组将首先由调用它的对象中的元素填充。然后，对于每个参数，它的值将被连接到数组中——对于普通对象或基元，参数本身将成为最终数组的一个元素；对于属性`Symbol.isConcatSpreadable`设置为真的数组或类数组对象，参数的每个元素都将是独立地添加到最终数组中。`concat` 方法不会递归到嵌套数组参数中。

`concat()` 方法是一种复制方法。它不会更改 `this` 或作为参数提供的任何数组，而是返回包含与原始数组中的元素相同的元素的浅拷贝。

如果任何源数组是稀疏数组，`concat()` 方法会保留空槽。

`concat()` 方法是通用的。`this` 值的处理方式与其他参数相同（除了它会先转换为对象），这意味着普通对象将直接添加到结果数组中，而 `@@isConcatSpreadable` 属性为真值的类数组对象将展开并添加到数组中。

<hr>

## 示例

### 连接两个数组
以下代码将两个数组合并为一个新数组：

```javascript
const letters = ["a", "b", "c"];
const numbers = [1, 2, 3];

const alphaNumeric = letters.concat(numbers);
console.log(alphaNumeric);
// results in ['a', 'b', 'c', 1, 2, 3]
```

### 连接三个数组
以下代码将三个数组合并为一个新数组：

```javascript
const num1 = [1, 2, 3];
const num2 = [4, 5, 6];
const num3 = [7, 8, 9];

const numbers = num1.concat(num2, num3);

console.log(numbers);
// results in [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### 将值连接到数组
以下代码将三个值连接到数组：

```javascript
const letters = ["a", "b", "c"];

const alphaNumeric = letters.concat(1, [2, 3]);

console.log(alphaNumeric);
// results in ['a', 'b', 'c', 1, 2, 3]
```

### 合并嵌套数组
以下代码合并数组并保留引用：

```javascript
const num1 = [[1]];
const num2 = [2, [3]];

const numbers = num1.concat(num2);

console.log(numbers);
// [[1], 2, [3]]

// 修改 num1 的第一个元素
num1[0].push(4);

console.log(numbers);
// [[1, 4], 2, [3]]
```

### 使用 Symbol.isConcatSpreadable 合并类数组对象
`concat` 默认情况下不会将类数组对象视作数组——仅在 Symbol.`isConcatSpreadable` 被设置为真值（例如，true）时才会将类数组对象视作数组。

```javascript
const obj1 = { 0: 1, 1: 2, 2: 3, length: 3 };
const obj2 = { 0: 1, 1: 2, 2: 3, length: 3, [Symbol.isConcatSpreadable]: true };
console.log([0].concat(obj1, obj2));
// [ 0, { '0': 1, '1': 2, '2': 3, length: 3 }, 1, 2, 3 ]
```

### 在稀疏数组上使用 concat()
如果任何源数组是稀疏的，则结果数组也将是稀疏的：

```javascript
console.log([1, , 3].concat([4, 5])); // [1, empty, 3, 4, 5]
console.log([1, 2].concat([3, , 5])); // [1, 2, 3, empty, 5]
```
### 在非数组对象上调用 concat()
如果 `this` 值不是数组，它会被转换为一个对象，然后以与 `concat()` 的参数相同的方式处理。在这种情况下，返回值始终是一个普通的新数组。

```javascript
console.log(Array.prototype.concat.call({}, 1, 2, 3)); // [{}, 1, 2, 3]
console.log(Array.prototype.concat.call(1, 2, 3)); // [ [Number: 1], 2, 3 ]
const arrayLike = { [Symbol.isConcatSpreadable]: true, length: 2, 0: 1, 1: 2 };
console.log(Array.prototype.concat.call(arrayLike, 3, 4)); // [1, 2, 3, 4]
```
