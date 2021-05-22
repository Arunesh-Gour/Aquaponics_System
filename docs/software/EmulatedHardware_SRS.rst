=========================================
Software Requirement Specifications (SRS)
=========================================

.. This is Software Requirement Specification document (SRS).
   Not to be confused with SysRS (System Requirement Specification) document.

:Software name: Emulated hardware.
:Category: IoT emulation.

Introduction
============
Emulated hardware is a module containing several IoT device stubs ranging from
sensors to actuators.

Purpose
-------
Since the hardware in not accessible for system training, monitoring, testing
and implementation / deployment, there is a need to address this situation
by implementing a stub module for all hardwares in order to simulate project's
implementation and demonstrate working.

Intended audience
-----------------
This SRS is intended majorily for software developers working on hardware
controller, hardware emulation or interface.
It lists out detailed information for implementation of hardware emulation.

Intended use
------------
To design and / or implement software modules according to given reference,
API format and other details.

Scope
-----
Emulated hardware consists of 2 segments for IoTs - sensors and actuators.
Sensors only provide reading of current state, while actuators provide both
reading and control write operations.

Sensors
^^^^^^^
:Soil quality monitoring IoT: Tracks ph, levels of phosphorus, nitrogen, etc.
                              present in soil.
:Water nutrient monitoring IoT: Tracks ph, levels of sodium, nitrogen,
                                phosphorus, oxygen, etc. present in water.
:Water level monitoring IoT: Tracks water level in tank.
:Water thermometer IoT: Tracks temperature levels of water in tank.
:External weather sensor IoT: External temperature, humidity, rain sensor.

Controllers
^^^^^^^^^^^
:Water heater IoT: Heats up water.
:Water inlet valve IoT: Controls influx of fresh water into the tank.
:Water outlet valve IoT: Controls outflux of water from tank, to discard it.
:Water filter inlet valve IoT: Pumps water from tank to filteration unit.
:Water filter outlet valve IoT: Pumps water from filteration unit to tank.
:Power controller IoT: Controls power to all system & IoTs.

Definitions and acronyms
------------------------
.. Definitions and acronyms.

Overall description
===================
User needs
----------
.. Who will use and how.

Assumptions and dependencies
----------------------------
.. Dependent on external factor.
Assumes the readings of IoTs are controlled by another module to simulate
real conditions, and is independent of controllers and main system.

System features and requirements
================================
Functional requirements
-----------------------
.. Functional requirements.

External interface requirements
-------------------------------
.. User.
   Hardware.
   Software.
   Communication.
All actuators and sensors have just 2 public functions - read() and write().
The variable to be read or written will be passed as string, while value to
be overwritten will be passed as respective object.

To make IoT devices, use IoTStubEssentials' modules as base class and derive
required classes as per requirement.

To make and use hidden functions, append function name with an underscore as
``_`` before the function name.

System features
---------------
.. Features required for system to work.

Non-functional requirements
---------------------------
.. Performance.
   Safety.
   Security.
   Quality.
