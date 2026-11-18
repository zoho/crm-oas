Error response with code INVALID_DATA: invalid data provided for execute_on

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "execute_on",
        "supported_values": [
          "create",
          "edit",
          "create_or_edit"
        ],
        "json_path": "$.approval_process[*].execute_on"
      },
      "status": "error"
    }
  ]
}
```
