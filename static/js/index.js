function answercheck() {
	var table = document.getElementById('question_list');
	var answered = 0;
	var inputs = document.getElementsByTagName('input');
	for (i in inputs) {
		if (inputs[i].checked) {
			answered++;
		};
	};
	if (answered === table.rows.length - 1) document.querySelector('#button').disabled = false;
};