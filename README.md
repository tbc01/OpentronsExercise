# OpentronsExercise
![image](https://user-images.githubusercontent.com/25331992/167935108-5e467555-71b7-4dcc-a207-43f5320f864b.png)

## Requirements

- pandas: https://pandas.pydata.org/
- opentrons api: https://docs.opentrons.com/v2/

## Edit dilution_exercise.py to accomplish the following
**Objective: All concentrations of the samples in column 1 of rack 7 are 9 ug/mL, where the sample in A1 of rack 7 is transferred from the sample in A1 of rack 10, etc**
Steps:
**1.** Transfer (a possibly variable) volume of buffer from the reservoir on rack 11.
**2.** Transfer (a possibly variable) amount of sample from each of A1...12 on rack 10 to the corresponding well in rack 7.

**Constraints:**
1. Each tip can only touch 1 sample (necessary to pick up and drop tips)
2. The volume taken from any well in column 1 of rack 10 is less than 25 mL.
3. The total volume in any well in column 1 of rack 7 is less than 180 mL.

**Note**

When taking a volume_x of sample with concentration_x and a buffer volume_y, the concentration of the resulting volume is:

<img src="https://render.githubusercontent.com/render/math?math=\mathrm{concentration}_z = \mathrm{concentration}_x\times\frac{\mathrm{volume}_x}{\mathrm{volume}_x ++++ \mathrm{volume}_y}">


**Appendix**

labware and locations defined in dilution_exercise.py

![image](https://user-images.githubusercontent.com/25331992/167941364-2682cd35-5af5-4309-b6af-4a8045e976ae.png)
