### `application/json` — UpdateDisplayLabel

Update display label

```json
{
  "global_picklists": [
    {
      "id": "111111000000055935",
      "display_label": "Updated Priority Level"
    }
  ]
}
```

### `application/json` — AddPicklistValue

Add new picklist value

```json
{
  "global_picklists": [
    {
      "id": "111111000000055935",
      "pick_list_values": [
        {
          "display_value": "Critical",
          "type": "used"
        }
      ]
    }
  ]
}
```

### `application/json` — UpdatePicklistValue

Update existing picklist value

```json
{
  "global_picklists": [
    {
      "id": "111111000000055935",
      "pick_list_values": [
        {
          "id": "111111000000055938",
          "display_value": "High Priority"
        }
      ]
    }
  ]
}
```

### `application/json` — MoveToUnused

Move one value to unused

```json
{
  "global_picklists": [
    {
      "id": "111111000000055935",
      "pick_list_values": [
        {
          "id": "111111000000055938",
          "type": "unused"
        }
      ]
    }
  ]
}
```

### `application/json` — DeletePicklistValue

Delete one picklist value

```json
{
  "global_picklists": [
    {
      "id": "111111000000055935",
      "pick_list_values": [
        {
          "id": "111111000000055938",
          "_delete": true
        }
      ]
    }
  ]
}
```
