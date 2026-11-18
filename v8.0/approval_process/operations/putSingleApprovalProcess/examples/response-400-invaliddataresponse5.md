Unsupported value provided for the overall approval type

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "overall_approval_type",
        "json_path": "$.approval_process[0].rules[0].overall_approval_type",
        "supported_values": [
          "anyone",
          "everyone_sequential",
          "everyone_parallel"
        ]
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```
