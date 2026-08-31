Mixed create results

```json
{
  "currencies": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111111000000129264"
      },
      "message": "The currency created successfully.",
      "status": "success"
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "iso_code",
        "json_path": "$.currencies[1].iso_code"
      },
      "message": "Currency isocode given seems to be invalid",
      "status": "error"
    }
  ]
}
```
