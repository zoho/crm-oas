INVALID_DATA error for the execute_on field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "text",
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
