**INVALID_DATA** error: invalid data type in the **id** field

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.transitions[*].owners[*].resources[*].id"
      },
      "status": "error"
    }
  ]
}
```
