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

var _christmas = 
    [
        { anim : "ColorPattern", delay : 0, amt : "2.5%", max : 20, params : { colors : ["FF0000", "00FF00"], width : "25%", dir : true, start : 0, end : 0 } },
        { anim: "ColorPattern", delay: 500, amt: "25%", max: 10, params: { colors: ["FF0000", "00FF00"], width: "25%", dir: true, start: 0, end: 0 } },
    ];

var _batch_anim = 
    {
        "Christmas": { display: "batch", params: _christmas },
    }