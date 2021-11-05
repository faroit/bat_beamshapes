'''
Source parameter estimation
===========================
Sounds recorded in nature are often directional (bird songs, bat calls, etc.). This
directionality means a set of observations (reduction in call level) may be only due
to the animal turning one way or the other - and not necessarily because of an actual 
change in sound production. Fitting a `source model <../general_intro.rst>` helps in accounting for 
sound directionality and actually being able to estimate many other aspects of sound production. 

Let's simulate an example to show the power of actually using a source model to study 
animal sound production. Of course, any type of sound can be studied this way!! 

'''
import matplotlib.pyplot as plt
import numpy as np 
import beamshapes.sim_reclevels as simlevels



#%% 
# Let's simulate a bat that emits five calls as it flies through a room with 12 microphones. 
# We'll pretend our simulated bat is a flying piston in a sphere for now. In general, here we'll
# simulate the following progressive trends 1) reduction in call level 2) 'widening' of the beam. 
# These two trends mimic what a bat coming in to capture an insect will do. 

# Define mic positions  in 2D at flight height of the bat
mic_posns = np.zeros((12,2))
# define x-positions
mic_posns[:4,0] = 0 # first three mics on left wall
mic_posns[4:8,0] = np.linspace(0.5,2,4)
mic_posns[-4:,0] = 2.5

# define y-positions 
mic_posns[:4,1] = np.linspace(0,2,4)
mic_posns[4:8,1] = 2.5
mic_posns[-4:,1] = np.linspace(0,2,4)[::-1]

# Define on-axis level for each of the 5 calls (dB SPL re 20 muPa at 1m)
# These levels are semi-realistic!
onaxis_levels = [100, 96, 90, 84, 84]

# Define the directivity function broadly by altering ka for each call
overall_ka = [10, 5, 4, 3, 2]
#%%
# Where was the bat at each of the 5 call emissinos?
flight_path_x =  np.array([0.45, 1.0, 1.5, 2.0, 2.4])
flight_path_y = np.array([0.3, 0.8, 1.2, 0.6, 0.4])
flight_path = np.column_stack((flight_path_x, flight_path_y))

# Where was the bat aiming it's call? 
call_directions = np.deg2rad(np.array([15, 60, 140, 160, 200]))


plt.figure()
plt.plot(flight_path[:,0], flight_path[:,1], '*')
plt.plot(mic_posns[:,0], mic_posns[:,1],'r*')

for i, direction in enumerate(call_directions):
    arrow_dx, arrow_dy = np.sin(direction), np.cos(direction)
    arrow_dx *= 0.5
    arrow_dy *= 0.5
    plt.arrow(flight_path[i,0], flight_path[i,1],arrow_dx, arrow_dy, head_width=0.05)
    plt.text(flight_path[i,0]-0.5, flight_path[i,1]+0.1,f'direction: {np.round(np.degrees(call_directions[i]),2)}')
    plt.text(flight_path[i,0]-0.1, flight_path[i,1]+0.2,f'SL: {onaxis_levels[i]}')
    plt.text(flight_path[i,0]-0.1, flight_path[i,1]+0.3,f'ka: {overall_ka[i]}')

#%%
# Calculate the received levels at each mic assuming an omnidirectional call

received_omnidirn_level = np.zeros((mic_posns.shape[0], 5))
for i, call_level in enumerate(onaxis_levels):
    received_omnidirn_level[:,i] = simlevels.calc_mic_level_nobeamshape(call_level,
                                                       flight_path[i,:].reshape(-1,2),
                                                       mic_posns)
#%% 
# Having calculated the received levels assuming an omnidirectional call, let's now
# include the beamshapes arising from a piston in a sphere. Let's start by calculating the 
# relative bat to mic 
