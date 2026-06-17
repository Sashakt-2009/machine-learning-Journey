
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

### Important attributes of an `ndarray`

1. **ddarray.dim:** number of dimensions of array

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

we can access an individual element of this array as we would access an element in the original list: using the integer index of the element within square brackets.

```python
a[0]

>>> 1
```

the first element of the array is accessed using index 0, not 1


