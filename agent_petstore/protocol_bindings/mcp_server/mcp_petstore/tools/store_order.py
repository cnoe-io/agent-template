# Copyright 2025 CNOE
# SPDX-License-Identifier: Apache-2.0
# Generated by CNOE OpenAPI MCP Codegen tool

"""Tools for /store/order operations"""

import logging
from typing import Dict, Any
from agent_petstore.protocol_bindings.mcp_server.mcp_petstore.api.client import make_api_request, assemble_nested_body

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def place_order(
    body_id: int = None,
    body_petId: int = None,
    body_quantity: int = None,
    body_shipDate: str = None,
    body_status: str = None,
    body_complete: bool = None,
) -> Dict[str, Any]:
    '''
    Place an order for a pet.

    Args:
        body_id (int, optional): The unique identifier for the order. Defaults to None.
        body_petId (int, optional): The ID of the pet being ordered. Defaults to None.
        body_quantity (int, optional): The quantity of the pet to order. Defaults to None.
        body_shipDate (str, optional): The shipping date for the order in ISO 8601 format. Defaults to None.
        body_status (str, optional): The status of the order (e.g., 'placed', 'approved', 'delivered'). Defaults to None.
        body_complete (bool, optional): Whether the order is complete. Defaults to None.

    Returns:
        Dict[str, Any]: The JSON response from the API call containing order details or error information.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        ---
        post:
          summary: Place an order for a pet
          description: Place a new order in the store.
          operationId: placeOrder
          requestBody:
            required: true
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    id:
                      type: integer
                      format: int64
                      description: The unique identifier for the order.
                    petId:
                      type: integer
                      format: int64
                      description: The ID of the pet being ordered.
                    quantity:
                      type: integer
                      format: int32
                      description: The quantity of the pet to order.
                    shipDate:
                      type: string
                      format: date-time
                      description: The shipping date for the order in ISO 8601 format.
                    status:
                      type: string
                      description: The status of the order (e.g., 'placed', 'approved', 'delivered').
                    complete:
                      type: boolean
                      description: Whether the order is complete.
                  required: []
          responses:
            '200':
              description: Successful operation
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      id:
                        type: integer
                        format: int64
                      petId:
                        type: integer
                        format: int64
                      quantity:
                        type: integer
                        format: int32
                      shipDate:
                        type: string
                        format: date-time
                      status:
                        type: string
                      complete:
                        type: boolean
            '400':
              description: Invalid Order
    '''
    logger.debug("Making POST request to /store/order")

    params = {}
    data = {}

    flat_body = {}
    if body_id is not None:
        flat_body["id"] = body_id
    if body_petId is not None:
        flat_body["petId"] = body_petId
    if body_quantity is not None:
        flat_body["quantity"] = body_quantity
    if body_shipDate is not None:
        flat_body["shipDate"] = body_shipDate
    if body_status is not None:
        flat_body["status"] = body_status
    if body_complete is not None:
        flat_body["complete"] = body_complete
    data = assemble_nested_body(flat_body)

    success, response = await make_api_request("/store/order", method="POST", params=params, data=data)

    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get("error", "Request failed")}
    return response