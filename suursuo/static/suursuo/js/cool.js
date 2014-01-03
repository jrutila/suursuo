$(document).ready(function () {
  var upAmnt = 30;

  $("nav.home li").each(function () {
    var style = $("a", this).attr('data-background');
    var $div = $("<div class='bg'></div>");
    $div.attr('style', style);
    $("a", this).html("<span class='text'>"+$("a", this).html()+"</span>");
    $("a", this).prepend($div); //<img src='/static/images/heading1.png'/></div>"));
    $(this).append("<div class='up'></div>");
  });

  $("nav li").mouseenter(function() {
    if ($(this).height() > 300)
    {
      $("div.up", this).height(upAmnt+30);
      $(this).animate({
        top: '-='+upAmnt+'px'
      }, 30);
    }
    });
  $("nav li").mouseleave(function() {
    $("div.up", this).height(0);
    $(this).animate({
      top: '0px'
    }, 30);
  });

  $(window).resize(narrowize);
  narrowize();
});

function narrowize()
{
  if ($('nav ul#mainmenu li').length * (parseInt($('nav #mainmenu li').css('min-width')) + 12) > $('nav ul#mainmenu').width())
  {
    $("html").addClass('narrow');
    return;
  }
  $("html").removeClass('narrow');
}
