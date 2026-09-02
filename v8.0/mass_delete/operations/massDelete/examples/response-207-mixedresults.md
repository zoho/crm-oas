An example of partial success: some records deleted, others failed validation.

```json
{
  "data": [
    {
      "status": "success",
      "code": "SUCCESS",
      "message": "record is deleted",
      "details": {
        "id": "1990117000035107169"
      }
    },
    {
      "status": "error",
      "code": "INVALID_DATA",
      "message": "Record locked or invalid permissions",
      "details": {
        "id": "1990117000035827873"
      }
    }
  ]
}
```
