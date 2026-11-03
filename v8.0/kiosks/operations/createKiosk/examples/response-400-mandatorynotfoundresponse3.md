MANDATORY_NOT_FOUND error when the required status field is missing from a kiosk item

```json
{
  "kiosks": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "status",
        "json_path": "$.kiosks[*].status"
      },
      "status": "error"
    }
  ]
}
```
