# Examples: getFieldsWithID

**GET /settings/fields/{fieldId}**

## Response examples

### Status `200` — `application/json` — FullExample

Metadata of a single field retrieved successfully

```json
{
  "fields": [
    {
      "associated_module": null,
      "webhook": true,
      "operation_type": {
        "web_update": true,
        "api_create": true,
        "web_create": true,
        "api_update": true
      },
      "colour_code_enabled_by_system": false,
      "field_label": "Address 1 - Latitude",
      "tooltip": null,
      "display_format_properties": null,
      "type": "used",
      "field_read_only": false,
      "customizable_properties": [
        "mandatory"
      ],
      "display_label": "Address 1 - Latitude",
      "read_only": false,
      "association_details": null,
      "businesscard_supported": false,
      "multi_module_lookup": {},
      "id": "4832675000000710341",
      "created_time": "2025-11-17T19:09:17+05:30",
      "filterable": false,
      "visible": true,
      "profiles": [
        {
          "permission_type": "read_write",
          "name": "Administrator",
          "id": "4832675000000015972"
        },
        {
          "permission_type": "read_write",
          "name": "Standard",
          "id": "4832675000000015975"
        }
      ],
      "view_type": {
        "view": true,
        "edit": true,
        "quick_create": false,
        "create": true
      },
      "separator": false,
      "searchable": true,
      "history_tracking_enabled": false,
      "external": null,
      "api_name": "Address_1_Coordinates_Latitude",
      "parent_field": {
        "api_name": "Address_1_Coordinates",
        "name": "Address 1 - Coordinates",
        "id": "4832675000000710334"
      },
      "unique": {},
      "enable_colour_code": false,
      "child_fields": null,
      "pick_list_values": [],
      "system_mandatory": false,
      "private": null,
      "virtual_field": false,
      "json_type": "double",
      "crypt": null,
      "range": null,
      "created_source": "default",
      "display_type": -1,
      "ui_type": 38,
      "modified_time": "2025-11-17T19:09:17+05:30",
      "public": false,
      "email_parser": {
        "fields_update_supported": false,
        "record_operations_supported": false
      },
      "currency": {},
      "custom_field": true,
      "lookup": {},
      "hipaa_compliance": null,
      "convert_mapping": {
        "Contacts": null,
        "Deals": null,
        "Accounts": null
      },
      "address": {
        "type": "latitude"
      },
      "rollup_summary": {},
      "length": 50,
      "column_name": "LEADCF69",
      "display_field": false,
      "pick_list_values_sorted_lexically": false,
      "sortable": true,
      "global_picklist": null,
      "display_format": null,
      "history_tracking": null,
      "data_type": "double",
      "formula": {},
      "additional_column": null,
      "hipaa_compliance_enabled": false,
      "decimal_place": 9,
      "mass_update": false,
      "multiselectlookup": {},
      "auto_number": {}
    }
  ]
}
```

### Status `400` — `application/json` — ErrorExample

```json
{
  "code": "INVALID_MODULE",
  "message": "the module name given seems to be invalid",
  "details": {},
  "status": "error"
}
```

### Status `500` — `application/json` — ErrorExample

```json
{
  "code": "INTERNAL_ERROR",
  "message": "Internal Server Error",
  "details": {},
  "status": "error"
}
```
