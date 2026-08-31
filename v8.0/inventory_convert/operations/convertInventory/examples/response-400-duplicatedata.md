Duplicate unique field value in the target module

```json
{
  "data": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "Billing_Street",
        "duplicate_record": {
          "Owner": {
            "name": "Poovi MBUser2",
            "id": "111111000000058229",
            "zuid": "44653171"
          },
          "module": {
            "api_name": "Sales_Orders",
            "id": "111111000000002766"
          },
          "id": "111111000000536282"
        },
        "json_path": "$.data[0].Billing_Street",
        "more_records": false
      },
      "message": "duplicate data",
      "status": "error"
    }
  ]
}
```
