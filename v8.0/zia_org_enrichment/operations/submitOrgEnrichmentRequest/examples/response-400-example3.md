Expected trigger fields missing

```json
{
  "__zia_org_enrichment": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_fields": [
          {
            "api_name": "name",
            "json_path": "$.__zia_org_enrichment[0].enrich_based_on.name"
          },
          {
            "api_name": "email",
            "json_path": "$.__zia_org_enrichment[0].enrich_based_on.email"
          },
          {
            "api_name": "website",
            "json_path": "$.__zia_org_enrichment[0].enrich_based_on.website"
          }
        ]
      },
      "message": "Specify atleast one field",
      "status": "error"
    }
  ]
}
```
