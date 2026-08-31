Mixed batch delete when one record deleted, one fails with INVALID_DATA

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "id": "4671651000010893004"
      },
      "message": "record not deleted",
      "status": "error",
      "error_meta": "invalid_field"
    },
    {
      "code": "SUCCESS",
      "details": {
        "id": "4671651000000950132"
      },
      "message": "record deleted",
      "status": "success"
    }
  ]
}
```
