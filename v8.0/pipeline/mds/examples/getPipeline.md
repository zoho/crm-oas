# Examples: getPipeline

**GET /settings/pipeline/{pipelineIdentifier}**

## Response examples

### Status `200` — `application/json` — SinglePipelineGetResponse

```json
{
  "pipeline": [
    {
      "display_value": "Standard (JackFer)",
      "default": true,
      "maps": [
        {
          "display_value": "Qualification",
          "sequence_number": 1,
          "forecast_category": {
            "name": "Pipeline",
            "id": "2766660000000007092"
          },
          "actual_value": "Qualification",
          "id": "2766660000000007104",
          "forecast_type": "Open"
        }
      ],
      "actual_value": "Standard (JackFer)",
      "id": "2766660000055809075"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidLayoutID

```json
{
  "code": "INVALID_DATA",
  "details": {
    "param_name": "layout_id"
  },
  "message": "Invalid layoutid",
  "status": "error"
}
```
