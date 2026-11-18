Error response with code **INVALID_DATA**: Invalid data type (Field: **module**)

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "module",
        "expected_data_type": "jsonobject",
        "json_path": "$.transitions[*].during_inputs[*].related_list.module"
      },
      "status": "error"
    }
  ]
}
```
