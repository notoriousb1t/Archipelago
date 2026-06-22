"""
TLoZ Dungeon Entrance Shuffle
Modeled after ALttP's EntranceShuffle.py (dungeons_simple mode).

Shuffles which overworld entrance connects to which dungeon Region.
The dungeon Regions and their items/locations are untouched; only the
Entrance->Region connections on the overworld are remapped.
"""
from __future__ import annotations

import typing

from .Entrances import dungeon_entrances

if typing.TYPE_CHECKING:
    from . import TLoZWorld


def shuffle_dungeons(world) -> None:
    multiworld = world.multiworld
    player = world.player
    overworld = multiworld.get_region("Overworld", player)

    # Get overworld entrance objects
    entrance_objects = []
    for i in range(1, 10):
        entrance_name = dungeon_entrances[i - 1].ow_name
        entrance = next(e for e in overworld.exits if e.name == entrance_name)
        entrance_objects.append(entrance)

    # Shuffle dungeon IDs
    dungeon_numbers = list(range(1, 10))
    world.random.shuffle(dungeon_numbers)

    # Map entrance slot to target dungeon
    world.dungeon_entrance_map = {
        i: dungeon_numbers[i - 1] for i in range(1, 10)
    }

    # Reconnect entrances to shuffled targets
    for i, entrance in enumerate(entrance_objects, start=1):
        target_dungeon = world.dungeon_entrance_map[i]
        target_region = multiworld.get_region(f"Level {target_dungeon}", player)

        if entrance.connected_region is not None:
            entrance.connected_region.entrances.remove(entrance)
        entrance.connect(target_region)


def write_dungeon_entrances(world, rom_data: bytearray) -> None:
    if not world.dungeon_entrance_map:
        return

    door_table_address = 0x18490

    for entrance_slot, dungeon_number in world.dungeon_entrance_map.items():
        slot_info = dungeon_entrances[entrance_slot - 1]
        dungeon_info = dungeon_entrances[dungeon_number - 1]

        address = door_table_address + slot_info.ow_index
        new_cave_index = dungeon_info.uw_index

        # Keep lower 2 bits (screen property flags) intact
        current_byte = rom_data[address]
        lower_bits = current_byte & 0x03
        rom_data[address] = new_cave_index | lower_bits
