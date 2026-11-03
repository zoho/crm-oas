# Kiosk States

- [OpenAPI specification](kiosks_states.yaml)
- [Get all states of a kiosk](operations/getAllKioskStates/operation.md)
  - To retrieve all the states configured in a kiosk in your Zoho CRM organization, along with their transition details and basic metadata such as name, type, and associated fields. Each state represents a screen, action, decision, or GetRecords. Available in: Standard, Professional, Enterprise, and Ultimate editions.
  - [Examples](operations/getAllKioskStates/examples/)
- [Create a kiosk state](operations/createKioskState/operation.md)
  - Creates a state (screen, action, decision, or GetRecords) in a Kiosk identified by Kiosk ID. Only **one state** can be created per request. The Kiosk must be in **draft** status; use the [Clone a Kiosk API](kiosks.yaml#$.paths./settings/kiosks/{kioskId}/actions/clone.post) if it is published or inactive. Call this API repeatedly to add more states, then [publish](kiosks.yaml#$.paths./settings/kiosks/{kioskId}/actions/activate.put) the Kiosk and [associate](kiosks_get_records.yaml#$.paths./settings/kiosks/{kioskId}/associations.put) it with the required CRM component. To modify an existing state, use the [Update Kiosk States API](kiosks_state.yaml#$.paths./settings/kiosks/{kioskId}/states.put).
  - [Examples](operations/createKioskState/examples/)
- [Get a specific kiosk state by ID](operations/getKioskState/operation.md)
  - To retrieve the complete configuration of one specific state within a kiosk in Zoho CRM, including its transitions, associated fields, and configured properties. Use the include_inner_details query parameter to expand nested type information. The response structure varies based on the state type: screen, decision, action, or get_records. To obtain the state ID required for this request, use the [Get Kiosk States API](kiosks_states.yaml#$.paths./settings/kiosks/{kioskId}/states.get) To obtain the Kiosk ID required for this request, use the [Get Kiosks API](kiosks.yaml#$.paths./settings/kiosks.get)
  - [Examples](operations/getKioskState/examples/)
- [Kiosk State](operations/updateKioskState/operation.md)
  - To update a particular state in a specific Kiosk in Zoho CRM using the Kiosk ID and state ID. Each state represents a screen, action, decision, or GetRecords. A Kiosk must be in the draft status to update a state. This operation is not supported when the Kiosk is in the published or inactive status. You can update only one state per request. The state must already exist before it can be updated. To create a new state, use the [Create a Kiosk State API](kiosks_states.yaml#$.paths./settings/kiosks/{kioskId}/states.post). Once the Kiosk is fully configured, [publish](kiosks.yaml#$.paths./settings/kiosks/{kioskId}/actions/activate.put) it and [associate](kiosks_get_records.yaml#$.paths./settings/kiosks/{kioskId}/associations.put) it with the required CRM component.
  - [Examples](operations/updateKioskState/examples/)
- [Delete a kiosk state](operations/deleteKioskState/operation.md)
  - To delete a specific state from a kiosk configuration in your Zoho CRM account. Removing a state eliminates all its associated configurations, transitions, and connected elements. Use the delete_dependent_states query parameter to control whether dependent states are also removed or left as disconnected components. The kiosk must be in draft status to perform this action. Predefined states (start state and end state) cannot be deleted. Available in Standard, Professional, Enterprise, and Ultimate editions.
  - [Examples](operations/deleteKioskState/examples/)
