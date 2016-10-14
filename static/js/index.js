//轮播自动播放
$('#myCarousel').carousel({
	//自动4秒播放
	interval: 4000,
});
// //设置垂直居中
// $('.carousel-control').css('line-height', $('.carousel-inner img').height() + 'px');
// $(window).resize(function () {
// 	var $height = $('.carousel-inner img').eq(0).height() || 
// 				  $('.carousel-inner img').eq(1).height() || 
// 				  $('.carousel-inner img').eq(2).height();
// 	$('.carousel-control').css('line-height', $height + 'px');
// });
//设置文字垂直居中，谷歌浏览器加载图片的顺序问题，导致高度无法获取
$(window).load(function() {
	$('.text').eq(0).css('margin-top', ($('.auto').eq(0).height() - $('.text').eq(0).height()) / 2 + 'px');
});
$(window).resize(function() {
	$('.text').eq(0).css('margin-top', ($('.auto').eq(0).height() - $('.text').eq(0).height()) / 2 + 'px');
});
$(window).load(function() {
	$('.text').eq(1).css('margin-top', ($('.auto').eq(1).height() - $('.text').eq(1).height()) / 2 + 'px');
});
$(window).resize(function() {
	$('.text').eq(1).css('margin-top', ($('.auto').eq(1).height() - $('.text').eq(1).height()) / 2 + 'px');
});

