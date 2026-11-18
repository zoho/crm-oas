INVALID_DATA error when generated_type exceeds 50 characters

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "generated_type",
        "maximum_length": 50,
        "json_path": "$.approval_process[*].generated_type"
      },
      "status": "error"
    }
  ]
}
```
