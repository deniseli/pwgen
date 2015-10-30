var MIN_LEN = 12;
var BIG_NBSP = "&nbsp;&nbsp;&nbsp;&nbsp;";

var addWord = function() {
    var randArr = window.crypto.getRandomValues(new Uint16Array(1));
    var randNum = randArr * words.length / Math.pow(2, 16);
    this.pw.push(words[Math.floor(randNum)]);
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
    $("#pwgen").append("<button id='addWord'>Add a word</button>");
    $("#addWord").click(addWordToScreen.bind(this));
};

$("#pwgen").remove();
$("body").append("<div id='pwgen'></div>");
$("body").append("<input type='checkbox' id='delimit'>Delimit with spaces?</input>");
$("#pwgen").append("<span id='pw'></span>");
$("#pwgen").append("<button id='genMinLen'>Generate an initial password</button>");

this.pw = [];
$("#genMinLen").click(generateMinLenPw.bind(this));
