var system = require('system');
var args = system.args;
var webPage = require('webpage');

if (args.length === 1) {
  console.error('Try to pass some arguments when invoking this script!');
  phantom.exit(1);
} else {
    fileName = args[1];
}
var fs = require('fs');

var content = fs.read(fileName);
if (content === "") {
    console.error('fails to load file');
}
var cookiesContent = fs.read('cookies.txt');

// use phantom.addCookie to add it
function resolveCookiesContent(content) {
    arrayOfLines = content.match(/[^\r\n]+/g);
    ret = []
    for (var i in arrayOfLines) {
        line = arrayOfLines[i]
        if (line[0] == '#' || line[0] == '$') {
            continue;
        }
        // ignore empty lines.
        if (line.replace(/^\s+|\s+$/g, '') === '') {
            continue;
        }
        fields = line.split('\t')
        phantom.addCookie({
            'name' : fields[5],
            'value' : fields[6],
            'domain' : fields[0]
        })

    }
}

resolveCookiesContent(cookiesContent)

var main_config = JSON.parse(content)
var running_pages = 0
var running_pages_callback = []

function global_handle_subpage(pauseIfEmpty) {
    if (running_pages_callback.length != 0) {
        var callback = running_pages_callback.shift()
        callback()
    } else {
        var load = function () {
            var httpUrl = 'http://' + main_config.host + main_config.path
            var mainLoadPage = new LoadPage(httpUrl, main_config, null)

            mainLoadPage.loadPage()
        }
        if (!pauseIfEmpty) {
            console.log('direct load')
            load()
        } else if (running_pages == 0) {
            console.log('pausing for 80 seconds')
            setTimeout(load, 80000)
        }
    }
}


var loadPagePrototype = {
    handlePage: function (status) {
        var object = this
        if (status == 'fail') {
            running_pages--
            object.nextPage()
        } else {
            var urls = object.page.evaluate(function (config) {
                var targets = document.querySelectorAll(config.target)
                var ret = []
                for (var i in targets) {
                    var target = targets[i]
                    if (config.url_attrib instanceof Array) {
                        for (var j in config.url_attrib) {
                            var url_attrib = config.url_attrib[j]
                            if (target.hasOwnProperty(url_attrib)) {
                                ret.push(target[url_attrib])
                            }
                        }
                    } else if (typeof config.url_attrib === "string") {
                        var url_attrib = config.url_attrib
                        if (target.hasOwnProperty(url_attrib)) {
                        ret.push(target[url_attrib])
                        }
                    } else {
                    }
                }
                return ret
            }, object.config);
            // workaround phantomjs bug.
            urls = JSON.parse(JSON.stringify(urls))
            if (object.config.hasOwnProperty('sub'))
                object.handleSubPages(object.config.sub, urls)
            else
                object.handleResources(urls)
            running_pages--
            // object.page.render('shit.png')
            global_handle_subpage(true)
        }
    },
    loadPage : function () {
        var object = this
        var httpUrl = this.url
        running_pages++
        this.page.open(httpUrl, function (status) {
            object.handlePage(status)
        });
    },
    handleSubPages : function (sub_config, urls) {
        if (main_config.hasOwnProperty('max_parallel_pages')) {
            while (running_pages < main_config.max_parallel_pages) {
                if (urls.length === 0)
                    break
                var url = urls.shift(0)
                this.continueSubPage(sub_config, url)
            }
            if (urls.length !== 0) {
                // Add sub pages to the queue.
                var that = this
                running_pages_callback.push(function () {
                    that.handleSubPages(sub_config, urls)
                })
            } 
        } else {
            while (urls.length != 0) {
                var url = urls.shift()
                this.continueSubPage(sub_config, url)
            }
        }
    },
    continueSubPage : function (sub_config, url) {
        if (url.indexOf('http') != 0) {
            url = 'http://' + main_config.host + url
        }
        var newLoadPage = new LoadPage(url, sub_config, this)
        newLoadPage.loadPage()
    },
    handleResources : function(urls) {
        for (var i in urls)
            console.log(urls[i])
    },
    nextPage: function() {
        running_pages++;
        this.nexting = true;
        this.page.evaluate(function (config) {
            var targets = document.querySelectorAll(config.next_page)
            targets.click()
        });
        var object = this;
    }
}

function LoadPage(url, config, parentPage) {
    this.config = config
    this.url = url
    this.page = webPage.create()
    // debuging code
    // this.page.onConsoleMessage = function(msg, lineNum, sourceId) {
    //     console.log('CONSOLE: ' + msg + ' (from line #' + lineNum + ' in "' + sourceId + '")');
    // };
    this.parentPage = parentPage
    this.nexting = false
}

LoadPage.prototype = loadPagePrototype

global_handle_subpage(false)
