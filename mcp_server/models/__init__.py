# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T05:04:39+00:00

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field, RootModel


class Subscription(BaseModel):
    field_context: Optional[str] = Field(
        None, alias='@context', examples=['https://mercure.rocks/']
    )
    active: bool
    id: str = Field(..., examples=['/.well-known/mercure/subscriptions'])
    lastEventID: Optional[str] = Field(
        None, examples=['urn:uuid:5e94c686-2c0b-4f9b-958c-92ccc3bbb4eb']
    )
    payload: Optional[Dict[str, Any]] = None
    subscriber: str = Field(
        ..., examples=['urn:uuid:bb3de268-05b0-4c65-b44e-8f9acefc29d6']
    )
    topic: str = Field(..., examples=['https://example.com/{selector}'])
    type: str = Field(..., examples=['Subscription'])


class Subscriptions(BaseModel):
    field_context: str = Field(
        ..., alias='@context', examples=['https://mercure.rocks/']
    )
    id: str = Field(..., examples=['/.well-known/mercure/subscriptions'])
    lastEventID: str = Field(
        ..., examples=['urn:uuid:5e94c686-2c0b-4f9b-958c-92ccc3bbb4eb']
    )
    subscriptions: List[Subscription]
    type: str = Field(..., examples=['Subscriptions'])


class Topic(RootModel[List[str]]):
    root: List[str]
