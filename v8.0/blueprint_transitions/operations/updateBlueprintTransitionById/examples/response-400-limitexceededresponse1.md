Error response when the transition exceeds the allowed number of during fields

```json
{
  "transitions": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "api_name": "transition",
        "limit": 10,
        "json_path": "$.blueprint[0].chart_data[0].transition"
      },
      "message": "Blueprint transition during fields limit exceed",
      "status": "error"
    }
  ]
}
```
