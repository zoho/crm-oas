Invalid data in the **name** field (**INVALID_DATA**)

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 5,
        "json_path": "$.transitions[*].during_inputs[*].related_list.name"
      },
      "status": "error"
    }
  ]
}
```
