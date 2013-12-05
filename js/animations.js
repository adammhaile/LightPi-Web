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
        "Halloween 1": { width: "90px", step: 5, delay: 0, colors: ["FF5C00", "000000"] },
        "Halloween 2": { width: "10%", step: 5, delay: 250, colors: ["FF5C00", "4B0082"] },
        "Christmas": { width: 90, step: 5, delay: 0, colors: ["FF0000", "00FF00"] },
        "4th of July": { width: 90, step: 5, delay: 0, colors: ["FF0000", "FFFFFF", "0000FF"] },
        "Hanukkah": { width: 90, step: 5, delay: 0, colors: ["FFFFFF", "0000FF"] },
    };

var _misc_anim =
    {
        "Rainbow": { display: "rainbow", params: {delay: 0} },
        "Rainbow Cycle": { display: "rainbow_cycle", params: { delay: 0 } },
        "Color Wipe*": { display: "color_wipe", getColor: true, params: { delay: 0, color: null } },
        "Color Chase*": { display: "color_chase", getColor: true, params: { delay: 0, color: null } },
    };

var _christmas = 
    [
        { anim : "pattern", delay : 0, amt : "2.5%", max : 20, params : { colors : ["FF0000", "00FF00"], width : "25%", dir : true, start : 0, end : 0 } },
        { anim: "pattern", delay: 500, amt: "25%", max: 10, params: { colors: ["FF0000", "00FF00"], width: "25%", dir: true, start: 0, end: 0 } },
    ];

var _batch_anim = 
    {
        "Christmas": { display: "batch", params: _christmas },
    }