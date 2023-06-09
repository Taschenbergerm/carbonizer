default = {
    "backgroundColor": "rgba(0, 0, 0, 0)",
    "code": "",
    "dropShadow": True,
    "dropShadowBlurRadius": "68px",
    "dropShadowOffsetY": "20px",
    "exportSize": "2x",
    "fontFamily": "Hack",
    "firstLineNumber": 1,
    "fontSize": "14px",
    "language": "auto",
    "lineNumbers": False,
    "paddingHorizontal": "56px",
    "paddingVertical": "56px",
    "squaredImage": False,
    "theme": "seti",
    "watermark": False,
    "widthAdjustment": True,
    "windowControls": True,
    "windowTheme": None,
}
query_param = {
    "backgroundColor": "bg",
    "code": "code",
    "dropShadow": "ds",
    "dropShadowBlurRadius": "dsblur",
    "dropShadowOffsetY": "dsyoff",
    "exportSize": "es",
    "fontFamily": "fm",
    "firstLineNumber": "fl",
    "fontSize": "fs",
    "language": "l",
    "lineNumbers": "ln",
    "paddingHorizontal": "ph",
    "paddingVertical": "pv",
    "squaredImage": "si",
    "theme": "t",
    "watermark": "wm",
    "widthAdjustment": "wa",
    "windowControls": "wc",
    "windowTheme": "wt",
}

ignored = [
    # Can't pass these as URL (So no support now)
    "backgroundImage",
    "backgroundImageSelection",
    "backgroundMode",
    "squaredImage",
    "hiddenCharacters",
    "name",
    "lineHeight",
    "loading",
    "icon",
    "isVisible",
    "selectedLines",
]
