**NOT_ALLOWED** error when completing an appointment without a job sheet.

```json
{
  "data": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "Status",
        "json_path": "$.data[0].Status"
      },
      "message": "Appointment cannot be marked as completed without creating the jobsheet",
      "status": "error"
    }
  ]
}
```
