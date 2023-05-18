# **Overview**
This is a python library that has some tools to decode hypixel item and inventory data. There are also some extra tools to retrieve the data (such as the items in an inventory) easier and faster.

# **Usage**
## **Decoding**
```python
hynbt.decode(data) # returns a nbt decoded object.
```

```python
hynbt.pretty(nbt) # returns a string displaying the tree of the nbt data
```

```python
hynbt.prettydecode(data) # both functions above but merged
```

## **Inventories**
```python
hynbt.invItemList(inv) # returns a list of the item ids in the inventory
```

## **Encoding**
\>> Not finished <<
