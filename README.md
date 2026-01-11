# Breakdown-Pro
Breakdown-Pro Breakdown Pro for Nuke Frame_Breakdown is a professional Nuke tool that captures a single frame from selected nodes and saves breakdown images automatically. It is designed for fast look-dev, reviews, and shot breakdowns.



HI im Nitin Kashyap   VFX Compositor


![Nuke](https://img.shields.io/badge/Nuke-Compatible-Green)
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)






<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=C++,py,qt," />
  </a>
</p>





<h1 align="center">
    <img src="https://readme-typing-svg.herokuapp.com/?font=Righteous&size=35&center=true&vCenter=true&width=500&height=70&duration=5000&lines=Hi+There!+👋;+I'm+Nitin+Kashyap;" />
</h1>

# new version Breakdown Pro_v1.2

    New Version add file explorer Open_Folder Button   Breakdown Folder
    
    add dot marker ToggleSwitch Button

<img width="883" height="592" alt="Install_05" src="https://github.com/user-attachments/assets/dff65232-e48a-479e-9d49-db1936ca3f78" />



<img width="723" height="466" alt="Install_01" src="https://github.com/user-attachments/assets/a82488ef-2462-49c7-ac8d-47b8c0312e3f" />




Platform       : Windows / Linux / macOS

Python : 3.10

Python : 3.11
                                        
Tested on with Nuke (12+ / 13+ / 14+ / 15+ / 16+ )




# Features

Capture current frame from selected nodes

Works with one or multiple nodes

Supported formats:

exr

png, jpg

tif, tiff

dpx, cin

tga, targa

Optional output colorspace control

Optional Dot Marker creation in DAG

Auto creates output folder

Auto deletes temporary Write nodes

Sound notification after capture

Compatible with Nuke 12 – 16

<img width="721" height="462" alt="Install_03" src="https://github.com/user-attachments/assets/249c92dc-8a14-4ae9-a533-147d31a2f904" />



# Installation

    

    
    
    
    
    git clone https://github.com/Nitinkashyap96/Breakdown_Pro.git

  
    
    
    Step 1: Copy Script
    
    Copy Breakdown Pro folder  to your .nuke folder.
    
    Windows
    
    C:/Users/<username>/.nuke/
    
    
    Linux / macOS
    
    ~/.nuke/

    


    Step 2: Add init.py Entry
    
    Open (or create) init.py inside .nuke and add:
    
    nuke.pluginAddPath("./Breakdown Pro")
    
    Restart Nuke.



# How to Use

Open your Nuke script

Save the script

Select one or more nodes in the DAG

Open:

Nuke → NK_Tools → Frame Breakdown


Choose file format

(Optional) Enable colorspace

(Optional) Enable Dot Marker

Click CAPTURE

Output Location

Files are saved next to your .nk file:

/your_project/breakdowns/


<img width="732" height="468" alt="Install_04" src="https://github.com/user-attachments/assets/c31542b3-c54d-4aec-8bb3-4dacde39d68a" />







# File Naming

ScriptName_001_NodeName.1001.exr

Dot Marker (Optional)

Creates a green Dot below the node

Label: Breakdown

Helps visually identify breakdown points in the DAG

Colorspace Handling

EXR: Written natively with compression

Non-EXR: Selected output colorspace is applied

Notes

Script must be saved before capture

Only captures single frame (by design)

Safe to use (no changes to original nodes)

<img width="1615" height="1631" alt="Install_02" src="https://github.com/user-attachments/assets/425f2eac-4cb8-494a-ab16-1326b651ea0d" />

