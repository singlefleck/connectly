from datetime import datetime
from enum import StrEnum
from typing import Annotated, Literal
from uuid import UUID
from pydantic import BaseModel, ConfigDict, Field, StringConstraints


DisplayName = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        min_length=1,
        max_length=50,
    ),
]

class RoomStatus(StrEnum):
    WAITING = "waiting"
    ACTIVE = "active"
    CLOSED = "closed"


class CreateRoomRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    display_name: DisplayName


class JoinRoomRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    display_name: DisplayName

class ParticipantResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    participant_id: UUID
    display_name: DisplayName
    joined_at: datetime

class RoomResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    room_id: UUID
    status: RoomStatus
    max_participants: Literal[2] = 2
    participants: list[ParticipantResponse] = Field(
        default_factory=list,
        max_length=2,
    )
    created_at: datetime