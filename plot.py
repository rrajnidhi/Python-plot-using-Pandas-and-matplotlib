import numpy as np
from matplotlib import pyplot as plt
import pandas
fig, ax1 = plt.subplots()


df = pandas.read_csv ('local_pos_alt.csv')

# plot 1
plt.title("Altitude comparison from local topic and recovery alt") 
ax1.set_xlabel('time')
ax1.set_ylabel('from px4 local position topic')
df.px4_local_z=df.px4_local_z*-1
ax1.plot(df.time, df.px4_local_z,color="blue")

#max
ymax = df['px4_local_z'].max()
xmax=df[df['px4_local_z']==ymax].index.values
ax1.annotate(ymax, xy=(xmax, ymax), xytext=(xmax, ymax + 5), arrowprops=dict(facecolor='black'),)


ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
ax2.set_ylabel(' red is recovery altitude')  # we already handled the x-label with ax1
ax2.plot(df.time, df.recovery_alt, color="red")



# plot 2
fig, ax3 = plt.subplots()
plt.title("Altitude from Global position topic") 
ax3.set_xlabel('time')
ax3.set_ylabel('Global position altitude')
reference_altitude=154.97855
df.px4_gps_z=df.px4_gps_z-reference_altitude
ax3.plot(df.time, df.px4_gps_z,color="red")

#max
ymax = df['px4_gps_z'].max()
xmax=df[df['px4_gps_z']==ymax].index.values
ax3.annotate(ymax, xy=(xmax, ymax), xytext=(xmax, ymax + 5), arrowprops=dict(facecolor='black'),)

# plot 3
fig, ax4 = plt.subplots()
plt.title("Altitude from raw GPS topic") 
ax3.set_xlabel('time')
ax3.set_ylabel('Raw GPS altitude')
reference_altitude=154.97855
df.px4_raw_gps_alt=df.px4_raw_gps_alt/1000
df.px4_raw_gps_alt=df.px4_raw_gps_alt-reference_altitude
ax4.plot(df.time, df.px4_raw_gps_alt,color="green")

#max
ymax = df['px4_raw_gps_alt'].max()
xmax=df[df['px4_raw_gps_alt']==ymax].index.values
ax4.annotate(ymax, xy=(xmax, ymax), xytext=(xmax, ymax + 5), arrowprops=dict(facecolor='black'),)




#for plotting in same graph

# ax3 = ax1.twinx()
# fig, ax3 = plt.subplots()
# ax3.set_xlabel('time')
# ax3.set_ylabel('from px4 GPS position topic')
# reference_altitude=154.97855
# df.px4_gps_z=df.px4_gps_z-reference_altitude
# ax3.plot(df.time,df.px4_gps_z)

# fig, ax4 = plt.subplots()
# ax4.set_xlabel('time')
# ax4.set_ylabel('from px4 GPS RAW position topic')
# df.px4_raw_gps_alt=df.px4_raw_gps_alt/1000-reference_altitude
# ax3.plot(df.time,df.px4_raw_gps_alt)




plt.show()