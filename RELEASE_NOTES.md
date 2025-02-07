# PyGPSClient Release Notes

### RELEASE v1.0.2

FIX:

1. Fix failure to update vacc and hacc in banner from NMEA PUBX00 message

### RELEASE v1.0.1

ENHANCEMENTS:

1. NMEA handler updated to use new pynmeagps library (>=0.1.7) rather than pynmea2. This lightweight library obviates the need to perform NMEA lat/lon and other format conversions and makes the parsed NMEA representation more consistent with UBX.

### RELEASE v1.0.0

Version and status updated to v1.0.0 Production/Stable

ENHANCEMENTS:

1. Timeout setting added to common Serial port control dialog. 
2. Serial port baudrate configuration settings range extended to 921600.


### RELEASE v0.2.27-beta

ENHANCEMENTS:

1. Updated for pyubx2 v1.0.4.
2. Minimum required pyubx2 version is now 1.0.4. 

### RELEASE v0.2.26-beta

ENHANCEMENTS:

1. Add CFG-RATE configuration panel to UBX Configuration dialog for legacy devices (can already use CFG-VALSET for modern devices).


### RELEASE v0.2.25-beta

ENHANCEMENTS:

1. Improved handling of mixed protocol streams.
2. Add GNSS Stop/Start to ubxpresets examples (tx to djdan7).

### RELEASE v0.2.24-beta

FIXES:

1. Setup.py updated to fix previous PyPi deploy failure.

### RELEASE v0.2.23-beta

ENHANCEMENTS:

1. Updated for pyubx2 v1.0.2.
2. Minimum required pyubx2 version is now 1.0.2. 

### RELEASE v0.2.22-beta

FIXES:

1. Minor tweaks to CFG-VAL* UBX configuration panel to populate 'Value' field with result of CFG-VALGET poll in the same format as required for updates using CFG-VALSET (e.g. hex string for 'X' attributes).

### RELEASE v0.2.21-beta

ENHANCEMENTS:

1. UBX config panel CFG-VALGET query will return value in 'value' field as well as in Console.

FIXES:

1. Prevent CFG-VAL send command if no keyname selected.
2. Default layer (7) added to CFG-VALGET query layer options.

### RELEASE v0.2.20-beta

ENHANCEMENTS:

1. Serial port configuration panel refactored to generic Frame subclass
`SerialConfigFrame` in `common` package, to facilitate reuse in other
 tkinter apps.
2. Allow button click to refresh UBX hardware/firmware widget.
3. Simplify pending command confirmations for UBX config widgets.
4. Pylint tidy up.


### RELEASE v0.2.19-beta

ENHANCEMENTS:

1. UBX config dialog panel reworked to include CFG-VALSET/DEL/GET config widget.
2. UBX config widgets separated out into discrete modules/classes.
3. Minimum required pyubx2 version is now 0.3.4. 

FIXES:

1. Invalid Key error in CFG-MSG config dialog panel for some NMEA message types.

### RELEASE v0.2.18-beta

ENHANCEMENTS:

1. Add optional GNSS color code legend to graph view.
2. Add 'Show Legend' and 'Show Zero Signal' options in the settings panel (obviating need to amend `globals.py`).

### RELEASE v0.2.17-beta

FIXES:

1. Fix build issue

### RELEASE v0.2.16-beta

ENHANCEMENTS:

Improved handling of multiple GNSS in graph and satellite views:
1. Satellites with zero signal will no longer be displayed by default (this behaviour can be modified via the `GNSS_HIDE_NULL` constant in globals.py)
2. For consistency between NMEA GSV, UBX NAV-SAT and NAV-SVINFO message types, GLONASS satellites will be assigned an NMEA SVID (65-96) by default, rather than their slot number (1-24) (this behaviour can be modified via the `GLONASS_NMEA` constant in `globals.py`)
3. Different GNSS will be more clearly color-coded (color code defined in `GNSS_COLS` in `globals.py`).
4. Minimum required pyubx2 version is now 0.3.1.

### RELEASE v0.2.15-beta

ENHANCEMENTS:

Various minor updates to cater for Generation 9 UBX messages.

1. Satellite and Graph views now use data from NAV-SAT and/or NAV-SVINFO messages.
2. Large number of extensions parsed from MON-VER (for version and GNSS/AS data).
3. Additional console color tags added for G9 NAV messages.
4. Minimum pyubx2 version is now 0.3.0.

### RELEASE v0.2.14-beta

FIXES:

1. removed debug print() statement from UBXHandler - sorry about that.

### RELEASE v0.2.13-beta

ENHANCEMENTS:

1. Antenna status and power added to UBX config dialog.

### RELEASE v0.2.12-beta

ENHANCEMENTS:

1. PortID added to UBX Config panel
2. Comments updated
3. Minimum required pyubx2 version now 0.2.8

### RELEASE v0.2.11-beta

1. Status updated to Beta
2. No functional changes.

### RELEASE v0.2.10-alpha

ENHANCEMENTS:

1. About dialog now shows pynmea2 and pyubx2 versions.
2. Minor cody tidy up and refactoring.
3. Min pyubx2 version is now 0.2.4

### RELEASE v0.2.9-alpha

ENHANCEMENTS:

1. Updated for Travis CI integration. No changes in functionality.

### RELEASE v0.2.8-alpha

FIXES:

1. Static speed conversions corrected
