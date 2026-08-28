# Layout Activate and Deactivate API

- [OpenAPI specification](layouts_activate_deactivate.yaml)
- [Activate Layout](mds/activateLayout.md)
  - Activates a single deactivated layout, making it available for use within the specified module. Optionally allows adding or removing profile associations during activation. Only one layout can be activated per request. This operation is idempotent - attempting to activate an already active layout returns an error (ALREADY_ACTIVATED). The status key in the response from the [Get Layouts API](layouts.yaml#$.paths./settings/layouts.get) indicates whether the layout is active or inactive.
  - [Examples](mds/examples/activateLayout.md)
- [Deactivate Layout](mds/layoutDeactivate.md)
  - Deactivates an active layout and transfers its configuration (profile associations, permissions, field mappings) to another active layout within the same module. At least one active layout must remain in the module. This operation is idempotent - attempting to deactivate an already deactivated layout returns an error (ALREADY_DEACTIVATED).
  - [Examples](mds/examples/layoutDeactivate.md)
