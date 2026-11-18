Error response when the **layout** field has an invalid data type

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "layout",
        "expected_data_type": "jsonobject",
        "json_path": "$.transitions[*].during_inputs[*].related_list.layout"
      },
      "status": "error"
    }
  ]
}
```
