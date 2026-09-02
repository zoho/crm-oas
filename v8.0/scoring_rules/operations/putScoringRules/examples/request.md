### `application/json` — SamplePutRequest

Sample update Scoring Rules request body

```json
{
  "scoring_rules": [
    {
      "id": "111114000000072349",
      "field_rules": [
        {
          "criteria": {
            "field": {
              "api_name": "Country",
              "id": "111114000000004892",
              "data_type": "text"
            },
            "comparator": "not_equal",
            "value": "${EMPTY}",
            "type": "value"
          },
          "score": -10
        },
        {
          "id": "111114000000004892",
          "score": 45
        }
      ]
    },
    {
      "id": "111114000000072349",
      "name": "Altered Scoring"
    },
    {
      "id": "111114000000072349",
      "signal_rules": [
        {
          "id": "111114000000012345",
          "_delete": null
        }
      ],
      "custom_fields": [
        {
          "field_label": "Contact Total Score",
          "reference_field": {
            "api_name": "Score"
          }
        }
      ]
    }
  ]
}
```
