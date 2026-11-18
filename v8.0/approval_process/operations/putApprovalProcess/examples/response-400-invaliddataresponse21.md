INVALID_DATA error when the id at $.approval_process[*].id exceeds 25 characters

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "maximum_length": 25,
        "json_path": "$.approval_process[*].id"
      },
      "status": "error"
    }
  ]
}
```
