### `application/json` — Example

```json
{
  "data_enrichment": [
    {
      "type": "personal",
      "module": {
        "id": "917992000000000129",
        "api_name": "Contacts"
      },
      "input_data_field_mapping": [
        {
          "enrich_field": {
            "name": "email"
          },
          "crm_field": {
            "id": "917992000000000449",
            "api_name": "Email"
          }
        }
      ],
      "output_data_field_mapping": [
        {
          "enrich_field": {
            "name": "last_name"
          },
          "crm_field": {
            "id": "917992000000000443",
            "api_name": "Last_Name"
          }
        },
        {
          "enrich_field": {
            "name": "primary_email"
          },
          "crm_field": {
            "id": "917992000000000449",
            "api_name": "Email"
          }
        },
        {
          "enrich_field": {
            "name": "secondary_email"
          },
          "crm_field": {
            "id": "917992000000026001",
            "api_name": "Secondary_Email"
          }
        },
        {
          "enrich_field": {
            "name": "primary_contact"
          },
          "crm_field": {
            "id": "917992000000000457",
            "api_name": "Phone"
          }
        },
        {
          "enrich_field": {
            "name": "social_media_twitter"
          },
          "crm_field": {
            "id": "917992000000035003",
            "api_name": "Twitter"
          }
        },
        {
          "enrich_field": {
            "name": "primary_address_info_state"
          },
          "crm_field": {
            "id": "917992000000000503",
            "api_name": "Other_State"
          }
        },
        {
          "enrich_field": {
            "name": "primary_address_info_city"
          },
          "crm_field": {
            "id": "917992000000000499",
            "api_name": "Other_City"
          }
        },
        {
          "enrich_field": {
            "name": "primary_address_info_country"
          },
          "crm_field": {
            "id": "917992000000000511",
            "api_name": "Other_Country"
          }
        },
        {
          "enrich_field": {
            "name": "first_name"
          },
          "crm_field": {
            "id": "917992000000000441",
            "api_name": "First_Name"
          }
        }
      ]
    }
  ]
}
```
