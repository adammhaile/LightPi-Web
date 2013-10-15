<html>
<head>
    <title>LightPi Web</title>
    <meta name="viewport" content ="width=device-width,initial-scale=1,user-scalable=yes" />
    <LINK href="/css/button.css" rel="stylesheet" type="text/css">
    <LINK href="/css/ui-darkness/jquery-ui-1.10.3.custom.min.css" rel="stylesheet" type="text/css">
    <style>
        body {
            max-width: 720px;
        }

        .porch {
            width: 22%;
        }
    </style>
    <script src="/js/jquery-2.0.3.min.js"></script>
    <script src="/js/jquery-ui-1.10.3.custom.min.js"></script>
    <script type="text/javascript">
        function apiSuccess(data) {
            console.log("Call success!");
        }
        function apiFail() {
            console.log("Call failed!");
        }
        function allOff() {
            $.get("/api/off", apiSuccess)
            .fail(apiFail);
        }
        function apiFill(color) {
            if (color != "") {
                $.get("/api/fill/" + color, apiSuccess)
                .fail(apiFail);
            }
        }
        function patternChange() {
            pattern = $('#patterns').val()
            if (pattern != "") {
                $.get("/api/pattern" + pattern, apiSuccess)
                .fail(apiFail);
            }
        }
        function fill_color_change() {
            fill = $('#fill_colors').val()
            if (fill != "") {
                apiFill(fill);
            }
        }
        function apiLast() {
            $.get("/api/last", apiSuccess)
            .fail(apiFail);
        }

        function apiBrightness(value) {
            $.get("/api/brightness/" + value, apiSuccess)
            .fail(apiFail);
        }

        function getBrightnessCallback(value) {
            setBrightnessLabel(value);
            $("#brightness_slider").slider("value", parseInt(value));
        }

        function apiGetBrightness() {
            $.get("/api/brightness/get", getBrightnessCallback)
            .fail(apiFail);
        }

        function setBrightnessLabel(value) {
            $('#brightness_label').html(value + "%");
        }

        window.onload = function () {
            $('#apiOff').click(function () { allOff(); return false; });
            $('#apiLast').click(function () { apiLast(); return false; });
            $('#patterns').change(patternChange);
            $('#fill_colors').change(fill_color_change);
            $('#brightness_slider').slider(
                {
                    slide: function(event, ui){
                        setBrightnessLabel(ui.value);
                    },
                    change: function(event, ui) {
                        apiBrightness(ui.value);
                    },
                    max: 100,
                    min: 10,
                });

            apiGetBrightness();
        }
    </script>
</head>
<body>
    <a class="button" id="apiOff" href="#" style="width:100%">All Off</a>
    <br />
    <br />
    <a class="button" id="apiLast" href="#" style="width:100%">Run Last</a>
    <br />
    <br />
    <div id="brightness_label"></div>
    <div id="brightness_slider"></div>
    <br />
    <br />
    <a class="button porch" id="p100" href="#" onclick="apiFill('ffffffe6');">100%</a>
    <a class="button porch" id="p75" href="#" onclick="apiFill('ffffffC0');">75%</a>
    <a class="button porch" id="p50" href="#" onclick="apiFill('ffffff80');">50%</a>
    <a class="button porch" id="p25" href="#" onclick="apiFill('ffffff40');">25%</a>
    <br />
    <br />
    <select id="fill_colors">
        <option value="">Select a Color</option>
        <option value="FF0000">Red</option>
        <option value="FF7F00">Orange</option>
        <option value="FFFF00">Yellow</option>
        <option value="00FF00">Green</option>
        <option value="0000FF">Blue</option>
        <option value="4B0082">Indigo</option>
        <option value="8B00FF">Violet</option>
    </select>
    <br />
    <br />
    <select id="patterns">
        <option value="">Select a Pattern</option>
        <option value="/3/1/0/FF7F00-000000">Halloween 1</option>
        <option value="/3/1/0/FF7F00-4B0082">Halloween 2</option>
        <option value="/3/1/0/FF0000-00FF00">Christmas</option>
        <option value="/3/1/0/FF0000-FFFFFF-0000FF">4th of July</option>
        <option value="/3/1/0/FFFFFF-0000FF">Hanukkah</option>
    </select>
</body>
</html>