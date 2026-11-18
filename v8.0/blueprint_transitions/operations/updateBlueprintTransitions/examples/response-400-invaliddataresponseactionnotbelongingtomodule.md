Error response with code INVALID_DATA: The action does not belong to the current module of the transition (Field: id)

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.transition[0].actions[0].id"
      },
      "message": "The action does not belong to the current module of the transition",
      "status": "error"
    }
  ]
}
```
