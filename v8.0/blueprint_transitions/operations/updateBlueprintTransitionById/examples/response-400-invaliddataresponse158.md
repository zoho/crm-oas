**INVALID_DATA** error when a **field** value has an invalid data type

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "field",
        "expected_data_type": "jsonobject",
        "json_path": "$.transitions[*].criteria.group[*].group[*].field"
      },
      "status": "error"
    }
  ]
}
```
