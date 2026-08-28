# Examples: updateLayout

**PATCH /settings/layouts/{id}**

## Parameter examples

### `id` (path) — ValidId

Valid layout ID

```json
"111111000000098320"
```

### `module` (query) — StandardModule

Standard module

```json
"Leads"
```

### `module` (query) — CustomModule

Custom module

```json
"Custom_Projects"
```

## Request examples

### `application/json` — RenameLayout

Rename an existing custom layout

```json
{
  "layouts": [
    {
      "name": "Updated CL1"
    }
  ]
}
```

### `application/json` — AddProfilePermission

Granting a CRM profile access to a layout

```json
{
  "layouts": [
    {
      "profiles": [
        {
          "id": "111111000000000395"
        }
      ]
    }
  ]
}
```

### `application/json` — RemoveProfilePermission

Revokes a CRM profile's access to a layout via the delete flag

```json
{
  "layouts": [
    {
      "profiles": [
        {
          "id": "111111000000000393",
          "_delete": true
        }
      ]
    }
  ]
}
```

### `application/json` — ToggleBusinessCard

Toggle the business card display setting on a layout

```json
{
  "layouts": [
    {
      "show_business_card": false
    }
  ]
}
```

### `application/json` — CreateCustomSection

Creating a new custom section within a layout

```json
{
  "layouts": [
    {
      "sections": [
        {
          "sequence_number": 6,
          "tab_traversal": "left_to_right",
          "column_count": 1,
          "name": "Custom Section 2",
          "display_label": "Custom Section 2"
        }
      ]
    }
  ]
}
```

### `application/json` — AddFieldToSection

Adding an existing field to a layout section

```json
{
  "layouts": [
    {
      "sections": [
        {
          "id": "3722469000001374014",
          "fields": [
            {
              "id": "3722469000001347394"
            }
          ]
        }
      ]
    }
  ]
}
```

### `application/json` — UpdateFieldSequence

Reorder a field's position within a layout section

```json
{
  "layouts": [
    {
      "sections": [
        {
          "id": "3722469000001374014",
          "fields": [
            {
              "id": "3722469000001347394",
              "sequence_number": 2
            }
          ]
        }
      ]
    }
  ]
}
```

### `application/json` — DeleteSection

Permanently removes a section and its field assignments from a layout

```json
{
  "layouts": [
    {
      "sections": [
        {
          "id": "3722469000001374014",
          "_delete": {
            "permanent": true
          }
        }
      ]
    }
  ]
}
```

### `application/json` — MoveFieldToUnused

Relocates a field to the unused items section without deleting it

```json
{
  "layouts": [
    {
      "sections": [
        {
          "id": "3722469000001347180",
          "fields": [
            {
              "id": "3722469000001347394",
              "_delete": {
                "permanent": false
              }
            }
          ]
        }
      ]
    }
  ]
}
```

### `application/json` — CreateNewField

Adds a new custom field definition to a layout section

```json
{
  "layouts": [
    {
      "sections": [
        {
          "id": "3722469000001347180",
          "fields": [
            {
              "field_label": "CF1",
              "length": 16,
              "sequence_number": 1,
              "data_type": "text"
            }
          ]
        }
      ]
    }
  ]
}
```

### `application/json` — MultipleFieldsAcrossSections

Adds up to five fields spread across multiple layout sections in one request

```json
{
  "layouts": [
    {
      "sections": [
        {
          "id": "3722469000001374014",
          "fields": [
            {
              "id": "3722469000001347394"
            },
            {
              "id": "3722469000001347395"
            }
          ]
        },
        {
          "id": "3722469000001374015",
          "fields": [
            {
              "id": "3722469000001347396"
            },
            {
              "id": "3722469000001347397"
            },
            {
              "id": "3722469000001347398"
            }
          ]
        }
      ]
    }
  ]
}
```

### `application/json` — CreateFieldWithAssociation

Creating a new field with a Field-Of-Lookup association

```json
{
  "layouts": [
    {
      "sections": [
        {
          "id": "3722469000001347180",
          "fields": [
            {
              "field_label": "Account Revenue",
              "data_type": "integer",
              "length": 9,
              "association_details": {
                "lookup_field": {
                  "id": "3722469000001347500",
                  "api_name": "Account_Lookup"
                },
                "related_field": {
                  "id": "3722469000001347600",
                  "api_name": "Annual_Revenue"
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

### `application/json` — UpdateFieldWithAssociation

Attach a Field-Of-Lookup association to an existing layout field

```json
{
  "layouts": [
    {
      "sections": [
        {
          "id": "3722469000001347180",
          "fields": [
            {
              "id": "3722469000001347394",
              "association_details": {
                "lookup_field": {
                  "id": "3722469000001347500"
                },
                "related_field": {
                  "id": "3722469000001347600"
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

### `application/json` — AddMirrorComponentToSection

Adding a mirror field component to a layout section

```json
{
  "layouts": [
    {
      "sections": [
        {
          "id": "3722469000001374014",
          "fields": [
            {
              "id": "3359388011000000523",
              "sequence_number": 3,
              "element_type": "mirror_field",
              "lookup_field": {
                "id": "3359388000000000523",
                "api_name": "Account_Name"
              }
            }
          ]
        }
      ]
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — Success

Layout updated successfully with confirmation details

```json
{
  "layouts": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "3722469000001346011"
      },
      "message": "layout updated",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidFieldId

Invalid field ID provided

```json
{
  "layouts": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.layouts[0].sections[0].fields[0].id"
      },
      "message": "the id given seems to be invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidTabTraversal

Invalid data type for tab traversal value

```json
{
  "layouts": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "text",
        "api_name": "tab_traversal",
        "json_path": "$.layouts[0].sections[0].tab_traversal"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — SystemKeywordNotAllowed

Layout name contains a reserved system keyword

```json
{
  "layouts": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "name",
        "json_path": "$.layouts[0].name"
      },
      "message": "System keyword not allowed in layout label",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — RequiredParamMissing

Required module parameter missing from request

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

### Status `400` — `application/json` — InvalidModule

Invalid module name provided

```json
{
  "code": "INVALID_MODULE",
  "details": {},
  "message": "the module name given seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidSectionIdOrApiName

Section missing required ID or display label

```json
{
  "layouts": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_fields": [
          {
            "api_name": "id",
            "json_path": "$.layouts[0].sections[0].id"
          },
          {
            "api_name": "display_label",
            "json_path": "$.layouts[0].sections[0].display_label"
          }
        ]
      },
      "message": "should contain either id or display_label",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingForSection

Section ID or api_name absent during a section operation

```json
{
  "layouts": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "_delete",
          "json_path": "$.layouts[0].sections[0]._delete"
        },
        "api_name": "api_name",
        "json_path": "$.layouts[0].sections[0].api_name"
      },
      "message": "section id or api_name is missing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingForField

Field ID or field_label absent during a field operation

```json
{
  "layouts": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_fields": [
          {
            "api_name": "id",
            "json_path": "$.layouts[0].sections[0].fields[0].id"
          },
          {
            "api_name": "field_label",
            "json_path": "$.layouts[0].sections[0].fields[0].field_label"
          }
        ]
      },
      "message": "should contain either id or field_label",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NotAllowedRelatedFieldLengthHigher

Related field length exceeds target field length in FoL mapping

```json
{
  "layouts": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "id",
        "json_path": "$.layouts[0].sections[0].fields[0].association_details.related_field.id"
      },
      "message": "related field length is higher",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchFieldLength

Field length and related field length incompatible for FoL mapping

```json
{
  "layouts": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "length",
          "json_path": "$.layouts[0].sections[0].fields[0].length"
        },
        "api_name": "id",
        "json_path": "$.layouts[0].sections[0].fields[0].association_details.related_field.id"
      },
      "message": "Field length mismatch for FOL mapping",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NotSupportedAssociationDetails

Field-of-Lookup association not supported for the specified field

```json
{
  "layouts": [
    {
      "code": "NOT_SUPPORTED",
      "details": {
        "api_name": "association_details",
        "json_path": "$.layouts[0].sections[0].fields[0].association_details"
      },
      "message": "Field of lookup association is not supported for this field",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — FeatureNotSupportedAssociationDetails

License does not support Field-of-Lookup feature

```json
{
  "layouts": [
    {
      "code": "FEATURE_NOT_SUPPORTED",
      "details": {
        "api_name": "association_details",
        "json_path": "$.layouts[0].sections[0].fields[0].association_details"
      },
      "message": "Your License does not support this feature",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — LimitExceededFoLMapping

Field-of-Lookup mapping limit reached for lookup

```json
{
  "layouts": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "limit": 5,
        "limit_due_to": [
          {
            "api_name": "id",
            "json_path": "$.layouts[0].sections[0].fields[0].association_details.lookup_field.id"
          }
        ]
      },
      "message": "Field of Lookup mapping limit is reached for the lookup",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — AmbiguityDuringProcessingRelatedField

Ambiguity detected when both ID and api_name identify different related_fields

```json
{
  "layouts": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "details": {
        "ambiguity_due_to": [
          {
            "api_name": "id",
            "json_path": "$.layouts[0].sections[0].fields[0].association_details.related_field.id"
          },
          {
            "api_name": "api_name",
            "json_path": "$.layouts[0].sections[0].fields[0].association_details.related_field.api_name"
          }
        ]
      },
      "message": "ambiguity while processing the related_field",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ExpectedFieldMissingRelatedField

No ID or api_name supplied for related_field in association_details

```json
{
  "layouts": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_fields": [
          {
            "api_name": "id",
            "json_path": "$.layouts[0].sections[0].fields[0].association_details.related_field.id"
          },
          {
            "api_name": "api_name",
            "json_path": "$.layouts[0].sections[0].fields[0].association_details.related_field.api_name"
          }
        ]
      },
      "message": "One of the required fields is missing",
      "status": "error"
    }
  ]
}
```

### Status `401` — `application/json` — AuthenticationFailure

Authentication failure

```json
{
  "code": "AUTHENTICATION_FAILURE",
  "details": {},
  "message": "Authentication failed",
  "status": "error"
}
```

### Status `401` — `application/json` — OAuthScopeMismatch

OAuth scope mismatch

```json
{
  "code": "OAUTH_SCOPE_MISMATCH",
  "details": {},
  "message": "Invalid oauth scope to access this URL",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermission

CRM profile lacks permission to update layouts

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Customize_Zoho_CRM"
    ]
  },
  "message": "permission denied",
  "status": "error"
}
```

### Status `405` — `application/json` — InvalidMethod

Invalid HTTP method used for this endpoint

```json
{
  "code": "INVALID_REQUEST_METHOD",
  "details": {},
  "message": "The http request method type is not a valid one",
  "status": "error"
}
```

### Status `500` — `application/json` — InternalError

Server error

```json
{
  "code": "INTERNAL_ERROR",
  "details": {},
  "message": "Internal Server Error",
  "status": "error"
}
```
