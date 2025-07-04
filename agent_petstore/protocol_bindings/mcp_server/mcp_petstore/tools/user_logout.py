# Copyright 2025 CNOE
# SPDX-License-Identifier: Apache-2.0
# Generated by CNOE OpenAPI MCP Codegen tool

"""Tools for /user/logout operations"""

import logging
from typing import Dict, Any
from agent_petstore.protocol_bindings.mcp_server.mcp_petstore.api.client import make_api_request, assemble_nested_body

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def logout_user() -> Dict[str, Any]:
    '''
    Logs out the currently logged-in user session.

    Args:
        None

    Returns:
        Dict[str, Any]: The JSON response from the API call indicating the result of the logout operation.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
      get:
        summary: Log out user
        description: Logs out the currently authenticated user from the system.
        operationId: logoutUser
        tags:
          - user
        responses:
          '200':
            description: Successful logout
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    message:
                      type: string
                      example: "Successfully logged out."
          '401':
            description: Unauthorized - User is not logged in
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    error:
                      type: string
                      example: "User not authenticated."
          '500':
            description: Internal server error
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    error:
                      type: string
                      example: "Request failed"
    '''
    logger.debug("Making GET request to /user/logout")

    params = {}
    data = {}

    flat_body = {}
    data = assemble_nested_body(flat_body)

    success, response = await make_api_request("/user/logout", method="GET", params=params, data=data)

    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get("error", "Request failed")}
    return response