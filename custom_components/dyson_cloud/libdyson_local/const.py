"""Constants for Dyson Python library."""
from enum import Enum, auto

DEVICE_TYPE_360_EYE = "N223"
DEVICE_TYPE_360_HEURIST = "276"
DEVICE_TYPE_PURE_COOL_LINK = "475"
DEVICE_TYPE_PURE_COOL_LINK_DESK = "469"
DEVICE_TYPE_PURE_COOL = "438"
DEVICE_TYPE_PURIFIER_COOL = "438K"
DEVICE_TYPE_PURE_COOL_FORMALDEHYDE = "438E"
DEVICE_TYPE_PURE_COOL_DESK = "520"
DEVICE_TYPE_PURE_HUMIDIFY_COOL = "358"
DEVICE_TYPE_PURIFIER_HUMIDIFY_COOL_FORMALDEHYDE_358E = "358E"
DEVICE_TYPE_PURIFIER_HUMIDIFY_COOL_FORMALDEHYDE_358K = "358K"
DEVICE_TYPE_PURE_HOT_COOL_LINK = "455"
DEVICE_TYPE_PURE_HOT_COOL = "527"
DEVICE_TYPE_PURE_HOT_COOL_NEW = "527E"
DEVICE_TYPE_PURIFIER_HOT_COOL = "527K"

DEVICE_TYPE_NAMES = {
    DEVICE_TYPE_360_EYE: "360 Eye robot vacuum",
    DEVICE_TYPE_360_HEURIST: "360 Heurist robot vacuum",
    DEVICE_TYPE_PURE_COOL: "Pure Cool",
    DEVICE_TYPE_PURIFIER_COOL: "Purifier Cool",
    DEVICE_TYPE_PURE_COOL_FORMALDEHYDE: "Pure Cool Formaldehyde",
    DEVICE_TYPE_PURE_COOL_DESK: "Pure Cool Desk",
    DEVICE_TYPE_PURE_COOL_LINK: "Pure Cool Link",
    DEVICE_TYPE_PURE_COOL_LINK_DESK: "Pure Cool Link Desk",
    DEVICE_TYPE_PURE_HOT_COOL: "Pure Hot+Cool",
    DEVICE_TYPE_PURE_HOT_COOL_NEW: "Pure Hot+Cool (New)",
    DEVICE_TYPE_PURE_HOT_COOL_LINK: "Pure Hot+Cool Link",
    DEVICE_TYPE_PURE_HUMIDIFY_COOL: "Pure Humidify+Cool",
    DEVICE_TYPE_PURIFIER_HUMIDIFY_COOL_FORMALDEHYDE_358E: "Purifier Humidify+Cool Formaldehyde",
    DEVICE_TYPE_PURIFIER_HUMIDIFY_COOL_FORMALDEHYDE_358K: "Purifier Humidify+Cool Formaldehyde",
    DEVICE_TYPE_PURIFIER_HOT_COOL: "Purifier Hot+Cool",
}

ENVIRONMENTAL_OFF = -1
ENVIRONMENTAL_INIT = -2
ENVIRONMENTAL_FAIL = -3


class MessageType(Enum):
    """Update message type."""

    STATE = auto()
    ENVIRONMENTAL = auto()


class AirQualityTarget(Enum):
    """Air Quality Target."""

    OFF = "OFF"
    GOOD = "0004"
    SENSITIVE = "0003"
    DEFAULT = "0002"
    VERY_SENSITIVE = "0001"


class HumidifyOscillationMode(Enum):
    """Pure Humidify+Cool oscillation mode."""

    DEGREE_45 = "0045"
    DEGREE_90 = "0090"
    BREEZE = "BRZE"
    CUST = "CUST"


class WaterHardness(Enum):
    """Water Hardness."""

    SOFT = "Soft"
    MEDIUM = "Medium"
    HARD = "Hard"


class VacuumState(Enum):
    """Dyson vacuum state."""

    FAULT_CALL_HELPLINE = "FAULT_CALL_HELPLINE"
    FAULT_CONTACT_HELPLINE = "FAULT_CONTACT_HELPLINE"
    FAULT_CRITICAL = "FAULT_CRITICAL"
    FAULT_GETTING_INFO = "FAULT_GETTING_INFO"
    FAULT_LOST = "FAULT_LOST"
    FAULT_ON_DOCK = "FAULT_ON_DOCK"
    FAULT_ON_DOCK_CHARGED = "FAULT_ON_DOCK_CHARGED"
    FAULT_ON_DOCK_CHARGING = "FAULT_ON_DOCK_CHARGING"
    FAULT_REPLACE_ON_DOCK = "FAULT_REPLACE_ON_DOCK"
    FAULT_RETURN_TO_DOCK = "FAULT_RETURN_TO_DOCK"
    FAULT_RUNNING_DIAGNOSTIC = "FAULT_RUNNING_DIAGNOSTIC"
    FAULT_USER_RECOVERABLE = "FAULT_USER_RECOVERABLE"
    FULL_CLEAN_ABANDONED = "FULL_CLEAN_ABANDONED"
    FULL_CLEAN_ABORTED = "FULL_CLEAN_ABORTED"
    FULL_CLEAN_CHARGING = "FULL_CLEAN_CHARGING"
    FULL_CLEAN_DISCOVERING = "FULL_CLEAN_DISCOVERING"
    FULL_CLEAN_FINISHED = "FULL_CLEAN_FINISHED"
    FULL_CLEAN_INITIATED = "FULL_CLEAN_INITIATED"
    FULL_CLEAN_NEEDS_CHARGE = "FULL_CLEAN_NEEDS_CHARGE"
    FULL_CLEAN_PAUSED = "FULL_CLEAN_PAUSED"
    FULL_CLEAN_RUNNING = "FULL_CLEAN_RUNNING"
    FULL_CLEAN_TRAVERSING = "FULL_CLEAN_TRAVERSING"
    INACTIVE_CHARGED = "INACTIVE_CHARGED"
    INACTIVE_CHARGING = "INACTIVE_CHARGING"
    INACTIVE_DISCHARGING = "INACTIVE_DISCHARGING"
    MAPPING_ABORTED = "MAPPING_ABORTED"
    MAPPING_CHARGING = "MAPPING_CHARGING"
    MAPPING_FINISHED = "MAPPING_FINISHED"
    MAPPING_INITIATED = "MAPPING_INITIATED"
    MAPPING_NEEDS_CHARGE = "MAPPING_NEEDS_CHARGE"
    MAPPING_PAUSED = "MAPPING_PAUSED"
    MAPPING_RUNNING = "MAPPING_RUNNING"


class VacuumEyePowerMode(Enum):
    """Dyson 360 Eye power mode."""

    QUIET = "halfPower"
    MAX = "fullPower"


class VacuumHeuristPowerMode(Enum):
    """Dyson 360 Heurist power mode."""

    QUIET = "1"
    HIGH = "2"
    MAX = "3"


class CleaningType(Enum):
    """Vacuum cleaning type."""

    IMMEDIATE = "immediate"
    MANUAL = "manual"
    SCHEDULED = "scheduled"


class CleaningMode(Enum):
    """Vacuum cleaning mode."""

    GLOBAL = "global"
    ZONE_CONFIGURED = "zoneConfigured"