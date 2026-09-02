### `application/json` — DuplicateCheckPreferenceForContacts

Duplicate check preference for Contacts

```json
{
  "duplicate_check_preference": {
    "type": "mapped_module_records",
    "type_configurations": [
      {
        "field_mappings": [
          {
            "mapped_field": {
              "api_name": "Phone",
              "name": "Contacts",
              "id": "1124664000000000457"
            },
            "current_field": {
              "api_name": "Phone",
              "name": "Leads",
              "id": "1124664000000000565"
            }
          }
        ],
        "mapped_module": {
          "api_name": "Contacts",
          "name": "Contacts",
          "id": "1124664000000000129"
        }
      }
    ]
  }
}
```

### `application/json` — DuplicateCheckPreferenceForConvertedLead

Duplicate check preference for converted Leads

```json
{
  "duplicate_check_preference": {
    "type": "converted_records",
    "type_configurations": []
  }
}
```
