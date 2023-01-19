from dataclasses import dataclass, field


@dataclass
class Unit:
    unit_name: str
    unit_played: int
    unit_playrate: str
    unit_avg_placement: str
    unit_image: str
    unit_items: dict[str:(dict[str:int])] = field(default_factory=dict)


def generate_unit(unit_name, unit_played, unit_playrate, unit_avg_placement, unit_image, unit_items):
    new_unit = Unit(unit_name, unit_played, unit_playrate, unit_avg_placement, unit_image, unit_items)
    return new_unit