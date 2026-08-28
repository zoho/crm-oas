# Examples: getUserLicenseFeatureDetails

**GET /__features/user_licenses**

## Response examples

### Status `200` — `application/json` — SuccessResponse

Get User License Feature Details

```json
{
  "__features": [
    {
      "components": null,
      "api_name": "user_licenses",
      "parent_feature": null,
      "module_supported": false,
      "details": {
        "available_count": {
          "total": 3
        },
        "used_count": {
          "total": 7
        },
        "limits": {
          "total": 10
        }
      },
      "feature_label": "UserLicenses"
    }
  ]
}
```

### Status `400` — `application/json` — SuccessResponse

Error response

```json
{
  "code": "INVALID_MODULE",
  "details": {},
  "message": "the module name given seems to be invalid",
  "status": "error"
}
```
