from pylandsat import Scene
'''
scenes that were randomly selected for preprocessing
'''
def get_data():
    sens8 = 'toydata/LC08_L1TP_076010_20160713_20170222_01_T1'
    sens7 = 'toydata/LE07_L1TP_076010_20200614_20200711_01_T1'
    sens5 = 'toydata/LT05_L1TP_076010_20060904_20160911_01_T1'
    sens4 = 'toydata/LT04_L1TP_076010_19920617_20160929_01_T1'
    sens3 = 'toydata/LM03_L1TP_083010_19820728_20180413_01_T2'
    sens2 = 'toydata/LM02_L1TP_083010_19770814_20180422_01_T2'
    sens1 = 'toydata/LM01_L1GS_083010_19730703_20180428_01_T2'

    scene_sens8 = Scene(sens8)
    scene_sens7 = Scene(sens7)
    scene_sens5 = Scene(sens5)
    scene_sens4 = Scene(sens4)
    scene_sens3 = Scene(sens3)
    scene_sens2 = Scene(sens2)
    scene_sens1 = Scene(sens1)

    scene_list = []
    scene_list.extend((scene_sens1, scene_sens2, scene_sens3, scene_sens4, scene_sens5,scene_sens7,scene_sens8))

    return scene_list

