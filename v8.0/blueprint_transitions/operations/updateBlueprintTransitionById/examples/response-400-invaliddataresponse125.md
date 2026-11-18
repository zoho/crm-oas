Error response with code INVALID_DATA: Invalid data type (Field: ID)

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.transitions[*].actions[*].details.module.id"
      },
      "status": "error"
    }
  ]
}
```
