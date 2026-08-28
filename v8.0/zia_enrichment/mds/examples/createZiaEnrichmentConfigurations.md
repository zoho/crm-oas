# Examples: createZiaEnrichmentConfigurations

**POST /settings/zia/data_enrichment**

## Request examples

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

## Response examples

### Status `201` — `application/json` — Example

```json
{
  "data_enrichment": [
    {
      "code": "SUCCESS",
      "details": {
        "created_time": "2025-11-13T12:25:39+05:30",
        "id": "917992000008626025",
        "created_by": {
          "id": "917992000000417001",
          "name": "Brendon Caster"
        }
      },
      "message": "Enrichment created successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — Example1

```json
{
  "data_enrichment": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "jsonarray",
        "api_name": "output_data_field_mapping || input_data_field_mapping",
        "json_path": "$.data_enrichment[0].(output_data_field_mapping || input_data_field_mapping)"
      },
      "message": "Invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — Example2

```json
{
  "data_enrichment": [
    {
      "code": "INVALID_DATA",
      "message": "the given type seems to be invalid",
      "details": {
        "api_name": "type",
        "json_path": "$.data_enrichment[0].type",
        "supported_values": [
          "organization",
          "personal"
        ]
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — Example3

```json
{
  "data_enrichment": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "limit": 50,
        "limit_due_to": [
          {
            "api_name": "data_enrichment",
            "json_path": "$.data_enrichment"
          }
        ]
      },
      "message": "data enrichment configurations limit exceeded",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — Example4

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

### Status `400` — `application/json` — Example5

```json
{
  "data_enrichment": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "details": {
        "ambiguity_due_to": [
          {
            "api_name": "api_name",
            "json_path": "$.data_enrichment[0].module.api_name"
          },
          {
            "api_name": "id",
            "json_path": "$.data_enrichment[0].module.id"
          }
        ]
      },
      "message": "Ambiguity while processing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — Example6

```json
{
  "code": "FEATURE_NOT_ENABLED",
  "details": {},
  "message": "Data Enrichment feature not enabled",
  "status": "error"
}
```

### Status `403` — `application/json` — Example

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Manage_Data_Enrichment"
    ]
  },
  "message": "No permission to access this feature",
  "status": "error"
}
```
