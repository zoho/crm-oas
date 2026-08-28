# Examples: getNotifications

**GET /actions/watch**

## Response examples

### Status `200` — `application/json` — Sample

Successful response listing active notification channels

```json
{'watch': [{'notify_on_related_action': False, 'channel_expiry': TimeStamp(2023, 8, 2, 16, 51, 3, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=46800), '-11:00')), 'return_affected_field_values': False, 'resource_uri': 'https://www.zohoapis.com/crm/v8/Leads', 'resource_id': '554023000000000125', 'notify_url': 'https://webhook.site/2c9xxx0fa9', 'resource_name': 'Leads', 'fields': None, 'notification_condition': [{'field_selection': {'group_operator': 'and', 'group': [{'field': {'api_name': 'Last_Name', 'id': '554023000000000559'}, 'group_operator': None, 'group': None}, {'field': {'api_name': 'Full_Name', 'id': '554023000000000597'}, 'group_operator': None, 'group': None}]}, 'module': {'api_name': 'Leads', 'id': '554023000000000125'}, 'type': 'field_selection'}], 'channel_id': '1000000068001', 'events': ['Leads.edit', 'Leads.create', 'Leads.delete'], 'token': 'xyz'}, {'notify_on_related_action': False, 'channel_expiry': TimeStamp(2023, 8, 11, 2, 12, 33, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=46800), '-11:00')), 'return_affected_field_values': False, 'resource_uri': 'https://www.zohoapis.com/crm/v8/Contacts', 'resource_id': '554023000000000129', 'notify_url': 'https://webhook.site/2c9axx20fa9', 'resource_name': 'Contacts', 'fields': None, 'notification_condition': None, 'channel_id': '10000', 'events': ['Contacts.create'], 'token': 'deals.all.notif'}, {'notify_on_related_action': False, 'channel_expiry': TimeStamp(2023, 8, 11, 2, 13, 1, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=46800), '-11:00')), 'return_affected_field_values': False, 'resource_uri': 'https://www.zohoapis.com/crm/v8/Deals', 'resource_id': '554023000000000131', 'notify_url': 'https://webhook.site/2c9a0xx20fa9', 'resource_name': 'Deals', 'fields': None, 'notification_condition': [{'field_selection': {'group_operator': 'or', 'group': [{'field': {'api_name': 'Stage', 'id': '554023000000000525'}, 'group_operator': None, 'group': None}, {'group_operator': 'or', 'group': [{'field': {'api_name': 'Account_Name', 'id': '554023000000000523'}, 'group_operator': None, 'group': None}, {'field': {'api_name': 'Lead_Source', 'id': '554023000000000535'}, 'group_operator': None, 'group': None}]}]}, 'module': {'api_name': 'Deals', 'id': '554023000000000131'}, 'type': 'field_selection'}], 'channel_id': '10000', 'events': ['Deals.edit', 'Deals.create', 'Deals.delete'], 'token': 'deals.all.notif'}], 'info': {'per_page': 200, 'count': 3, 'page': 1, 'more_records': False}}
```

### Status `400` — `application/json` — MandatoryNotFound

Required field notify_url missing from the request

```json
{
  "code": "MANDATORY_NOT_FOUND",
  "message": "required field not found",
  "details": {
    "api_name": "notify_url"
  },
  "status": "error"
}
```

### Status `400` — `application/json` — ModuleNotSupported

Unsupported module referenced in the events field

```json
{
  "code": "INVALID_DATA",
  "message": "invalid data",
  "details": {
    "api_name": "events"
  },
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidFieldInFields

Invalid field reference in the fields parameter

```json
{
  "code": "INVALID_DATA",
  "message": "invalid data",
  "details": {
    "api_name": "fields",
    "json_path": "$.watch[0].fields[1]"
  },
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidNotificationConditionDataType

Invalid data type for the notification_condition field

```json
{
  "code": "INVALID_DATA",
  "message": "invalid data",
  "details": {
    "api_name": "notification_condition",
    "json_path": "$.watch[0].notification_condition"
  },
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataTypeForUnderscoreDelete

Invalid data type for the _delete field

```json
{
  "code": "INVALID_DATA",
  "message": "invalid data",
  "details": {
    "api_name": "_delete",
    "expected_data_type": "boolean",
    "json_path": "$.watch[0]._delete"
  },
  "status": "error"
}
```

### Status `400` — `application/json` — RequestFieldModuleNotAvailableInNotificationCondition

Specified module is not available in the notification condition

```json
{
  "code": "INVALID_DATA",
  "message": "required field not found",
  "details": {
    "api_name": "module",
    "json_path": "$.watch[0].notification_condition[0].module"
  },
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataTypeForModuleInNotificationCondition

Invalid data type for the module field in the notification condition

```json
{
  "code": "INVALID_DATA",
  "message": "invalid data",
  "details": {
    "api_name": "module",
    "expected_data_type": "jsonobject",
    "json_path": "$.watch[0].notification_condition[0].module"
  },
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataTypeForApiNameInModuleOfNotificationCondition

Invalid data type for api_name in the notification condition module

```json
{
  "code": "INVALID_DATA",
  "message": "invalid data",
  "details": {
    "api_name": "api_name",
    "expected_data_type": "string",
    "json_path": "$.watch[0].notification_condition[0].module.api_name"
  },
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataTypeForIdInModuleOfNotificationCondition

Invalid data type for the module ID field in the notification condition

```json
{
  "code": "INVALID_DATA",
  "message": "invalid data",
  "details": {
    "api_name": "id",
    "expected_data_type": "string",
    "json_path": "$.watch[0].notification_condition[0].module.api_name"
  },
  "status": "error"
}
```

### Status `400` — `application/json` — BothApiNameAndIdIsMissingInModuleOfNotificationCondition

Both api_name and module ID missing from the notification condition

```json
{
  "code": "EXPECTED_FIELD_MISSING",
  "message": "Specify atleast one field",
  "details": {
    "expected_fields": [
      {
        "api_name": "api_name",
        "json_path": "$.watch[0].notification_condition[0].module.api_name"
      },
      {
        "api_name": "id",
        "json_path": "$.watch[0].notification_condition[0].module.id"
      }
    ]
  },
  "status": "error"
}
```

### Status `400` — `application/json` — AmbiguityWhileProcessingModuleApiNameAndIdInNotificationCondition

Ambiguity between api_name and module ID in the notification condition

```json
{
  "code": "AMBIGUITY_DURING_PROCESSING",
  "message": "AMBIGUITY_DURING_PROCESSING",
  "details": {
    "ambiguity_due_to": [
      {
        "api_name": "api_name",
        "json_path": "$.watch[0].notification_condition[0].module.api_name"
      },
      {
        "api_name": "id",
        "json_path": "$.watch[0].notification_condition[0].module.id"
      }
    ]
  },
  "status": "error"
}
```

### Status `400` — `application/json` — DependentFieldMissingInModuleOfNotificationCondition

Dependent field field_selection missing from the notification condition

```json
{
  "code": "DEPENDENT_FIELD_MISSING",
  "message": "DEPENDENT_FIELD_MISSING",
  "details": {
    "api_name": "field_selection",
    "json_path": "$.watch[0].notification_condition[0].field_selection",
    "dependee": {
      "api_name": "type",
      "json_path": "$.watch[0].notification_condition[0].type"
    }
  },
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataTypeForFieldSelection

Invalid data type for the field_selection field

```json
{
  "code": "INVALID_DATA",
  "message": "invalid data",
  "details": {
    "api_name": "field_selection",
    "json_path": "$.watch[0].notification_condition[0].field_selection",
    "expected_data_type": "jsonobject"
  },
  "status": "error"
}
```

### Status `400` — `application/json` — MandatoryGroupOperatorNotFound

Required group_operator field missing from the field_selection

```json
{
  "code": "MANDATORY_NOT_FOUND",
  "message": "required field not found",
  "details": {
    "api_name": "group_operator",
    "json_path": "$.watch[0].notification_condition[0].field_selection.group_operator"
  },
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataTypeForGroupOperator

Invalid data type for the group_operator field

```json
{
  "code": "INVALID_DATA",
  "message": "invalid data",
  "details": {
    "api_name": "group_operator",
    "json_path": "$.watch[0].notification_condition[0].field_selection.group_operator",
    "expected_data_type": "text"
  },
  "status": "error"
}
```

### Status `400` — `application/json` — UnsupportedValueForGroupOperator

Unsupported value for the group_operator field

```json
{
  "code": "INVALID_DATA",
  "message": "invalid data",
  "details": {
    "api_name": "group_operator",
    "json_path": "$.watch[0].notification_condition[0].field_selection.group_operator",
    "supported_values": [
      "or",
      "and"
    ]
  },
  "status": "error"
}
```

### Status `400` — `application/json` — MandatoryFieldOrGroupNotFound

Required field or group array missing from the notification condition

```json
{
  "code": "MANDATORY_NOT_FOUND",
  "message": "required field not found",
  "details": {
    "api_name": "field",
    "json_path": "$.watch[0].notification_condition.field_selection.field"
  },
  "status": "error"
}
```

### Status `400` — `application/json` — NotificationCriteriaLimitExceeded

Field reference limit exceeded in the field_selection

```json
{
  "code": "INVALID_DATA",
  "message": "invalid data",
  "details": {
    "api_name": "field_selection",
    "json_path": "$.watch[0].notification_condition.field_selection",
    "maximum_length": 10
  },
  "status": "error"
}
```

### Status `400` — `application/json` — MandatoryTypeNotFound

Required type field missing from the notification condition

```json
{
  "code": "MANDATORY_NOT_FOUND",
  "message": "required field not found",
  "details": {
    "api_name": "type",
    "json_path": "$.watch[0].notification_condition[0].type"
  },
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataTypeForType

Invalid data type for the type field

```json
{
  "code": "INVALID_DATA",
  "message": "invalid data",
  "details": {
    "api_name": "type",
    "json_path": "$.watch[0].notification_condition[0].type",
    "expected_data_type": "text"
  },
  "status": "error"
}
```

### Status `400` — `application/json` — UnsupportedValueForType

Unsupported value for the type field

```json
{
  "code": "INVALID_DATA",
  "message": "invalid data",
  "details": {
    "api_name": "type",
    "json_path": "$.watch[0].notification_condition[0].type",
    "supported_values": [
      "field_selection"
    ]
  },
  "status": "error"
}
```

### Status `401` — `application/json` — OauthScopeMismatch

Missing required OAuth scope

```json
{
  "code": "OAUTH_SCOPE_MISMATCH",
  "message": "Unauthorized",
  "status": "error"
}
```

### Status `429` — `application/json` — RateLimitExceeded

API rate limit exceeded

```json
{
  "code": "RATE_LIMIT_EXCEEDED",
  "message": "Too many requests. Please try again later.",
  "status": "error"
}
```

### Status `500` — `application/json` — Sample

Unexpected internal server error

```json
{
  "code": "INTERNAL_ERROR",
  "message": "An unexpected error occurred.",
  "status": "error"
}
```
