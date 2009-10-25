# Python stubs generated by omniidl from idl_old/Fissures.idl

import omniORB, _omnipy
from omniORB import CORBA, PortableServer
_0_CORBA = CORBA

_omnipy.checkVersion(3,0, __file__)


#
# Start of module "Fissures"
#
__name__ = "idl.Fissures"
_0_Fissures = omniORB.openModule("idl.Fissures", r"idl_old/Fissures.idl")
_0_Fissures__POA = omniORB.openModule("idl.Fissures__POA", r"idl_old/Fissures.idl")

_0_Fissures.VERSION = "1.0"

# struct Orientation
_0_Fissures.Orientation = omniORB.newEmptyClass()
class Orientation (omniORB.StructBase):
    _NP_RepositoryId = "IDL:iris.edu/Fissures/Orientation:1.0"

    def __init__(self, azimuth, dip):
        self.azimuth = azimuth
        self.dip = dip

_0_Fissures.Orientation = Orientation
_0_Fissures._d_Orientation  = (omniORB.tcInternal.tv_struct, Orientation, Orientation._NP_RepositoryId, "Orientation", "azimuth", omniORB.tcInternal.tv_float, "dip", omniORB.tcInternal.tv_float)
_0_Fissures._tc_Orientation = omniORB.tcInternal.createTypeCode(_0_Fissures._d_Orientation)
omniORB.registerType(Orientation._NP_RepositoryId, _0_Fissures._d_Orientation, _0_Fissures._tc_Orientation)
del Orientation

# struct Dimension
_0_Fissures.Dimension = omniORB.newEmptyClass()
class Dimension (omniORB.StructBase):
    _NP_RepositoryId = "IDL:iris.edu/Fissures/Dimension:1.0"

    def __init__(self, width, height):
        self.width = width
        self.height = height

_0_Fissures.Dimension = Dimension
_0_Fissures._d_Dimension  = (omniORB.tcInternal.tv_struct, Dimension, Dimension._NP_RepositoryId, "Dimension", "width", omniORB.tcInternal.tv_long, "height", omniORB.tcInternal.tv_long)
_0_Fissures._tc_Dimension = omniORB.tcInternal.createTypeCode(_0_Fissures._d_Dimension)
omniORB.registerType(Dimension._NP_RepositoryId, _0_Fissures._d_Dimension, _0_Fissures._tc_Dimension)
del Dimension

# typedef ... DimensionSeq
class DimensionSeq:
    _NP_RepositoryId = "IDL:iris.edu/Fissures/DimensionSeq:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Fissures.DimensionSeq = DimensionSeq
_0_Fissures._d_DimensionSeq  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:iris.edu/Fissures/Dimension:1.0"], 0)
_0_Fissures._ad_DimensionSeq = (omniORB.tcInternal.tv_alias, DimensionSeq._NP_RepositoryId, "DimensionSeq", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:iris.edu/Fissures/Dimension:1.0"], 0))
_0_Fissures._tc_DimensionSeq = omniORB.tcInternal.createTypeCode(_0_Fissures._ad_DimensionSeq)
omniORB.registerType(DimensionSeq._NP_RepositoryId, _0_Fissures._ad_DimensionSeq, _0_Fissures._tc_DimensionSeq)
del DimensionSeq

# enum UnitBase
_0_Fissures.METER = omniORB.EnumItem("METER", 0)
_0_Fissures.GRAM = omniORB.EnumItem("GRAM", 1)
_0_Fissures.SECOND = omniORB.EnumItem("SECOND", 2)
_0_Fissures.AMPERE = omniORB.EnumItem("AMPERE", 3)
_0_Fissures.KELVIN = omniORB.EnumItem("KELVIN", 4)
_0_Fissures.MOLE = omniORB.EnumItem("MOLE", 5)
_0_Fissures.CANDELA = omniORB.EnumItem("CANDELA", 6)
_0_Fissures.COUNT = omniORB.EnumItem("COUNT", 7)
_0_Fissures.COMPOSITE = omniORB.EnumItem("COMPOSITE", 8)
_0_Fissures.UnitBase = omniORB.Enum("IDL:iris.edu/Fissures/UnitBase:1.0", (_0_Fissures.METER, _0_Fissures.GRAM, _0_Fissures.SECOND, _0_Fissures.AMPERE, _0_Fissures.KELVIN, _0_Fissures.MOLE, _0_Fissures.CANDELA, _0_Fissures.COUNT, _0_Fissures.COMPOSITE,))

_0_Fissures._d_UnitBase  = (omniORB.tcInternal.tv_enum, _0_Fissures.UnitBase._NP_RepositoryId, "UnitBase", _0_Fissures.UnitBase._items)
_0_Fissures._tc_UnitBase = omniORB.tcInternal.createTypeCode(_0_Fissures._d_UnitBase)
omniORB.registerType(_0_Fissures.UnitBase._NP_RepositoryId, _0_Fissures._d_UnitBase, _0_Fissures._tc_UnitBase)

# valuetype Unit
_0_Fissures._d_Unit = (omniORB.tcInternal.tv__indirect, ["IDL:iris.edu/Fissures/Unit:1.0"])
omniORB.typeMapping["IDL:iris.edu/Fissures/Unit:1.0"] = _0_Fissures._d_Unit
_0_Fissures.Unit = omniORB.newEmptyClass()

class Unit (_0_CORBA.ValueBase):
    _NP_RepositoryId = "IDL:iris.edu/Fissures/Unit:1.0"

    def __init__(self, *args, **kwargs):
        if args:
            if len(args) != 6:
                raise TypeError("Unit() takes 6 arguments "
                                "(%d given)" % len(args))
            self.the_unit_base = args[0]
            self.elements = args[1]
            self.power = args[2]
            self.name = args[3]
            self.multi_factor = args[4]
            self.exponent = args[5]
        if kwargs:
            self.__dict__.update(kwargs)

omniORB.registerValueFactory(Unit._NP_RepositoryId, Unit)

_0_Fissures.Unit = Unit
_0_Fissures._d_Unit  = (omniORB.tcInternal.tv_value, Unit, Unit._NP_RepositoryId, "Unit", _0_CORBA.VM_NONE, None, _0_CORBA.tcInternal.tv_null, "the_unit_base", omniORB.typeMapping["IDL:iris.edu/Fissures/UnitBase:1.0"], _0_CORBA.PUBLIC_MEMBER, "elements", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:iris.edu/Fissures/Unit:1.0"], 0), _0_CORBA.PUBLIC_MEMBER, "power", omniORB.tcInternal.tv_long, _0_CORBA.PUBLIC_MEMBER, "name", (omniORB.tcInternal.tv_string,0), _0_CORBA.PUBLIC_MEMBER, "multi_factor", omniORB.tcInternal.tv_double, _0_CORBA.PUBLIC_MEMBER, "exponent", omniORB.tcInternal.tv_long, _0_CORBA.PUBLIC_MEMBER)
_0_Fissures._tc_Unit = omniORB.tcInternal.createTypeCode(_0_Fissures._d_Unit)
omniORB.registerType(Unit._NP_RepositoryId, _0_Fissures._d_Unit, _0_Fissures._tc_Unit)
del Unit


# typedef ... UnitSeq
class UnitSeq:
    _NP_RepositoryId = "IDL:iris.edu/Fissures/UnitSeq:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Fissures.UnitSeq = UnitSeq
_0_Fissures._d_UnitSeq  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:iris.edu/Fissures/Unit:1.0"], 0)
_0_Fissures._ad_UnitSeq = (omniORB.tcInternal.tv_alias, UnitSeq._NP_RepositoryId, "UnitSeq", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:iris.edu/Fissures/Unit:1.0"], 0))
_0_Fissures._tc_UnitSeq = omniORB.tcInternal.createTypeCode(_0_Fissures._ad_UnitSeq)
omniORB.registerType(UnitSeq._NP_RepositoryId, _0_Fissures._ad_UnitSeq, _0_Fissures._tc_UnitSeq)
del UnitSeq

# valuetype UnitRange
_0_Fissures._d_UnitRange = (omniORB.tcInternal.tv__indirect, ["IDL:iris.edu/Fissures/UnitRange:1.0"])
omniORB.typeMapping["IDL:iris.edu/Fissures/UnitRange:1.0"] = _0_Fissures._d_UnitRange
_0_Fissures.UnitRange = omniORB.newEmptyClass()

class UnitRange (_0_CORBA.ValueBase):
    _NP_RepositoryId = "IDL:iris.edu/Fissures/UnitRange:1.0"

    def __init__(self, *args, **kwargs):
        if args:
            if len(args) != 3:
                raise TypeError("UnitRange() takes 3 arguments "
                                "(%d given)" % len(args))
            self.the_units = args[0]
            self.min_value = args[1]
            self.max_value = args[2]
        if kwargs:
            self.__dict__.update(kwargs)

omniORB.registerValueFactory(UnitRange._NP_RepositoryId, UnitRange)

_0_Fissures.UnitRange = UnitRange
_0_Fissures._d_UnitRange  = (omniORB.tcInternal.tv_value, UnitRange, UnitRange._NP_RepositoryId, "UnitRange", _0_CORBA.VM_NONE, None, _0_CORBA.tcInternal.tv_null, "the_units", omniORB.typeMapping["IDL:iris.edu/Fissures/Unit:1.0"], _0_CORBA.PUBLIC_MEMBER, "min_value", omniORB.tcInternal.tv_double, _0_CORBA.PUBLIC_MEMBER, "max_value", omniORB.tcInternal.tv_double, _0_CORBA.PUBLIC_MEMBER)
_0_Fissures._tc_UnitRange = omniORB.tcInternal.createTypeCode(_0_Fissures._d_UnitRange)
omniORB.registerType(UnitRange._NP_RepositoryId, _0_Fissures._d_UnitRange, _0_Fissures._tc_UnitRange)
del UnitRange


# valuetype Quantity
_0_Fissures._d_Quantity = (omniORB.tcInternal.tv__indirect, ["IDL:iris.edu/Fissures/Quantity:1.0"])
omniORB.typeMapping["IDL:iris.edu/Fissures/Quantity:1.0"] = _0_Fissures._d_Quantity
_0_Fissures.Quantity = omniORB.newEmptyClass()

class Quantity (_0_CORBA.ValueBase):
    _NP_RepositoryId = "IDL:iris.edu/Fissures/Quantity:1.0"

    def __init__(self, *args, **kwargs):
        if args:
            if len(args) != 2:
                raise TypeError("Quantity() takes 2 arguments "
                                "(%d given)" % len(args))
            self.value = args[0]
            self.the_units = args[1]
        if kwargs:
            self.__dict__.update(kwargs)

omniORB.registerValueFactory(Quantity._NP_RepositoryId, Quantity)

_0_Fissures.Quantity = Quantity
_0_Fissures._d_Quantity  = (omniORB.tcInternal.tv_value, Quantity, Quantity._NP_RepositoryId, "Quantity", _0_CORBA.VM_NONE, None, _0_CORBA.tcInternal.tv_null, "value", omniORB.tcInternal.tv_double, _0_CORBA.PUBLIC_MEMBER, "the_units", omniORB.typeMapping["IDL:iris.edu/Fissures/Unit:1.0"], _0_CORBA.PUBLIC_MEMBER)
_0_Fissures._tc_Quantity = omniORB.tcInternal.createTypeCode(_0_Fissures._d_Quantity)
omniORB.registerType(Quantity._NP_RepositoryId, _0_Fissures._d_Quantity, _0_Fissures._tc_Quantity)
del Quantity


# typedef ... Length
class Length:
    _NP_RepositoryId = "IDL:iris.edu/Fissures/Length:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Fissures.Length = Length
_0_Fissures._d_Length  = omniORB.typeMapping["IDL:iris.edu/Fissures/Quantity:1.0"]
_0_Fissures._ad_Length = (omniORB.tcInternal.tv_alias, Length._NP_RepositoryId, "Length", omniORB.typeMapping["IDL:iris.edu/Fissures/Quantity:1.0"])
_0_Fissures._tc_Length = omniORB.tcInternal.createTypeCode(_0_Fissures._ad_Length)
omniORB.registerType(Length._NP_RepositoryId, _0_Fissures._ad_Length, _0_Fissures._tc_Length)
del Length

# typedef ... TimeInterval
class TimeInterval:
    _NP_RepositoryId = "IDL:iris.edu/Fissures/TimeInterval:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Fissures.TimeInterval = TimeInterval
_0_Fissures._d_TimeInterval  = omniORB.typeMapping["IDL:iris.edu/Fissures/Quantity:1.0"]
_0_Fissures._ad_TimeInterval = (omniORB.tcInternal.tv_alias, TimeInterval._NP_RepositoryId, "TimeInterval", omniORB.typeMapping["IDL:iris.edu/Fissures/Quantity:1.0"])
_0_Fissures._tc_TimeInterval = omniORB.tcInternal.createTypeCode(_0_Fissures._ad_TimeInterval)
omniORB.registerType(TimeInterval._NP_RepositoryId, _0_Fissures._ad_TimeInterval, _0_Fissures._tc_TimeInterval)
del TimeInterval

# typedef ... TimeIntervalSeq
class TimeIntervalSeq:
    _NP_RepositoryId = "IDL:iris.edu/Fissures/TimeIntervalSeq:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Fissures.TimeIntervalSeq = TimeIntervalSeq
_0_Fissures._d_TimeIntervalSeq  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:iris.edu/Fissures/TimeInterval:1.0"], 0)
_0_Fissures._ad_TimeIntervalSeq = (omniORB.tcInternal.tv_alias, TimeIntervalSeq._NP_RepositoryId, "TimeIntervalSeq", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:iris.edu/Fissures/TimeInterval:1.0"], 0))
_0_Fissures._tc_TimeIntervalSeq = omniORB.tcInternal.createTypeCode(_0_Fissures._ad_TimeIntervalSeq)
omniORB.registerType(TimeIntervalSeq._NP_RepositoryId, _0_Fissures._ad_TimeIntervalSeq, _0_Fissures._tc_TimeIntervalSeq)
del TimeIntervalSeq

# enum LocationType
_0_Fissures.GEOGRAPHIC = omniORB.EnumItem("GEOGRAPHIC", 0)
_0_Fissures.GEOCENTRIC = omniORB.EnumItem("GEOCENTRIC", 1)
_0_Fissures.LocationType = omniORB.Enum("IDL:iris.edu/Fissures/LocationType:1.0", (_0_Fissures.GEOGRAPHIC, _0_Fissures.GEOCENTRIC,))

_0_Fissures._d_LocationType  = (omniORB.tcInternal.tv_enum, _0_Fissures.LocationType._NP_RepositoryId, "LocationType", _0_Fissures.LocationType._items)
_0_Fissures._tc_LocationType = omniORB.tcInternal.createTypeCode(_0_Fissures._d_LocationType)
omniORB.registerType(_0_Fissures.LocationType._NP_RepositoryId, _0_Fissures._d_LocationType, _0_Fissures._tc_LocationType)

# struct Location
_0_Fissures.Location = omniORB.newEmptyClass()
class Location (omniORB.StructBase):
    _NP_RepositoryId = "IDL:iris.edu/Fissures/Location:1.0"

    def __init__(self, latitude, longitude, elevation, depth, type):
        self.latitude = latitude
        self.longitude = longitude
        self.elevation = elevation
        self.depth = depth
        self.type = type

_0_Fissures.Location = Location
_0_Fissures._d_Location  = (omniORB.tcInternal.tv_struct, Location, Location._NP_RepositoryId, "Location", "latitude", omniORB.tcInternal.tv_float, "longitude", omniORB.tcInternal.tv_float, "elevation", omniORB.typeMapping["IDL:iris.edu/Fissures/Length:1.0"], "depth", omniORB.typeMapping["IDL:iris.edu/Fissures/Length:1.0"], "type", omniORB.typeMapping["IDL:iris.edu/Fissures/LocationType:1.0"])
_0_Fissures._tc_Location = omniORB.tcInternal.createTypeCode(_0_Fissures._d_Location)
omniORB.registerType(Location._NP_RepositoryId, _0_Fissures._d_Location, _0_Fissures._tc_Location)
del Location

# typedef ... ISODateTime
class ISODateTime:
    _NP_RepositoryId = "IDL:iris.edu/Fissures/ISODateTime:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Fissures.ISODateTime = ISODateTime
_0_Fissures._d_ISODateTime  = (omniORB.tcInternal.tv_string,0)
_0_Fissures._ad_ISODateTime = (omniORB.tcInternal.tv_alias, ISODateTime._NP_RepositoryId, "ISODateTime", (omniORB.tcInternal.tv_string,0))
_0_Fissures._tc_ISODateTime = omniORB.tcInternal.createTypeCode(_0_Fissures._ad_ISODateTime)
omniORB.registerType(ISODateTime._NP_RepositoryId, _0_Fissures._ad_ISODateTime, _0_Fissures._tc_ISODateTime)
del ISODateTime

# struct Time
_0_Fissures.Time = omniORB.newEmptyClass()
class Time (omniORB.StructBase):
    _NP_RepositoryId = "IDL:iris.edu/Fissures/Time:1.0"

    def __init__(self, date_time, leap_seconds_version):
        self.date_time = date_time
        self.leap_seconds_version = leap_seconds_version

_0_Fissures.Time = Time
_0_Fissures._d_Time  = (omniORB.tcInternal.tv_struct, Time, Time._NP_RepositoryId, "Time", "date_time", omniORB.typeMapping["IDL:iris.edu/Fissures/ISODateTime:1.0"], "leap_seconds_version", omniORB.tcInternal.tv_long)
_0_Fissures._tc_Time = omniORB.tcInternal.createTypeCode(_0_Fissures._d_Time)
omniORB.registerType(Time._NP_RepositoryId, _0_Fissures._d_Time, _0_Fissures._tc_Time)
del Time

# typedef ... TimeSeq
class TimeSeq:
    _NP_RepositoryId = "IDL:iris.edu/Fissures/TimeSeq:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Fissures.TimeSeq = TimeSeq
_0_Fissures._d_TimeSeq  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:iris.edu/Fissures/Time:1.0"], 0)
_0_Fissures._ad_TimeSeq = (omniORB.tcInternal.tv_alias, TimeSeq._NP_RepositoryId, "TimeSeq", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:iris.edu/Fissures/Time:1.0"], 0))
_0_Fissures._tc_TimeSeq = omniORB.tcInternal.createTypeCode(_0_Fissures._ad_TimeSeq)
omniORB.registerType(TimeSeq._NP_RepositoryId, _0_Fissures._ad_TimeSeq, _0_Fissures._tc_TimeSeq)
del TimeSeq

# struct TimeRange
_0_Fissures.TimeRange = omniORB.newEmptyClass()
class TimeRange (omniORB.StructBase):
    _NP_RepositoryId = "IDL:iris.edu/Fissures/TimeRange:1.0"

    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

_0_Fissures.TimeRange = TimeRange
_0_Fissures._d_TimeRange  = (omniORB.tcInternal.tv_struct, TimeRange, TimeRange._NP_RepositoryId, "TimeRange", "start_time", omniORB.typeMapping["IDL:iris.edu/Fissures/Time:1.0"], "end_time", omniORB.typeMapping["IDL:iris.edu/Fissures/Time:1.0"])
_0_Fissures._tc_TimeRange = omniORB.tcInternal.createTypeCode(_0_Fissures._d_TimeRange)
omniORB.registerType(TimeRange._NP_RepositoryId, _0_Fissures._d_TimeRange, _0_Fissures._tc_TimeRange)
del TimeRange

# typedef ... TimeRangeSeq
class TimeRangeSeq:
    _NP_RepositoryId = "IDL:iris.edu/Fissures/TimeRangeSeq:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Fissures.TimeRangeSeq = TimeRangeSeq
_0_Fissures._d_TimeRangeSeq  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:iris.edu/Fissures/TimeRange:1.0"], 0)
_0_Fissures._ad_TimeRangeSeq = (omniORB.tcInternal.tv_alias, TimeRangeSeq._NP_RepositoryId, "TimeRangeSeq", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:iris.edu/Fissures/TimeRange:1.0"], 0))
_0_Fissures._tc_TimeRangeSeq = omniORB.tcInternal.createTypeCode(_0_Fissures._ad_TimeRangeSeq)
omniORB.registerType(TimeRangeSeq._NP_RepositoryId, _0_Fissures._ad_TimeRangeSeq, _0_Fissures._tc_TimeRangeSeq)
del TimeRangeSeq

# struct ComplexNumber
_0_Fissures.ComplexNumber = omniORB.newEmptyClass()
class ComplexNumber (omniORB.StructBase):
    _NP_RepositoryId = "IDL:iris.edu/Fissures/ComplexNumber:1.0"

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

_0_Fissures.ComplexNumber = ComplexNumber
_0_Fissures._d_ComplexNumber  = (omniORB.tcInternal.tv_struct, ComplexNumber, ComplexNumber._NP_RepositoryId, "ComplexNumber", "real", omniORB.tcInternal.tv_float, "imaginary", omniORB.tcInternal.tv_float)
_0_Fissures._tc_ComplexNumber = omniORB.tcInternal.createTypeCode(_0_Fissures._d_ComplexNumber)
omniORB.registerType(ComplexNumber._NP_RepositoryId, _0_Fissures._d_ComplexNumber, _0_Fissures._tc_ComplexNumber)
del ComplexNumber

# typedef ... ComplexNumberSeq
class ComplexNumberSeq:
    _NP_RepositoryId = "IDL:iris.edu/Fissures/ComplexNumberSeq:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Fissures.ComplexNumberSeq = ComplexNumberSeq
_0_Fissures._d_ComplexNumberSeq  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:iris.edu/Fissures/ComplexNumber:1.0"], 0)
_0_Fissures._ad_ComplexNumberSeq = (omniORB.tcInternal.tv_alias, ComplexNumberSeq._NP_RepositoryId, "ComplexNumberSeq", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:iris.edu/Fissures/ComplexNumber:1.0"], 0))
_0_Fissures._tc_ComplexNumberSeq = omniORB.tcInternal.createTypeCode(_0_Fissures._ad_ComplexNumberSeq)
omniORB.registerType(ComplexNumberSeq._NP_RepositoryId, _0_Fissures._ad_ComplexNumberSeq, _0_Fissures._tc_ComplexNumberSeq)
del ComplexNumberSeq
class Area (_0_CORBA.ValueBase):
    _NP_RepositoryId = "IDL:iris.edu/Fissures/Area:1.0"

    def __init__(self, *args, **kwargs):
        raise RuntimeError("Cannot construct objects of this type.")

_0_Fissures.Area = Area
_0_Fissures._d_Area  = (omniORB.tcInternal.tv_value, Area, Area._NP_RepositoryId, "Area", _0_CORBA.VM_ABSTRACT, None, _0_CORBA.tcInternal.tv_null, )
_0_Fissures._tc_Area = omniORB.tcInternal.createTypeCode(_0_Fissures._d_Area)
omniORB.registerType(Area._NP_RepositoryId, _0_Fissures._d_Area, _0_Fissures._tc_Area)
del Area


# valuetype GlobalArea
_0_Fissures._d_GlobalArea = (omniORB.tcInternal.tv__indirect, ["IDL:iris.edu/Fissures/GlobalArea:1.0"])
omniORB.typeMapping["IDL:iris.edu/Fissures/GlobalArea:1.0"] = _0_Fissures._d_GlobalArea
_0_Fissures.GlobalArea = omniORB.newEmptyClass()

class GlobalArea (_0_Fissures.Area):
    _NP_RepositoryId = "IDL:iris.edu/Fissures/GlobalArea:1.0"

    def __init__(self, *args, **kwargs):
        if args:
            if len(args) != 0:
                raise TypeError("GlobalArea() takes 0 arguments "
                                "(%d given)" % len(args))
            pass
        if kwargs:
            self.__dict__.update(kwargs)

omniORB.registerValueFactory(GlobalArea._NP_RepositoryId, GlobalArea)

_0_Fissures.GlobalArea = GlobalArea
_0_Fissures._d_GlobalArea  = (omniORB.tcInternal.tv_value, GlobalArea, GlobalArea._NP_RepositoryId, "GlobalArea", _0_CORBA.VM_NONE, None, _0_CORBA.tcInternal.tv_null, )
_0_Fissures._tc_GlobalArea = omniORB.tcInternal.createTypeCode(_0_Fissures._d_GlobalArea)
omniORB.registerType(GlobalArea._NP_RepositoryId, _0_Fissures._d_GlobalArea, _0_Fissures._tc_GlobalArea)
del GlobalArea


# valuetype BoxArea
_0_Fissures._d_BoxArea = (omniORB.tcInternal.tv__indirect, ["IDL:iris.edu/Fissures/BoxArea:1.0"])
omniORB.typeMapping["IDL:iris.edu/Fissures/BoxArea:1.0"] = _0_Fissures._d_BoxArea
_0_Fissures.BoxArea = omniORB.newEmptyClass()

class BoxArea (_0_Fissures.Area):
    _NP_RepositoryId = "IDL:iris.edu/Fissures/BoxArea:1.0"

    def __init__(self, *args, **kwargs):
        if args:
            if len(args) != 4:
                raise TypeError("BoxArea() takes 4 arguments "
                                "(%d given)" % len(args))
            self.min_latitude = args[0]
            self.max_latitude = args[1]
            self.min_longitude = args[2]
            self.max_longitude = args[3]
        if kwargs:
            self.__dict__.update(kwargs)

omniORB.registerValueFactory(BoxArea._NP_RepositoryId, BoxArea)

_0_Fissures.BoxArea = BoxArea
_0_Fissures._d_BoxArea  = (omniORB.tcInternal.tv_value, BoxArea, BoxArea._NP_RepositoryId, "BoxArea", _0_CORBA.VM_NONE, None, _0_CORBA.tcInternal.tv_null, "min_latitude", omniORB.tcInternal.tv_float, _0_CORBA.PUBLIC_MEMBER, "max_latitude", omniORB.tcInternal.tv_float, _0_CORBA.PUBLIC_MEMBER, "min_longitude", omniORB.tcInternal.tv_float, _0_CORBA.PUBLIC_MEMBER, "max_longitude", omniORB.tcInternal.tv_float, _0_CORBA.PUBLIC_MEMBER)
_0_Fissures._tc_BoxArea = omniORB.tcInternal.createTypeCode(_0_Fissures._d_BoxArea)
omniORB.registerType(BoxArea._NP_RepositoryId, _0_Fissures._d_BoxArea, _0_Fissures._tc_BoxArea)
del BoxArea


# valuetype PointDistanceArea
_0_Fissures._d_PointDistanceArea = (omniORB.tcInternal.tv__indirect, ["IDL:iris.edu/Fissures/PointDistanceArea:1.0"])
omniORB.typeMapping["IDL:iris.edu/Fissures/PointDistanceArea:1.0"] = _0_Fissures._d_PointDistanceArea
_0_Fissures.PointDistanceArea = omniORB.newEmptyClass()

class PointDistanceArea (_0_Fissures.Area):
    _NP_RepositoryId = "IDL:iris.edu/Fissures/PointDistanceArea:1.0"

    def __init__(self, *args, **kwargs):
        if args:
            if len(args) != 4:
                raise TypeError("PointDistanceArea() takes 4 arguments "
                                "(%d given)" % len(args))
            self.latitude = args[0]
            self.longitude = args[1]
            self.min_distance = args[2]
            self.max_distance = args[3]
        if kwargs:
            self.__dict__.update(kwargs)

omniORB.registerValueFactory(PointDistanceArea._NP_RepositoryId, PointDistanceArea)

_0_Fissures.PointDistanceArea = PointDistanceArea
_0_Fissures._d_PointDistanceArea  = (omniORB.tcInternal.tv_value, PointDistanceArea, PointDistanceArea._NP_RepositoryId, "PointDistanceArea", _0_CORBA.VM_NONE, None, _0_CORBA.tcInternal.tv_null, "latitude", omniORB.tcInternal.tv_float, _0_CORBA.PUBLIC_MEMBER, "longitude", omniORB.tcInternal.tv_float, _0_CORBA.PUBLIC_MEMBER, "min_distance", omniORB.typeMapping["IDL:iris.edu/Fissures/Quantity:1.0"], _0_CORBA.PUBLIC_MEMBER, "max_distance", omniORB.typeMapping["IDL:iris.edu/Fissures/Quantity:1.0"], _0_CORBA.PUBLIC_MEMBER)
_0_Fissures._tc_PointDistanceArea = omniORB.tcInternal.createTypeCode(_0_Fissures._d_PointDistanceArea)
omniORB.registerType(PointDistanceArea._NP_RepositoryId, _0_Fissures._d_PointDistanceArea, _0_Fissures._tc_PointDistanceArea)
del PointDistanceArea


# enum FlinnEngdahlType
_0_Fissures.SEISMIC_REGION = omniORB.EnumItem("SEISMIC_REGION", 0)
_0_Fissures.GEOGRAPHIC_REGION = omniORB.EnumItem("GEOGRAPHIC_REGION", 1)
_0_Fissures.FlinnEngdahlType = omniORB.Enum("IDL:iris.edu/Fissures/FlinnEngdahlType:1.0", (_0_Fissures.SEISMIC_REGION, _0_Fissures.GEOGRAPHIC_REGION,))

_0_Fissures._d_FlinnEngdahlType  = (omniORB.tcInternal.tv_enum, _0_Fissures.FlinnEngdahlType._NP_RepositoryId, "FlinnEngdahlType", _0_Fissures.FlinnEngdahlType._items)
_0_Fissures._tc_FlinnEngdahlType = omniORB.tcInternal.createTypeCode(_0_Fissures._d_FlinnEngdahlType)
omniORB.registerType(_0_Fissures.FlinnEngdahlType._NP_RepositoryId, _0_Fissures._d_FlinnEngdahlType, _0_Fissures._tc_FlinnEngdahlType)

# valuetype FlinnEngdahlRegion
_0_Fissures._d_FlinnEngdahlRegion = (omniORB.tcInternal.tv__indirect, ["IDL:iris.edu/Fissures/FlinnEngdahlRegion:1.0"])
omniORB.typeMapping["IDL:iris.edu/Fissures/FlinnEngdahlRegion:1.0"] = _0_Fissures._d_FlinnEngdahlRegion
_0_Fissures.FlinnEngdahlRegion = omniORB.newEmptyClass()

class FlinnEngdahlRegion (_0_Fissures.Area):
    _NP_RepositoryId = "IDL:iris.edu/Fissures/FlinnEngdahlRegion:1.0"

    def __init__(self, *args, **kwargs):
        if args:
            if len(args) != 2:
                raise TypeError("FlinnEngdahlRegion() takes 2 arguments "
                                "(%d given)" % len(args))
            self.type = args[0]
            self.number = args[1]
        if kwargs:
            self.__dict__.update(kwargs)

omniORB.registerValueFactory(FlinnEngdahlRegion._NP_RepositoryId, FlinnEngdahlRegion)

_0_Fissures.FlinnEngdahlRegion = FlinnEngdahlRegion
_0_Fissures._d_FlinnEngdahlRegion  = (omniORB.tcInternal.tv_value, FlinnEngdahlRegion, FlinnEngdahlRegion._NP_RepositoryId, "FlinnEngdahlRegion", _0_CORBA.VM_NONE, None, _0_CORBA.tcInternal.tv_null, "type", omniORB.typeMapping["IDL:iris.edu/Fissures/FlinnEngdahlType:1.0"], _0_CORBA.PUBLIC_MEMBER, "number", omniORB.tcInternal.tv_long, _0_CORBA.PUBLIC_MEMBER)
_0_Fissures._tc_FlinnEngdahlRegion = omniORB.tcInternal.createTypeCode(_0_Fissures._d_FlinnEngdahlRegion)
omniORB.registerType(FlinnEngdahlRegion._NP_RepositoryId, _0_Fissures._d_FlinnEngdahlRegion, _0_Fissures._tc_FlinnEngdahlRegion)
del FlinnEngdahlRegion


# struct Plottable
_0_Fissures.Plottable = omniORB.newEmptyClass()
class Plottable (omniORB.StructBase):
    _NP_RepositoryId = "IDL:iris.edu/Fissures/Plottable:1.0"

    def __init__(self, x_coor, y_coor):
        self.x_coor = x_coor
        self.y_coor = y_coor

_0_Fissures.Plottable = Plottable
_0_Fissures._d_Plottable  = (omniORB.tcInternal.tv_struct, Plottable, Plottable._NP_RepositoryId, "Plottable", "x_coor", (omniORB.tcInternal.tv_sequence, omniORB.tcInternal.tv_long, 0), "y_coor", (omniORB.tcInternal.tv_sequence, omniORB.tcInternal.tv_long, 0))
_0_Fissures._tc_Plottable = omniORB.tcInternal.createTypeCode(_0_Fissures._d_Plottable)
omniORB.registerType(Plottable._NP_RepositoryId, _0_Fissures._d_Plottable, _0_Fissures._tc_Plottable)
del Plottable

# typedef ... PlottableSeq
class PlottableSeq:
    _NP_RepositoryId = "IDL:iris.edu/Fissures/PlottableSeq:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Fissures.PlottableSeq = PlottableSeq
_0_Fissures._d_PlottableSeq  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:iris.edu/Fissures/Plottable:1.0"], 0)
_0_Fissures._ad_PlottableSeq = (omniORB.tcInternal.tv_alias, PlottableSeq._NP_RepositoryId, "PlottableSeq", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:iris.edu/Fissures/Plottable:1.0"], 0))
_0_Fissures._tc_PlottableSeq = omniORB.tcInternal.createTypeCode(_0_Fissures._ad_PlottableSeq)
omniORB.registerType(PlottableSeq._NP_RepositoryId, _0_Fissures._ad_PlottableSeq, _0_Fissures._tc_PlottableSeq)
del PlottableSeq

# valuetype Sampling
_0_Fissures._d_Sampling = (omniORB.tcInternal.tv__indirect, ["IDL:iris.edu/Fissures/Sampling:1.0"])
omniORB.typeMapping["IDL:iris.edu/Fissures/Sampling:1.0"] = _0_Fissures._d_Sampling
_0_Fissures.Sampling = omniORB.newEmptyClass()

class Sampling (_0_CORBA.ValueBase):
    _NP_RepositoryId = "IDL:iris.edu/Fissures/Sampling:1.0"

    def __init__(self, *args, **kwargs):
        if args:
            if len(args) != 2:
                raise TypeError("Sampling() takes 2 arguments "
                                "(%d given)" % len(args))
            self.numPoints = args[0]
            self.interval = args[1]
        if kwargs:
            self.__dict__.update(kwargs)

omniORB.registerValueFactory(Sampling._NP_RepositoryId, Sampling)

_0_Fissures.Sampling = Sampling
_0_Fissures._d_Sampling  = (omniORB.tcInternal.tv_value, Sampling, Sampling._NP_RepositoryId, "Sampling", _0_CORBA.VM_NONE, None, _0_CORBA.tcInternal.tv_null, "numPoints", omniORB.tcInternal.tv_long, _0_CORBA.PUBLIC_MEMBER, "interval", omniORB.typeMapping["IDL:iris.edu/Fissures/TimeInterval:1.0"], _0_CORBA.PUBLIC_MEMBER)
_0_Fissures._tc_Sampling = omniORB.tcInternal.createTypeCode(_0_Fissures._d_Sampling)
omniORB.registerType(Sampling._NP_RepositoryId, _0_Fissures._d_Sampling, _0_Fissures._tc_Sampling)
del Sampling


# typedef ... SamplingSeq
class SamplingSeq:
    _NP_RepositoryId = "IDL:iris.edu/Fissures/SamplingSeq:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Fissures.SamplingSeq = SamplingSeq
_0_Fissures._d_SamplingSeq  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:iris.edu/Fissures/Sampling:1.0"], 0)
_0_Fissures._ad_SamplingSeq = (omniORB.tcInternal.tv_alias, SamplingSeq._NP_RepositoryId, "SamplingSeq", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:iris.edu/Fissures/Sampling:1.0"], 0))
_0_Fissures._tc_SamplingSeq = omniORB.tcInternal.createTypeCode(_0_Fissures._ad_SamplingSeq)
omniORB.registerType(SamplingSeq._NP_RepositoryId, _0_Fissures._ad_SamplingSeq, _0_Fissures._tc_SamplingSeq)
del SamplingSeq

# typedef ... ErrorCode
class ErrorCode:
    _NP_RepositoryId = "IDL:iris.edu/Fissures/ErrorCode:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Fissures.ErrorCode = ErrorCode
_0_Fissures._d_ErrorCode  = omniORB.tcInternal.tv_long
_0_Fissures._ad_ErrorCode = (omniORB.tcInternal.tv_alias, ErrorCode._NP_RepositoryId, "ErrorCode", omniORB.tcInternal.tv_long)
_0_Fissures._tc_ErrorCode = omniORB.tcInternal.createTypeCode(_0_Fissures._ad_ErrorCode)
omniORB.registerType(ErrorCode._NP_RepositoryId, _0_Fissures._ad_ErrorCode, _0_Fissures._tc_ErrorCode)
del ErrorCode
_0_Fissures.NOT_FOUND = 2
_0_Fissures.ILLEGAL_PARM = 3
_0_Fissures.ILLEGAL_ATTRIBUTE = 4

# struct Error
_0_Fissures.Error = omniORB.newEmptyClass()
class Error (omniORB.StructBase):
    _NP_RepositoryId = "IDL:iris.edu/Fissures/Error:1.0"

    def __init__(self, error_code, error_description):
        self.error_code = error_code
        self.error_description = error_description

_0_Fissures.Error = Error
_0_Fissures._d_Error  = (omniORB.tcInternal.tv_struct, Error, Error._NP_RepositoryId, "Error", "error_code", omniORB.typeMapping["IDL:iris.edu/Fissures/ErrorCode:1.0"], "error_description", (omniORB.tcInternal.tv_string,0))
_0_Fissures._tc_Error = omniORB.tcInternal.createTypeCode(_0_Fissures._d_Error)
omniORB.registerType(Error._NP_RepositoryId, _0_Fissures._d_Error, _0_Fissures._tc_Error)
del Error

# exception FissuresException
_0_Fissures.FissuresException = omniORB.newEmptyClass()
class FissuresException (CORBA.UserException):
    _NP_RepositoryId = "IDL:iris.edu/Fissures/FissuresException:1.0"

    def __init__(self, the_error):
        CORBA.UserException.__init__(self, the_error)
        self.the_error = the_error

_0_Fissures.FissuresException = FissuresException
_0_Fissures._d_FissuresException  = (omniORB.tcInternal.tv_except, FissuresException, FissuresException._NP_RepositoryId, "FissuresException", "the_error", omniORB.typeMapping["IDL:iris.edu/Fissures/Error:1.0"])
_0_Fissures._tc_FissuresException = omniORB.tcInternal.createTypeCode(_0_Fissures._d_FissuresException)
omniORB.registerType(FissuresException._NP_RepositoryId, _0_Fissures._d_FissuresException, _0_Fissures._tc_FissuresException)
del FissuresException

# exception NotImplemented
_0_Fissures.NotImplemented = omniORB.newEmptyClass()
class NotImplemented (CORBA.UserException):
    _NP_RepositoryId = "IDL:iris.edu/Fissures/NotImplemented:1.0"

    def __init__(self):
        CORBA.UserException.__init__(self)

_0_Fissures.NotImplemented = NotImplemented
_0_Fissures._d_NotImplemented  = (omniORB.tcInternal.tv_except, NotImplemented, NotImplemented._NP_RepositoryId, "NotImplemented")
_0_Fissures._tc_NotImplemented = omniORB.tcInternal.createTypeCode(_0_Fissures._d_NotImplemented)
omniORB.registerType(NotImplemented._NP_RepositoryId, _0_Fissures._d_NotImplemented, _0_Fissures._tc_NotImplemented)
del NotImplemented

# abstract interface FissuresIterator
_0_Fissures._d_FissuresIterator = (omniORB.tcInternal.tv_abstract_interface, "IDL:iris.edu/Fissures/FissuresIterator:1.0", "FissuresIterator")
omniORB.typeMapping["IDL:iris.edu/Fissures/FissuresIterator:1.0"] = _0_Fissures._d_FissuresIterator
_0_Fissures.FissuresIterator = omniORB.newEmptyClass()
class FissuresIterator :
    _NP_RepositoryId = _0_Fissures._d_FissuresIterator[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_Fissures.FissuresIterator = FissuresIterator
_0_Fissures._tc_FissuresIterator = omniORB.tcInternal.createTypeCode(_0_Fissures._d_FissuresIterator)
omniORB.registerType(FissuresIterator._NP_RepositoryId, _0_Fissures._d_FissuresIterator, _0_Fissures._tc_FissuresIterator)

# FissuresIterator operations and attributes
FissuresIterator._d_how_many = ((), (omniORB.tcInternal.tv_long, ), None)
FissuresIterator._d_reset = ((), (), None)
FissuresIterator._d_destroy = ((), (), None)

# FissuresIterator object reference
class _objref_FissuresIterator (CORBA.Object):
    _NP_RepositoryId = FissuresIterator._NP_RepositoryId

    def __init__(self):
        CORBA.Object.__init__(self)

    def how_many(self, *args):
        return _omnipy.invoke(self, "how_many", _0_Fissures.FissuresIterator._d_how_many, args)

    def reset(self, *args):
        return _omnipy.invoke(self, "reset", _0_Fissures.FissuresIterator._d_reset, args)

    def destroy(self, *args):
        return _omnipy.invoke(self, "destroy", _0_Fissures.FissuresIterator._d_destroy, args)

    __methods__ = ["how_many", "reset", "destroy"] + CORBA.Object.__methods__

omniORB.registerObjref(FissuresIterator._NP_RepositoryId, _objref_FissuresIterator)
_0_Fissures._objref_FissuresIterator = _objref_FissuresIterator
del FissuresIterator, _objref_FissuresIterator

# FissuresIterator skeleton
__name__ = "idl.Fissures__POA"
class FissuresIterator (PortableServer.Servant):
    _NP_RepositoryId = _0_Fissures.FissuresIterator._NP_RepositoryId


    _omni_op_d = {"how_many": _0_Fissures.FissuresIterator._d_how_many, "reset": _0_Fissures.FissuresIterator._d_reset, "destroy": _0_Fissures.FissuresIterator._d_destroy}

FissuresIterator._omni_skeleton = FissuresIterator
_0_Fissures__POA.FissuresIterator = FissuresIterator
omniORB.registerSkeleton(FissuresIterator._NP_RepositoryId, FissuresIterator)
del FissuresIterator
__name__ = "idl.Fissures"

# struct AuditInfo
_0_Fissures.AuditInfo = omniORB.newEmptyClass()
class AuditInfo (omniORB.StructBase):
    _NP_RepositoryId = "IDL:iris.edu/Fissures/AuditInfo:1.0"

    def __init__(self, party, description):
        self.party = party
        self.description = description

_0_Fissures.AuditInfo = AuditInfo
_0_Fissures._d_AuditInfo  = (omniORB.tcInternal.tv_struct, AuditInfo, AuditInfo._NP_RepositoryId, "AuditInfo", "party", (omniORB.tcInternal.tv_string,0), "description", (omniORB.tcInternal.tv_string,0))
_0_Fissures._tc_AuditInfo = omniORB.tcInternal.createTypeCode(_0_Fissures._d_AuditInfo)
omniORB.registerType(AuditInfo._NP_RepositoryId, _0_Fissures._d_AuditInfo, _0_Fissures._tc_AuditInfo)
del AuditInfo

# typedef ... AuditInfoOpt
class AuditInfoOpt:
    _NP_RepositoryId = "IDL:iris.edu/Fissures/AuditInfoOpt:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Fissures.AuditInfoOpt = AuditInfoOpt
_0_Fissures._d_AuditInfoOpt  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:iris.edu/Fissures/AuditInfo:1.0"], 1)
_0_Fissures._ad_AuditInfoOpt = (omniORB.tcInternal.tv_alias, AuditInfoOpt._NP_RepositoryId, "AuditInfoOpt", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:iris.edu/Fissures/AuditInfo:1.0"], 1))
_0_Fissures._tc_AuditInfoOpt = omniORB.tcInternal.createTypeCode(_0_Fissures._ad_AuditInfoOpt)
omniORB.registerType(AuditInfoOpt._NP_RepositoryId, _0_Fissures._ad_AuditInfoOpt, _0_Fissures._tc_AuditInfoOpt)
del AuditInfoOpt

# struct AuditElement
_0_Fissures.AuditElement = omniORB.newEmptyClass()
class AuditElement (omniORB.StructBase):
    _NP_RepositoryId = "IDL:iris.edu/Fissures/AuditElement:1.0"

    def __init__(self, time_occurred, information):
        self.time_occurred = time_occurred
        self.information = information

_0_Fissures.AuditElement = AuditElement
_0_Fissures._d_AuditElement  = (omniORB.tcInternal.tv_struct, AuditElement, AuditElement._NP_RepositoryId, "AuditElement", "time_occurred", omniORB.typeMapping["IDL:iris.edu/Fissures/Time:1.0"], "information", omniORB.typeMapping["IDL:iris.edu/Fissures/AuditInfo:1.0"])
_0_Fissures._tc_AuditElement = omniORB.tcInternal.createTypeCode(_0_Fissures._d_AuditElement)
omniORB.registerType(AuditElement._NP_RepositoryId, _0_Fissures._d_AuditElement, _0_Fissures._tc_AuditElement)
del AuditElement

# typedef ... AuditTrail
class AuditTrail:
    _NP_RepositoryId = "IDL:iris.edu/Fissures/AuditTrail:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Fissures.AuditTrail = AuditTrail
_0_Fissures._d_AuditTrail  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:iris.edu/Fissures/AuditElement:1.0"], 0)
_0_Fissures._ad_AuditTrail = (omniORB.tcInternal.tv_alias, AuditTrail._NP_RepositoryId, "AuditTrail", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:iris.edu/Fissures/AuditElement:1.0"], 0))
_0_Fissures._tc_AuditTrail = omniORB.tcInternal.createTypeCode(_0_Fissures._ad_AuditTrail)
omniORB.registerType(AuditTrail._NP_RepositoryId, _0_Fissures._ad_AuditTrail, _0_Fissures._tc_AuditTrail)
del AuditTrail

# abstract interface AuditSystemAccess
_0_Fissures._d_AuditSystemAccess = (omniORB.tcInternal.tv_abstract_interface, "IDL:iris.edu/Fissures/AuditSystemAccess:1.0", "AuditSystemAccess")
omniORB.typeMapping["IDL:iris.edu/Fissures/AuditSystemAccess:1.0"] = _0_Fissures._d_AuditSystemAccess
_0_Fissures.AuditSystemAccess = omniORB.newEmptyClass()
class AuditSystemAccess :
    _NP_RepositoryId = _0_Fissures._d_AuditSystemAccess[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_Fissures.AuditSystemAccess = AuditSystemAccess
_0_Fissures._tc_AuditSystemAccess = omniORB.tcInternal.createTypeCode(_0_Fissures._d_AuditSystemAccess)
omniORB.registerType(AuditSystemAccess._NP_RepositoryId, _0_Fissures._d_AuditSystemAccess, _0_Fissures._tc_AuditSystemAccess)

# AuditSystemAccess operations and attributes
AuditSystemAccess._d_get_audit_trail = ((), (omniORB.typeMapping["IDL:iris.edu/Fissures/AuditTrail:1.0"], ), {_0_Fissures.NotImplemented._NP_RepositoryId: _0_Fissures._d_NotImplemented})

# AuditSystemAccess object reference
class _objref_AuditSystemAccess (CORBA.Object):
    _NP_RepositoryId = AuditSystemAccess._NP_RepositoryId

    def __init__(self):
        CORBA.Object.__init__(self)

    def get_audit_trail(self, *args):
        return _omnipy.invoke(self, "get_audit_trail", _0_Fissures.AuditSystemAccess._d_get_audit_trail, args)

    __methods__ = ["get_audit_trail"] + CORBA.Object.__methods__

omniORB.registerObjref(AuditSystemAccess._NP_RepositoryId, _objref_AuditSystemAccess)
_0_Fissures._objref_AuditSystemAccess = _objref_AuditSystemAccess
del AuditSystemAccess, _objref_AuditSystemAccess

# AuditSystemAccess skeleton
__name__ = "idl.Fissures__POA"
class AuditSystemAccess (PortableServer.Servant):
    _NP_RepositoryId = _0_Fissures.AuditSystemAccess._NP_RepositoryId


    _omni_op_d = {"get_audit_trail": _0_Fissures.AuditSystemAccess._d_get_audit_trail}

AuditSystemAccess._omni_skeleton = AuditSystemAccess
_0_Fissures__POA.AuditSystemAccess = AuditSystemAccess
omniORB.registerSkeleton(AuditSystemAccess._NP_RepositoryId, AuditSystemAccess)
del AuditSystemAccess
__name__ = "idl.Fissures"

#
# End of module "Fissures"
#
__name__ = "idl.idl.Fissures_idl"

_exported_modules = ( "idl.Fissures", )

# The end.
