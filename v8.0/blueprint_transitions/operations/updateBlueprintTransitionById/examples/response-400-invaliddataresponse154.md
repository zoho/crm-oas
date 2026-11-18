Error response when the **group** field has an invalid data type

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "group",
        "expected_data_type": "jsonarray",
        "json_path": "$.transitions[*].criteria.group[*].group"
      },
      "status": "error"
    }
  ]
}
```
