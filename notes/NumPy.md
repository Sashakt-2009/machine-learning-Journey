
# NumPy

## **Array:** a table of elements (usually numbers), all of the same type, indexed by a tuple of non-negative integers. In NumPy dimensions are called axes

### 1D array

`[1,2,4]`

### 2D array

```python
[[1,2,3],
 [3,4,4]]
  ```

- NumPy’s array class is called `ndarray`.
- In NumPy a multidimensional array's index can be understood as **`(..., n, r, c)`** where the last index is column, second to last index is row and so on. Or abetter way to understand is th first index is the fastest changing then is the second index, then second to last index changes second to last and the last index changes the last

### Important attributes of an `ndarray`

1. **ddarray.ndim:** number of dimensions of array

2. **ndarray.shape:** This is a tuple of integers indicating the size of the array in each dimension. For a matrix with n rows and m columns, shape will be `(n,m)`

3. **ndarray.size:** total no of elements in array. Product od elements of `shape`

## **Array creation:**

```python
a = np.array([[1, 2, 3],
              [4, 5, 6]])
a.shape

>>> (2, 3)
```

*Most NumPy arrays have some restrictions. For instance:*

- All elements of the array must be of the same type of data.

- Once created, the total size of the array can’t change.

- The shape must be “rectangular”, not “jagged”; e.g., each row of a two-dimensional array must have the same number of columns.

## Array Basics

```python
a = np.array([1, 2, 3, 4, 5, 6])
a

>>> array([1, 2, 3, 4, 5, 6])
```

- we can access an individual element of this array as we would access an element in the original list: using the integer index of the element within square brackets.

```python
a[0]

>>> 1
```

the first element of the array is accessed using index 0, not 1

- *Besides creating an array from a sequence of elements, you can easily create an array filled with `0`’s:*

```python
np.zeros(2)
>>> array([0., 0.])
```

- *Or an array filled with `1`’s:*

```python
np.ones(2)
>>> array([1., 1.])
```

- *The function empty `creates` an array whose initial content is random and depends on the state of the memory. The reason to use `empty` over `zeros` (or something similar) is speed:*

```python
# Create an empty array with 2 elements
np.empty(2) 
>>> array([3.14, 42.  ])  # may vary
```

- *You can create an array with a range of elements:*

```python
np.arange(4)
>>> array([0, 1, 2, 3])
```

- *And even an array that contains a range of evenly spaced intervals. To do this, you will specify the first `number, last number, and the step size`:*

```python
np.arange(2, 9, 2)
>>> rray([2, 4, 6, 8])
```

You can also use `np.linspace()` to create an array with values that are spaced linearly in a specified interval:

```python
np.linspace(0, 10, num=5)
>>> array([ 0. ,  2.5,  5. ,  7.5, 10. ])
```

### Specifying your `data type`

While the default data type is floating point `(np.float64)`, you can explicitly specify which data type you want using the `dtype` keyword.

```python
x = np.ones(2, dtype=np.int64)
x
array([1, 1])
```

## Adding, Removing, and Sorting Elements

- **Sorting:** Use `np.sort()` to return a sorted copy of an array in *ascending order*
Other advanced sorting functions include `argsort` (indirect sort), `lexsort` (sort on multiple keys), `searchsorted` (find elements in a sorted array), and `partition`(partial sort)

- **Concatenating:** You can join two or more existing arrays using `np.concatenate()`

- **Removing Elements:** It is simplest to use **indexing** to select only the elements you want to keep

## Reshaping and Dimensionality

**Reshaping:** The `arr.reshape()` method gives an array a new shape without changing its data
The new shape must have the same total number of elements as the original

**Adding Axes:** You can increase the dimensions of an array *(e.g., converting a 1D array to a 2D row or column vector)* using:
`np.newaxis`: Increases dimensions by one each time it is used

**`np.expand_dims`:** Inserts a new axis at a specified index position

## Advanced Indexing and Slicing

**Boolean Indexing:** You can select values that fulfill specific conditions, such as `a[a < 5]` or using logical operators like `& (and)` and `| (or)` to filter complex criteria

**`np.nonzero()`:** This function *returns the indices* of elements that are **non-zero or meet a specific condition**

## Creating Arrays from Existing Data

**Stacking:** Combine arrays *vertically* using `np.vstack()` or *horizontally* using `np.hstack()`

**Splitting:** Use `np.hsplit()` to split an array into several smaller arrays, either by specifying the number of equal-sized arrays or the columns where the split should occur

## Views vs. Copies

**Views (Shallow Copy):** Created by *slicing or the `.view()` method*; they refer to the **same memory as the original array**. Modifying a view will change the original array

**Copies (Deep Copy):** Created using the `.copy()` method; this creates a **completely new array** with its own data

## Basic Operations and Broadcasting

**Arithmetic:** You can perform addition, subtraction, and multiplication directly between arrays of the same size

**Broadcasting:** This mechanism allows NumPy to perform operations on *arrays of different shapes*, provided their dimensions are compatible (e.g., when one dimension is 1)

**Aggregations:** NumPy provides functions like `sum()`, `min()`, `max()`, `mean()`, `prod()`, `(product)`, and `std()` (standard deviation)
You can perform these on the *entire array or specify an axis* to aggregate across rows or columns

## Transposing and Reversing

**Transposing:** Use `arr.T` or `arr.transpose()` to reverse or *change the axes* of a matrix

**Reversing:** `np.flip()` allows you to *reverse the contents of an array* along one or all axes

## Note: For more details on specific parts or other functions, methods visit [NumPY](https://numpy.org/doc/2.3/user/absolute_beginners.html)
