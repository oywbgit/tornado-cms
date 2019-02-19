#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = 'ouyangweibiao'

format = {
    ".":"application/x-",
    ".*":"application/octet-stream",
    ".pdf":"application/pdf",
    ".ai":"application/postscript",
    ".json":"application/json",
    ".js":"application/javascript",
    ".ogg":"application/ogg",
    ".rdf":"application/rdf+xml",
    ".woff":"application/octet-stream",
    ".ttf":"application/octet-stream",
    ".xhtml":"application/xhtml+xml",
    ".xml":"application/xml",
    ".zip":"application/zip",
    ".gzip":"application/gzip",
    "0.001":"application/x-001",
    "0.301":"application/x-301",
    "0.906":"application/x-906",
    ".a11":"application/x-a11",
    ".awf":"application/vnd.adobe.workflow",
    ".bmp":"application/x-bmp",
    ".c4t":"application/x-c4t",
    ".cal":"application/x-cals",
    ".cdf":"application/x-netcdf",
    ".cel":"application/x-cel",
    ".cg4":"application/x-g4",
    ".cit":"application/x-cit",
    ".bot":"application/x-bot",
    ".c90":"application/x-c90",
    ".cat":"application/vnd.ms-pki.seccat",
    ".cdr":"application/x-cdr",
    ".cer":"application/x-x509-ca-cert",
    ".cgm":"application/x-cgm",
    ".cmx":"application/x-cmx",
    ".crl":"application/pkix-crl",
    ".csi":"application/x-csi",
    ".cut":"application/x-cut",
    ".dbm":"application/x-dbm",
    ".cmp":"application/x-cmp",
    ".cot":"application/x-cot",
    ".crt":"application/x-x509-ca-cert",
    ".dbf":"application/x-dbf",
    ".dbx":"application/x-dbx",
    ".dcx":"application/x-dcx",
    ".dgn":"application/x-dgn",
    ".dll":"application/x-msdownload",
    ".dot":"application/msword",
    ".der":"application/x-x509-ca-cert",
    ".dib":"application/x-dib",
    ".doc":"application/msword",
    ".drw":"application/x-drw",
    ".dwf":"application/x-dwf",
    ".dxb":"application/x-dxb",
    ".edn":"application/vnd.adobe.edn",
    ".dwg":"application/x-dwg",
    ".dxf":"application/x-dxf",
    ".emf":"application/x-emf",
    ".epi":"application/x-epi",
    ".eps":"application/postscript",
    ".exe":"application/x-msdownload",
    ".fdf":"application/vnd.fdf",
    ".eps":"application/x-ps",
    ".etd":"application/x-ebx",
    ".fif":"application/fractals",
    ".frm":"application/x-frm",
    ".gbr":"application/x-gbr",
    ".g4":"application/x-g4",
    ".gl2":"application/x-gl2",
    ".hgl":"application/x-hgl",
    ".hpg":"application/x-hpgl",
    ".hqx":"application/mac-binhex40",
    ".hta":"application/hta",
    ".gp4":"application/x-gp4",
    ".hmr":"application/x-hmr",
    ".hpl":"application/x-hpl",
    ".hrf":"application/x-hrf",
    ".icb":"application/x-icb",
    ".ig4":"application/x-g4",
    ".iii":"application/x-iphone",
    ".ins":"application/x-internet-signup",
    ".iff":"application/x-iff",
    ".igs":"application/x-igs",
    ".img":"application/x-img",
    ".isp":"application/x-internet-signup",
    ".lar":"application/x-laplayer-reg",
    ".latex":"application/x-latex",
    ".lbm":"application/x-lbm",
    ".ls":"application/x-javascript",
    ".ltr":"application/x-ltr",
    ".man":"application/x-troff-man",
    ".mac":"application/x-mac",
    ".mdb":"application/x-mdb",
    ".mfp":"application/x-shockwave-flash",
    ".mi":"application/x-mi",
    ".mil":"application/x-mil",
    ".mocha":"application/x-javascript",
    ".mpd":"application/vnd.ms-project",
    ".mpp":"application/vnd.ms-project",
    ".mpt":"application/vnd.ms-project",
    ".mpw":"application/vnd.ms-project",
    ".mpx":"application/vnd.ms-project",
    ".mxp":"application/x-mmxp",
    ".nrf":"application/x-nrf",
    ".out":"application/x-out",
    ".p12":"application/x-pkcs12",
    ".p7c":"application/pkcs7-mime",
    ".p7r":"application/x-pkcs7-certreqresp",
    ".pc5":"application/x-pc5",
    ".pcl":"application/x-pcl",
    ".pdx":"application/vnd.adobe.pdx",
    ".pgl":"application/x-pgl",
    ".pko":"application/vnd.ms-pki.pko",
    ".p10":"application/pkcs10",
    ".p7b":"application/x-pkcs7-certificates",
    ".p7m":"application/pkcs7-mime",
    ".p7s":"application/pkcs7-signature",
    ".pci":"application/x-pci",
    ".pcx":"application/x-pcx",
    ".pfx":"application/x-pkcs12",
    ".pic":"application/x-pic",
    ".pl":"application/x-perl",
    ".plt":"application/x-plt",
    ".ppa":"application/vnd.ms-powerpoint",
    ".pps":"application/vnd.ms-powerpoint",
    ".prf":"application/pics-rules",
    ".prt":"application/x-prt",
    ".pwz":"application/vnd.ms-powerpoint",
    ".ra":"audio/vnd.rn-realaudio",
    ".ras":"application/x-ras",
    ".pot":"application/vnd.ms-powerpoint",
    ".ppm":"application/x-ppm",
    ".ppt":"application/vnd.ms-powerpoint",
    ".pr":"application/x-pr",
    ".prn":"application/x-prn",
    ".ps":"application/x-ps",
    ".ptn":"application/x-ptn",
    ".red":"application/x-red",
    ".rjs":"application/vnd.rn-realsystem-rjs",
    ".rlc":"application/x-rlc",
    ".rm":"application/vnd.rn-realmedia",
    ".rat":"application/rat-file",
    ".rec":"application/vnd.rn-recording",
    ".rgb":"application/x-rgb",
    ".rjt":"application/vnd.rn-realsystem-rjt",
    ".rle":"application/x-rle",
    ".rmf":"application/vnd.adobe.rmf",
    ".rmj":"application/vnd.rn-realsystem-rmj",
    ".rmp":"application/vnd.rn-rn_music_package",
    ".rmvb":"application/vnd.rn-realmedia-vbr",
    ".rnx":"application/vnd.rn-realplayer",
    ".rpm":"audio/x-pn-realaudio-plugin",
    ".rms":"application/vnd.rn-realmedia-secure",
    ".rmx":"application/vnd.rn-realsystem-rmx",
    ".rsml":"application/vnd.rn-rsml",
    ".rv":"video/vnd.rn-realvideo",
    ".sat":"application/x-sat",
    ".sdw":"application/x-sdw",
    ".slb":"application/x-slb",
    ".sam":"application/x-sam",
    ".sdp":"application/sdp",
    ".sit":"application/x-stuffit",
    ".sld":"application/x-sld",
    ".smi":"application/smil",
    ".smk":"application/x-smk",
    ".smil":"application/smil",
    ".spc":"application/x-pkcs7-certificates",
    ".spl":"application/futuresplash",
    ".ssm":"application/streamingmedia",
    ".stl":"application/vnd.ms-pki.stl",
    ".sst":"application/vnd.ms-pki.certstore",
    ".tdf":"application/x-tdf",
    ".tga":"application/x-tga",
    ".sty":"application/x-sty",
    ".swf":"application/x-shockwave-flash",
    ".tg4":"application/x-tg4",
    ".vdx":"application/vnd.visio",
    ".vpg":"application/x-vpeg005",
    ".vsw":"application/vnd.visio",
    ".vtx":"application/vnd.visio",
    ".torrent":"application/x-bittorrent",
    ".vda":"application/x-vda",
    ".vsd":"application/vnd.visio",
    ".vss":"application/vnd.visio",
    ".vst":"application/x-vst",
    ".vsx":"application/vnd.visio",
    ".wb1":"application/x-wb1",
    ".wb3":"application/x-wb3",
    ".wiz":"application/msword",
    ".wk4":"application/x-wk4",
    ".wks":"application/x-wks",
    ".wb2":"application/x-wb2",
    ".wk3":"application/x-wk3",
    ".wkq":"application/x-wkq",
    ".wmf":"application/x-wmf",
    ".wmd":"application/x-ms-wmd",
    ".wp6":"application/x-wp6",
    ".wpg":"application/x-wpg",
    ".wq1":"application/x-wq1",
    ".wri":"application/x-wri",
    ".ws":"application/x-ws",
    ".wmz":"application/x-ms-wmz",
    ".wpd":"application/x-wpd",
    ".wpl":"application/vnd.ms-wpl",
    ".wr1":"application/x-wr1",
    ".wrk":"application/x-wrk",
    ".ws2":"application/x-ws",
    ".xdp":"application/vnd.adobe.xdp",
    ".xfd":"application/vnd.adobe.xfd",
    ".xfdf":"application/vnd.adobe.xfdf",
    ".xls":"application/vnd.ms-excel",
    ".xwd":"application/x-xwd",
    ".sis":"application/vnd.symbian.install",
    ".x_t":"application/x-x_t",
    ".apk":"application/vnd.android.package-archive",
    ".x_b":"application/x-x_b",
    ".sisx":"application/vnd.symbian.install",
    ".ipa":"application/vnd.iphone",
    ".xap":"application/x-silverlight-app",
    ".xlw":"application/x-xlw",
    ".xpl":"audio/scpls",
    ".anv":"application/x-anv",
    ".uin":"application/x-icq",
    "0.323":"text/h323",
    ".biz":"text/xml",
    ".cml":"text/xml",
    ".asa":"text/asa",
    ".asp":"text/asp",
    ".css":"text/css",
    ".csv":"text/csv",
    ".dcd":"text/xml",
    ".dtd":"text/xml",
    ".ent":"text/xml",
    ".fo":"text/xml",
    ".htc":"text/x-component",
    ".html":"text/html",
    ".htx":"text/html",
    ".htm":"text/html",
    ".htt":"text/webviewhtml",
    ".jsp":"text/html",
    ".math":"text/xml",
    ".mml":"text/xml",
    ".mtx":"text/xml",
    ".plg":"text/html",
    ".rt":"text/vnd.rn-realtext",
    ".sol":"text/plain",
    ".spp":"text/xml",
    ".stm":"text/html",
    ".svg":"text/xml",
    ".tld":"text/xml",
    ".txt":"text/plain",
    ".uls":"text/iuls",
    ".vml":"text/xml",
    ".tsd":"text/xml",
    ".vcf":"text/x-vcard",
    ".vxml":"text/xml",
    ".wml":"text/vnd.wap.wml",
    ".wsdl":"text/xml",
    ".wsc":"text/scriptlet",
    ".xdr":"text/xml",
    ".xql":"text/xml",
    ".xsd":"text/xml",
    ".xslt":"text/xml",
    ".xq":"text/xml",
    ".xquery":"text/xml",
    ".xsl":"text/xml",
    ".odc":"text/x-ms-odc",
    ".r3t":"text/vnd.rn-realtext3d",
    ".sor":"text/plain",
    ".acp":"audio/x-mei-aac",
    ".aif":"audio/aiff",
    ".aiff":"audio/aiff",
    ".aifc":"audio/aiff",
    ".au":"audio/basic",
    ".la1":"audio/x-liquid-file",
    ".lavs":"audio/x-liquid-secure",
    ".lmsff":"audio/x-la-lms",
    ".m3u":"audio/mpegurl",
    ".midi":"audio/mid",
    ".mid":"audio/mid",
    ".mp2":"audio/mp2",
    ".mp3":"audio/mp3",
    ".mnd":"audio/x-musicnet-download",
    ".mp1":"audio/mp1",
    ".mns":"audio/x-musicnet-stream",
    ".mpga":"audio/rn-mpeg",
    ".pls":"audio/scpls",
    ".ram":"audio/x-pn-realaudio",
    ".rmi":"audio/mid",
    ".rmm":"audio/x-pn-realaudio",
    ".snd":"audio/basic",
    ".wav":"audio/wav",
    ".wax":"audio/x-ms-wax",
    ".wma":"audio/x-ms-wma",
    ".asf":"video/x-ms-asf",
    ".asx":"video/x-ms-asf",
    ".avi":"video/avi",
    ".IVF":"video/x-ivf",
    ".m1v":"video/x-mpeg",
    ".m2v":"video/x-mpeg",
    ".m4e":"video/mpeg4",
    ".movie":"video/x-sgi-movie",
    ".mp2v":"video/mpeg",
    ".mp4":"video/mpeg4",
    ".mpa":"video/x-mpg",
    ".mpe":"video/x-mpeg",
    ".mpg":"video/mpg",
    ".mpeg":"video/mpg",
    ".mps":"video/x-mpeg",
    ".mpv":"video/mpg",
    ".mpv2":"video/mpeg",
    ".wm":"video/x-ms-wm",
    ".wmv":"video/x-ms-wmv",
    ".wmx":"video/x-ms-wmx",
    ".wvx":"video/x-ms-wvx",
    ".tif":"image/tiff",
    ".fax":"image/fax",
    ".gif":"image/gif",
    ".ico":"image/x-icon",
    ".jfif":"image/jpeg",
    ".jpe":"image/jpeg",
    ".jpeg":"image/jpeg",
    ".jpg":"image/jpeg",
    ".net":"image/pnetvue",
    ".png":"image/png",
    ".rp":"image/vnd.rn-realpix",
    ".tiff":"image/tiff",
    ".wbmp":"image/vnd.wap.wbmp",
    ".eml":"message/rfc822",
    ".mht":"message/rfc822",
    ".mhtml":"message/rfc822",
    ".nws":"message/rfc822",
    "0.907":"drawing/907",
    ".slk":"drawing/x-slk",
    ".top":"drawing/x-top",
    ".class":"java/*",
    ".java":"java/*",
}

if __name__ == "__main__":
    import os
    # ss = ""
    # end = os.path.splitext(ss)[-1]
    # print(end)
    # print(format[end])
    # print(format[end][1])
    print('.ttfff' in format.keys())