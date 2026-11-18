Error response with code INVALID_DATA: Action Limit Exceeds (Field: actions)

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "details": {
        "action_type": "Fieldupdate",
        "api_name": "actions",
        "limit": 5,
        "json_path": "$.transition[0].actions",
        "configured_count": 6
      },
      "message": "Action Limit Exceeds",
      "status": "error"
    }
  ]
}
```
