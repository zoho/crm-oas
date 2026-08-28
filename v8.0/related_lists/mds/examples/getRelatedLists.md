# Examples: getRelatedLists

**GET /settings/related_lists**

## Parameter examples

### `module` (query) — Leads

CRM Leads module

```json
"Leads"
```

### `module` (query) — Contacts

CRM Contacts module

```json
"Contacts"
```

### `module` (query) — Accounts

CRM Accounts module

```json
"Accounts"
```

### `module` (query) — Deals

CRM Deals/Opportunities module

```json
"Deals"
```

### `layout_id` (query) — ValidLayoutId

Example of a valid layout ID

```json
"4150868000000091023"
```

### `status` (query) — Visible

Show only visible related lists

```json
"visible"
```

### `status` (query) — Hidden

Show only user-hidden related lists

```json
"user_hidden"
```

### `status` (query) — ScheduledDeletion

Show only related lists scheduled for deletion

```json
"scheduled_for_deletion"
```

### `extra_properties` (query) — Enabled

Include extra properties in the response

```json
true
```

### `extra_properties` (query) — Disabled

Return only default properties

```json
false
```

### `include_inner_details` (query) — All

Include all inner details

```json
"all"
```

## Response examples

### Status `200` — `application/json` — SuccessResponse

Successful retrieval of related lists

```json
{
  "related_lists": [
    {
      "id": "4150868000000091023",
      "sequence_number": "1",
      "display_label": "Contacts",
      "api_name": "Contacts",
      "module": {
        "api_name": "Contacts",
        "id": "4150868000000002175"
      },
      "name": "Contacts",
      "action": null,
      "href": null,
      "type": "default",
      "customize_sort": true,
      "customize_fields": true,
      "customize_display_label": true,
      "status": "visible",
      "parent_related_lists": [
        {
          "api_name": "Deals",
          "id": "4150868000000091050"
        }
      ]
    }
  ]
}
```

### Status `200` — `application/json` — FullResponseAllFieldsPopulated

Related list with all optional fields populated

```json
{
  "related_lists": [
    {
      "id": "4150868000000091023",
      "sequence_number": "1",
      "display_label": "Contacts",
      "api_name": "Contacts",
      "module": {
        "api_name": "Contacts",
        "id": "4150868000000002175"
      },
      "name": "Contacts",
      "action": "add_existing",
      "href": "Contacts/{ENTITYID}/Contacts",
      "type": "default",
      "connectedlookupApiName": "Account_Name",
      "customize_sort": true,
      "customize_fields": true,
      "customize_display_label": true,
      "status": "visible",
      "visibility": 1,
      "personality_name": "contacts_personality",
      "record_operations": {
        "edit": true,
        "create": true,
        "bulk_edit": false,
        "delete": true,
        "disassociate": true,
        "assign": false
      },
      "connectedmodule": "Accounts",
      "linkingmodule": "Contacts_X_Accounts",
      "parent_related_lists": [
        {
          "api_name": "Deals",
          "id": "4150868000000091050"
        }
      ],
      "_layout_specific_properties": [
        {
          "sequence_number": "2",
          "status": "visible",
          "layout": {
            "name": "Standard",
            "id": "4150868000000091100"
          }
        }
      ]
    }
  ]
}
```

### Status `200` — `application/json` — AllNullableFieldsNull

Related list with all nullable fields set to null

```json
{
  "related_lists": [
    {
      "id": "4150868000000091023",
      "sequence_number": "1",
      "display_label": "Notes",
      "api_name": "Notes",
      "module": null,
      "name": "Notes",
      "action": null,
      "href": null,
      "type": "default",
      "customize_sort": false,
      "customize_fields": false,
      "customize_display_label": false,
      "status": "visible",
      "connectedmodule": null,
      "linkingmodule": null,
      "parent_related_lists": null,
      "_layout_specific_properties": null
    }
  ]
}
```

### Status `200` — `application/json` — MultiselectLookupRelatedList

Related list of type multiselectlookup with full config

```json
{
  "related_lists": [
    {
      "id": "4150868000000091080",
      "sequence_number": "5",
      "display_label": "Products",
      "api_name": "Products",
      "module": {
        "api_name": "Products",
        "id": "4150868000000002200",
        "plural_label": "Products"
      },
      "name": "Products",
      "action": null,
      "href": null,
      "type": "multiselectlookup",
      "connectedlookupApiName": "Product_Name",
      "customize_sort": true,
      "customize_fields": true,
      "customize_display_label": true,
      "status": "visible",
      "connectedmodule": "Products",
      "linkingmodule": "Deals_X_Products",
      "parent_related_lists": null,
      "multiselectlookup": {
        "field": {
          "api_name": "Product_Name",
          "field_label": "Product Name",
          "id": "4150868000000002300"
        },
        "linking_details": {
          "visibility": 1,
          "module": {
            "plural_label": "Deals_X_Products",
            "api_name": "Deals_X_Products",
            "id": "4150868000000002400"
          },
          "lookup_field": {
            "api_name": "Deal_Name",
            "id": "4150868000000002500"
          },
          "connected_lookup_field": {
            "api_name": "Product_Name",
            "id": "4150868000000002600"
          }
        },
        "connected_details": {
          "field": {
            "api_name": "Deal_Name",
            "field_label": "Deal Name",
            "id": "4150868000000002700"
          },
          "module": {
            "plural_label": "Deals",
            "api_name": "Deals",
            "id": "4150868000000002800"
          },
          "related_list": {
            "display_label": "Deals",
            "api_name": "Deals",
            "id": "4150868000000002900"
          }
        },
        "field_enabled": true
      }
    }
  ]
}
```

### Status `200` — `application/json` — UserHiddenRelatedList

Related list with user_hidden status

```json
{
  "related_lists": [
    {
      "id": "4150868000000091090",
      "sequence_number": "10",
      "display_label": "Hidden List",
      "api_name": "Custom_RL",
      "module": {
        "api_name": "Custom_Module",
        "id": "4150868000000003000"
      },
      "name": "Custom RL",
      "action": null,
      "href": null,
      "type": "custom",
      "customize_sort": false,
      "customize_fields": true,
      "customize_display_label": true,
      "status": "user_hidden",
      "parent_related_lists": [
        {
          "api_name": "Accounts",
          "id": "4150868000000091060"
        }
      ]
    }
  ]
}
```

### Status `200` — `application/json` — ScheduledForDeletionRelatedList

Related list scheduled for deletion

```json
{
  "related_lists": [
    {
      "id": "4150868000000091095",
      "sequence_number": "15",
      "display_label": "Old List",
      "api_name": "Deprecated_RL",
      "module": {
        "api_name": "Old_Module",
        "id": "4150868000000003100"
      },
      "name": "Deprecated RL",
      "action": null,
      "href": null,
      "type": "default",
      "customize_sort": false,
      "customize_fields": false,
      "customize_display_label": false,
      "status": "scheduled_for_deletion",
      "parent_related_lists": [
        {
          "api_name": "Leads",
          "id": "4150868000000091070"
        }
      ]
    }
  ]
}
```

### Status `200` — `application/json` — MultipleLayoutSpecificProperties

Related list with multiple layout-specific property entries

```json
{
  "related_lists": [
    {
      "id": "4150868000000091023",
      "sequence_number": "1",
      "display_label": "Contacts",
      "api_name": "Contacts",
      "module": {
        "api_name": "Contacts",
        "id": "4150868000000002175"
      },
      "name": "Contacts",
      "action": null,
      "href": null,
      "type": "default",
      "customize_sort": true,
      "customize_fields": true,
      "customize_display_label": true,
      "status": "visible",
      "parent_related_lists": [
        {
          "api_name": "Deals",
          "id": "4150868000000091050"
        }
      ],
      "_layout_specific_properties": [
        {
          "sequence_number": "1",
          "status": "visible",
          "layout": {
            "name": "Standard",
            "id": "4150868000000091100"
          }
        },
        {
          "sequence_number": "3",
          "status": "user_hidden",
          "layout": {
            "name": "Custom Layout",
            "id": "4150868000000091200"
          }
        }
      ]
    }
  ]
}
```

### Status `400` — `application/json` — InvalidModule

Invalid module name

```json
{
  "status": "error",
  "code": "INVALID_MODULE",
  "message": "the module name given seems to be invalid",
  "details": {
    "param_name": "module"
  }
}
```

### Status `400` — `application/json` — NotSupported

Module not supported by this API

```json
{
  "status": "error",
  "code": "NOT_SUPPORTED",
  "message": "the given module is not supported for this api",
  "details": {
    "param_name": "module"
  }
}
```

### Status `400` — `application/json` — InvalidParameterValue

Invalid value for the status parameter

```json
{
  "status": "error",
  "code": "INVALID_DATA",
  "message": "The status given is invalid.",
  "details": {
    "param_name": "status",
    "supported_values": [
      "visible",
      "user_hidden",
      "scheduled_for_deletion"
    ]
  }
}
```

### Status `400` — `application/json` — RequiredParamMissing

Required module parameter is missing

```json
{
  "code": "REQUIRED_PARAM_MISSING",
  "details": {
    "param_name": "module"
  },
  "message": "One of the expected parameter is missing",
  "status": "error"
}
```

### Status `401` — `application/json` — InvalidToken

Invalid or expired OAuth token

```json
{
  "code": "INVALID_TOKEN",
  "details": {},
  "message": "invalid oauth token",
  "status": "error"
}
```

### Status `401` — `application/json` — OAuthScopeMismatch

OAuth token missing the required scope

```json
{
  "code": "OAUTH_SCOPE_MISMATCH",
  "details": {},
  "message": "invalid oauth scope to access this URL",
  "status": "error"
}
```
