# Call Preferences

- [OpenAPI specification](call_preferences.yaml)
- [Call Preferences](mds/getCallPreferences.md)
  - To retrieve the current Call Preferences configuration for your Zoho CRM organization. The response reports whether the **From Number** and **To Number** fields are currently enabled on records in the Calls module.
  - [Examples](mds/examples/getCallPreferences.md)
- [Call Preferences](mds/updateCallPreferences.md)
  - To update the Call Preferences configuration for your Zoho CRM organization by enabling or disabling the **From Number** and **To Number** fields on records in the Calls module. A preference cannot be disabled when the corresponding field is marked as mandatory, when it is referenced by a Validation Rule, Layout Rule, Blueprint, or Workflow, or when the organization has an active telephony integration or active calendar booking for calls that depends on it.
  - [Examples](mds/examples/updateCallPreferences.md)
