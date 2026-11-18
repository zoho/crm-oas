INVALID_DATA error: overall_approval_type field contains invalid data

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "overall_approval_type",
        "supported_values": [
          "anyone",
          "everyone_parallel",
          "everyone_sequential"
        ],
        "json_path": "$.approval_process[*].rules[*].overall_approval_type"
      },
      "status": "error"
    }
  ]
}
```
