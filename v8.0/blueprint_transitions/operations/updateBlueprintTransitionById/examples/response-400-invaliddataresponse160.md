**INVALID_DATA** error when **api_name** has an invalid data type

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.transitions[*].criteria.group[*].group[*].field.api_name"
      },
      "status": "error"
    }
  ]
}
```
