### `application/json` — BasicConversion

Basic lead conversion to Contact only

```json
{
  "data": [
    {
      "overwrite": false,
      "notify_lead_owner": true,
      "notify_new_entity_owner": false
    }
  ]
}
```

### `application/json` — ConversionWithDeal

Lead conversion with Deal creation

```json
{
  "data": [
    {
      "overwrite": false,
      "notify_lead_owner": true,
      "notify_new_entity_owner": true,
      "Deals": {
        "Deal_Name": "Enterprise Package Deal",
        "Pipeline": "Standard (Standard)",
        "Stage": "Qualification",
        "Closing_Date": "2025-12-31",
        "Amount": 50000,
        "Probability": 60
      }
    }
  ]
}
```
