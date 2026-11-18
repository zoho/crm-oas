INVALID_DATA error for an invalid data type in **api_name**

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.transitions[*].during_inputs[*].related_list.layout.api_name"
      },
      "status": "error"
    }
  ]
}
```
