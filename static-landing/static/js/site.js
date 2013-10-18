/*modal for sign up*/
$(function() {
	$(".modal-signup").click(function() {
		$("#modal-signup").show();
		return false;
	});
	$(".modal-close").click(function() {
		$("#modal-signup").hide();
	});	
});

/*process images to be responsive*/
$(function () {
	$("img").addClass("img-responsive");
});

/*process prev images*/
$(function () {
	$(".prev").click(function() {
		var posts = $(".post-featured>div");
		for (var i = 0 ; i < posts.length; i++) {
			if (jQuery(posts[i]).css('display') == "block") {
				jQuery(posts[i]).fadeOut();
				jQuery(posts[(i + 1) % posts.length]).fadeIn();
				break;
			}
		}
		return false;
	});
});

/*process next images*/
$(function () {
	$(".next").click(function() {
		var posts = $(".post-featured>div");
		for (var i = posts.length - 1 ; i >= 0; i--) {
			if (jQuery(posts[i]).css('display') == "block") {
				jQuery(posts[i]).fadeOut();
				if (i - 1 < 0) {
					jQuery(posts[i - 1 + posts.length]).fadeIn();
				}
				jQuery(posts[i - 1]).fadeIn();
				break;
			}
		}
		return false;
	});
});



