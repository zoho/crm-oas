### `application/json` — UpdateDisplayLabel

Update display label

```json
{
  "global_picklists": [
    {
      "display_label": "Updated Priority Level"
    }
  ]
}
```

### `application/json` — UpdateApiName

Update API name

```json
{
  "global_picklists": [
    {
      "api_name": "updated_priority_level__s"
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
