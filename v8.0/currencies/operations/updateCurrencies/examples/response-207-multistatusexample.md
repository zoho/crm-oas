Mixed update results

```json
{
  "currencies": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111111000000129300"
      },
      "message": "The currency updated successfully.",
      "status": "success"
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "exchange_rate",
        "json_path": "$.currencies[1].exchange_rate"
      },
      "message": "Exchange rate given seems to be invalid",
      "status": "error"
    }
  ]
}
```
