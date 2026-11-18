Multi-status response with mixed update results

```json
{
  "approval_process": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111111000000930221"
      },
      "message": "approval process updated successfully",
      "status": "success"
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.approval_process[1]id"
      },
      "message": "invalid approval process id",
      "status": "error"
    }
  ]
}
```
