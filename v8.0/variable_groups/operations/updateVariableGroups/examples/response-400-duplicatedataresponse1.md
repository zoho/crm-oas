Error response for duplicate variable group data

```json
{
  "variable_groups": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "name",
        "json_path": "$.variable_groups[0].name"
      },
      "message": "duplicate data",
      "status": "error"
    },
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "name",
        "json_path": "$.variable_groups[1].name"
      },
      "message": "duplicate data",
      "status": "error"
    }
  ]
}
```
