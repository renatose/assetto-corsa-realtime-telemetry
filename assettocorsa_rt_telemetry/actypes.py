from struct import Struct
from collections import namedtuple


def format_string(_string: bytes):
    try:
        r_string = _string.decode(encoding="UTF-16", errors="ignore")
    except UnicodeDecodeError:
        print("Had a hard time decoding string:", _string)
        return _string

    r_string = r_string.split("%")
    return r_string[0]


HandShaker = Struct('iii')

HandShakerResponse = Struct('100s100sii100s100s')
THandShakerResponse = namedtuple('HandShakerResponse', 'carName driverName identifier version trackName trackConfig')


def resolve_handshake_response(message):
    if type(message) is not bytes:
        print("Feed me bytes, not: ", type(message), message)
        return THandShakerResponse("", "", 0, 0, "", "")
    unpacked = HandShakerResponse.unpack(message)
    return THandShakerResponse(format_string(unpacked[0]), format_string(unpacked[1]), unpacked[2], unpacked[3],
                               format_string(unpacked[4]), format_string(unpacked[5]))


RTCarInfo = Struct('ci'
                   'fff'
                   '??????'
                   'fff'
                   'iiii'
                   'fffffif'
                   '4f4f4f4f4f4f4f4f4f4f4f4f4f4f'
                   'ff'
                   '3f')

TRTCarInfo = namedtuple('RTCarInfo', 'identifier size '
                                     'speed_Kmh speed_Mph speed_Ms '
                                     'isAbsEnabled isAbsInAction isTcInAction isTcEnabled isInPit isEngineLimiterOn '
                                     'accG_vertical accG_horizontal accG_frontal '
                                     'lapTime lastLap bestLap lapCount '
                                     'gas brake clutch engineRPM steer gear cgHeight '
                                     'wheelAngularSpeed0 wheelAngularSpeed1 wheelAngularSpeed2 wheelAngularSpeed3 '
                                     'slipAngle0 slipAngle1 slipAngle2 slipAngle3 '
                                     'slipAngle_ContactPatch0 slipAngle_ContactPatch1 '
                                     ' slipAngle_ContactPatch2 slipAngle_ContactPatch3 '
                                     'slipRatio0 slipRatio1 slipRatio2 slipRatio3 '
                                     'tyreSlip0 tyreSlip1 tyreSlip2 tyreSlip3 '
                                     'ndSlip0 ndSlip1 ndSlip2 ndSlip3 '
                                     'load0 load1 load2 load3 '
                                     'Dy0 Dy1 Dy2 Dy3 '
                                     'Mz0 Mz1 Mz2 Mz3 '
                                     'tyreDirtyLevel0 tyreDirtyLevel1 tyreDirtyLevel2 tyreDirtyLevel3 '
                                     'camberRAD0 camberRAD1 camberRAD2 camberRAD3 '
                                     'tyreRadius0 tyreRadius1 tyreRadius2 tyreRadius3 '
                                     'tyreLoadedRadius0 tyreLoadedRadius1 tyreLoadedRadius2 tyreLoadedRadius3 '
                                     'suspensionHeight0 suspensionHeight1 suspensionHeight2 suspensionHeight3 '
                                     'carPositionNormalized carSlope '
                                     'carCoordinatesX carCoordinatesY carCoordinatesZ')


def resolve_car_info(message):
    return TRTCarInfo._make(RTCarInfo.unpack(message))
