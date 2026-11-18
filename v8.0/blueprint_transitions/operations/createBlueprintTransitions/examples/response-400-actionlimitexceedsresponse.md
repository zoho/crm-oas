**INVALID_DATA** error: action limit exceeded for the **actions** field

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
