# Examples: getFeatureDetails

**GET /__features**

## Response examples

### Status `200` — `application/json` — SuccessResponse

List all features with usage limits and component details

```json
{
  "__features": [
    {
      "components": [
        {
          "api_name": "global_picklist_per_module",
          "module_supported": false,
          "details": {
            "limits": {
              "edition_limit": 15,
              "total": 15
            }
          },
          "feature_label": "Global Picklist Per Module"
        }
      ],
      "api_name": "global_picklists",
      "parent_feature": null,
      "module_supported": false,
      "details": {
        "available_count": {
          "total": 3
        },
        "used_count": {
          "total": 0
        },
        "limits": {
          "edition_limit": 30,
          "total": 30
        }
      },
      "feature_label": "Global Picklists"
    },
    {
      "components": null,
      "api_name": "team_spaces",
      "parent_feature": null,
      "module_supported": false,
      "details": {
        "limits": {
          "edition_limit": 25,
          "total": 25
        }
      },
      "feature_label": "Teamspace"
    }
  ],
  "info": {
    "per_page": 200,
    "count": 200,
    "page": 1,
    "more_records": true
  }
}
```

### Status `400` — `application/json` — SuccessResponse

Invalid module API name in the request

```json
{
  "code": "INVALID_MODULE",
  "details": {},
  "message": "the module name given seems to be invalid",
  "status": "error"
}
```
