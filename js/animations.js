var _colors =
    {
        "Red": "FF0000",
        "Orange": "FF5C00",
        "Yellow": "FFFF00",
        "Green": "00FF00",
        "Blue": "0000FF",
        "Indigo": "4B0082",
        "Violet": "8B00FF",
    };

var _led_patterns =
    {
        "Halloween 1": { width: 3, step: 1, delay: 0, colors: ["FF5C00", "000000"] },
        "Halloween 2": { width: 3, step: 1, delay: 0, colors: ["FF5C00", "4B0082"] },
        "Christmas": { width: 3, step: 1, delay: 0, colors: ["FF0000", "00FF00"] },
        "4th of July": { width: 3, step: 1, delay: 0, colors: ["FF0000", "FFFFFF", "0000FF"] },
        "Hanukkah": { width: 3, step: 1, delay: 0, colors: ["FFFFFF", "0000FF"] },
    };

var _misc_anim =
    {
        "Rainbow": { display: "rainbow", params: {delay: 0} },
        "Rainbow Cycle": { display: "rainbow_cycle", params: { delay: 0 } },
        "Color Wipe*": { display: "color_wipe", getColor: true, params: { delay: 0, color: null } },
        "Color Chase*": { display: "color_chase", getColor: true, params: { delay: 0, color: null } },
    };