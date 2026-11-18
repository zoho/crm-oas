Unsupported overall_approval_type value outside the supported set

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
