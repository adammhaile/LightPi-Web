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

var _rainbowColors =
    [
        "FF0000",
        "FF5C00",
        "FFFF00",
        "00FF00",
        "0000FF",
        "4B0082",
        "8B00FF",
    ];

var _christmas = 
    [
        { anim : "ColorPattern", delay : 0, amt : "2.5%", max : 20, params : { colors : ["FF0000", "00FF00"], width : "33%", dir : true, start : 0, end : 0 } },
        { anim: "ColorPattern", delay: 500, amt: "33%", max: 10, params: { colors: ["FF0000", "00FF00"], width: "33%", dir: true, start: 0, end: 0 } },
    ];

var _demo =
    [
        { anim: "Rainbow", delay: 0, amt: "2.5%", max: 40, params: {} },
        { anim: "RainbowCycle", delay: 0, amt: "2.5%", max: 40, params: {} },
        { anim: "ColorPattern", delay: 0, amt: "2.5%", max: 40, params: { colors: _rainbowColors, width: "10%", dir: true, start: 0, end: 0 } },
        { anim: "ColorWipe", delay: 0, amt: 2, max: 180, params: { color: "FF0000" } },
        { anim: "ColorWipe", delay: 0, amt: 2, max: 180, params: { color: "00FF00" } },
        { anim: "ColorWipe", delay: 0, amt: 2, max: 180, params: { color: "0000FF" } },
        { anim: "ColorChase", delay: 0, amt: 2, max: 180, params: { color: "FF0000", width : 6 } },
        { anim: "ColorChase", delay: 0, amt: 2, max: 180, params: { color: "00FF00", width: "2%" } },
        { anim: "ColorChase", delay: 0, amt: 2, max: 180, params: { color: "0000FF", width: 10 } },
        { anim: "ColorFade", delay: 0, amt: 1, max: 80, params: { colors: _rainbowColors } },
        { anim: "PartyMode", delay: 0, amt: 1, max: 40, params: { colors: _rainbowColors } },
        { anim: "FireFlies", delay: 0, amt: 1, max: 80, params: { colors: _rainbowColors, width : 2, count : 10 } },
        { anim: "LarsonScanner", delay: 0, amt: 4, max: 360, params: { color: "FF0000", tail: 9 } },
        { anim: "LarsonRainbow", delay: 0, amt: 4, max: 360, params: { tail: 9 } },
        { anim: "Wave", delay: 0, amt: 1, max: 360, params: { color: "00FF00", cycles : 4 } },
    ];

var _batch_anim = 
    {
        "Demo Mode": _demo,
        "Christmas": _christmas,
    }