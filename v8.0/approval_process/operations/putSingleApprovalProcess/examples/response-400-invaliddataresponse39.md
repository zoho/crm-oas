INVALID_DATA error when the rules array exceeds one entry

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "rules",
        "maximum_length": 1,
        "json_path": "$.approval_process[*].rules"
      },
      "status": "error"
    }
  ]
}
```
