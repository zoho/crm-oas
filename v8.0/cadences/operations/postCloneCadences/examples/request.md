### `application/json` — SamplePostRequest

Sample clone Cadence request body

```json
{
  "cadences": [
    {
      "name": "cadence",
      "description": "description",
      "module": {
        "api_name": "Leads",
        "id": "111112000000002628"
      },
      "type": "custom_view",
      "custom_view": {
        "id": "111112000000051112"
      },
      "execution_details": {
        "execute_every": {
          "period": "hours",
          "unit": 1
        }
      }
    }
  ]
}
```
