from opentrons import protocol_api
import pandas as pd
import json

metadata = {'apiLevel': '2.10'}
def run(protocol: protocol_api.ProtocolContext):

    #robot needs to know what each labware component is
    LABWARE = {'reservoir':'thermo_12002301_microplate_reservoir_1well_pp_96pbottom_sw_300000ul',
                  'start':'gbo_675801_microplate_96well_ps_fbottom_rw_199ul_uvstar_halfarea',
               'dilution':'gbo_650101_microplate_96well_ps_ubottom_rw_323ul'}
    
    #robot needs to know where each labware is
    PLATE_RACKS = {'reservoir':11, #reservoir
               'start':10, #bravo plate
               'dilution':7 #output plate
               }

    #robot needs to know what type of tip only p20 is used here is on what racks (tips can be on more than 1 rack)
    TIP_RACKS = {20:[8]}



    #actually load the labware
    plates = {}
    for k in PLATE_RACKS:
        with open('./labware/' + LABWARE[k] +'.json','r') as f:
            plate_def = json.load(f)
            plates[k] = protocol.load_labware_from_definition(plate_def, PLATE_RACKS[k])

    tips = {}
    for k in TIP_RACKS:
        tips[k] = []
        for rack in TIP_RACKS[k]:
            tips[k]+=[protocol.load_labware('opentrons_96_tiprack_{}ul'.format(k), rack)]

    #these are the actual ppettes that move things around
    p20  = protocol.load_instrument('p20_single_gen2','left',tip_racks=tips[20])

    #read input into pandas dataframe

    #TODO: PERFORM THE DILUTION FROM COLUMN 1 of START PLATE TO COLUMN 1 of DILUTION PLATE 
    #      s.t. concentration of all samples in diultion plate is 9 ug/mL
    #Easiest method is to iterate through the input dataframe and add the appropriate amount of reservoir
    #then iterate again and add the appropriate amount of sample.  This is to save tips.

    #EXAMPLE MOVE: take 15 mL of the sample in A1 of the start plate and dispense it in A1 of the dilution plate
    p20.pick_up_tip()
    p20.aspirate(15,plates['start']['A1'])
    p20.dispense(15,plates['dilution']['A1'])

