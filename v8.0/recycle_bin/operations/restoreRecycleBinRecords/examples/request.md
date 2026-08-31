### `application/json` — RestoreByIds

Restore specific records by IDs

```json
{
  "ids": [
    "111111000000077729",
    "111111000000077734"
  ]
}
```

### `application/json` — RestoreByFilters

Restore records matching filter criteria

```json
{
  "filters": {
    "group_operator": "AND",
    "group": [
      {
        "field": {
          "api_name": "display_name"
        },
        "comparator": "contains",
        "value": "Amazon Marketplace"
      },
      {
        "field": {
          "api_name": "module"
        },
        "comparator": "equal",
        "value": "Leads"
      }
    ]
  }
}
```

### `application/json` — RestoreAll

Restore all records

```json
{
  "restore_all_records": true
}
```
