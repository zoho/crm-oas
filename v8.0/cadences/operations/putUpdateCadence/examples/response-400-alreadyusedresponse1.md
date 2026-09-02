Field value already in use error

```json
{
  "cadences": [
    {
      "code": "ALREADY_USED",
      "details": {
        "api_name": "triggers",
        "exists_in": {
          "api_name": "triggers",
          "json_path": "$.cadences[0].follow_ups[1].triggers[0]"
        },
        "json_path": "$.cadences[0].follow_ups[1].triggers[1]"
      },
      "message": "trigger type is already given in the same request under different key",
      "status": "error"
    }
  ]
}
```
