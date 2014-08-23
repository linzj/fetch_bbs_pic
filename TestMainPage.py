# coding: UTF-8
import PageDelegate, PageRoutines
from Print import printTest

test_html = """<html lang="zh-CN" class="ua-linux ua-webkit"><head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name="renderer" content="webkit">

    <title>
    我的小组话题
</title>
    
    
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="Sun, 6 Mar 2005 01:00:00 GMT">
    


    <script type="text/javascript" defer="" async="" src="http://s.doubanio.com/dae/fundin/piwik.js"></script><script type="text/javascript" src="http://img3.douban.com/f/shire/55c9fe0e9ecb5725037e9839fc515504008dae74/js/ad.js" async="true"></script><script>var _head_start = new Date();</script>
    <script src="http://img3.douban.com/f/shire/8033e1c2528bb6402c478e00176afb3562abbc21/js/jquery.min.js"></script>
    <script src="http://img3.douban.com/f/shire/6072cbd9e3d56db50f819890f57164950110117c/js/douban.js"></script>
    <link href="http://img3.douban.com/f/shire/b744ecd0276b46482458cb4ecaee3f256902adec/css/douban.css" rel="stylesheet" type="text/css">
    <style type="text/css">
    
        
    </style>
    
    <link rel="stylesheet" href="http://img3.douban.com/misc/mixed_static/60ad9c220bd3d5a5.css">
    <script></script>


    <link rel="shortcut icon" href="http://img3.douban.com/favicon.ico" type="image/x-icon">
<style type="text/css"></style><script src="http://www.google-analytics.com/ga.js" async="true"></script></head>

<body>
  
    
    <script type="text/javascript">var _body_start = new Date();</script>
    
   







<div id="db-global-nav" class="global-nav">
  <div class="bd">
    






<div class="top-nav-info">
    

    <span class="perf-metric"><!-- _performtips_ --></span>
    <ul>
       
       <li><a id="top-nav-doumail-link" href="http://www.douban.com/doumail/">豆邮</a></li>
       <li class="nav-user-account">
       <a target="_blank" href="http://www.douban.com/accounts/" class="bn-more"><span>linzj的帐号</span><span class="arrow"></span></a>
       <div class="more-items">
      <table cellpadding="0" cellspacing="0">
            <tbody><tr><td><a href="http://www.douban.com/mine/">我的豆瓣</a></td></tr>
            <tr><td><a target="_blank" href="http://www.douban.com/accounts/">我的帐号</a></td></tr>
            <tr><td><a href="http://www.douban.com/accounts/logout?source=group&amp;ck=ZB2t">退出</a></td></tr>
         </tbody></table>
       </div>

       </li>
     </ul>
</div>


    <div class="top-nav-reminder">
        <a href="http://www.douban.com/notification/" class="lnk-remind">提醒
        </a>
    <div id="top-nav-notimenu" class="more-items">
      <div class="bd">
          <p>加载中...</p>
      </div>
    </div>
    </div>
    

    <div class="global-nav-items">
      <ul>
          
            
            <li>
            <a href="http://www.douban.com/" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-main&quot;,&quot;uid&quot;:&quot;87494755&quot;}">豆瓣</a>
            </li>
          
            
            <li>
            <a href="http://book.douban.com/" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-book&quot;,&quot;uid&quot;:&quot;87494755&quot;}">读书</a>
            </li>
          
            
            <li>
            <a href="http://movie.douban.com/" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-movie&quot;,&quot;uid&quot;:&quot;87494755&quot;}">电影</a>
            </li>
          
            
            <li>
            <a href="http://music.douban.com/" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-music&quot;,&quot;uid&quot;:&quot;87494755&quot;}">音乐</a>
            </li>
          
            
            <li>
            <a href="http://www.douban.com/location/" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-location&quot;,&quot;uid&quot;:&quot;87494755&quot;}">同城</a>
            </li>
          
            
            <li class="on">
            <a href="http://www.douban.com/group/" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-group&quot;,&quot;uid&quot;:&quot;87494755&quot;}">小组</a>
            </li>
          
            
            <li>
            <a href="http://read.douban.com/?dcs=top-nav&amp;dcm=douban" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-read&quot;,&quot;uid&quot;:&quot;87494755&quot;}">阅读</a>
            </li>
          
            
            <li>
            <a href="http://douban.fm/" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-fm&quot;,&quot;uid&quot;:&quot;87494755&quot;}">豆瓣FM</a>
            </li>
          
            
            <li>
            <a href="http://dongxi.douban.com/?dcs=top-nav&amp;dcm=douban" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-commodity&quot;,&quot;uid&quot;:&quot;87494755&quot;}">东西</a>
            </li>
          
            <li>
              <a href="#more" class="bn-more"><span>更多</span></a>
              <div class="more-items">
                <table cellpadding="0" cellspacing="0">
                    
                    <tbody><tr><td><a href="http://9.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-9&quot;,&quot;uid&quot;:&quot;87494755&quot;}">九点</a></td></tr>
                    
                    <tr><td><a href="http://alphatown.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-town&quot;,&quot;uid&quot;:&quot;87494755&quot;}">阿尔法城</a></td></tr>
                    
                    <tr><td><a href="http://www.douban.com/mobile/" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-mobile&quot;,&quot;uid&quot;:&quot;87494755&quot;}">移动应用</a></td></tr>
                </tbody></table>
              </div>
            </li>
      </ul>
    </div>
  </div>
</div>



   
    









<div id="db-nav-group" class="nav">
  <div class="nav-wrap">
  <div class="nav-primary clearfix">
    <div class="nav-logo">
      <a href="http://www.douban.com/group/">豆瓣小组</a>
    </div>

    <div class="nav-items">
    <ul>
        
        <li class="nav-item-first"><a href="http://www.douban.com/group/">我的小组</a></li>
      <li><a href="http://www.douban.com/group/explore">精选</a></li>
      <li><a href="http://www.douban.com/group/explore/culture">文化</a></li>
      <li><a href="http://www.douban.com/group/explore/travel">行摄</a></li>
      <li><a href="http://www.douban.com/group/explore/ent">娱乐</a></li>
      <li><a href="http://www.douban.com/group/explore/fashion">时尚</a></li>
      <li><a href="http://www.douban.com/group/explore/life">生活</a></li>
      <li><a href="http://www.douban.com/group/explore/tech">科技</a></li>
   </ul>
   </div>

    <div class="nav-search">
      <form id="form" action="http://www.douban.com/group/search" method="get">
        <fieldset>
          <legend>搜索：</legend>
          
          <input type="hidden" name="cat" value="1019">
          <label for="inp-query" style="display: none;">小组、话题</label>
          <div class="inp"><input id="inp-query" name="q" size="22" maxlength="60" value="" placeholder="小组、话题"></div>
          <div class="inp-btn"><input type="submit" value="搜索"></div>
        </fieldset>
      </form>
    </div>
  </div>
  </div>

</div>

<script>
Do(function(){
  var nav = $('#db-nav-group');
  var inp=$("#inp-query"),label=inp.closest(".nav-search").find("label");if("placeholder" in inp[0]){label.hide();inp.attr("placeholder",label.text())}else{if(inp.val()!==""){label.hide()}inp.parent().click(function(){inp.focus();label.hide()}).end().focusin(function(){label.hide()}).focusout(function(){if($.trim(this.value)===""){label.show()}else{label.hide()}}).keydown(function(){label.hide()})}inp.parents("form").submit(function(){if(!$.trim(inp.val()).length){return false}});nav.find(".lnk-more, .lnk-account").click(function(b){b.preventDefault();var d,a=$(this),c=a.hasClass("lnk-more")?$("#db-productions"):$("#db-usr-setting");if(!c.data("init")){d=a.offset();c.css({"margin-left":(d.left-$(window).width()/2-c.width()+a.width()+parseInt(a.css("padding-right"),10))+"px",left:"50%",top:d.top+a.height()+"px"});c.data("init",1);c.hide();$("body").click(function(g){var f=$(g.target);if(f.hasClass("lnk-more")||f.hasClass("lnk-account")||f.closest("#db-usr-setting").length||f.closest("#db-productions").length){return}c.hide()})}if(c.css("display")==="none"){$(".dropdown").hide();c.show()}else{$(".dropdown").hide()}});
});
</script>




    <div id="wrapper">
        

        
<div id="content">
    
    <h1><div class="head-nav">我的小组话题</div></h1>

    <div class="grid-16-8 clearfix">
        
        
        <div class="article">
               
  







<div class="pro-banner" style="display: block;">
  <img src="http://t.douban.com/img/files/file-1407489302.png">
  <a href="javascript:void(0)" class="lnk-close"></a>
  <a href="http://www.douban.com/mobile/group" target="_blank" class="lnk-pro"></a>
</div>

  <div class="topics">
      <table class="olt">
          <tbody>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/57582070/" title="【晒正能量】下雨了没带伞却看到了彩虹" class="title">【晒正能量】下雨了没带伞却看到了彩虹</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">1068回应</td>
                      <td class="td-time" title="2014-08-22 22:22:45" nowrap="nowrap">7秒前</td>
                      <td class="td-group"><a href="http://www.douban.com/group/haixiuzu/" class="">请不要害羞（微信...</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/56997527/" title="【晒大长腿】看到自己的大腿儿都会害羞怎么办~" class="title">【晒大长腿】看到自己的大腿儿都会害羞怎么办~</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">667回应</td>
                      <td class="td-time" title="2014-08-22 22:22:37" nowrap="nowrap">15秒前</td>
                      <td class="td-group"><a href="http://www.douban.com/group/haixiuzu/" class="">请不要害羞（微信...</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/59966779/" title="【晒】眼睛。只有眼睛（我不是高圆圆- -）" class="title">【晒】眼睛。只有眼睛（我不是高圆圆- -）</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">476回应</td>
                      <td class="td-time" title="2014-08-22 22:22:20" nowrap="nowrap">32秒前</td>
                      <td class="td-group"><a href="http://www.douban.com/group/haixiuzu/" class="">请不要害羞（微信...</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/60095680/" title="【晒】长腿偶呢 更新腿照 再说不长就哭" class="title">【晒】长腿偶呢 更新腿照 再说不长就哭</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">1161回应</td>
                      <td class="td-time" title="2014-08-22 22:22:16" nowrap="nowrap">36秒前</td>
                      <td class="td-group"><a href="http://www.douban.com/group/haixiuzu/" class="">请不要害羞（微信...</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/60353686/" title="只是想找人聊天" class="title">只是想找人聊天</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">20回应</td>
                      <td class="td-time" title="2014-08-22 22:22:12" nowrap="nowrap">40秒前</td>
                      <td class="td-group"><a href="http://www.douban.com/group/haixiuzu/" class="">请不要害羞（微信...</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/57936038/" title="【晒】这是舒克还是贝塔？？？" class="title">【晒】这是舒克还是贝塔？？？</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">2064回应</td>
                      <td class="td-time" title="2014-08-22 22:22:11" nowrap="nowrap">41秒前</td>
                      <td class="td-group"><a href="http://www.douban.com/group/haixiuzu/" class="">请不要害羞（微信...</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/60269943/" title="【晒】真的是铅笔和小制服" class="title">【晒】真的是铅笔和小制服</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">306回应</td>
                      <td class="td-time" title="2014-08-22 22:21:56" nowrap="nowrap">56秒前</td>
                      <td class="td-group"><a href="http://www.douban.com/group/haixiuzu/" class="">请不要害羞（微信...</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/60339595/" title="【晒】头发＋昨天和叔见面了" class="title">【晒】头发＋昨天和叔见面了</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">135回应</td>
                      <td class="td-time" title="2014-08-22 22:21:38" nowrap="nowrap">1分钟前</td>
                      <td class="td-group"><a href="http://www.douban.com/group/haixiuzu/" class="">请不要害羞（微信...</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/59991936/" title="【晒大粗眉】更新了啊" class="title">【晒大粗眉】更新了啊</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">1774回应</td>
                      <td class="td-time" title="2014-08-22 22:21:16" nowrap="nowrap">1分钟前</td>
                      <td class="td-group"><a href="http://www.douban.com/group/haixiuzu/" class="">请不要害羞（微信...</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/60310931/" title="【晒】能有几个人看懂" class="title">【晒】能有几个人看懂</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">126回应</td>
                      <td class="td-time" title="2014-08-22 22:20:25" nowrap="nowrap">2分钟前</td>
                      <td class="td-group"><a href="http://www.douban.com/group/haixiuzu/" class="">请不要害羞（微信...</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/54465386/" title="【曬】誰說台灣的妹子，不会打简体字" class="title">【曬】誰說台灣的妹子，不会打简体字</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">1759回应</td>
                      <td class="td-time" title="2014-08-22 22:20:02" nowrap="nowrap">2分钟前</td>
                      <td class="td-group"><a href="http://www.douban.com/group/haixiuzu/" class="">请不要害羞（微信...</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/60090304/" title="【晒肥胖】我是来努力减肥的！" class="title">【晒肥胖】我是来努力减肥的！</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">499回应</td>
                      <td class="td-time" title="2014-08-22 22:19:54" nowrap="nowrap">2分钟前</td>
                      <td class="td-group"><a href="http://www.douban.com/group/haixiuzu/" class="">请不要害羞（微信...</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/59654015/" title="【晒】屌丝女提前更了，晚上家族聚会呢没时间" class="title">【晒】屌丝女提前更了，晚上家族聚会呢没时间</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">366回应</td>
                      <td class="td-time" title="2014-08-22 22:19:35" nowrap="nowrap">3分钟前</td>
                      <td class="td-group"><a href="http://www.douban.com/group/haixiuzu/" class="">请不要害羞（微信...</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/57817296/" title="【晒】身上肉多多(｡•ˇ‸ˇ•｡)" class="title">【晒】身上肉多多(｡•ˇ‸ˇ•｡)</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">2695回应</td>
                      <td class="td-time" title="2014-08-22 22:19:10" nowrap="nowrap">3分钟前</td>
                      <td class="td-group"><a href="http://www.douban.com/group/haixiuzu/" class="">请不要害羞（微信...</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/59976645/" title="【晒】这样的制服喜欢么  小胖妞今天也努力在更新" class="title">【晒】这样的制服喜欢么  小胖妞今天也努力在更新</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">287回应</td>
                      <td class="td-time" title="2014-08-22 22:19:01" nowrap="nowrap">3分钟前</td>
                      <td class="td-group"><a href="http://www.douban.com/group/haixiuzu/" class="">请不要害羞（微信...</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/60331368/" title="【晒】都是胸器，小胸还怎么活？" class="title">【晒】都是胸器，小胸还怎么活？</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">135回应</td>
                      <td class="td-time" title="2014-08-22 22:18:41" nowrap="nowrap">4分钟前</td>
                      <td class="td-group"><a href="http://www.douban.com/group/haixiuzu/" class="">请不要害羞（微信...</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/59752746/" title="【晒一发泳衣】" class="title">【晒一发泳衣】</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">161回应</td>
                      <td class="td-time" title="2014-08-22 22:18:32" nowrap="nowrap">4分钟前</td>
                      <td class="td-group"><a href="http://www.douban.com/group/haixiuzu/" class="">请不要害羞（微信...</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/60351800/" title="【晒午后慵懒】小日系风" class="title">【晒午后慵懒】小日系风</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">10回应</td>
                      <td class="td-time" title="2014-08-22 22:18:20" nowrap="nowrap">4分钟前</td>
                      <td class="td-group"><a href="http://www.douban.com/group/haixiuzu/" class="">请不要害羞（微信...</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/59733758/" title="【晒】冒充什么年纪什么身高好呢？" class="title">【晒】冒充什么年纪什么身高好呢？</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">775回应</td>
                      <td class="td-time" title="2014-08-22 22:17:48" nowrap="nowrap">5分钟前</td>
                      <td class="td-group"><a href="http://www.douban.com/group/haixiuzu/" class="">请不要害羞（微信...</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/60068462/" title="【晒】一坨坨肉～" class="title">【晒】一坨坨肉～</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">304回应</td>
                      <td class="td-time" title="2014-08-22 22:17:26" nowrap="nowrap">5分钟前</td>
                      <td class="td-group"><a href="http://www.douban.com/group/haixiuzu/" class="">请不要害羞（微信...</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/60353446/" title="［晒］ 短 穿" class="title">［晒］ 短 穿</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">6回应</td>
                      <td class="td-time" title="2014-08-22 22:17:23" nowrap="nowrap">5分钟前</td>
                      <td class="td-group"><a href="http://www.douban.com/group/haixiuzu/" class="">请不要害羞（微信...</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/60338983/" title="【晒】小鹿" class="title">【晒】小鹿</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">121回应</td>
                      <td class="td-time" title="2014-08-22 22:17:19" nowrap="nowrap">5分钟前</td>
                      <td class="td-group"><a href="http://www.douban.com/group/haixiuzu/" class="">请不要害羞（微信...</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/60200329/" title="【晒？】可是有什么好晒的" class="title">【晒？】可是有什么好晒的</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">87回应</td>
                      <td class="td-time" title="2014-08-22 22:17:08" nowrap="nowrap">5分钟前</td>
                      <td class="td-group"><a href="http://www.douban.com/group/haixiuzu/" class="">请不要害羞（微信...</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/60286153/" title="【晒】手作比基尼，深蹲确实有效……哈哈" class="title">【晒】手作比基尼，深蹲确实有效……哈哈</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">396回应</td>
                      <td class="td-time" title="2014-08-22 22:16:06" nowrap="nowrap">6分钟前</td>
                      <td class="td-group"><a href="http://www.douban.com/group/haixiuzu/" class="">请不要害羞（微信...</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/60304793/" title="【晒】哈哈突然觉得太不好意思了" class="title">【晒】哈哈突然觉得太不好意思了</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">248回应</td>
                      <td class="td-time" title="2014-08-22 22:15:00" nowrap="nowrap">7分钟前</td>
                      <td class="td-group"><a href="http://www.douban.com/group/haixiuzu/" class="">请不要害羞（微信...</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/59998252/" title="【晒】只是暂别…嘛…啥都没有…就是小透明～" class="title">【晒】只是暂别…嘛…啥都没有…就是小透明～</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">575回应</td>
                      <td class="td-time" title="2014-08-22 22:14:41" nowrap="nowrap">8分钟前</td>
                      <td class="td-group"><a href="http://www.douban.com/group/haixiuzu/" class="">请不要害羞（微信...</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/58118241/" title="【晒】腿腿腿 胆小勿入" class="title">【晒】腿腿腿 胆小勿入</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">1401回应</td>
                      <td class="td-time" title="2014-08-22 22:13:36" nowrap="nowrap">9分钟前</td>
                      <td class="td-group"><a href="http://www.douban.com/group/haixiuzu/" class="">请不要害羞（微信...</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/60341685/" title="【晒】狐狸未成精~" class="title">【晒】狐狸未成精~</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">88回应</td>
                      <td class="td-time" title="2014-08-22 22:13:26" nowrap="nowrap">9分钟前</td>
                      <td class="td-group"><a href="http://www.douban.com/group/haixiuzu/" class="">请不要害羞（微信...</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/60092244/" title="【晒】眼袋or卧蚕 傻傻分不清楚，" class="title">【晒】眼袋or卧蚕 傻傻分不清楚，</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">339回应</td>
                      <td class="td-time" title="2014-08-22 22:12:55" nowrap="nowrap">9分钟前</td>
                      <td class="td-group"><a href="http://www.douban.com/group/haixiuzu/" class="">请不要害羞（微信...</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/55006271/" title="【晒植物】喜欢植物的女孩子有么？求友邻。" class="title">【晒植物】喜欢植物的女孩子有么？求友邻。</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">308回应</td>
                      <td class="td-time" title="2014-08-22 22:11:30" nowrap="nowrap">11分钟前</td>
                      <td class="td-group"><a href="http://www.douban.com/group/haixiuzu/" class="">请不要害羞（微信...</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/57730737/" title="【晒】tattoo是信仰。晒我的纹身和头发！纹身已完成正脸已上！" class="title">【晒】tattoo是信仰。晒我的纹身和头发！纹身已完...</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">1195回应</td>
                      <td class="td-time" title="2014-08-22 22:10:43" nowrap="nowrap">12分钟前</td>
                      <td class="td-group"><a href="http://www.douban.com/group/haixiuzu/" class="">请不要害羞（微信...</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/54853278/" title="【晒高达！！！！！！！！！】RG完成~（伦家会一字马哟~）" class="title">【晒高达！！！！！！！！！】RG完成~（伦家会一字...</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">1155回应</td>
                      <td class="td-time" title="2014-08-22 22:10:24" nowrap="nowrap">12分钟前</td>
                      <td class="td-group"><a href="http://www.douban.com/group/haixiuzu/" class="">请不要害羞（微信...</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/58032942/" title="【晒】给我一个吻~" class="title">【晒】给我一个吻~</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">1475回应</td>
                      <td class="td-time" title="2014-08-22 22:10:21" nowrap="nowrap">12分钟前</td>
                      <td class="td-group"><a href="http://www.douban.com/group/haixiuzu/" class="">请不要害羞（微信...</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/59989047/" title="【晒】我麻麻二十岁时候的衣服" class="title">【晒】我麻麻二十岁时候的衣服</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">382回应</td>
                      <td class="td-time" title="2014-08-22 22:09:55" nowrap="nowrap">12分钟前</td>
                      <td class="td-group"><a href="http://www.douban.com/group/haixiuzu/" class="">请不要害羞（微信...</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/60180041/" title="成都" class="title">成都</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">6回应</td>
                      <td class="td-time" title="2014-08-22 22:08:14" nowrap="nowrap">14分钟前</td>
                      <td class="td-group"><a href="http://www.douban.com/group/loli20/" class="">我们都有混乱过</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/60352143/" title="一起的姑娘总是高个大长腿，其实好想和娇小型的来一发" class="title">一起的姑娘总是高个大长腿，其实好想和娇小型的来一发</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">0回应</td>
                      <td class="td-time" title="2014-08-22 22:05:55" nowrap="nowrap">16分钟前</td>
                      <td class="td-group"><a href="http://www.douban.com/group/loli20/" class="">我们都有混乱过</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/59743519/" title="晒空姐制服，晒黑色高跟" class="title">晒空姐制服，晒黑色高跟</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">24回应</td>
                      <td class="td-time" title="2014-08-22 22:03:56" nowrap="nowrap">18分钟前</td>
                      <td class="td-group"><a href="http://www.douban.com/group/274363/" class="">【晒XX】女神来了-...</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/60320706/" title="第一次、进不去肿么办" class="title">第一次、进不去肿么办</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">22回应</td>
                      <td class="td-time" title="2014-08-22 22:03:24" nowrap="nowrap">19分钟前</td>
                      <td class="td-group"><a href="http://www.douban.com/group/loli20/" class="">我们都有混乱过</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/60312694/" title="伦家想找简单的哥哥聊天嘛 25以下的来来~~~" class="title">伦家想找简单的哥哥聊天嘛 25以下的来来~~~</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">2回应</td>
                      <td class="td-time" title="2014-08-22 22:02:46" nowrap="nowrap">20分钟前</td>
                      <td class="td-group"><a href="http://www.douban.com/group/274363/" class="">【晒XX】女神来了-...</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/59272515/" title="妹子們都喜歡被口嗎？" class="title">妹子們都喜歡被口嗎？</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">29回应</td>
                      <td class="td-time" title="2014-08-22 21:58:31" nowrap="nowrap">24分钟前</td>
                      <td class="td-group"><a href="http://www.douban.com/group/loli20/" class="">我们都有混乱过</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/57885593/" title="平胸真的是没救了么？！哭。。。" class="title">平胸真的是没救了么？！哭。。。</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">514回应</td>
                      <td class="td-time" title="2014-08-22 21:44:52" nowrap="nowrap">38分钟前</td>
                      <td class="td-group"><a href="http://www.douban.com/group/loli20/" class="">我们都有混乱过</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/60126664/" title="已到帝都，在工体～征姑娘" class="title">已到帝都，在工体～征姑娘</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">5回应</td>
                      <td class="td-time" title="2014-08-22 20:53:58" nowrap="nowrap">今天20:53</td>
                      <td class="td-group"><a href="http://www.douban.com/group/loli20/" class="">我们都有混乱过</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/60137874/" title="大中国西南面的，有不？" class="title">大中国西南面的，有不？</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">7回应</td>
                      <td class="td-time" title="2014-08-22 20:53:29" nowrap="nowrap">今天20:53</td>
                      <td class="td-group"><a href="http://www.douban.com/group/loli20/" class="">我们都有混乱过</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/60337759/" title="有昆明的妹子不？" class="title">有昆明的妹子不？</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">3回应</td>
                      <td class="td-time" title="2014-08-22 20:22:06" nowrap="nowrap">今天20:22</td>
                      <td class="td-group"><a href="http://www.douban.com/group/loli20/" class="">我们都有混乱过</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/60315560/" title="马上就要开学了，早返校的萝莉有大叔" class="title">马上就要开学了，早返校的萝莉有大叔</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">1回应</td>
                      <td class="td-time" title="2014-08-22 19:50:35" nowrap="nowrap">今天19:50</td>
                      <td class="td-group"><a href="http://www.douban.com/group/loli20/" class="">我们都有混乱过</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/55210947/" title="天天都要，他被我榨干了！" class="title">天天都要，他被我榨干了！</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">181回应</td>
                      <td class="td-time" title="2014-08-22 19:12:11" nowrap="nowrap">今天19:12</td>
                      <td class="td-group"><a href="http://www.douban.com/group/loli20/" class="">我们都有混乱过</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/60083749/" title="混乱过，才发现自己真的不适合混乱，如此也好" class="title">混乱过，才发现自己真的不适合混乱，如此也好</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">10回应</td>
                      <td class="td-time" title="2014-08-22 19:12:05" nowrap="nowrap">今天19:12</td>
                      <td class="td-group"><a href="http://www.douban.com/group/loli20/" class="">我们都有混乱过</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/60157693/" title="快来点评一下好嘛！请喷请夸奖啦来吧！！" class="title">快来点评一下好嘛！请喷请夸奖啦来吧！！</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">8回应</td>
                      <td class="td-time" title="2014-08-22 18:37:11" nowrap="nowrap">今天18:37</td>
                      <td class="td-group"><a href="http://www.douban.com/group/274363/" class="">【晒XX】女神来了-...</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/59846476/" title="晒成果喽" class="title">晒成果喽</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">1回应</td>
                      <td class="td-time" title="2014-08-22 18:31:41" nowrap="nowrap">今天18:31</td>
                      <td class="td-group"><a href="http://www.douban.com/group/274363/" class="">【晒XX】女神来了-...</a></td>
                  </tr>
                  
                  <tr class="pl">
                      <td class="td-subject">
                        <a href="http://www.douban.com/group/topic/59722570/" title="晒晒更健康" class="title">晒晒更健康</a>
                      </td>
                      <td class="td-reply" nowrap="nowrap">1回应</td>
                      <td class="td-time" title="2014-08-22 18:31:23" nowrap="nowrap">今天18:31</td>
                      <td class="td-group"><a href="http://www.douban.com/group/274363/" class="">【晒XX】女神来了-...</a></td>
                  </tr>
          </tbody>
      </table>
  </div>
  
    
    

    
        <div class="paginator">
        <span class="prev">
            &lt;前页
        </span>
        
        

                <span class="thispage" data-total-page="9223372036854775807">1</span>
                
            <a href="/group/?start=50">2</a>
        
                
            <a href="/group/?start=100">3</a>
        
                
            <a href="/group/?start=150">4</a>
        
                
            <a href="/group/?start=200">5</a>
        
                
            <a href="/group/?start=250">6</a>
        
                
            <a href="/group/?start=300">7</a>
        
                
            <a href="/group/?start=350">8</a>
        
                
            <a href="/group/?start=400">9</a>
        
            <span class="break">...</span>
        <span class="next">
            <link rel="next" href="/group/?start=50">
            <a href="/group/?start=50">后页&gt;</a>
        </span>

        </div>



        </div>
        <div class="aside">
                
  




  
  <div class="mod profile-entry">
  <div class="pic">
  <a href="/group/people/87494755/"><img src="http://img3.douban.com/icon/user_normal.jpg"></a>
  </div>
  <div class="info">
    <a href="/group/people/87494755/">我的小组主页</a>
    <p><a href="http://www.douban.com/group/people/87494755/publish">发起(1)</a> &nbsp;
    | &nbsp; <a href="http://www.douban.com/group/people/87494755/reply">回应(1)</a>
  </p></div>
</div>


  







<div id="g-reguler-groups" class="mod">
  <div class="hd">
  <span class="more"><a href="http://www.douban.com/group/people/87494755/joins">全部》</a></span>
  
    <h2>
        常去的小组
            
    </h2>

  </div>
  <div class="content">
      <ul>
          <li class="">
          <a href="http://www.douban.com/group/haixiuzu/"><img src="http://img3.douban.com/icon/g433459-3.jpg" title="请不要害羞（微信公众：haixiuzu1024）" alt="请不要害羞（微信公众：haixiuzu1024）" class=""></a>
          </li>
          <li class="">
          <a href="http://www.douban.com/group/loli20/"><img src="http://img3.douban.com/icon/g199863-10.jpg" title="我们都有混乱过" alt="我们都有混乱过" class=""></a>
          </li>
          <li class="">
          <a href="http://www.douban.com/group/274363/"><img src="http://img3.douban.com/icon/g274363-2.jpg" title="【晒XX】女神来了-不羞涩招女管理员" alt="【晒XX】女神来了-不羞涩招女管理员" class=""></a>
          </li>
      </ul>
  </div>
</div>


  <!-- douban ad begin -->
  <div id="dale_group_home_new_top_right"></div>
  <!-- douban ad end -->

  




  

<div class="mod mod-app-entrance">
<h3>手机扫描二维码，把小组装进口袋</h3>
<div class="bd">
    <div class="pic">
        <img src="http://img3.douban.com/pics/group/app_qr1.png" width="80" height="80">
    </div>
    <div class="content">
    <a href="http://www.douban.com/mobile/ipa?app_name=group" target="_blank" class="lnk-app-download lnk-app-iphone">iPhone</a>
    <a href="http://www.douban.com/mobile/ipa?app_name=group-ipad" target="_blank" class="lnk-app-download lnk-app-ipad">iPad</a>
    <a href="http://andariel.douban.com/d/com.douban.group" target="_blank" class="lnk-app-download lnk-app-android">Android</a>
    </div>
</div>
</div>


  <div class="mod">
    

<div class="create-group">
    

        <a href="/group/new_group"><i>+</i>申请创建小组</a>
</div>

  </div>
  


<div id="group-contact" class="mod">
  <ul>
    <li class="group-wb"><a href="http://e.weibo.com/Group2005" target="_blank">豆瓣小组在微博</a></li>
    <li class="feed-back"><span>联系</span> </li>
  </ul>
</div>


  <!-- douban ad begin -->
  <div id="dale_newgroup_home_bottom_right_201211"></div>
  <!-- douban ad end -->

        </div>
        <div class="extra">
            
    <!-- douban ad begin -->
    <div id="dale_newgroup_home_bottom_banner_201211"></div>
    <!-- douban ad end -->

        </div>
    </div>
</div>

        
<div id="footer">
    

<span id="icp" class="fleft gray-link">
    © 2005－2014 douban.com, all rights reserved
</span>

<span class="fright">
    <a href="http://www.douban.com/about">关于豆瓣</a>
    · <a href="http://www.douban.com/jobs">在豆瓣工作</a>
    · <a href="http://www.douban.com/about?topic=contactus">联系我们</a>
    · <a href="http://www.douban.com/about?policy=disclaimer">免责声明</a>
    
    · <a href="http://www.douban.com/help/group">帮助中心</a>
    · <a href="http://developers.douban.com/" target="_blank">开发者</a>
    · <a href="http://www.douban.com/mobile/group">手机小组</a>
    · <a href="http://www.douban.com/partner/">豆瓣广告</a>
</span>


</div>

    </div>
    <script type="text/javascript">
    Do(function() {
      // 不再提醒
      Douban.init_delete_reply_notify=function(b){var a=function(g){g.preventDefault();var c=$(g.target);var h=c[0].href.split("#")[1];$.get("/j/accounts/remove_notify?id="+h);var d=c.closest(".item-req");if($.contains($(".top-nav-reminder")[0],d[0])){d=d.parent();var f=d.siblings().length;d.fadeOut(function(){d.remove()});if(f===0){d.closest(".bd").find(".no-new-notis").show()}}else{d.fadeOut()}};if(b.type==="click"){a(b)}else{$(b).click(a)}};
      Douban.init_discard_notify=function(b){var a=function(i){i.preventDefault();var c="/j/notification/discard";var f=$(i.target);var d=f[0].name;$.post_withck(c,{id:d},function(e){},"json");var g=f.closest(".item-req");if($.contains($(".top-nav-reminder")[0],g[0])){g=g.parent();var h=g.siblings().length;g.fadeOut(function(){g.remove()});if(h===0){g.closest(".bd").find(".no-new-notis").show()}}else{g.fadeOut()}};if(b.type==="click"){a(b)}else{$(b).click(a)}};

      var notimenu = $('#top-nav-notimenu');
      notimenu.bind('moreitem:show', function() {
        $.ajax({
          url: 'http://www.douban.com/j/notification/nav_pop',
          data: {
            ck: get_cookie('ck'),
            k: '87494755:cbcee2e748be5549fe0c2511b4456345eebab9f2',
            from_push: notimenu.data('from_push')
          },
          dataType: 'jsonp',
          success: function(e) {
            if (e.r) {
              return;
            }
            notimenu.html(e.s);
            if (e.n === 0) {
              $('#db-global-nav .top-nav-reminder .num').remove();
            } else {
              $('#db-global-nav .top-nav-reminder .num span').html(e.n);
            }
            set_cookie({push_noty_num: e.n});
            if (window.load_event_monitor) {
              load_event_monitor($('#db-global-nav'));
            }
          }
        });
      });

      window.DOUBAN_SITE_URL = 'http://www.douban.com';
        var current_noty_num=current_doumail_num=0;function updateNotyNum(b){current_noty_num=b;var a=$("#db-global-nav .top-nav-reminder");if(!b){a.find(".num").remove();return}var c=a.find(".num span");if(!c.length){a.append('<span class="num"><span>'+b+"</span><i></i></span>")}else{c.html(b)}if(b>0&&b<10){a.css("margin-right","5px")}else{if(b>10){a.css("margin-right","15px")}}}function updateDoumailNum(b){current_doumail_num=b;var c=$("#top-nav-doumail-link");var a=c.find("em");if(!b){a.remove();return}var d="("+b+")";if(!a.length){c.append("<em>"+d+"</em>")}else{a.html(d)}}function addCheckNotyLog(){$("#top-nav-notimenu").data("from_push","Y")}function addCheckDoumailLog(c){var b=document.getElementById("top-nav-doumail-link");b.onclick=function(){moreurl(this,{from:"check_doumail_from_push",uid:c})}}function showDesktopNotification(c){if(!window.Notification){return}var b=get_cookie("enable_push_desktop_noty");b=b=="1";if(!b){return}var a="";if(c.type=="notification"){a="你收到一个新提醒"}else{if(c.type=="doumail"){a="你收到一封新豆邮"}else{return}}var d=new Notification("豆瓣",{body:a,tag:c.id,icon:"http://img3.douban.com/pics/icon/dou36.png"});d.onclick=function(){window.focus();this.close()};d.onshow=function(){setTimeout(function(){d.close()},3000)}}function get_auth_token(a){$.ajax({url:DOUBAN_SITE_URL+"/j/push/get_token_with_ts",dataType:"jsonp",success:function(b){a(b.token,b.timestamp)}})}var timer=null;function startSyncNotyNumsCrossTabs(){clearTimeout(timer);timer=setTimeout(function(){var b=parseInt(get_cookie("push_noty_num")||"0",10),a=parseInt(get_cookie("push_doumail_num")||"0",10);if(b!=current_noty_num){updateNotyNum(b)}if(a!=current_doumail_num){updateDoumailNum(a)}if(!b&&!a){clearTimeout(timer)}else{timer=setTimeout(arguments.callee,1500)}},1500)}var retry_times=0,max_retry=50,retry_interval_unit=1000*3;function connectSSE(b,a,g){if(!window.EventSource){return}var d="notification:user:"+b,c=(b+"_"+g)+":"+a,i="http://push.douban.com:4394/sse?channel="+d+"&auth="+c;var f=null;try{f=new EventSource(i)}catch(h){return}f.addEventListener("open",function(){retry_times=0},false);f.addEventListener("error",function(j){if(this.readyState==EventSource.CLOSED||this.readyState==EventSource.CONNECTING){f.close();f=null;setTimeout(function(){retry_times+=1;if(retry_times<max_retry){get_auth_token(function(e,k){connectSSE(b,e,k)})}},retry_times*retry_interval_unit)}},false);f.addEventListener("message",function(k){var j=JSON.parse(k.data);if(j.type=="notification"){updateNotyNum(j.num);addCheckNotyLog();set_cookie({push_noty_num:j.num})}else{if(j.type=="doumail"){updateDoumailNum(j.num);addCheckDoumailLog(b);set_cookie({push_doumail_num:j.num})}}startSyncNotyNumsCrossTabs();showDesktopNotification(j)},false)};
        
        connectSSE('87494755', 'b8f29259e24fb028e2060877c183b567ba5d3891', '1408717372');
        
        set_cookie({
          push_noty_num: 0,
          push_doumail_num: 0
        });

    });
    </script><script type="text/javascript">
Do(function(){
  var popup;var nav=$("#db-global-nav");var more=nav.find(".bn-more");nav.delegate(".bn-more, .top-nav-reminder .lnk-remind","click",function(c){c.preventDefault();var a=$(this);var b=a.parent();if(popup){popup.parent().removeClass("more-active");if($.contains(b[0],popup[0])){popup=null;return}}b.addClass("more-active");popup=b.find(".more-items");popup.trigger("moreitem:show");return});$(document).click(function(a){if($(a.target).closest(".more-items").length||$(a.target).closest(".more-active").length){return}if(popup){popup.parent().removeClass("more-active");popup=null}});
});

Do(function() {
  $('.pro-banner').show();
  $(document).delegate('.pro-banner a.lnk-close', 'click', function(e) {
    $(this).parent().remove();
    $.post_withck('/j/group/hide_promotion', {
      'name': 'new_app'
    });
  });
});
</script>
    
  <!-- douban ad begin -->
  




    
<script type="text/javascript">
    (function (global) {
        var newNode = global.document.createElement('script'),
            existingNode = global.document.getElementsByTagName('script')[0],
            adSource = 'http://erebor.douban.com/',
            userId = '87494755',
            browserId = 'oA364r7higo',
            ipAddress = '119.130.187.226',
            criteria = '3:/group/',
            preview = '',
            debug = false,
            adSlots = ['dale_group_home_new_top_right', 'dale_newgroup_home_bottom_right_201211', 'dale_newgroup_home_bottom_banner_201211'];

        global.DoubanAdRequest = {src: adSource, uid: userId, bid: browserId, ip: ipAddress, crtr: criteria, prv: preview, debug: debug};
        global.DoubanAdSlots = (global.DoubanAdSlots || []).concat(adSlots);

        newNode.setAttribute('type', 'text/javascript');
        newNode.setAttribute('src', 'http://img3.douban.com/f/shire/55c9fe0e9ecb5725037e9839fc515504008dae74/js/ad.js');
        newNode.setAttribute('async', true);
        existingNode.parentNode.insertBefore(newNode, existingNode);
    })(this);
</script>










  <!-- douban ad end -->

    
    





<script type="text/javascript">
var _paq = _paq || [];
_paq.push(['trackPageView']);
_paq.push(['enableLinkTracking']);
(function() {
    var p=(('https:' == document.location.protocol) ? 'https' : 'http'), u=p+'://fundin.douban.com/';
    _paq.push(['setTrackerUrl', u+'piwik']);
    _paq.push(['setSiteId', '100001']);
    var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0]; 
    g.type='text/javascript';
    g.defer=true; 
    g.async=true; 
    g.src=p+'://s.doubanio.com/dae/fundin/piwik.js';
    s.parentNode.insertBefore(g,s);
})();
</script>

<script type="text/javascript">
var _gaq = _gaq || [];
_gaq.push(['_setAccount', 'UA-7019765-1']);
_gaq.push(['_addOrganic', 'baidu', 'word']);
_gaq.push(['_addOrganic', 'soso', 'w']);
_gaq.push(['_addOrganic', '3721', 'name']);
_gaq.push(['_addOrganic', 'youdao', 'q']);
_gaq.push(['_addOrganic', 'so.360.cn', 'q']);
_gaq.push(['_addOrganic', 'vnet', 'kw']);
_gaq.push(['_addOrganic', 'sogou', 'query']);
_gaq.push(['_addIgnoredOrganic', '豆瓣']);
_gaq.push(['_addIgnoredOrganic', 'douban']);
_gaq.push(['_addIgnoredOrganic', '豆瓣网']);
_gaq.push(['_addIgnoredOrganic', 'www.douban.com']);
_gaq.push(['_setDomainName', '.douban.com']);


    _gaq.push(['_setCustomVar', 1, 'responsive_view_mode', 'desktop', 3]); 

_gaq.push(['_trackPageview']);
_gaq.push(['_trackPageLoadTime']);
    _gaq.push(['_setVar', '8749']);

window._ga_init = function() {
    var ga = document.createElement('script');
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    ga.setAttribute('async', 'true');
    document.documentElement.firstChild.appendChild(ga);
};
if (window.addEventListener) {
    window.addEventListener('load', _ga_init, false);
} else {
    window.attachEvent('onload', _ga_init);
}
</script>





    <!-- sindar4c-->


  <script>_SPLITTEST='movie.tv-chart-gaia'</script>

<script>var _check_hijack = function () {
    var _sig = "oA364r7h", _login = true, bid = get_cookie('bid');
    if (location.protocol != "file:" && (
            typeof(bid) != "string" && _login ||
            typeof(bid) == "string" && bid.substring(0,8) != _sig)) {
        location.href += (/\?/.test(location.href)?"&":"?") + (
                "_r=" + Math.random().toString(16).substring(2));
    }};
if (typeof(Do) != 'undefined') Do(_check_hijack);
else if (typeof(get_cookie) != 'undefined') _check_hijack();
</script>



<iframe style="display: none !important; position: fixed !important; padding: 0px !important; margin: 0px !important; left: 0px !important; top: 0px !important; width: 100% !important; height: 100% !important; z-index: 2147483647 !important; border: none !important; background-color: transparent !important;"></iframe></body></html>"""

class TestMainPageDelegate(PageDelegate.PageDelegateBase):
    def do_children(self, topic_urls, jar):
        for topic_url in topic_urls:
            printTest('topic_url: %s' % topic_url)
    def do_next_pages(self, next_pages):
        for next_page in next_pages:
            printTest('next_page: %s' % next_page)

    def gen_head_from_jar(self, jar):
        pass
    def get_from_url(self, http_request, callback):
        printTest('method: %s, host: %s, path: %s' % (http_request.method, http_request.host, http_request.path))
        callback(test_html)


def main():
    delegate = TestMainPageDelegate()
    PageRoutines.do_main_page(PageDelegate.HttpRequest('GET', 'douban.com', '/'), None, {'topic' : 'td.td-subject>a.title', 'next_page' : 'span.next>a', 'url_attrib' : 'href'}, delegate)

if __name__ == '__main__':
    main()
