Multi-status bulk update variable groups response

```json
{
  "variable_groups": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111111000000117081"
      },
      "message": "variable group updated successfully",
      "status": "success"
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
