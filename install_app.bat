{\rtf1\ansi\ansicpg1252\cocoartf2759
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 CourierNewPSMT;}
{\colortbl;\red255\green255\blue255;\red83\green83\blue83;}
{\*\expandedcolortbl;;\cssrgb\c40000\c40000\c40000;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs36 \cf2 \expnd0\expndtw0\kerning0
python -m PyInstaller --noconfirm --log-level=WARN ^\
    --onefile --noconsole ^\
    --hidden-import= tkinter ^\
    --icon=./logo.ico ^\
    ProjectA.py}