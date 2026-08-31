```json
{
  "data_enrichment": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_fields": [
          {
            "api_name": "id",
            "json_path": "$.data_enrichment[0].input_data_field_mapping[0].crm_field.id"
          },
          {
            "api_name": "api_name",
            "json_path": "$.data_enrichment[0].output_data_field_mapping[0].crm_field.api_name"
          }
        ]
      },
      "message": "Crm field cannot be empty",
      "status": "error"
    }
  ]
}
```
