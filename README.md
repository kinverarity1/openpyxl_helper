# openpyxl_helper

This provides access to all openpyxl functionality:

```python
>>> import openpyxl_helper as openpyxl
```

With the addition of a function that loads a worksheet as a pandas DataFrame, ignoring hidden rows:

```python
>>> df = openpyxl.load_worksheet("blah.xlsx")
```

That's it.