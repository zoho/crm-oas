### `application/json` — BasicFieldUpdate

Example of updating a single field across multiple records.

```json
{
  "data": [
    {
      "Venue": "Estancia"
    }
  ],
  "ids": [
    "1990117000035808053",
    "1990117000035808020"
  ]
}
```

### `application/json` — NestedObjectUpdate

An example of updating fields that reference nested objects.

```json
{
  "data": [
    {
      "Pipeline": "1990117000027199960",
      "Stage": "Value Proposition",
      "Layout": {
        "id": "1990117000000095023",
        "display_label": "Standard"
      }
    }
  ],
  "ids": [
    "1990117000035107169"
  ]
}
```

### `application/json` — CvidUpdate

An example of scheduling an asynchronous mass update using a Custom View.

```json
{
  "data": [
    {
      "Age": "12121"
    }
  ],
  "cvid": "1990117000000091529"
}
```
