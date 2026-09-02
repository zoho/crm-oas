**RECORD_LOCKED** error when the appointment record is locked and cannot be modified.

```json
{
  "data": [
    {
      "code": "RECORD_LOCKED",
      "details": {
        "api_name": "id",
        "action": "record_locking",
        "json_path": "$.data[0].id"
      },
      "message": "Sorry, you cannot perform this operation as the record is locked.",
      "status": "error"
    }
  ]
}
```
