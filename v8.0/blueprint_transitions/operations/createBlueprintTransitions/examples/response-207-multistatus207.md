Mixed response with one transition created and one failed

```json
{
  "transitions": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111112000000000856"
      },
      "message": "transition created successfully",
      "status": "success"
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "json_path": "$.transitions[1].module",
        "api_name": "api_name"
      },
      "message": "the value given is invalid",
      "status": "error"
    }
  ]
}
```
