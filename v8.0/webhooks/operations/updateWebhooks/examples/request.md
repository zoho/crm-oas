### `application/json` — SamplePutRequest

Bulk update request for a webhook with all required fields

```json
{
  "webhooks": [
    {
      "headers": {
        "module_parameters": [
          {
            "name": "lead_email",
            "value": "${!Leads.Email}"
          },
          {
            "name": "lead_id",
            "value": "${!Leads.Id}"
          },
          {
            "name": "lead_owner",
            "value": "${!Leads.Owner}"
          }
        ],
        "custom_parameters": [
          {
            "name": "source",
            "value": "website"
          },
          {
            "name": "version",
            "value": "1.0"
          }
        ]
      },
      "module": {
        "api_name": "Leads",
        "id": "5725767000000002175"
      },
      "description": "Protected Data",
      "body": {
        "raw_data_content": "{\n  \"lead_id\": \"${!Leads.Id}\",\n  \"email\": \"${!Leads.Email}\",\n  \"owner\": \"${!Leads.Owner}\",\n  \"source\": \"website\",\n  \"version\": \"1.0\"\n}",
        "format": "JSON",
        "type": "raw"
      },
      "url": "https://webhook.site/3588de27-e3bd-4237-894b-f140143f3d99",
      "feature_type": "workflow",
      "http_method": "POST",
      "name": "Zoho's Data",
      "authentication": {
        "type": "general"
      }
    }
  ]
}
```
