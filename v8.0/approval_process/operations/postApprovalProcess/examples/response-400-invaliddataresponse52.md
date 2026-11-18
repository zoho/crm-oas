Invalid data error on the overall_approval_type field in the create request

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
