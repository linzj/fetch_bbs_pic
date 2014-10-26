var system = require('system');
var args = system.args;
var webPage = require('webpage')

if (args.length === 1) {
  console.error('Try to pass some arguments when invoking this script!');
  phantom.exit(1)
} else {
    fileName = args[1]
}
var fs = require('fs');

var content = fs.read(fileName);
if (content == "")
    console.error('fails to load file')

var main_config = JSON.parse(content)
var running_pages = 0
var running_pages_callback = []

function global_handle_subpage() {
    if (running_pages_callback.length != 0) {
        var callback = running_pages_callback.shift()
        callback()
    } else {
        var httpUrl = 'http://' + main_config.host + main_config.path
        var mainLoadPage = new LoadPage(httpUrl, main_config, null)

        mainLoadPage.loadPage()
    }
}


var loadPagePrototype = {
    loadPage : function () {
        var object = this
        var httpUrl = this.url
        this.page.open(httpUrl, function (status) {
            if (status == 'fail') {
                object.nextPage()
            } else {
                var urls = object.page.evaluate(function (config) {
                    var targets = document.querySelectorAll(config.target)
                    var ret = []
                    for (var i in targets) {
                        var target = targets[i]
                            console.log('nimabi: ' + target.href)
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
                            console.log('nimabi')
                        }
                    }
                    return ret
                }, object.config);
                if (object.config.hasOwnProperty('sub'))
                    object.handleSubPages(object.config.sub, urls)
                else
                    object.handleResources(urls)
                running_pages--
                object.page.render('shit.png')
                global_handle_subpage()
            }
        });
    },
    handleSubPages : function (sub_config, urls) {
        if (main_config.hasOwnProperty('max_parallel_pages')) {
            while (running_pages < main_config.max_parallel_pages) {
                if (urls.length == 0)
                    break
                var url = urls.shift()
                this.continueSubPage(sub_config, url)
            }
            if (urls.length != 0) {
                // Add sub pages to the queue.
                running_pages_callback.push(this.handleSubPages.bind(this, sub_config, urls))
            } 
        } else {
            while (urls.length != 0) {
                var url = urls.shift()
                this.continueSubPage(sub_config, url)
            }
        }
    },
    continueSubPage : function (sub_config, url) {
        running_pages++
        if (url.indexOf('http') != 0) {
            url = 'http://' + main_config.host + url
        }
        var newLoadPage = new LoadPage(url, sub_config, this)
        newLoadPage.loadPage()
    },
    handleResources : function(urls) {
        for (var i in urls)
            console.log(urls[i])
    }
}

function LoadPage(url, config, parentPage) {
    this.config = config
    this.url = url
    this.page = webPage.create()
    this.page.onConsoleMessage = function(msg, lineNum, sourceId) {
        console.log('CONSOLE: ' + msg + ' (from line #' + lineNum + ' in "' + sourceId + '")');
    };
    this.tasks = 0
    this.parentPage = parentPage
}

LoadPage.prototype = loadPagePrototype

global_handle_subpage()
