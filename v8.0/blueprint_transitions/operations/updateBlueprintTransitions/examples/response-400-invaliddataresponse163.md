Error response with code INVALID_DATA: Invalid data type (Field: api_name)

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
