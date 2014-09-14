
menu_height = 48;

function getNewSize() {
	var stream = $('#stream');
	var scale_width = $(window).width() / stream.width();
 	var scale_height = ($(window).height() - menu_height) / stream.height();

  	if (scale_width < scale_height) {
  		new_width = $(window).width();
  		new_height = stream.height() * new_width / stream.width();
  	}
  	else {
  		new_height = $(window).height() - menu_height;
  		new_width = stream.width() * new_height / stream.height();
  	}
  	return {'height':new_height, 'width':new_width};
}

function scaleImage() {
	var stream = $('#stream');

	var new_size = getNewSize();

	stream.attr('height', new_size['height']);
	stream.attr('width', new_size['width']);
};

$(document).ready(scaleImage);

$(window).resize(scaleImage);
