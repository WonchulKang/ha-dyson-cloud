"""Support for Dyson cloud account."""

import asyncio
import logging
from functools import partial

from homeassistant.exceptions import ConfigEntryNotReady
from .libdyson_local.cloud.account import DysonAccountCN
from .libdyson_local.cloud.device_info import DysonDeviceInfo
from .libdyson_local.const import DEVICE_TYPE_360_EYE
from .libdyson_local.discovery import DysonDiscovery
from .libdyson_local.dyson_device import DysonDevice
from .libdyson_local.exceptions import DysonException, DysonNetworkError
from homeassistant.config_entries import ConfigEntry, SOURCE_DISCOVERY
from homeassistant.const import CONF_HOST, EVENT_HOMEASSISTANT_STOP
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity import Entity
from homeassistant.components.zeroconf import async_get_instance
from .libdyson_local.cloud import DysonAccount
from custom_components.dyson_local import DOMAIN as DYSON_LOCAL_DOMAIN

from .const import CONF_AUTH, CONF_REGION, DATA_ACCOUNT, DATA_DEVICES, DOMAIN

_LOGGER = logging.getLogger(__name__)

PLATFORMS = ["camera"]


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up Dyson integration."""
    hass.data[DOMAIN] = {}
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Dyson from a config entry."""
    # Get devices list
    if entry.data[CONF_REGION] == "CN":
        account = DysonAccountCN(entry.data[CONF_AUTH])
    else:
        account = DysonAccount(entry.data[CONF_AUTH])
    try:
        devices = await hass.async_add_executor_job(account.devices)
    except DysonNetworkError:
        _LOGGER.error("Cannot connect to Dyson cloud service.")
        raise ConfigEntryNotReady

    for device in devices:
        hass.async_create_task(
            hass.config_entries.flow.async_init(
                DYSON_LOCAL_DOMAIN,
                context={"source": SOURCE_DISCOVERY},
                data=device,
            )
        )

    hass.data[DOMAIN][entry.entry_id] = {
        DATA_ACCOUNT: account,
        DATA_DEVICES: devices,
    }
    for component in PLATFORMS:
        hass.async_create_task(
            hass.config_entries.async_forward_entry_setup(entry, component)
        )

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload Dyson cloud."""
    # Nothing needs clean up
    return True
