### `application/json` — MultipleIds

An example of mass delete operation using multiple record IDs.

```json
{
  "ids": [
    "1990117000035827873",
    "1990117000035107169",
    "1990117000035107158",
    "1990117000035107147",
    "1990117000035107136",
    "1990117000035107125",
    "1990117000035107114",
    "1990117000035107103",
    "1990117000035107092",
    "1990117000035107081"
  ]
}
```

### `application/json` — CVIDAndTerritory

An example of mass delete operation using Custom View ID and territory filter.

```json
{
  "cvid": "3652397000000538003",
  "territory": {
    "id": "3652397000007622003",
    "include_child": true
  }
}
```
