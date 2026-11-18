# GET /settings/blueprints/usage_configurations
**Operation:** `getBlueprintUsageConfigurations` — Get blueprint usage configurations
> To retrieve the configuration details required to configure a blueprint for a specific module in your Zoho CRM organization.

**Parameters:**
- `module` (query, string, required) [maxLen=255] {style=form, explode=True}: Specify the API name of the module. Refer to the [Get Modules](modules.yaml#$.paths./settings/modules.get) resource for valid values.

**Schemas:**
`ActionSubOption`:
  > Represents the metadata of a sub-action, including its API name, internal name, and display label.
  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the sub-action.
  - `name` (string) **REQ** [maxLen=255] — Represents the internal name of the sub-action.
  - `display_name` (string) **REQ** [maxLen=255] — Represents the display label of the sub-action.
  additionalProperties: any

**Responses:**

- **200**: Returns the blueprint usage configuration details required to configure a blueprint for the specified module. — Schema: `BlueprintUsageConfigurationsResponse` [application/json]
    > Contains the list of Blueprint usage configuration objects returned in a successful response.
    schema: `BlueprintUsageConfigurationsResponse`
    - `blueprints` (array of object `BlueprintUsageConfiguration`) [maxItems=1] **REQ** — List of Blueprint usage configuration objects for the module, each detailing the capabilities, limits, and constraints per Blueprint element.
      schema: `BlueprintUsageConfiguration`
      - `timebox` (object `TimeboxConfiguration`) **REQ** — Represents the timeboxing configuration, including the allowed periods and minimum values.
        schema: `TimeboxConfiguration`
        - `period` (array of object `TimeboxPeriodOption`) [maxItems=5] **REQ** — Represents the timebox period of the Blueprint.
          schema: `TimeboxPeriodOption`
          - `name` (string) **REQ** [maxLen=255] — Represents the internal name of the timebox period option.
          - `display_name` (string) **REQ** [maxLen=255] — Represents the display label of the timebox period option.
        - `minimum_values` (object `TimeboxMinimumValues`) **REQ** — Represents the minimum unit and period required when timeboxing is enabled.
          schema: `TimeboxMinimumValues`
          - `unit` (integer/int32) **REQ** — Represents the numeric minimum value of the timebox, such as **15**.
          - `period` (string) **REQ** [maxLen=255] — Represents the unit of time for the minimum timebox, such as **minutes**.
      - `process` (object `ProcessUsageConstraints`) **REQ** — Represents the constraints for defining a process, including name and description validation and the supported type values.
        schema: `ProcessUsageConstraints`
        - `name` (object `ProcessNameConstraints`) **REQ** — Represents the validation rules for process names in Blueprint usage configurations, including the unsupported characters and the maximum length.
          schema: `ProcessNameConstraints`
          - `unsupported_characters` (array of string) [maxItems=25] **REQ** — List of characters not allowed in the Blueprint process name.
            items: [maxLen=255]
          - `max_length` (integer/int32) **REQ** — Represents the maximum allowed length of the Blueprint process name.
        - `description` (object `ProcessDescriptionConstraints`) **REQ** — Represents the validation rules for process descriptions, including the unsupported characters and the maximum permitted length.
          schema: `ProcessDescriptionConstraints`
          - `unsupported_characters` (array of string) [maxItems=25] **REQ** — List of characters not allowed in the Blueprint process description.
            items: [maxLen=255]
          - `max_length` (integer/int32) **REQ** — Represents the maximum allowed length of the Blueprint process description.
        - `type` (array of object) [maxItems=2] **REQ** — List of supported process types.
          oneOf:
            - `BlueprintTypeCompatibility` — Declares the Blueprint type and identifies the components that are unsupported by that type.
              - `blueprint_type` (string) **REQ** [maxLen=255] — Represents the internal name of the Blueprint type.
              - `unsupported_components` (null) **REQ** — Reserved for future use.
            - `BlueprintTypeUnsupportedComponents` — Specifies a Blueprint type and the components that are unsupported for that type.
              - `blueprint_type` (string) **REQ** [maxLen=255] — Represents the internal name of the Blueprint type.
              - `unsupported_components` (array of object) [maxItems=2] **REQ** — List of components unsupported by the Blueprint type.
                oneOf:
                  - `UnsupportedComponentInputRules` — Identifies an unsupported component and lists the input sub-components that cannot be used with it.
                    - `name` (string) **REQ** [maxLen=255] — Represents the name of the unsupported component.
                    - `input_components` (array of string) [maxItems=2] **REQ** — List of input sub-components that cannot be used with the component.
                      items: [maxLen=255]
                  - `UnsupportedComponentTypeRules` — Defines the types that are not allowed for a named component in the current Blueprint context.
                    - `types` (array of string) [maxItems=1] **REQ** — List of component types that are not allowed for the component.
                      items: [maxLen=255]
                    - `name` (string) **REQ** [maxLen=255] — Represents the name of the component.
      - `owners` (object `OwnerSelectionConstraints`) **REQ** — Represents the allowed owner types, the maximum number of selectable owners, and the display label used in the CRM UI.
        schema: `OwnerSelectionConstraints`
        - `types` (array of string) [maxItems=6] **REQ** — List of the allowed owner types that can be selected.
          items: [maxLen=255]
        - `limit` (integer/int32) **REQ** — Represents the maximum number of owners that can be selected.
        - `display_name` (string) **REQ** [maxLen=255] — Represents the display label of the owner selector.
      - `transitions` (object `TransitionUsageConstraints`) **REQ** — Represents the rules for transitions, including trigger type options and name and description validation constraints.
        schema: `TransitionUsageConstraints`
        - `trigger_type` (array of object `TransitionTriggerTypeProfileDetailed`) [maxItems=50] **REQ** — List of trigger types available for the transition.
          schema: `TransitionTriggerTypeProfileDetailed`
          - `supported_transition_types` (array of object `TransitionTypeSupportProfileDetailed`) [maxItems=3] **REQ** — List of transition types supported by the trigger type.
            schema: `TransitionTypeSupportProfileDetailed`
            - `supported_components` (array of object `TransitionTypeSupportedComponent`) [maxItems=50] **REQ** — List of components allowed in the transition type.
              schema: `TransitionTypeSupportedComponent`
              - `mandate_subcomponent` (boolean) **REQ** — Indicates whether choosing sub-components is mandatory for the component.
Possible values:
**true** - Choosing sub-components is mandatory.
**false** - Choosing sub-components is not mandatory.
              - `name` (string) **REQ** [maxLen=255] — Represents the name of the component.
              - `supported_subcomponents` (array of string) [maxItems=50, nullable] **REQ** — List of sub-components that the component supports, or null when none are available.
                items: [maxLen=255]
            - `name` (string) **REQ** [maxLen=255] — Represents the internal name of the transition type.
            - `limit` (integer/int32) **REQ** [nullable] — Represents the maximum number of times the transition type can be used, or null when no limit applies.
            - `common_source` (boolean) **REQ** — Indicates whether the transitions of this type share a common source state.
Possible values:
**true** - The transitions share a common source state.
**false** - The transitions do not share a common source state.
          - `name` (string) **REQ** [maxLen=255] — Represents the internal name of the transition trigger type.
        - `name` (object `TransitionNameConstraints`) **REQ** — Represents the validation rules for transition names, including the unsupported characters and the maximum length.
          schema: `TransitionNameConstraints`
          - `unsupported_characters` (array of string) [maxItems=25] **REQ** — List of characters that are not allowed in a transition name.
            items: [maxLen=255]
          - `max_length` (integer/int32) **REQ** — Represents the maximum number of characters allowed in a transition name.
        - `description` (object `TransitionDescriptionConstraints`) **REQ** — Represents the validation rules for transition descriptions, including the unsupported characters and the maximum length.
          schema: `TransitionDescriptionConstraints`
          - `unsupported_characters` (array of string) [maxItems=25] **REQ** — List of characters that are not allowed in a transition description.
            items: [maxLen=255]
          - `max_length` (integer/int32) **REQ** — Represents the maximum number of characters allowed in a transition description.
      - `input_components` (object `InputComponentConstraints`) **REQ** — Represents the allowed input component types and the maximum number permitted.
        schema: `InputComponentConstraints`
        - `types` (array of object) [maxItems=8] **REQ** — List of input component types permitted, along with their capabilities.
          oneOf:
            - `ComponentTypeCapability` — Represents a component type's validation support, standalone behavior, per-component limits, and unsupported values.
              - `validation_supported` (boolean) **REQ** — Indicates whether validation is supported for this component type.
Possible values:
**true** - Validation is supported for this component type.
**false** - Validation is not supported for this component type.
              - `sub_components` (null) — Reserved for future use.
              - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the component type.
              - `name` (string) **REQ** [maxLen=255] — Represents the name of the component type.
              - `standalone_component` (boolean) **REQ** — Indicates whether the component can be used as a standalone component.
Possible values:
**true** - The component can be used as a standalone component.
**false** - The component cannot be used as a standalone component.
              - `limit_per_component` (integer/int32) **REQ** [nullable] — Represents the maximum number of times the component type can be used within a single component.
              - `unsupported_values` (array of string) [maxItems=1] **REQ** — List of values that the component type cannot use.
                items: [maxLen=255]
            - `ComponentTypeCapabilityWithSubtypes` — Represents the capabilities of a component type, including its validation support and the list of supported component sub-types.
              - `validation_supported` (boolean) **REQ** — Indicates whether validation is supported for the component type.
Possible values:
**true** - Validation is supported for the component type.
**false** - Validation is not supported for the component type.
              - `sub_components` (array of object `ComponentSubTypeCapability`) [maxItems=3] **REQ** — List of component sub-types supported by the component.
                schema: `ComponentSubTypeCapability`
                - `validation_supported` (boolean) **REQ** — Indicates whether validation is supported for the component sub-type.
Possible values:
**true** - Validation is supported for the component sub-type.
**false** - Validation is not supported for the component sub-type.
                - `sub_components` (null) — Reserved for future use.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name that identifies the component sub-type.
                - `name` (string) **REQ** [maxLen=255] — Represents the name that identifies the component sub-type.
                - `standalone_component` (boolean) **REQ** — Indicates whether the component can be used as a standalone component.
Possible values:
**true** - The component can be used as a standalone component.
**false** - The component cannot be used as a standalone component.
                - `limit_per_component` (integer/int32) **REQ** — Represents the maximum number of times the component sub-type can be used within a single component.
                - `unsupported_values` (null) **REQ** — Reserved for future use.
              - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the component type.
              - `name` (string) **REQ** [maxLen=255] — Represents the name that identifies the component type.
              - `standalone_component` (boolean) **REQ** — Indicates whether the component can be used as a standalone component.
Possible values:
**true** - The component can be used as a standalone component.
**false** - The component cannot be used as a standalone component.
              - `limit_per_component` (integer/int32) **REQ** [nullable] — Represents the maximum number of times the component type can be used within a single component.
              - `unsupported_values` (null) **REQ** — Reserved for future use.
            - `ComponentTypeCapabilityBasic` — Represents the basic capabilities of a component type, where per-component limits and unsupported values may be unspecified.
              - `validation_supported` (boolean) **REQ** — Indicates whether validation is supported for this component type.
Possible values:
**true** - Validation is supported for this component type.
**false** - Validation is not supported for this component type.
              - `sub_components` (null) — Reserved for future use.
              - `api_name` (string) **REQ** [maxLen=255] — Represents the API name that identifies the component type.
              - `name` (string) **REQ** [maxLen=255] — Represents the name that identifies the component type.
              - `standalone_component` (boolean) **REQ** — Indicates whether the component can be used as a standalone component.
Possible values:
**true** - The component can be used as a standalone component.
**false** - The component cannot be used as a standalone component.
              - `limit_per_component` (null) **REQ** — Reserved for future use.
              - `unsupported_values` (null) **REQ** — Reserved for future use.
            - `ComponentTypeCapabilityConstrained` — Represents the capabilities of a component type with an explicit per-component limit.
              - `validation_supported` (boolean) **REQ** — Indicates whether validation is supported for the component type.
Possible values:
**true** - Validation is supported for the component type.
**false** - Validation is not supported for the component type.
              - `sub_components` (null) — Reserved for future use.
              - `api_name` (string) **REQ** [maxLen=255] — Represents the API name that identifies the component type.
              - `name` (string) **REQ** [maxLen=255] — Represents the name that identifies the component type.
              - `standalone_component` (boolean) **REQ** — Indicates whether the component can be used as a standalone component.
Possible values:
**true** - The component can be used as a standalone component.
**false** - The component cannot be used as a standalone component.
              - `limit_per_component` (integer/int32) **REQ** — Represents the maximum number of times the component type can be used within a single component.
              - `unsupported_values` (null) **REQ** — Reserved for future use.
        - `limit` (integer/int32) **REQ** — Represents the maximum number of input components permitted.
      - `actions` (array of object) [maxItems=14] **REQ** — List of capability profile objects for the actions in the Blueprint, detailing the limits and constraints of each action.
        oneOf:
          - `ActionCapabilityProfile` — Represents the capabilities and limits of an action, including availability flags, sub-actions, and presentation metadata.
            - `new` (boolean) **REQ** — Indicates whether the action is newly available.
Possible values:
**true** - The action is newly available.
**false** - The action is not newly available.
            - `sub_actions` (array of object `ActionSubOption`) [maxItems=6] **REQ** — List of sub-action objects nested under this Blueprint action.
            - `associate_action` (boolean) **REQ** — Indicates whether the action can be associated with a Blueprint transition.
Possible values:
**true** - The action can be associated with a Blueprint transition.
**false** - The action cannot be associated with a Blueprint transition.
            - `limit_per_action` (integer/int32) **REQ** [nullable] — Represents the maximum number of times the action can be used.
            - `execute_type` (null) — Reserved for future use.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the Blueprint action.
            - `mandate_subactions` (boolean) — Indicates whether sub-actions are mandatory for the action.
Possible values:
**true** - Sub-actions are mandatory for the action.
**false** - Sub-actions are not mandatory for the action.
            - `clickable` (boolean) **REQ** — Indicates whether the action is clickable in the CRM UI.
Possible values:
**true** - The action is clickable in the CRM UI.
**false** - The action is not clickable in the CRM UI.
            - `name` (string) **REQ** [maxLen=255] — Represents the internal name of the Blueprint action.
            - `limit` (integer/int32) **REQ** — Represents the maximum number of actions allowed in the Blueprint.
            - `display_name` (string) **REQ** [maxLen=255] — Represents the display label of the Blueprint action.
          - `ActionCapabilityProfileBasic` — Represents the basic capabilities of an action, with usage limits and interaction flags where the per-action sub-action limit may be undefined.
            - `new` (boolean) **REQ** — Indicates whether the action is newly available in the Blueprint.
Possible values:
**true** - The action is newly available.
**false** - The action is not newly available.
            - `sub_actions` (null) — Reserved for future use.
            - `associate_action` (boolean) **REQ** — Indicates whether the action can be associated with a Blueprint transition.
Possible values:
**true** - The action can be associated with a Blueprint transition.
**false** - The action cannot be associated with a Blueprint transition.
            - `limit_per_action` (integer/int32) **REQ** [nullable] — Represents the maximum number of times the action can be used, or null when no per-action limit applies.
            - `execute_type` (null) — Reserved for future use.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the Blueprint action.
            - `mandate_subactions` (boolean) — Indicates whether sub-actions are mandatory for the Blueprint action.
Possible values:
**true** - Sub-actions are mandatory for the action.
**false** - Sub-actions are not mandatory for the action.
            - `clickable` (boolean) **REQ** — Indicates whether the action is clickable in the CRM UI.
Possible values:
**true** - The action is clickable in the CRM UI.
**false** - The action is not clickable in the CRM UI.
            - `name` (string) **REQ** [maxLen=255] — Represents the internal name of the Blueprint action.
            - `limit` (integer/int32) **REQ** — Represents the maximum number of actions allowed in the Blueprint.
            - `display_name` (string) **REQ** [maxLen=255] — Represents the display label of the Blueprint action shown in the CRM UI.
          - `ActionCapabilityProfileWithRestrictions` — Represents the capabilities of an action, including unsupported actions, usage limits, and interaction flags.
            - `new` (boolean) **REQ** — Indicates whether the action is newly available.
Possible values:
**true** - The action is newly available.
**false** - The action is not newly available.
            - `sub_actions` (null) — Reserved for future use.
            - `associate_action` (boolean) **REQ** — Indicates whether the action can be associated with a Blueprint transition.
Possible values:
**true** - The action can be associated with a Blueprint transition.
**false** - The action cannot be associated with a Blueprint transition.
            - `limit_per_action` (integer/int32) **REQ** [nullable] — Represents the maximum number of times the action can be used, or null when no per-action usage limit applies.
            - `execute_type` (null) — Reserved for future use.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the Blueprint action.
            - `clickable` (boolean) **REQ** — Indicates whether the action is clickable in the CRM UI.
Possible values:
**true** - The action is clickable in the CRM UI.
**false** - The action is not clickable in the CRM UI.
            - `name` (string) **REQ** [maxLen=255] — Represents the internal name of the Blueprint action.
            - `limit` (integer/int32) **REQ** — Represents the maximum number of actions allowed in the Blueprint.
            - `display_name` (string) **REQ** [maxLen=255] — Represents the display label of the Blueprint action shown in the CRM UI.
            - `mandate_subactions` (boolean) — Indicates whether the sub-actions of the action are mandatory.
Possible values:
**true** - The sub-actions of the action are mandatory.
**false** - The sub-actions of the action are not mandatory.
            - `unsupported_actions` (array of string) [maxItems=3] **REQ** — List of the names of the actions that the Blueprint does not support.
              items: [maxLen=255]
          - `ActionCapabilityProfileWithExecution` — Represents the capabilities of an action, including execution types, sub-action rules, and usage limits.
            - `new` (boolean) **REQ** — Indicates whether the Blueprint action is newly available.
Possible values:
**true** - The action is newly available.
**false** - The action is not newly available.
            - `sub_actions` (array of object `ActionSubOption`) [maxItems=6] **REQ** — List of sub-action objects nested under the Blueprint action.
            - `associate_action` (boolean) **REQ** — Indicates whether the action can be associated with a Blueprint transition.
Possible values:
**true** - The action can be associated with a Blueprint transition.
**false** - The action cannot be associated with a Blueprint transition.
            - `limit_per_action` (integer/int32) **REQ** [nullable] — Represents the maximum number of times the action can be used.
            - `execute_type` (array of object) [maxItems=3] **REQ** — List of execution types supported by the action.
              oneOf:
                - `ActionExecutionTypeProfile` — Represents a supported execution type, whether a timebox is required, and the allowed period options.
                  - `period` (array of object `ExecutionPeriodOption`) [maxItems=5] **REQ** — List of the execution periods allowed for the action, such as minute, hour, or day.
                    schema: `ExecutionPeriodOption`
                    - `name` (string) **REQ** [maxLen=255] — Represents the internal name of the execution period option.
                    - `display_name` (string) **REQ** [maxLen=255] — Represents the display label of the execution period option.
                  - `timebox_required` (boolean) **REQ** — Indicates whether a timebox period is required for the execution type.
Possible values:
**true** - A timebox period is required for the execution type.
**false** - A timebox period is not required for the execution type.
                  - `name` (string) **REQ** [maxLen=255] — Represents the internal name of the execution type.
                - `ActionExecutionTypeProfileBasic` — Represents the basic metadata of an execution type, where period options may be unspecified.
                  - `timebox_required` (boolean) **REQ** — Indicates whether a timebox period is required for the execution type.
Possible values:
**true** - A timebox period is required for the execution type.
**false** - A timebox period is not required for the execution type.
                  - `name` (string) **REQ** [maxLen=255] — Represents the internal name of the execution type.
                  - `period` (null) **REQ** — Reserved for future use.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the Blueprint action.
            - `mandate_subactions` (boolean) **REQ** — Indicates whether the sub-actions of the Blueprint action are mandatory.
Possible values:
**true** - The sub-actions are mandatory.
**false** - The sub-actions are not mandatory.
            - `clickable` (boolean) **REQ** — Indicates whether the action is clickable in the CRM UI.
Possible values:
**true** - The action is clickable in the CRM UI.
**false** - The action is not clickable in the CRM UI.
            - `name` (string) **REQ** [maxLen=255] — Represents the internal name of the Blueprint action.
            - `limit` (integer/int32) **REQ** — Represents the maximum number of actions allowed in the Blueprint.
            - `display_name` (string) **REQ** [maxLen=255] — Represents the display label of the Blueprint action.
      - `states` (object `StateUsageConstraints`) **REQ** — Represents the limits and component support rules for states in a Blueprint, including the maximum count and the allowed components.
        schema: `StateUsageConstraints`
        - `supported_components` (array of object) [maxItems=2] **REQ** — List of component policies that define the components allowed on a state.
          oneOf:
            - `SupportedComponentPolicy` — Declares a supported component, indicates whether sub-components are mandatory, and lists the allowed sub-components.
              - `mandate_subcomponent` (boolean) **REQ** — Indicates whether choosing sub-components is mandatory for the component.
Possible values:
**true** - Choosing sub-components is mandatory.
**false** - Choosing sub-components is not mandatory.
              - `name` (string) **REQ** [maxLen=255] — Represents the name of the component.
              - `supported_subcomponents` (array of string) [maxItems=15] **REQ** — List of sub-components that the component supports.
                items: [maxLen=255]
            - `SupportedComponentPolicyNullableSubcomponents` — Represents a supported component policy in which sub-components can be unspecified or not applicable.
              - `mandate_subcomponent` (boolean) **REQ** — Indicates whether choosing sub-components is mandatory for the component.
Possible values:
**true** - Choosing sub-components is mandatory.
**false** - Choosing sub-components is not mandatory.
              - `name` (string) **REQ** [maxLen=255] — Represents the name of the component.
              - `supported_subcomponents` (null) **REQ** — Reserved for future use.
        - `limit` (integer/int32) **REQ** — Represents the maximum number of states permitted in the Blueprint.
      - `transition_groups` (array of object) [maxItems=3] **REQ** — List of transition group profile objects, each describing the capabilities and constraints of a transition group in the Blueprint.
        oneOf:
          - `TransitionGroupProfile` — Represents a transition group profile, including its supported components and display label.
            - `supported_components` (array of object `TransitionGroupComponentDescriptor`) [maxItems=2] **REQ** — Represents the components allowed in the transition group, along with the policy defined for each component.
              schema: `TransitionGroupComponentDescriptor`
              - `mandate_subcomponent` (boolean) **REQ** — Indicates whether choosing sub-components is mandatory.
Possible values:
**true** - Choosing sub-components is mandatory.
**false** - Choosing sub-components is not mandatory.
              - `name` (string) **REQ** [maxLen=255] — Represents the name of the component.
              - `supported_subcomponents` (null) **REQ** — Reserved for future use.
            - `name` (string) **REQ** [maxLen=255] — Represents the internal name of the transition group.
            - `display_name` (string) **REQ** [maxLen=255] — Represents the display label of the transition group.
          - `TransitionGroupProfileDetailed` — Represents a detailed transition group profile that lists the supported components along with their sub-components.
            - `supported_components` (array of object `TransitionGroupComponentDescriptorWithSubcomponents`) [maxItems=2] **REQ** — Represents the components allowed in the transition group, along with the policy defined for each component.
              schema: `TransitionGroupComponentDescriptorWithSubcomponents`
              - `mandate_subcomponent` (boolean) **REQ** — Indicates whether choosing sub-components for the component is mandatory.
Possible values:
**true** - Choosing at least one sub-component is mandatory.
**false** - Choosing sub-components is not mandatory.
              - `name` (string) **REQ** [maxLen=255] — Represents the name of the component.
              - `supported_subcomponents` (array of string) [maxItems=14] **REQ** — Represents the sub-components that the component supports.
                items: [maxLen=255]
            - `name` (string) **REQ** [maxLen=255] — Represents the internal name of the transition group.
            - `display_name` (string) **REQ** [maxLen=255] — Represents the display label of the transition group.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The request cannot be processed because the required module parameter is missing or the specified module API name is invalid.
**Resolution:** Specify a valid API name for the module parameter. [application/json]
    > Represents the error returned when the request cannot be processed, either because the required module parameter is missing or because the specified module API name is invalid.
    oneOf:
      - `MissingModuleParameterError` — Error response indicating that the required module parameter is missing.
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Represents the error code returned when an expected parameter is missing from the request.
Possible values:
REQUIRED_PARAM_MISSING - A mandatory parameter is missing from the request.
        - `details` (object) **REQ** — Represents additional details about the validation error, including the name of the missing parameter.
          - `param_name` (string) **REQ** [maxLen=255] — Represents the name of the parameter that is missing from the request.
        - `message` (string) **REQ** [enum=['One of the expected parameter is missing']] — Represents the error message returned when one of the expected parameters is missing from the request.
Possible values:
One of the expected parameter is missing - An expected parameter is missing from the request.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the failed request.
Possible values:
error - The request failed.
      - `InvalidModuleError` — Error response indicating that the provided module name is invalid.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code.
Possible values:
**INVALID_MODULE** - The module name given is invalid.
        - `details` (object) **REQ** — Contains the error details, including the name of the parameter that caused the error.
          - `param_name` (string) **REQ** [maxLen=255] — Represents the name of the parameter implicated in the error.
        - `message` (string) **REQ** [enum=['the module name given seems to be invalid']] — Represents the error message returned when the module name given seems to be invalid.
Possible values:
the module name given seems to be invalid - The specified module name is invalid.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the failed request.
Possible values:
error - The request failed.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.blueprint.READ
