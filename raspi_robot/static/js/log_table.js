
function evenRows() {
	$('#log_table tbody tr').each().removeClass('even');
	$('#log_table tbody tr:even').addClass('even');
} 

$(document).ready(evenRows);

$('#log_table tbody').bind('DOMSubtreeModified', evenRows);