
import nuke 
import os
import datetime
import Breakdown_Pro




version= "v1.0.0"
update_date= "1 Jan 2026"

# Create custom menu


menubar = nuke.menu("Nuke")

custom_menu = menubar.addMenu("NK_Breakdown")



# Add Frame Breakdown command

custom_menu.addCommand(
    "Breakdown Pro",
    "import Breakdown_Pro; Breakdown_Pro.show_frame_breakdown()",
    "["
)



license ="Copyright (C) 2025 by Nitin Kashyap,All rights reserved."
nuke.tprint(f"PipelineCore_nuke_installer {version},  build  {update_date}. \n{license}")