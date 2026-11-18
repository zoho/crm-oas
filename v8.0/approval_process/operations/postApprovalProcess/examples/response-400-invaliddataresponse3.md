INVALID_DATA error for invalid data on the execute_on field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "execute_on",
        "json_path": "$.approval_process[0].execute_on",
        "supported_values": [
          "create",
          "edit",
          "create_or_edit"
        ]
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```
