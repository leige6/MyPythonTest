(function() {
    var a = {};
    var b = -1 !== window.location.href.search(/#showdebug/);
    b && document.write('<div id="DebuggerDiv" style="padding:5px;display:none;border:1px solid #888;background-color:#000;z-index:99;color:#FFF"><strong>debug: <a href="#" onclick="document.getElementById(\'DebuggerDiv\').style.display=\'none\';return false">close</a></strong><br /><br /><span id="DebuggerSpan"></span></div>');
    sD = function(d) {
        b && (document.getElementById("DebuggerSpan").innerHTML = d,
        document.getElementById("DebuggerDiv").style.display = "block")
    }
    ;
    a = function() {
        e = function(d) {
            return encodeURIComponent(d)
        }
        ;
        project = "default";
        u = 0;
        m = 0;
        ct = 0;
        lt = 0;
        attr = document.getElementById("GBSF");
        charset = document.charset || document.characterSet;
        title = e(document.title);
        referr = document.referrer;
        lage = navigator.language || navigator.userLanguage;
        ss = screen.width + "x" + screen.height;
        title = title;
        referr = e(referr);
        queryUrl = "//sf.gamebar.com/index.php"
    }
    ;
    a.prototype.DT = function() {
        dtObj = new Date,
        ct = dtObj.getTime() / 1000
    }
    ;
    a.prototype.PD = function() {
        sf_info = "project:" + project + "<br>title:" + title + "<br>referr:" + referr + "<br>charset:" + charset + "<br>language:" + lage + "<br>screen:" + ss + "<br>datetime:" + ct + "<br>loadtime:" + lt;
        sD(sf_info)
    }
    ;
    a.prototype.PJ = function() {
        GBPV_project = attr.getAttribute("GID");
        if (typeof (GBPV_project) != "undefined") {
            project = GBPV_project || project
        }
        GBPV_unique = attr.getAttribute("UNIQUE");
        if (typeof (GBPV_unique) != "undefined") {
            u = GBPV_unique == "true" ? 1 : 0
        }
        GBPV_main = attr.getAttribute("MAIN");
        if (typeof (GBPV_main) != "undefined") {
            m = GBPV_main == "true" ? 1 : 0
        }
    }
    ;
    a.prototype.LDT = function() {
        load_time = attr.getAttribute("loadtime");
        if (typeof (load_time) != "undefined") {
            if (load_time == "1") {
                if (typeof (g_st_time) != "undefined") {
                    edObj = new Date();
                    lt = edObj.getTime() - g_st_time
                }
            }
        }
    }
    ;
    a.prototype.TPV = function() {
        querystr = "pj=" + project + "&t=" + title + "&r=" + referr + "&c=" + charset + "&l=" + lage + "&s=" + ss + "&dt=" + ct + "&o=" + lt + "&m=" + m + "&u=" + u;
        document.writeln('<script src="' + queryUrl + "?" + querystr + '">\x3c/script>')
    }
    ;
    var c = new a;
    if (attr == null ) {
        return false
    }
    c.DT(),
    c.PJ(),
    c.LDT(),
    c.PD();
    c.TPV()
}
)();