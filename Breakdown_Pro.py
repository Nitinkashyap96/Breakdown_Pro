#                         ################################################
#                         #            Author: Nitin Kashyap             #
#                         #        Frame_Breakdown_v1.0.0 for Nuke       #
#                         ################################################




#                            # #######################################                          #
#                            #                                       #                          #
#                            #            Author: Nitin Kashyap      #                          #
#                            #                                       #                          #
#                            # #######################################                          #
#                                                                                               #
#                            # Created by: Nitin Nitinkashyap                                   #
# -------------------------- # Frame_Breakdown_v1.0.0 for Nuke----------------------------------#                     


"""
======================================================================================
# Tool Name      : <Frame_Breakdown_v1.0.0>
# Version        : 1.0.0
#
# Author         : Nitin Kashyap

#
# Software       : Foundry Nuke (12+ / 13+ / 14+ / 15+ / 16+ / 17 )
# Language       : Python : 3.10+
# Platform       : Windows / Linux / macOS

# Installation   :
#   1. Copy script to ~/.nuke or NUKE_PATH
#   2. Add menu entry in menu.py





#
# Usage          :
#   - Access via Nuke → Custom → <Frame_Breakdown_v1.0.0>
#
# Changelog      :
#   v1.0.0  - Initial release
#
#
# Notes          :
#   - Tested with Nuke 15.x

#Copyright (c) 2025 Nitin Kashyap
======================================================================================
"""


""" Version/author information """
__version__ = "1.0.0"
__author__ = "Nitin Kashyap"
__date__ = "Jan 1 2026"




import sys
import nuke
import os
import shutil
import subprocess
import platform
import webbrowser



# ------------------------------------------------------------
# PySide Compatibility (Nuke 9 → 17)
# ------------------------------------------------------------

try:
    # PySide6 (Nuke 15+ some builds)
    from PySide6 import QtWidgets, QtGui, QtCore
    from PySide6.QtWidgets import QLabel, QCheckBox
    from PySide6.QtCore import Qt
    PYSIDE_VERSION = 6

except ImportError:
    try:
        # PySide2 (Nuke 10 → 15)
        from PySide2 import QtWidgets, QtGui, QtCore
        from PySide2.QtWidgets import QLabel, QCheckBox
        from PySide2.QtCore import Qt
        PYSIDE_VERSION = 2

    except ImportError:
        # PySide (Qt4 – Nuke 9)
        from PySide import QtGui, QtCore
        QtWidgets = QtGui
        QLabel = QtGui.QLabel
        QCheckBox = QtGui.QCheckBox
        Qt = QtCore.Qt
        PYSIDE_VERSION = 1





#####################################----------------------------------------######################################
#              # ---------------------------------------------------------------------------------------- #       #
#                                       SOUND ALERT Tools Install  ON Done finishes                               #
#              # ---------------------------------------------------------------------------------------- #       #
#                                                                                                                 #
#                                                                                                                 #


def Play_Render_Sound():
    """Play sound or voice notification when render finishes."""
    import os, platform, subprocess, nuke

    operatingSystem = platform.system()
    base_dir = os.path.dirname(__file__) if "__file__" in globals() else nuke.script_directory()
    sound_file = os.path.join(base_dir, "02.wav")

    try:
        if os.path.exists(sound_file):
            if operatingSystem == "Windows":
                import winsound
                winsound.PlaySound(sound_file, winsound.SND_FILENAME | winsound.SND_ASYNC)
            elif operatingSystem == "Darwin":
                subprocess.Popen(["afplay", sound_file])
            else:
                subprocess.Popen(["paplay", sound_file])
        else:
            if operatingSystem == "Windows":
                import winsound
                winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)
            elif operatingSystem == "Darwin":
                subprocess.Popen(["say", "Rendering finished"])
            else:
                subprocess.Popen(["spd-say", "Rendering finished"])
    except Exception as e:
        try:
            from PySide2.QtWidgets import QApplication
            QApplication.beep()
        except Exception:
            pass
        nuke.tprint(f"Render sound failed: {e}")
#                                                                                                                 #
#                                                                                                                 #
#                                                                                                                 #
#                                                                                                                 #
#####################################----------------------------------------######################################

# =========================================================
# COLORSPACE HELPERS (WRITE-BASED)
# =========================================================

def get_write_colorspaces():
    """
    Get valid Write colorspaces across all Nuke versions.
    """
    try:
        return nuke.colorspaces.list()
    except:
        dummy = nuke.createNode("Write", inpanel=False)
        cs = nuke.getColorspaceList(dummy["colorspace"])
        nuke.delete(dummy)
        return cs


def get_default_output_cs(cs_list):
    for cs in ("Output - sRGB", "Output - Rec.709", "sRGB", "rec709"):
        if cs in cs_list:
            return cs
    return cs_list[0]


# =========================================================
# FRAME BREAKDOWN UI
# =========================================================

class FrameBreakdown(QtWidgets.QDialog):

    def __init__(self):
        super(FrameBreakdown, self).__init__()

        self.setWindowTitle("Frame Breakdown | Author: Nitin Kashyap by FrameBreakdown |  Version: 1.0.0")
        self.resize(720, 300)

        self.setWindowFlags(
            Qt.Window |
            Qt.WindowMinimizeButtonHint |
            Qt.WindowMaximizeButtonHint |
            Qt.WindowCloseButtonHint
        )
        self.nodes = nuke.selectedNodes()
        if not self.nodes:
            nuke.message("Select at least ONE node.")
            self.close()
            return

        self.colorspaces = get_write_colorspaces()

        layout = QtWidgets.QVBoxLayout(self)

        #layout.addWidget(QtWidgets.QLabel(f"Selected Nodes: {len(self.nodes)}"))
        selected_label = QtWidgets.QLabel(f"Selected Nodes")
        selected_label.setStyleSheet("""
            color: Yellow;
            font-weight: bold;
            font-size: 15px;

        """)
        layout.addWidget(selected_label)

        # -------------------------------------------------
        # Frame 
        # -------------------------------------------------
        frame_label = QtWidgets.QLabel(f"Frame: {int(nuke.frame())}")
        frame_label.setStyleSheet("""
            color: white;
            font-weight: bold;
            font-size: 14px;
        """)
        layout.addWidget(frame_label)
        # -------------------------------------------------
        # File Type
        # -------------------------------------------------

        #layout.addWidget(QtWidgets.QLabel("File Type"))
        filetype_label = QtWidgets.QLabel("file_Type")
        filetype_label.setStyleSheet("""
            color: white;
            font-weight: bold;
            font-size: 12px;

        """)
        layout.addWidget(filetype_label)
        self.format_combo = QtWidgets.QComboBox()
        self.format_combo.addItems(["exr", "png", "jpg", "tif", "tiff", "dpx", "cin", "tga", "targa"])
        # Make the combo text bold
        self.format_combo.setStyleSheet("""
            QComboBox {
                font-weight: bold;
                font-size: 14px;  /* adjust size as needed */
                color: white;      /* optional: white text */
            }
            QComboBox QAbstractItemView {
                font-weight: bold; /* items in dropdown */
                font-size: 14px;
            }
        """)

        layout.addWidget(self.format_combo)

        # -------------------------------------------------
        # Output Colorspace (WRITE)
        # -------------------------------------------------

        self.cs_checkbox = QtWidgets.QCheckBox("Set Output Colorspace")
        self.cs_checkbox.setChecked(True)
        layout.addWidget(self.cs_checkbox)

        self.cs_combo = QtWidgets.QComboBox()
        self.cs_combo.addItems(self.colorspaces)
        self.cs_combo.setCurrentText(
            get_default_output_cs(self.colorspaces)
        )
        layout.addWidget(self.cs_combo)

        # -------------------------------------------------
        # Dot Marker
        # -------------------------------------------------

        self.dot_checkbox = QtWidgets.QCheckBox("Create Dot Marker")
        self.dot_checkbox.setChecked(False)
        layout.addWidget(self.dot_checkbox)

        # Create a horizontal line divider
        divider = QtWidgets.QFrame()
        divider.setFrameShape(QtWidgets.QFrame.HLine)
        divider.setFrameShadow(QtWidgets.QFrame.Sunken)
        divider.setLineWidth(5)
        
        # Add it to your layout
        layout.addWidget(divider)

        # -------------------------------------------------
        # Buttons (Polished UI)
        # -------------------------------------------------
        
        btns = QtWidgets.QHBoxLayout()
        btns.setSpacing(12)
        
        capture_btn = QtWidgets.QPushButton("CAPTURE")
        cancel_btn = QtWidgets.QPushButton("Cancel")
        
        # Bold fonts
        capture_font = capture_btn.font()
        capture_font.setBold(True)
        capture_font.setPointSize(10)
        capture_btn.setFont(capture_font)
        
        cancel_font = cancel_btn.font()
        cancel_font.setBold(True)
        cancel_btn.setFont(cancel_font)
        
        # Fixed height for consistency
        capture_btn.setFixedHeight(32)
        cancel_btn.setFixedHeight(32)
        
        # Stylesheet
        capture_btn.setStyleSheet("""
            QPushButton {
                background-color:#096301;
                color:white;
                border-radius:6px;
                font-weight:bold;
                font-size:15px;
            }
            QPushButton:hover { background-color:#11B800; }
            QPushButton:pressed { background-color:#064501; }
        """)
        cancel_btn.setStyleSheet("""
            QPushButton {
                background-color:#6b0f01;
                color:white;
                border-radius:6px;
                font-weight:bold;
                font-size:20px;
            }
            QPushButton:hover { background-color:#C20202; }
            QPushButton:pressed { background-color:#4a0700; }
        """)
        
        btns.addStretch()
        btns.addWidget(cancel_btn)
        btns.addWidget(capture_btn)
        layout.addLayout(btns)
        
        capture_btn.clicked.connect(self.capture_frame)
        cancel_btn.clicked.connect(self.close)


#        # Create a horizontal line divider
#        divider = QtWidgets.QFrame()
#        divider.setFrameShape(QtWidgets.QFrame.HLine)
#        divider.setFrameShadow(QtWidgets.QFrame.Sunken)
#        divider.setLineWidth(5)
#        
#        # Add it to your layout
#        layout.addWidget(divider)


        # author_label = QtWidgets.QLabel("Author: Nitin Kashyap by FrameBreakdown |  Version: 1.0.0")
        # author_font = author_label.font()
        # author_font.setBold(True)
        # author_font.setPointSize(author_font.pointSize() - 1)
        # author_label.setFont(author_font)
        # author_label.setAlignment(QtCore.Qt.AlignLeft)
        
        # layout.addWidget(author_label)

        # -------------------------------------------------
        # Help / Info 
        # -------------------------------------------------
        
        # Divider
        divider = QtWidgets.QFrame()
        divider.setFrameShape(QtWidgets.QFrame.HLine)
        divider.setFrameShadow(QtWidgets.QFrame.Sunken)
        layout.addWidget(divider)
        
        # Title
        help_title = QtWidgets.QLabel("Info")
        help_title.setStyleSheet("""
            color: #FFFFFF;
            font-weight: bold;
            font-size: 14px;
            font-weight:bold;
        """)
        layout.addWidget(help_title)
        
        # Info text
        help_text = QtWidgets.QLabel(
            "• Select one or more nodes in the DAG\n"
            "• Choose output file format ( exr png jpg tif tiff dpx cin tga targa recommended )\n"
            "• Captures the current timeline frame\n"
            "• Files are saved next to the .nk file\n"
            "• Optional Dot marker for visual reference"
        )
        
        help_text.setWordWrap(True)
        help_text.setStyleSheet("""
            color: #BFBFBF;
            font-size: 12px;
            background-color: #2A2A2A;
            padding: 8px;
            border-radius: 4px;
            font-weight:bold;
        """)
        
        layout.addWidget(help_text)

        #Github Button

        github_btn = QtWidgets.QPushButton("Github")
        github_btn.setStyleSheet("""
            QPushButton{
                color: #BFBFBF;
                font-size: 12px;
                background-color: #2A2A2A;
                padding: 8px;
                border-radius: 4px;
                font-weight:bold;

            }
            QPushButton:hover {
                background-color: #078F00;

            }
            QPushButton:pressed {
                background-color: #2A2A2A;

            }
        """)

        # Opne URL on click
        github_btn.clicked.connect(lambda: webbrowser.open("https://github.com/Nitinkashyap96"))

        layout.addWidget(github_btn)


        # Divider
        divider = QtWidgets.QFrame()
        divider.setFrameShape(QtWidgets.QFrame.HLine)
        divider.setFrameShadow(QtWidgets.QFrame.Sunken)
        layout.addWidget(divider)


        author_label = QtWidgets.QLabel("Author: Nitin Kashyap by FrameBreakdown |  Version: 1.0.0")
        author_font = author_label.font()
        author_font.setBold(True)
        author_font.setPointSize(author_font.pointSize() - 1)
        author_label.setFont(author_font)
        author_label.setAlignment(QtCore.Qt.AlignLeft)
        
        layout.addWidget(author_label)


    # =====================================================
    # CAPTURE
    # =====================================================

    def capture_frame(self):

        script_path = nuke.root().name()
        if script_path == "Root":
            nuke.message("Please save your script first.")
            return

        script_dir = os.path.dirname(script_path)
        script_name = os.path.splitext(os.path.basename(script_path))[0]

        frame = int(nuke.frame())
        ext = self.format_combo.currentText().lower()

        out_dir = os.path.join(script_dir, "breakdowns")
        os.makedirs(out_dir, exist_ok=True)

        written = 0

        for i, node in enumerate(self.nodes, 1):

            filename = f"{script_name}_{str(i).zfill(3)}_{node.name()}.{frame}.{ext}"
            filepath = os.path.join(out_dir, filename).replace("\\", "/")

            write = nuke.nodes.Write()
            write.setInput(0, node)
            write["file"].setValue(filepath)
            write["channels"].setValue("rgba")
            write["use_limit"].setValue(True)
            write["first"].setValue(frame)
            write["last"].setValue(frame)

            # ------------------------------------------
            # File type + COLORSPACE (CORRECT)
            # ------------------------------------------

            if ext == "exr":
                write["file_type"].setValue("exr")
                write["compression"].setValue("Zip (16 scanline)")
            else:
                write["file_type"].setValue(ext)
                if self.cs_checkbox.isChecked() and write.knob("colorspace"):
                    write["colorspace"].setValue(
                        self.cs_combo.currentText()
                    )

            try:
                nuke.execute(write, frame, frame)
                written += 1
            except RuntimeError as e:
                nuke.message(f"Write failed for {node.name()}:\n{e}")
            finally:
                nuke.delete(write)

            # ------------------------------------------
            # Dot Marker
            # ------------------------------------------

            if self.dot_checkbox.isChecked():
                dot = nuke.nodes.Dot()
                dot.setInput(0, node)
                dot.setXpos(node.xpos()+ 70)
                dot.setYpos(node.ypos() + 290)
                dot.setXpos(node.xpos()+ 70)
                dot.setYpos(node.ypos() + 575)
                dot["label"].setValue("Breakdown")
                dot["tile_color"].setValue(0x66FF66FF)




        # =========================================================
        # Show_Bold_Message
        # =========================================================
        def show_bold_message(text, color="#066b01"):
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Frame Breakdown")
            msg.setText(f"<span style='color:{color}; font-weight:bold; font-size:20px;'>{text}</span>")
            msg.exec_()
            Play_Render_Sound()

        
        # Example usage:
        show_bold_message(f"Frame Breakdown saved for {written} node(s).")
        #self.close()


# =========================================================
# LAUNCHER
# =========================================================
# Execution
def show_frame_breakdown():
    global installer_ui
    installer_ui = FrameBreakdown()
    installer_ui.show()

if __name__ == "__main__":
    show_frame_breakdown()





#show_frame_breakdown()



