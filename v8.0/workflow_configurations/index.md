# Workflow Configurations

- [OpenAPI specification](workflow_configurations.yaml)
- [Workflow Configuration](mds/getWorkflowConfigurations.md)
  - Retrieves the available triggers, actions, and related trigger details for a specific module. Use this endpoint before creating or updating workflow rules to discover which triggers and actions are supported, their per-type limits, scheduling compatibility, and related module triggers. The response includes three sections: triggers (events that fire the rule), actions (operations executed when the rule fires), and related_triggers_details (child/related modules like Notes or Calls that can also trigger rules on the parent module).
  - [Examples](mds/examples/getWorkflowConfigurations.md)
