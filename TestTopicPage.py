# coding: UTF-8

import PageDelegate
import PageRoutines
from Print import printTest

test_html = """<html lang="zh-CN" class="ua-linux ua-webkit"><head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name="renderer" content="webkit">

    <title>
    晒空姐制服，晒黑色高跟
</title>
    
    
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="Sun, 6 Mar 2005 01:00:00 GMT">
    


    <script type="text/javascript" defer="" async="" src="http://s.doubanio.com/dae/fundin/piwik.js"></script><script type="text/javascript" src="http://img3.douban.com/f/shire/55c9fe0e9ecb5725037e9839fc515504008dae74/js/ad.js" async="true"></script><script>var _head_start = new Date();</script>
    <script src="http://img3.douban.com/f/shire/8033e1c2528bb6402c478e00176afb3562abbc21/js/jquery.min.js"></script>
    <script src="http://img3.douban.com/f/shire/6072cbd9e3d56db50f819890f57164950110117c/js/douban.js"></script>
    <link href="http://img3.douban.com/f/shire/b744ecd0276b46482458cb4ecaee3f256902adec/css/douban.css" rel="stylesheet" type="text/css">
    <style type="text/css">
    
        

    

    </style>
    
<link rel="stylesheet" type="text/css" href="http://img3.douban.com/f/shire/ae32cb8310a09ba836b958b79d2cd1e706db2fed/css/ui/dialog.css">
<script type="text/javascript" src="http://img3.douban.com/f/shire/4b3bad5e25de78678d700dd5353570dce3e6bbcc/js/ui/dialog.js"></script>
<style type="text/css">
.dui-dialog .bd { padding: 40px; font-size: 10pt; }
.dui-dialog .ft { background: #e4e4e4; height: 40px; }
.dui-dialog .ft div { padding-top: 15px; }
.dui-dialog .dui-dialog-prompt { float: left; }
.dui-dialog .bn-flat { color: #ffffff; float:right; width: 50px; cursor:pointer;}
.dui-dialog .btn-ok { background: #6fb45d; }
.dui-dialog .btn-cancel { background: #999999; }
.aside .mod { margin-bottom: 20px; }
</style>

    <link rel="stylesheet" href="http://img3.douban.com/misc/mixed_static/a73cfcb8eb92cff.css">
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
    
    <h1>
    晒空姐制服，晒黑色高跟
</h1>

    <div class="grid-16-8 clearfix">
        
        
        <div class="article">
               
    
    <input type="hidden" id="start" value="0">
    <div class="topic-content clearfix">
        <div class="user-face">
            <a href="http://www.douban.com/group/people/34807404/"><img class="pil" src="http://img3.douban.com/icon/u34807404-48.jpg" alt="瑶❤瑶"></a>
        </div>
        <div class="topic-doc">
            <h3>
                <span class="from">来自: <a href="http://www.douban.com/group/people/34807404/">瑶❤瑶</a></span>
                <span class="color-green">2014-08-19 18:06:47</span>
            </h3>

            
            <div id="link-report" class="">

                <div class="topic-content">
                          
                          <p>超级喜欢买各种小衣衣，收到货后第一件事当然要试穿拍照呀！(*^__^*) </p>
                          
                          <div class="topic-figure cc">
                              <img src="http://img5.douban.com/view/group_topic/large/public/p18564739.jpg" alt="黑丝黑高跟" class="">
                                  <span class="topic-figure-title">黑丝黑高跟</span>
                          </div>
                          <div class="clear"></div>
                          
                          <div class="topic-figure cc">
                              <img src="http://img3.douban.com/view/group_topic/large/public/p18564810.jpg" alt="变身小空姐" class="">
                                  <span class="topic-figure-title">变身小空姐</span>
                          </div>
                          <div class="clear"></div>
                          
                          <div class="topic-figure cc">
                              <img src="http://img5.douban.com/view/group_topic/large/public/p18564857.jpg" alt="亲亲" class="">
                                  <span class="topic-figure-title">亲亲</span>
                          </div>
                          <div class="clear"></div>
              </div>

            
    
    <div class="topic-opt clearfix">





      &nbsp; &nbsp;

    </div>

            <div class="report" style="visibility: hidden;"><a rel="nofollow" href="javascript:void(0)">举报</a></div></div>
            
<script type="text/javascript" src="http://img3.douban.com/f/shire/17ffde78bc768c1de53c46d5b5f7fb7f5893c10e/js/report_dialog.js"></script>
<link rel="stylesheet" type="text/css" href="http://img3.douban.com/f/shire/8adca47fea9ac369117af7c709cefe5bbdaf23ae/css/report_dialog.css">



        </div>



        <div class="sns-bar" id="sep">
            <div class="sns-bar-rec">
            </div>
            <div class="sns-bar-fav">
                






<span class="fav-num" data-tid="59743519" data-tkind="1013">
      <a href="http://www.douban.com/group/topic/59743519/?type=like#sep">3人</a>
  喜欢
</span>


  
  <a class="fav-add btn-fav" title="标为喜欢？" href="#" data-user_id="87494755" data-name="晒空姐制服，晒黑色高跟" data-type="com.douban.group" data-desc="超级喜欢买各种小衣衣，收到货后第一件事当然要试穿拍照呀！(*^__^*)    " data-href="http://www.douban.com/group/topic/59743519/" data-image="" data-properties="{&quot;href&quot;:&quot;http:\/\/www.douban.com\/group\/274363\/&quot;,&quot;uid&quot;:&quot;274363&quot;,&quot;name&quot;:&quot;【晒XX】女神来了-不羞涩招女管理员&quot;}" data-text="" data-apikey="None" data-object_kind="1013" data-object_id="59743519" data-target_type="fav" data-target_action="0" data-action_props="{&quot;topic_title&quot;:&quot;晒空姐制服，晒黑色高跟&quot;,&quot;topic_url&quot;:&quot;http:\/\/www.douban.com\/group\/topic\/59743519\/&quot;}" data-tid="59743519" data-sanity_key="_9743b" data-update_num="update" data-tag_align="right" data-privacy="1" data-tkind="1013">喜欢</a>
      <script type="text/template" id="fav-tag-template">
        
<form action="" method="POST"><div style="display:none;"><input type="hidden" name="ck" value="ZB2t"/></div>
  <div class="tag-editor-bd">
      

<div class="tags-editor">
    <fieldset class="tags-writer">
        <label for="author_tags_clone6466">添加标签，多个标签用空格分隔，帮助你更好地整理内容</label>
        <input id="author_tags" name="author_tags" type="hidden" value="" />
        <input tabindex="3" id="author_tags_clone6466" class="author_tags_clone" name="author_tags_clone" type="text" value="" />
    </fieldset>
</div>
<div class="tags-control">
    <span class="tags-tip error-msg"></span>
    <a href="#" class="tags_more">展开全部<i class="triangle triangle-right"></i></a>
</div>

  </div>
  <div class="tag-editor-ft">
    <span class="bn-flat"><input type="submit" value="保存"></span>
  </div>
</form>

      </script>





            </div>
        </div>

    </div>





<div class="tabs" id="reviews">
  <a href="http://www.douban.com/group/topic/59743519/#sep" class="on">回应</a>
    <a href="http://www.douban.com/group/topic/59743519/?type=rec#sep">推荐</a>
  <a href="http://www.douban.com/group/topic/59743519/?type=like#sep">喜欢</a>

        <span style="float:right">
            <a href="http://www.douban.com/group/topic/59743519/?author=1#sep">只看楼主</a>
        </span>
</div>
    

                        

                    
    <ul class="topic-reply" id="comments">
        

<li class="clearfix comment-item" id="740047924" data-cid="740047924">
    <div class="user-face">
        <a href="http://www.douban.com/group/people/54421884/"><img class="pil" src="http://img3.douban.com/icon/u54421884-2.jpg" alt="唐僧取经爱唱歌"></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="http://www.douban.com/group/people/54421884/" class="">唐僧取经爱唱歌</a>
              <span class="pubtime">2014-08-19 18:12:56</span>
          </h4>
        </div>
        <p class="">前排占个座，之后的呢</p>

        <div class="operation_div" id="54421884">
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="740047924" class="lnk-delete-comment" title="真的要删除唐僧取经爱唱歌的发言?">删除</a>
            <div class="comment-report"><a rel="nofollow" href="javascript:void(0)">举报</a></div></div>
            <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <a href="http://www.douban.com/group/topic/59743519/?cid=740047924#last" class="lnk-reply">回应</a>
        </div>
    </div>
</li>

        

<li class="clearfix comment-item" id="740060498" data-cid="740060498">
    <div class="user-face">
        <a href="http://www.douban.com/group/people/34807404/"><img class="pil" src="http://img3.douban.com/icon/u34807404-48.jpg" alt="瑶❤瑶"></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="http://www.douban.com/group/people/34807404/" class="">瑶❤瑶</a>
              <span class="pubtime">2014-08-19 18:28:40</span>
          </h4>
        </div>
        <p class="">发太多就没意思了</p>

        <div class="operation_div" id="34807404">
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="740060498" class="lnk-delete-comment" title="真的要删除瑶❤瑶的发言?">删除</a>
            <div class="comment-report"><a rel="nofollow" href="javascript:void(0)">举报</a></div></div>
            <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <a href="http://www.douban.com/group/topic/59743519/?cid=740060498#last" class="lnk-reply">回应</a>
        </div>
    </div>
</li>

        

<li class="clearfix comment-item" id="740063178" data-cid="740063178">
    <div class="user-face">
        <a href="http://www.douban.com/group/people/72728720/"><img class="pil" src="http://img3.douban.com/icon/u72728720-7.jpg" alt="evanz1989"></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="http://www.douban.com/group/people/72728720/" class="">evanz1989</a>
              <span class="pubtime">2014-08-19 18:32:11</span>
          </h4>
        </div>
        <p class="">已阅</p>

        <div class="operation_div" id="72728720">
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="740063178" class="lnk-delete-comment" title="真的要删除evanz1989的发言?">删除</a>
            <div class="comment-report"><a rel="nofollow" href="javascript:void(0)">举报</a></div></div>
            <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <a href="http://www.douban.com/group/topic/59743519/?cid=740063178#last" class="lnk-reply">回应</a>
        </div>
    </div>
</li>

        

<li class="clearfix comment-item" id="740231984" data-cid="740231984">
    <div class="user-face">
        <a href="http://www.douban.com/group/people/57740011/"><img class="pil" src="http://img3.douban.com/icon/u57740011-5.jpg" alt="黑底白花别样红"></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="http://www.douban.com/group/people/57740011/" class="">黑底白花别样红</a>
              <span class="pubtime">2014-08-19 21:44:38</span>
          </h4>
        </div>
        <p class="">瑶瑶原来你在这</p>

        <div class="operation_div" id="57740011">
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="740231984" class="lnk-delete-comment" title="真的要删除黑底白花别样红的发言?">删除</a>
            <div class="comment-report"><a rel="nofollow" href="javascript:void(0)">举报</a></div></div>
            <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <a href="http://www.douban.com/group/topic/59743519/?cid=740231984#last" class="lnk-reply">回应</a>
        </div>
    </div>
</li>

        

<li class="clearfix comment-item" id="740278187" data-cid="740278187">
    <div class="user-face">
        <a href="http://www.douban.com/group/people/23629911/"><img class="pil" src="http://img3.douban.com/icon/u23629911-32.jpg" alt="酋长噢哈啦"></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="http://www.douban.com/group/people/23629911/" class="">酋长噢哈啦</a> (夸父)
              <span class="pubtime">2014-08-19 22:29:01</span>
          </h4>
        </div>
        <p class="">买了自己穿自己看么</p>

        <div class="operation_div" id="23629911">
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="740278187" class="lnk-delete-comment" title="真的要删除酋长噢哈啦的发言?">删除</a>
            <div class="comment-report"><a rel="nofollow" href="javascript:void(0)">举报</a></div></div>
            <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <a href="http://www.douban.com/group/topic/59743519/?cid=740278187#last" class="lnk-reply">回应</a>
        </div>
    </div>
</li>

        

<li class="clearfix comment-item" id="740294426" data-cid="740294426">
    <div class="user-face">
        <a href="http://www.douban.com/group/people/68334985/"><img class="pil" src="http://img3.douban.com/icon/u68334985-3.jpg" alt="李斗城"></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="http://www.douban.com/group/people/68334985/" class="">李斗城</a>
              <span class="pubtime">2014-08-19 22:44:19</span>
          </h4>
        </div>
        <p class="">这是xxoo节奏？</p>

        <div class="operation_div" id="68334985">
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="740294426" class="lnk-delete-comment" title="真的要删除李斗城的发言?">删除</a>
            <div class="comment-report"><a rel="nofollow" href="javascript:void(0)">举报</a></div></div>
            <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <a href="http://www.douban.com/group/topic/59743519/?cid=740294426#last" class="lnk-reply">回应</a>
        </div>
    </div>
</li>

        

<li class="clearfix comment-item" id="740301614" data-cid="740301614">
    <div class="user-face">
        <a href="http://www.douban.com/group/people/87883443/"><img class="pil" src="http://img3.douban.com/icon/u87883443-4.jpg" alt="lennon"></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="http://www.douban.com/group/people/87883443/" class="">lennon</a>
              <span class="pubtime">2014-08-19 22:51:16</span>
          </h4>
        </div>
        <p class="">坐下慢慢看</p>

        <div class="operation_div" id="87883443">
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="740301614" class="lnk-delete-comment" title="真的要删除lennon的发言?">删除</a>
            <div class="comment-report"><a rel="nofollow" href="javascript:void(0)">举报</a></div></div>
            <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <a href="http://www.douban.com/group/topic/59743519/?cid=740301614#last" class="lnk-reply">回应</a>
        </div>
    </div>
</li>

        

<li class="clearfix comment-item" id="740311746" data-cid="740311746">
    <div class="user-face">
        <a href="http://www.douban.com/group/people/luna8525/"><img class="pil" src="http://img3.douban.com/icon/u16412099-22.jpg" alt="404 Not Found"></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="http://www.douban.com/group/people/luna8525/" class="">404 Not Found</a> (乜比個書架啵過會生愛滋嘅咩？)
              <span class="pubtime">2014-08-19 23:01:10</span>
          </h4>
        </div>
        <p class="">这是南航？</p>

        <div class="operation_div" id="16412099">
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="740311746" class="lnk-delete-comment" title="真的要删除404 Not Found的发言?">删除</a>
            <div class="comment-report"><a rel="nofollow" href="javascript:void(0)">举报</a></div></div>
            <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <a href="http://www.douban.com/group/topic/59743519/?cid=740311746#last" class="lnk-reply">回应</a>
        </div>
    </div>
</li>

        

<li class="clearfix comment-item" id="740519777" data-cid="740519777">
    <div class="user-face">
        <a href="http://www.douban.com/group/people/76771259/"><img class="pil" src="http://img3.douban.com/icon/u76771259-8.jpg" alt="marine"></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="http://www.douban.com/group/people/76771259/" class="">marine</a> (努力追寻自己的未来)
              <span class="pubtime">2014-08-20 07:22:58</span>
          </h4>
        </div>
        <p class="">勾搭啊</p>

        <div class="operation_div" id="76771259">
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="740519777" class="lnk-delete-comment" title="真的要删除marine的发言?">删除</a>
            <div class="comment-report"><a rel="nofollow" href="javascript:void(0)">举报</a></div></div>
            <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <a href="http://www.douban.com/group/topic/59743519/?cid=740519777#last" class="lnk-reply">回应</a>
        </div>
    </div>
</li>

        

<li class="clearfix comment-item" id="740523458" data-cid="740523458">
    <div class="user-face">
        <a href="http://www.douban.com/group/people/90583212/"><img class="pil" src="http://img3.douban.com/icon/u90583212-4.jpg" alt="能量100码"></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="http://www.douban.com/group/people/90583212/" class="">能量100码</a>
              <span class="pubtime">2014-08-20 07:35:34</span>
          </h4>
        </div>
        <p class="">感觉非楼主本人</p>

        <div class="operation_div" id="90583212">
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="740523458" class="lnk-delete-comment" title="真的要删除能量100码的发言?">删除</a>
            <div class="comment-report"><a rel="nofollow" href="javascript:void(0)">举报</a></div></div>
            <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <a href="http://www.douban.com/group/topic/59743519/?cid=740523458#last" class="lnk-reply">回应</a>
        </div>
    </div>
</li>

        

<li class="clearfix comment-item" id="740525343" data-cid="740525343">
    <div class="user-face">
        <a href="http://www.douban.com/group/people/74725672/"><img class="pil" src="http://img3.douban.com/icon/u74725672-3.jpg" alt="多么痛的领悟"></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="http://www.douban.com/group/people/74725672/" class="">多么痛的领悟</a>
              <span class="pubtime">2014-08-20 07:41:30</span>
          </h4>
        </div>
        <p class="">穿这些给男朋友看？</p>

        <div class="operation_div" id="74725672">
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="740525343" class="lnk-delete-comment" title="真的要删除多么痛的领悟的发言?">删除</a>
            <div class="comment-report"><a rel="nofollow" href="javascript:void(0)">举报</a></div></div>
            <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <a href="http://www.douban.com/group/topic/59743519/?cid=740525343#last" class="lnk-reply">回应</a>
        </div>
    </div>
</li>

        

<li class="clearfix comment-item" id="740601208" data-cid="740601208">
    <div class="user-face">
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="http://www.douban.com/group/people/63665018/" class="">Meiis</a>
              <span class="pubtime">2014-08-20 09:53:35</span>
          </h4>
        </div>
        <p class="">小衣衣蛮好看的</p>

        <div class="operation_div" id="63665018">
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="740601208" class="lnk-delete-comment" title="真的要删除Meiis的发言?">删除</a>
            <div class="comment-report"><a rel="nofollow" href="javascript:void(0)">举报</a></div></div>
            <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <a href="http://www.douban.com/group/topic/59743519/?cid=740601208#last" class="lnk-reply">回应</a>
        </div>
    </div>
</li>

        

<li class="clearfix comment-item" id="740825101" data-cid="740825101">
    <div class="user-face">
        <a href="http://www.douban.com/group/people/34807404/"><img class="pil" src="http://img3.douban.com/icon/u34807404-48.jpg" alt="瑶❤瑶"></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="http://www.douban.com/group/people/34807404/" class="">瑶❤瑶</a>
              <span class="pubtime">2014-08-20 14:06:43</span>
          </h4>
        </div>
        <p class="">照片太多，随便晒两张</p>

        <div class="operation_div" id="34807404">
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="740825101" class="lnk-delete-comment" title="真的要删除瑶❤瑶的发言?">删除</a>
            <div class="comment-report"><a rel="nofollow" href="javascript:void(0)">举报</a></div></div>
            <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <a href="http://www.douban.com/group/topic/59743519/?cid=740825101#last" class="lnk-reply">回应</a>
        </div>
    </div>
</li>

        

<li class="clearfix comment-item" id="740829553" data-cid="740829553">
    <div class="user-face">
        <a href="http://www.douban.com/group/people/66447923/"><img class="pil" src="http://img3.douban.com/icon/u66447923-2.jpg" alt="董大师"></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="http://www.douban.com/group/people/66447923/" class="">董大师</a>
              <span class="pubtime">2014-08-20 14:11:31</span>
          </h4>
        </div>
        <p class="">太赞了...</p>

        <div class="operation_div" id="66447923">
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="740829553" class="lnk-delete-comment" title="真的要删除董大师的发言?">删除</a>
            <div class="comment-report"><a rel="nofollow" href="javascript:void(0)">举报</a></div></div>
            <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <a href="http://www.douban.com/group/topic/59743519/?cid=740829553#last" class="lnk-reply">回应</a>
        </div>
    </div>
</li>

        

<li class="clearfix comment-item" id="740840440" data-cid="740840440">
    <div class="user-face">
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="http://www.douban.com/group/people/84808979/" class="">枪十六</a>
              <span class="pubtime">2014-08-20 14:22:59</span>
          </h4>
        </div>
        <p class="">能点赞吗</p>

        <div class="operation_div" id="84808979">
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="740840440" class="lnk-delete-comment" title="真的要删除枪十六的发言?">删除</a>
            <div class="comment-report"><a rel="nofollow" href="javascript:void(0)">举报</a></div></div>
            <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <a href="http://www.douban.com/group/topic/59743519/?cid=740840440#last" class="lnk-reply">回应</a>
        </div>
    </div>
</li>

        

<li class="clearfix comment-item" id="740844886" data-cid="740844886">
    <div class="user-face">
        <a href="http://www.douban.com/group/people/80065102/"><img class="pil" src="http://img3.douban.com/icon/u80065102-2.jpg" alt="A gogo"></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="http://www.douban.com/group/people/80065102/" class="">A gogo</a>
              <span class="pubtime">2014-08-20 14:27:40</span>
          </h4>
        </div>
        <p class="">喜欢个</p>

        <div class="operation_div" id="80065102">
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="740844886" class="lnk-delete-comment" title="真的要删除A gogo的发言?">删除</a>
            <div class="comment-report"><a rel="nofollow" href="javascript:void(0)">举报</a></div></div>
            <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <a href="http://www.douban.com/group/topic/59743519/?cid=740844886#last" class="lnk-reply">回应</a>
        </div>
    </div>
</li>

        

<li class="clearfix comment-item" id="740853996" data-cid="740853996">
    <div class="user-face">
        <a href="http://www.douban.com/group/people/51431923/"><img class="pil" src="http://img3.douban.com/icon/u51431923-4.jpg" alt="低调的奢华"></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="http://www.douban.com/group/people/51431923/" class="">低调的奢华</a>
              <span class="pubtime">2014-08-20 14:36:49</span>
          </h4>
        </div>
        <p class="">大爱黑丝高跟，话说你腿好长啊，后入很爽的吧</p>

        <div class="operation_div" id="51431923">
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="740853996" class="lnk-delete-comment" title="真的要删除低调的奢华的发言?">删除</a>
            <div class="comment-report"><a rel="nofollow" href="javascript:void(0)">举报</a></div></div>
            <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <a href="http://www.douban.com/group/topic/59743519/?cid=740853996#last" class="lnk-reply">回应</a>
        </div>
    </div>
</li>

        

<li class="clearfix comment-item" id="741274930" data-cid="741274930">
    <div class="user-face">
        <a href="http://www.douban.com/group/people/74842922/"><img class="pil" src="http://img3.douban.com/icon/u74842922-12.jpg" alt="Adolf Hitler"></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="http://www.douban.com/group/people/74842922/" class="">Adolf Hitler</a>
              <span class="pubtime">2014-08-20 22:04:11</span>
          </h4>
        </div>
        <p class="">楼主实际职业是什么？</p>

        <div class="operation_div" id="74842922">
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="741274930" class="lnk-delete-comment" title="真的要删除Adolf Hitler的发言?">删除</a>
            <div class="comment-report"><a rel="nofollow" href="javascript:void(0)">举报</a></div></div>
            <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <a href="http://www.douban.com/group/topic/59743519/?cid=741274930#last" class="lnk-reply">回应</a>
        </div>
    </div>
</li>

        

<li class="clearfix comment-item" id="742504206" data-cid="742504206">
    <div class="user-face">
        <a href="http://www.douban.com/group/people/38858751/"><img class="pil" src="http://img3.douban.com/icon/u38858751-6.jpg" alt="callmeeden"></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="http://www.douban.com/group/people/38858751/" class="">callmeeden</a>
              <span class="pubtime">2014-08-22 08:30:05</span>
          </h4>
        </div>
        <p class="">cock</p>

        <div class="operation_div" id="38858751">
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="742504206" class="lnk-delete-comment" title="真的要删除callmeeden的发言?">删除</a>
            <div class="comment-report"><a rel="nofollow" href="javascript:void(0)">举报</a></div></div>
            <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <a href="http://www.douban.com/group/topic/59743519/?cid=742504206#last" class="lnk-reply">回应</a>
        </div>
    </div>
</li>

        

<li class="clearfix comment-item" id="742504660" data-cid="742504660">
    <div class="user-face">
        <a href="http://www.douban.com/group/people/57537585/"><img class="pil" src="http://img3.douban.com/icon/u57537585-2.jpg" alt="李香緣"></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="http://www.douban.com/group/people/57537585/" class="">李香緣</a> (愛米利)
              <span class="pubtime">2014-08-22 08:31:14</span>
          </h4>
        </div>
        <p class="">制服诱惑</p>

        <div class="operation_div" id="57537585">
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="742504660" class="lnk-delete-comment" title="真的要删除李香緣的发言?">删除</a>
            <div class="comment-report"><a rel="nofollow" href="javascript:void(0)">举报</a></div></div>
            <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <a href="http://www.douban.com/group/topic/59743519/?cid=742504660#last" class="lnk-reply">回应</a>
        </div>
    </div>
</li>

        

<li class="clearfix comment-item" id="742505611" data-cid="742505611">
    <div class="user-face">
        <a href="http://www.douban.com/group/people/90826639/"><img class="pil" src="http://img3.douban.com/icon/u90826639-8.jpg" alt="Knicker"></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="http://www.douban.com/group/people/90826639/" class="">Knicker</a>
              <span class="pubtime">2014-08-22 08:33:23</span>
          </h4>
        </div>
        <p class="">为毛这个评论这么少…</p>

        <div class="operation_div" id="90826639">
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="742505611" class="lnk-delete-comment" title="真的要删除Knicker的发言?">删除</a>
            <div class="comment-report"><a rel="nofollow" href="javascript:void(0)">举报</a></div></div>
            <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <a href="http://www.douban.com/group/topic/59743519/?cid=742505611#last" class="lnk-reply">回应</a>
        </div>
    </div>
</li>

        

<li class="clearfix comment-item" id="742885412" data-cid="742885412">
    <div class="user-face">
        <a href="http://www.douban.com/group/people/79719221/"><img class="pil" src="http://img3.douban.com/icon/u79719221-3.jpg" alt="暗夜小白"></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="http://www.douban.com/group/people/79719221/" class="">暗夜小白</a> (白白的骚爷~)
              <span class="pubtime">2014-08-22 16:08:13</span>
          </h4>
        </div>
        <p class="">多高</p>

        <div class="operation_div" id="79719221">
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="742885412" class="lnk-delete-comment" title="真的要删除暗夜小白的发言?">删除</a>
            <div class="comment-report"><a rel="nofollow" href="javascript:void(0)">举报</a></div></div>
            <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <a href="http://www.douban.com/group/topic/59743519/?cid=742885412#last" class="lnk-reply">回应</a>
        </div>
    </div>
</li>

        

<li class="clearfix comment-item" id="742888756" data-cid="742888756">
    <div class="user-face">
        <a href="http://www.douban.com/group/people/72337817/"><img class="pil" src="http://img3.douban.com/icon/u72337817-2.jpg" alt="小桌布"></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="http://www.douban.com/group/people/72337817/" class="">小桌布</a>
              <span class="pubtime">2014-08-22 16:11:44</span>
          </h4>
        </div>
        <p class="">大爱</p>

        <div class="operation_div" id="72337817">
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="742888756" class="lnk-delete-comment" title="真的要删除小桌布的发言?">删除</a>
            <div class="comment-report"><a rel="nofollow" href="javascript:void(0)">举报</a></div></div>
            <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <a href="http://www.douban.com/group/topic/59743519/?cid=742888756#last" class="lnk-reply">回应</a>
        </div>
    </div>
</li>

        

<li class="clearfix comment-item" id="743184746" data-cid="743184746">
    <div class="user-face">
        <a href="http://www.douban.com/group/people/56053744/"><img class="pil" src="http://img3.douban.com/icon/u56053744-16.jpg" alt="质量谢谢"></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="http://www.douban.com/group/people/56053744/" class="">质量谢谢</a> (OH NO!..WHAT IS MY MOTTO?)
              <span class="pubtime">2014-08-22 22:03:56</span>
          </h4>
        </div>
        
        <div class="reply-quote">
            <span class="short">楼主实际职业是什么？</span>
            <span class="all">楼主实际职业是什么？</span>
        <a href="#" class="toggle-reply">
        </a><span class="pubdate"><a href="http://www.douban.com/group/people/74842922/">Adolf Hitler</a></span></div>
        <p class="">目测楼凤</p>

        <div class="operation_div" id="56053744">
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="743184746" class="lnk-delete-comment" title="真的要删除质量谢谢的发言?">删除</a>
            <div class="comment-report"><a rel="nofollow" href="javascript:void(0)">举报</a></div></div>
            <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <a href="http://www.douban.com/group/topic/59743519/?cid=743184746#last" class="lnk-reply">回应</a>
        </div>
    </div>
</li>

        

<li class="clearfix comment-item" id="743227146" data-cid="743227146">
    <div class="user-face">
        <a href="http://www.douban.com/group/people/lxq0216/"><img class="pil" src="http://img3.douban.com/icon/u79325807-3.jpg" alt="来看评论的"></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="http://www.douban.com/group/people/lxq0216/" class="">来看评论的</a>
              <span class="pubtime">2014-08-22 22:48:51</span>
          </h4>
        </div>
        <p class="">已撸</p>

        <div class="operation_div" id="79325807">
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="743227146" class="lnk-delete-comment" title="真的要删除来看评论的的发言?">删除</a>
            <div class="comment-report"><a rel="nofollow" href="javascript:void(0)">举报</a></div></div>
            <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <a href="http://www.douban.com/group/topic/59743519/?cid=743227146#last" class="lnk-reply">回应</a>
        </div>
    </div>
</li>

    </ul>

            

<script type="text/javascript" src="http://img3.douban.com/f/shire/17ffde78bc768c1de53c46d5b5f7fb7f5893c10e/js/report_dialog.js"></script>
<link rel="stylesheet" type="text/css" href="http://img3.douban.com/f/shire/8adca47fea9ac369117af7c709cefe5bbdaf23ae/css/report_dialog.css">



            
        
    <h2>
        你的回应
            
    </h2>

        <div class="txd comment-form">
            <form name="comment_form" method="post" action="add_comment#last" onsubmit="this.onsubmit=function(){return false}"><div style="display:none;"><input type="hidden" name="ck" value="ZB2t"></div>
            <textarea id="last" name="rv_comment" rows="8" cols="54"></textarea><br>
            <script>
                if (window.location.hash.indexOf('#last') + 1) {
                    document.getElementById('last').focus();
                }
            </script>
            <input type="hidden" name="start" value="0">

            <span class="bn-flat-hot rr">
                <input name="submit_btn" type="submit" value="加上去">
            </span>
            

        </form></div>


        
    
    

    



        










        </div>
        <div class="aside" style="position: relative;">
                
    






    







<div id="fixed-anchor942" style="margin: 0px; padding: 0px; border: none; width: 100%; overflow: hidden;"></div>



    
    

      
    
    <div class="mod">
        
    <h2>
        最新话题
            
            <span class="pl">&nbsp;(
                
                    <a href="http://www.douban.com/group/274363/#topics" target="_self">更多</a>
                ) </span>
    </h2>

        <div class="topic-list">
          <ul>
                <li><a href="http://www.douban.com/group/topic/60312694/" title="伦家想找简单的哥哥聊天嘛 25以下的来来~~~">伦家想找简单的哥哥聊天嘛 25以下的来来~~~</a> &nbsp;
                <span class="pl">(咬一口豆豆酱) </span></li>
                <li><a href="http://www.douban.com/group/topic/59743519/" title="晒空姐制服，晒黑色高跟">晒空姐制服，晒黑色高跟</a> &nbsp;
                <span class="pl">(瑶❤瑶) </span></li>
                <li><a href="http://www.douban.com/group/topic/60157693/" title="快来点评一下好嘛！请喷请夸奖啦来吧！！">快来点评一下好嘛！请喷请夸奖啦来吧！！</a> &nbsp;
                <span class="pl">(Serenade) </span></li>
                <li><a href="http://www.douban.com/group/topic/59846476/" title="晒成果喽">晒成果喽</a> &nbsp;
                <span class="pl">(Earl) </span></li>
                <li><a href="http://www.douban.com/group/topic/59722570/" title="晒晒更健康">晒晒更健康</a> &nbsp;
                <span class="pl">(Earl) </span></li>
        </ul>
        </div>
      </div>

      
    <!-- douban ad begin -->
    <div id="dale_group_topic_new_top_right"></div>
    <div id="dale_group_topic_new_top_right_large"></div>
    <div id="dale_group_topic_new_top_right2"></div>
    <!-- douban ad end -->


    <!-- douban app begin -->
    

<div id="fixed-anchor392" style="margin: 0px; padding: 0px; border: none; width: 100%; overflow: hidden;"></div>

    <!-- douban app end -->

    <!-- douban ad begin -->
    <div id="dale_group_topic_doublemint"></div>
    
<!-- douban ad begin -->
<div id="fixed-anchor303" style="margin: 0px; padding: 0px; border: none; width: 100%; overflow: hidden;"></div>
<script type="text/javascript">
    (function (global) {
        var articles = global.document.getElementsByClassName('article'),
            asides = global.document.getElementsByClassName('aside');

        if (articles.length > 0 && asides.length > 0 && articles[0].offsetHeight >= asides[0].offsetHeight) {
            (global.DoubanAdSlots = global.DoubanAdSlots || []).push('dale_group_topic_new_bottom_right');
        }
    })(this);
</script>
<!-- douban ad end -->

    <!-- douban ad end -->

        <div class="fixed-fields" style="position: fixed; padding-top: 10px; width: 300px; top: 0px; left: auto; background-color: rgb(255, 255, 255);"><div id="g-side-info-member" class="side-reg">
  <div class="bd">
      <div class="group-item">
          <div class="pic">
               <a href="http://www.douban.com/group/274363/?ref=sidebar"><img src="http://img3.douban.com/icon/g274363-2.jpg"></a>
          </div>
          <div class="info">
              <div class="title">
				  <a href="http://www.douban.com/group/274363/?ref=sidebar">【晒XX】女神来了-不羞涩招女管理员</a>
              </div>
            <div class="member-info1">我是小组的成员</div>
      </div>
    </div>
  </div>
</div><div class="mod mod-app-entrance">
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
</div><div id="dale_group_topic_new_bottom_right"></div></div></div>
        <div class="extra">
            
    
<!-- douban ad begin -->
<div id="dale_group_topic_bottom_super_banner"></div>
<script type="text/javascript">
    (function (global) {
        var body = global.document.body,
            html = global.document.documentElement;

        var height = Math.max(body.scrollHeight, body.offsetHeight, html.clientHeight, html.scrollHeight, html.offsetHeight);
        if (height >= 2000) {
            (global.DoubanAdSlots = global.DoubanAdSlots || []).push('dale_group_topic_bottom_super_banner');
        }
    })(this);
</script>
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




$(function(){
    $("#joingroupbtn").click(function(){
        url = "/j/group/" + $(this).attr("name") + "/join";
        $.post_withck(url, {},
            function(sjson){
                var ret = eval("(" + sjson + ")");
                $("#joingroupbtn").hide();
                if (ret.result=="toomany"){
                    $("#replysect").html('<p class="attn" align="right">你已经加入了500个小组，无法再加入更多小组。</p>');
                }else{
                    $("#replysect").html('<br/><h2>你现在加入了这个小组，可以发表回应</h2><div class="txd comment-form"><form name="comment_form" method="post" action="add_comment"><div style="display:none;"><input type="hidden" name="ck" value="ZB2t"/></div><textarea name="rv_comment" rows="8" cols="54"></textarea><br/><input type="hidden" name="start" value="0"/><span class="bn-flat-hot rr"><input type="submit" value="加上去"/></span></form></div>');
                }
            });
        return false;
    });

    $(".topic-reply li").bind('mouseenter mouseleave click', function (e) {
        var $this = $(this),
            comment_user_id = $this.find(".operation_div").attr("id"),
            can_delete = 0;
        if (comment_user_id == 87494755){
            can_delete = 1;
        }
        if (can_delete==1){
            $this.find(".lnk-delete-comment").show();
        }
        switch (e.type) {
        case "mouseenter":
            $this.find(".operation-more").show();
            break;
        case "mouseleave":
            $this.find(".operation-more").hide();
            break;
        }
    });


    $('body').delegate('.reply-comment .lnk-close', 'click', function(e){
      e.preventDefault();
      $(this).parent().remove();
    });

});

</script><script type="text/javascript">
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
        
        connectSSE('87494755', '0908981b8bb65eefed2ffd498178ea9b5b592455', '1408719102');
        
        set_cookie({
          push_noty_num: 0,
          push_doumail_num: 0
        });

    });
    </script><script type="text/javascript" src="http://img3.douban.com/misc/mixed_static/5f6456112cdfc947.js"></script>
    


<div class="back-to-top" style="left: 1130px; position: fixed; bottom: 0px; display: block;">
    <a href="#" style="top: 0px;">↑回顶部</a>
</div>
<script>
Do(function(){var h=$(window);var k=$(document);var l;var a=$(".back-to-top");var b=$(".aside");var g;var i=$("#content");var d=$.browser.msie&&($.browser.version|0)<7;var f=function(n){if(!f.cache){f.cache=[]}if(f.cache[n]){return}var m=new Date;(new Image()).src="/stat.html?source=group&action=back_top&iden="+n+"&month="+(m.getMonth()+1)+"&day="+m.getDate()+"&timestamp="+(+new Date);f.cache[n]=1};var e=function(){if(e.value){return e.value}return i.offset().top+i.find(".article").outerHeight()+30};h.load(function(){e.value=e()});var c=function(m){if(m+g>=e()){a.css({position:"absolute",bottom:"",top:e()-a.outerHeight()+40})}else{if(!d){a.css({position:"fixed",top:"",bottom:0})}}a.show().find("a").stop().animate({top:0});f("show")};var j=function(){a.hide().find("a").css("top",40)};h.resize(function(){g=h.height();a.css("left",b.offset().left+b.width()+20);l=k.height()/g>3?Math.max(2*g,$(".aside").height()):0}).trigger("resize");h.scroll((function(){var m;return function(){if(m){clearTimeout(m)}setTimeout(function(){if(l===0){return}var n=k.scrollTop();if(n>l){c(n)}else{j()}},100)}})());a.find("a").click(function(m){m.preventDefault();k.scrollTop(0);f("use")});if(d){h.scroll(function(){if(k.scrollTop()+g>=e()){return}a.css("top",k.scrollTop()+g-a.height()+40)})}});
Do(function() {
  // comment fav num
  var commentsVotes = '{}',
      votes = $.parseJSON(commentsVotes),
      voteId;
  for (vote in votes) {
      voteId = vote.slice(1);
      $('li[data-cid="' + voteId + '"]').find('.comment-vote').append(' ('+ votes[vote] +')');
  }

  function removeComment(obj, cid){
    $.post_withck("/j/group/topic/59743519/remove_comment",{cid:cid}, function(d){
      d = $.parseJSON(d);
      if(d.r == 0){
        if(d.manager){
          window.location = d.url;
        }else{
          location.reload();
        }
      }else{
        alert(d.err_msg);
      }
    });
  }

  $('.reply-quote .toggle-reply').click(function(e) {
    e.preventDefault();
    var el = $(this);
    el.prevAll('span').toggle();
    el.find('span').toggle();
  });

$('.lnk-delete-comment').click(function(){
    var o = $(this);
    var comment = o.closest('.comment-item');
    var cid = $(this).attr("data-cid");
    var need_confirm = true;

    if(need_confirm){
      if(confirm($(this).attr('title'))){
      removeComment(comment, cid);
     }
    }else{
      removeComment(comment, cid);
    }
    return false;
  });

  $('.topic-reply').delegate('.lnk-fav', 'click', function() {
      if (!get_cookie('ck')) {
        $('.a_show_login').eq(0).trigger('click');
        return false;
      }
      var o = $(this),
          comment = o.closest('.comment-item'),
          cid = comment.attr("data-cid"),
          loadClass = 'start-processing';
      if (o.hasClass(loadClass)) {
          return;
      }
      o.addClass(loadClass);
      $.post_withck('/j/group/topic/59743519/add_comment_vote', {cid:cid, start:$('#start').val()}, function(d){
          d = $.parseJSON(d);
          if (d.r === 0 || d.r === 1) {
              var num = o.text().match(/\d+/) || 0;
              num = parseInt(num, 10);
              if (d.r === 0) {
                num ++;
              }
              o.replaceWith(
                  [
                      '<span>已赞 (',
                          num,
                      ')</span>'
                  ].join('')
              );
          }
      });
  });

  /* common dialog generator */
  function generate_group_prompt_dialog(dui_config){
    var prompt_dlg = dui.Dialog({
        title: (dui_config.title? dui_config.title: '操作提示'),
        content: (dui_config.content? dui_config.content: '操作内容'),
        width: (dui_config.width? dui_config.width: 400),
        buttons: [
            {text: '确定', method: function(){} }
        ]
    });
    var dui_dialog_ft_html = function(dui_config){
        if(dui_config.callback){
            $('.dui-dialog').delegate('.btn-ok', 'click', function(){
                dui_config.callback();
            });
        }
        $('.dui-dialog').delegate('.btn-cancel', 'click', function(){
            $(".dui-dialog").hide();
        });
        return '<div><span class="dui-dialog-prompt"><label><input type="checkbox" ' + (dui_config.checked? 'checked=checked ': '') + '/>' + dui_config.prompt + '</label></span><span class="bn-flat btn-cancel">取消</span><span class="bn-flat btn-ok">确定</span></div>';
    };
    prompt_dlg.open();
    prompt_dlg.node.find('.ft').html(dui_dialog_ft_html(dui_config));
  }
  /* common over */
  $('.ban-dialog-confirm').click(function(){
    var ban_action = function(){
        var ban_url = $('.ban-dialog-confirm').attr('href');
        var remove_topic_url = $('.remove-dialog-confirm').attr('href');
        console.log(ban_url);
        $.post(ban_url, {timestamp: (new Date()).getTime()}, function(d){
            $('.ban-dialog-confirm').closest('span').addClass('pl').html('已封禁');
            if($('.dui-dialog-prompt input').attr('checked')){
                window.location = remove_topic_url + "&delete_all=1";
            }
        });
        $('.dui-dialog').hide();
    };
    generate_group_prompt_dialog({content: '真的要把瑶❤瑶永久封禁？', prompt:'同时删除用户在本小组的所有发言和回应', checked: false, callback: ban_action});
    return false;
  });
  $('.remove-dialog-confirm').click(function(){
    var remove_action = function(){
        var ban_url = $('.ban-dialog-confirm').attr('href');
        var remove_topic_url = $('.remove-dialog-confirm').attr('href');
        if($('.dui-dialog-prompt input').attr('checked')){
            $.post(ban_url, {timestamp: (new Date()).getTime()},
                function(r){
                  window.location = remove_topic_url;
            });
        }else{
            window.location = remove_topic_url;
        }
    };
    generate_group_prompt_dialog({content: '真的要删除小组话题 晒空姐制服，晒黑色高跟？', prompt:'同时封禁该成员', callback: remove_action});
    return false;
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
            criteria = '1:274363|2:美女|2:图片|2:性感|2:丝袜|2:照片|3:/group/topic/59743519/',
            preview = '',
            debug = false,
            adSlots = ['dale_group_special3', 'dale_group_special4', 'dale_group_topic_new_top_right', 'dale_group_topic_new_top_right2', 'dale_group_topic_new_top_right_large', 'dale_group_topic_left_bottom', 'dale_group_topic_doublemint'];

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





    <!-- dis5-->


  <script>_SPLITTEST='movie.tv-chart-gaia'</script>

<link type="text/css" rel="stylesheet" href="http://img3.douban.com/f/shire/ae32cb8310a09ba836b958b79d2cd1e706db2fed/css/ui/dialog.css"><script type="text/javascript" src="http://img3.douban.com/f/shire/4b3bad5e25de78678d700dd5353570dce3e6bbcc/js/ui/dialog.js" async="true"></script><link type="text/css" rel="stylesheet" href="http://img3.douban.com/f/sns/356f2de9a7f8cc87fc48093c5439a06ef4f9b8da/css/sns/tag.css"><link type="text/css" rel="stylesheet" href="http://img3.douban.com/f/sns/6110987b4ef71a316ec46c79a9a48612ba59d3dd/css/sns/tag_editor.css"><script type="text/javascript" src="http://img3.douban.com/f/sns/f98a57424167be66f4b092f60b2864a78edf285b/js/sns/tag_editor.js" async="true"></script><script type="text/javascript" src="http://img3.douban.com/f/sns/e87fc7e21434035a4d12db4ed95489e6d5facbdc/js/sns/tag_editor_dialog.js" async="true"></script><script>var _check_hijack = function () {
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

class TestTopicDelegate(PageDelegate.PageDelegateBase):
    def do_img(self, image_urls, jar):
        for image_url in image_urls:
            printTest('image_url: %s' % image_url)
    def do_next_pages(self, next_pages):
        for next_page in next_pages:
            printTest('next_page: %s' % next_page)

    def gen_head_from_jar(self, jar):
        pass
    def get_from_url(self, http_request, callback):
        printTest('method: %s, host: %s, path: %s' % (http_request.method, http_request.host, http_request.path))
        callback(test_html)

def main():
    delegate = TestTopicDelegate()
    PageRoutines.do_topic_page(PageDelegate.HttpRequest('GET', 'douban.com', '/'), None, {'imgs' : 'div.topic-figure.cc>img', 'next_page' : '', 'url_attrib' : 'src'}, delegate)

if __name__ == '__main__':
    main()
