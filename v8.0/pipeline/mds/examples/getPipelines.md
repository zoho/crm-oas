# Examples: getPipelines

**GET /settings/pipeline**

## Response examples

### Status `200` — `application/json` — PipelineGetResponse

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
        },
        {
          "display_value": "Needs Analysis",
          "sequence_number": 2,
          "forecast_category": {
            "name": "Pipeline",
            "id": "2766660000000007092"
          },
          "actual_value": "Needs Analysis",
          "id": "2766660000000007106",
          "forecast_type": "Open"
        },
        {
          "display_value": "Identify Decision Makers",
          "sequence_number": 3,
          "forecast_category": {
            "name": "Pipeline",
            "id": "2766660000000007092"
          },
          "actual_value": "Id. Decision Makers",
          "id": "2766660000000007110",
          "forecast_type": "Open"
        },
        {
          "display_value": "Proposal/Price Quote",
          "sequence_number": 4,
          "forecast_category": {
            "name": "Pipeline",
            "id": "2766660000000007092"
          },
          "actual_value": "Proposal/Price Quote",
          "id": "2766660000000007112",
          "forecast_type": "Open"
        },
        {
          "display_value": "Negotiation/Review",
          "sequence_number": 5,
          "forecast_category": {
            "name": "Pipeline",
            "id": "2766660000000007092"
          },
          "actual_value": "Negotiation/Review",
          "id": "2766660000000007114",
          "forecast_type": "Open"
        },
        {
          "display_value": "Closed Won",
          "sequence_number": 6,
          "forecast_category": {
            "name": "Closed",
            "id": "2766660000000007094"
          },
          "actual_value": "Closed Won",
          "id": "2766660000000007116",
          "forecast_type": "Closed Won"
        },
        {
          "display_value": "Closed Lost",
          "sequence_number": 7,
          "forecast_category": {
            "name": "Omitted",
            "id": "2766660000000007096"
          },
          "actual_value": "Closed Lost",
          "id": "2766660000000007118",
          "forecast_type": "Closed Lost"
        },
        {
          "display_value": "Closed Lost to Competition",
          "sequence_number": 8,
          "forecast_category": {
            "name": "Omitted",
            "id": "2766660000000007096"
          },
          "actual_value": "Closed Lost to Competition",
          "id": "2766660000000007120",
          "forecast_type": "Closed Lost"
        },
        {
          "display_value": "dcba",
          "sequence_number": 9,
          "forecast_category": {
            "name": "Pipeline",
            "id": "2766660000000007092"
          },
          "actual_value": "dcba",
          "id": "2766660000030928184",
          "forecast_type": "Open"
        },
        {
          "display_value": "abcd",
          "sequence_number": 10,
          "forecast_category": {
            "name": "Pipeline",
            "id": "2766660000000007092"
          },
          "actual_value": "abcd",
          "id": "2766660000030928185",
          "forecast_type": "Open"
        },
        {
          "display_value": "ABC",
          "sequence_number": 11,
          "forecast_category": {
            "name": "Pipeline",
            "id": "2766660000000007092"
          },
          "actual_value": "ABC",
          "id": "2766660000030928272",
          "forecast_type": "Open"
        }
      ],
      "actual_value": "Standard (JackFer)",
      "id": "2766660000055809075"
    },
    {
      "display_value": "New",
      "default": false,
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
        },
        {
          "display_value": "Needs Analysis",
          "sequence_number": 2,
          "forecast_category": {
            "name": "Pipeline",
            "id": "2766660000000007092"
          },
          "actual_value": "Needs Analysis",
          "id": "2766660000000007106",
          "forecast_type": "Open"
        },
        {
          "display_value": "Identify Decision Makers",
          "sequence_number": 3,
          "forecast_category": {
            "name": "Pipeline",
            "id": "2766660000000007092"
          },
          "actual_value": "Id. Decision Makers",
          "id": "2766660000000007110",
          "forecast_type": "Open"
        },
        {
          "display_value": "Proposal/Price Quote",
          "sequence_number": 4,
          "forecast_category": {
            "name": "Pipeline",
            "id": "2766660000000007092"
          },
          "actual_value": "Proposal/Price Quote",
          "id": "2766660000000007112",
          "forecast_type": "Open"
        },
        {
          "display_value": "Negotiation/Review",
          "sequence_number": 5,
          "forecast_category": {
            "name": "Pipeline",
            "id": "2766660000000007092"
          },
          "actual_value": "Negotiation/Review",
          "id": "2766660000000007114",
          "forecast_type": "Open"
        },
        {
          "display_value": "Closed Won",
          "sequence_number": 6,
          "forecast_category": {
            "name": "Closed",
            "id": "2766660000000007094"
          },
          "actual_value": "Closed Won",
          "id": "2766660000000007116",
          "forecast_type": "Closed Won"
        }
      ],
      "actual_value": "New",
      "id": "2766660000055809086"
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
