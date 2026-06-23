from typing import List, NamedTuple


class DungeonEntrance(NamedTuple):
    """Data for a single dungeon entrance on the overworld.

    dungeon_name - Region/location group name (e.g. "Level 1"). Matches
                   the keys used in TLoZWorld.location_name_groups and the
                   Region names created in create_regions().
    ow_name      - Name of the overworld entrance (e.g. "Level 1 (Entrance)").
    ow_index     - Overworld screen index (0x00-0x7F) that addresses this.
    uw_index     - Vanilla cave index byte stored at that screen address.
                   Written to BASE_PC_ADDRESS + ow_index when remapping.
    """
    dungeon_name: str
    ow_name: str
    ow_index: int
    uw_index: int

# Entrance index for overworld.
_OW_LEVEL_1 = 0x37
_OW_LEVEL_2 = 0x3C
_OW_LEVEL_3 = 0x74
_OW_LEVEL_4 = 0x45
_OW_LEVEL_5 = 0x0B
_OW_LEVEL_6 = 0x22
_OW_LEVEL_7 = 0x42
_OW_LEVEL_8 = 0x6D
_OW_LEVEL_9 = 0x05

# Level index for underworld.
_UW_LEVEL_1 = 0x04
_UW_LEVEL_2 = 0x08
_UW_LEVEL_3 = 0x0C
_UW_LEVEL_4 = 0x10
_UW_LEVEL_5 = 0x14
_UW_LEVEL_6 = 0x18
_UW_LEVEL_7 = 0x1C
_UW_LEVEL_8 = 0x20
_UW_LEVEL_9 = 0x24

# Ordered list of all nine dungeon entrances, Level 1 through Level 9.
dungeon_entrances: List[DungeonEntrance] = [
    DungeonEntrance("Level 1", "Level 1 (Entrance)", ow_index=_OW_LEVEL_1, uw_index=_UW_LEVEL_1),
    DungeonEntrance("Level 2", "Level 2 (Entrance)", ow_index=_OW_LEVEL_2, uw_index=_UW_LEVEL_2),
    DungeonEntrance("Level 3", "Level 3 (Entrance)", ow_index=_OW_LEVEL_3, uw_index=_UW_LEVEL_3),
    DungeonEntrance("Level 4", "Level 4 (Entrance)", ow_index=_OW_LEVEL_4, uw_index=_UW_LEVEL_4),
    DungeonEntrance("Level 5", "Level 5 (Entrance)", ow_index=_OW_LEVEL_5, uw_index=_UW_LEVEL_5),
    DungeonEntrance("Level 6", "Level 6 (Entrance)", ow_index=_OW_LEVEL_6, uw_index=_UW_LEVEL_6),
    DungeonEntrance("Level 7", "Level 7 (Entrance)", ow_index=_OW_LEVEL_7, uw_index=_UW_LEVEL_7),
    DungeonEntrance("Level 8", "Level 8 (Entrance)", ow_index=_OW_LEVEL_8, uw_index=_UW_LEVEL_8),
    DungeonEntrance("Level 9", "Level 9 (Entrance)", ow_index=_OW_LEVEL_9, uw_index=_UW_LEVEL_9),
]
