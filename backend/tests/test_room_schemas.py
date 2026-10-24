from datetime import datetime, timezone
from uuid import uuid4

import pytest
from pydantic import ValidationError

from app.schemas.room import (
    CreateRoomRequest,
    JoinRoomRequest,
    ParticipantResponse,
    RoomResponse,
    RoomStatus,
)


def test_create_room_request_strips_display_name():
    request = CreateRoomRequest(display_name="  Alice  ")

    assert request.display_name == "Alice"


def test_join_room_rejects_blank_display_name():
    with pytest.raises(ValidationError):
        JoinRoomRequest(display_name="   ")


def test_create_room_rejects_extra_fields():
    with pytest.raises(ValidationError):
        CreateRoomRequest(
            display_name="Alice",
            unexpected_field="value",
        )


def test_room_response_accepts_two_participants():
    now = datetime.now(timezone.utc)

    alice = ParticipantResponse(
        participant_id=uuid4(),
        display_name="Alice",
        joined_at=now,
    )
    bob = ParticipantResponse(
        participant_id=uuid4(),
        display_name="Bob",
        joined_at=now,
    )

    room = RoomResponse(
        room_id=uuid4(),
        status=RoomStatus.ACTIVE,
        participants=[alice, bob],
        created_at=now,
    )

    assert len(room.participants) == 2
    assert room.max_participants == 2


def test_room_response_rejects_more_than_two_participants():
    now = datetime.now(timezone.utc)

    participants = [
        ParticipantResponse(
            participant_id=uuid4(),
            display_name=name,
            joined_at=now,
        )
        for name in ["Alice", "Bob", "Charlie"]
    ]

    with pytest.raises(ValidationError):
        RoomResponse(
            room_id=uuid4(),
            status=RoomStatus.ACTIVE,
            participants=participants,
            created_at=now,
        )


def test_room_response_rejects_capacity_above_two():
    with pytest.raises(ValidationError):
        RoomResponse(
            room_id=uuid4(),
            status=RoomStatus.WAITING,
            max_participants=3,
            created_at=datetime.now(timezone.utc),
        )