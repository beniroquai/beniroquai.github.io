#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
Connect to the microscope 
'''
from  opentrons_helper_class import * 
from microscope_client import MicroscopeClient 
microscope = MicroscopeClient(host="21.3.2.3", port=5000)
#!pip3 install zeroconf
#!pip3 install requests


# In[52]:


# lets assume the robots light source is in place 
microscope.set_laser_led(i_laser=0, i_led=1)


# lets define the position for the seventh well (ID)
offset_x = 5000
offset_y = -1000
offset_z = 1500

microscope.move((offset_x, offset_y, offset_z))

print(microscope.position)

#microscope.move()


# In[ ]:


offset_z
I_laser = 0
I_led = 1
id = 0


# In[65]:


# create the object for the well scanner 
wellscanner = Hi2Module( microscope, well_to_well_steps=9000,
             N_wells = 96, Nx = 8, Ny = 12)

# set the well-position of the well number  7 
wellscanner.set_offset_for_well_id_7(offset_x, offset_y)


#microscope.home()
for id in range(91,94):

    # first go to well ID 
    wellscanner.move_to_well_id(offset_z=None, well_index=id)
    
    # get the acutal position of the microscope
    current_x, current_y, _ = microscope.position['x'],  microscope.position['y'],  microscope.position['z']
    
   # current_x += np.radnom.rnadniintcurrent_x+ 500
    
    microscope.set_laser_led(I_laser,I_led)
    
    offset_z = microscope.autofocus_coarse(dz=1000, nz=15)
    current_x, current_y, _ = microscope.position['x'],  microscope.position['y'],  microscope.position['z']
    

    # 1. capture the in-focus image
    base_filename = 'data_generation_GAN_'
    params = {
        "filename": base_filename+"in_focus_edit3_"+str(id),
    }
    microscope.set_laser_led(I_laser,I_led)
    microscope.move((offset_x, offset_y, offset_z))
    time.sleep(1)
    microscope.capture_image_to_disk(params)

    max_dz = 200 # the maximum value the focus may differ => plus minus max_dz/2
    offset_z_defocus = offset_z+ np.random.randint(max_dz)-(max_dz//2)
    print(offset_z_defocus)

    # 2. cpature the defocus image 
    params = {
        "filename": base_filename+"de_focus_edit3_"+str(id),
    }

    microscope.move((current_x, current_y, offset_z_defocus))
    time.sleep(1) # debounce any vibvration
    microscope.capture_image_to_disk(params)



# In[53]:





# In[ ]:




num_cell_list = []
autofocus_dz = 2000
autofocus_Nz= 15
mytime = -time.time()
#t_duration = 20 # minutes
focus_pos_list = None # start with a fresh list
well_to_well_steps= 9000
t_duration = 60 # how long does the experiment preform?
t_period = 5 # min - how often should the expimrent be carried out?
is_autofocus = "normal"
is_find_prefocus = True

i_experiment = 0

timestamp = str( 0)

well_id_list = np.arange(0,32)
well_id_list = (7,0,24,31)

#
wellscanner = Hi2Module( microscope, well_to_well_steps=9000,
             N_wells = 96, Nx = 8, Ny = 12)

# set the well-position of the well number  7 
wellscanner.set_offset_for_well_id_7(offset_x, offset_y)

# test the functions 
well_xy_pos = wellscanner.wellid_to_xy(well_id_list)[0]

# fit 2d plane to focus points    
wellscanner.gen_focus_pos_list(calib_well_ids=well_id_list)

# get fitting parameters
c_fit = wellscanner.get_focus_fit_func()
print(c_fit)

# test motion
wellscanner.move_to_well_xy(offset_z=None, pos_xy=(0,0))
wellscanner.move_to_well_id(offset_z=None, well_index=(0,0))

# perform a testing well scan by moving robot to light position and do a whole plate scan
#move_to_coord(pipette_8, position_sample_light, offset=(0,0,0), minimum_z_height=minimum_z_height)
wellscanner.wellscan_list(
            i_experiment,
            well_id_list,
            autofocus_dz, 
            autofocus_Nz,
            name_experiment="wellscan_defocus_infocus_",
            is_autofocus=is_autofocus, 
            I_laser=0, 
            I_led=1,
            t_debounce=.5,
            is_find_prefocus=is_find_prefocus,
            process_func=None)

'''
wellscanner.wellscan_list(
            i_experiment,
            well_id_list,
            autofocus_dz, 
            autofocus_Nz,
            name_experiment="wellscan_",
            is_autofocus=False, 
            I_laser=0, 
            I_led=1,
            t_debounce=.5,
            is_find_prefocus=is_find_prefocus,
            process_func=None)
'''

microscope.autofocus_coarse
microscope.set_laser_led
microscope.move()


# ### Go to XY position
# ### Turn on light
# ### Do autofocus
# ### take a snapshot
# ### detune focus +/- random z value
# ### take snapshot_2

# In[ ]:




