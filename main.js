var MIN_LEN = 12;
var BIG_NBSP = "&nbsp;&nbsp;&nbsp;&nbsp;";

var addWord = function() {
    this.pw.push(words[Math.floor(Math.random() * words.length)]);
}

var updateText = function() {
    var delim = $("#delimit").prop("checked") ? " " : "";
    $("#pw").html(this.pw.join(delim) + BIG_NBSP);
};

var addWordToScreen = function() {
    addWord();
    updateText();
}

var generateMinLenPw = function() {
    this.pw = [];
    while (this.pw.join("").length < MIN_LEN) {
        addWord();
    }
    updateText();
    $("#addWord").remove();
    $("#pwgen").append("<a id='addWord'>" + BIG_NBSP + "Click to add a word</a>");
    $("#addWord").click(addWordToScreen.bind(this));
};

$("#pwgen").remove();
$("body").append("<div id='pwgen'></div>");
$("body").append("<input type='checkbox' id='delimit'>Delimit with spaces?</input>");
$("#pwgen").append("<span id='pw'></span>");
$("#pwgen").append("<a id='genMinLen'>Click to generate an initial password</a>");

this.pw = [];
$("#genMinLen").click(generateMinLenPw.bind(this));
