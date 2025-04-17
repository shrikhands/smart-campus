unique_locations = {1:'upper east side lofts',
                        2:'parking structure 1',
                        3:'rec and wellness center',
                        4:'library',
                        5:'collegetown drive',
                        6:'parking structure 2',
                        7:'riverside hall',
                        8:'hornet bookstore',
                        9:'amador hall',
                        10:'parking structure 3',
                        11:'sierra hall',
                        12:'yosemite hall',
                        13:'dining commons',
                        14:'sequoia hall',
                        15:'lot 4',
                        16:'american river courtyard',
                        17:'lot 2',
                        18:'lot 11',
                        19:'folsom hall',
                        20:'academic information resource center',
                        21:'mendocino hall',
                        22:'eureka hall',
                        23:'folsom blvd',
                        24:'lot 8',
                        25:'residence hall parking',
                        26:'shasta hall',
                        27:'draper hall',
                        28:'desmond hall',
                        29:'jenkins hall',
                        30:'university union',
                        31:'lot 7',
                        32:'brighton hall',
                        33:'del norte hall',
                        34:'lot 1',
                        35:'sutter hall',
                        36:'bike compound #1',
                        37:'non campus locations',
                        38:'lot 10',
                        39:'stadium',
                        40:'solano hall',
                        41:'river front center',
                        42:'state university drive',
                        43:'bike compound #3',
                        44:'parking structure 5'}

def getLocationNum(location):
    key_list = list(unique_locations.keys())
    val_list = list(unique_locations.values())
    return key_list[val_list.index(location)]

def getAllLocations():
    return unique_locations

def getLocationName(location_num):
    return unique_locations.get(location_num)