Partial batch success with one record created and one rejected due to an invalid Duration value.

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "generated_id_0"
      },
      "message": "Proper success message",
      "status": "success"
    },
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "data",
        "json_path": "$.data[0].data"
      },
      "message": "Mandatory field data not found",
      "status": "error",
      "error_meta": "mandatory_missing"
    }
  ]
}
```
