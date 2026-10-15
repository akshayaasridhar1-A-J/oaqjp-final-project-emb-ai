"use strict";

var EMOTIONS = ["anger", "disgust", "fear", "joy", "sadness"];

function RunSentimentAnalysis() {
    var text    = document.getElementById("textToAnalyze").value.trim();
    var btn     = document.getElementById("analyzeBtn");
    var loader  = document.getElementById("loader");
    var errBox  = document.getElementById("errorMsg");
    var results = document.getElementById("resultPanel");

    if (!text) {
        showError("Invalid text! Please try again.");
        return;
    }

    errBox.style.display  = "none";
    results.style.display = "none";
    loader.style.display  = "block";
    btn.disabled          = true;
    btn.textContent       = "Analyzing...";

    var url = "/emotionDetector?textToAnalyze=" + encodeURIComponent(text);

    fetch(url)
        .then(function(r) {
            return r.json().then(function(d) {
                return { status: r.status, data: d };
            });
        })
        .then(function(response) {
            loader.style.display = "none";
            btn.disabled         = false;
            btn.textContent      = "Analyze Emotion";

            if (response.status !== 200 || response.data.error) {
                showError(
                    response.data.message || "Error. Please try again."
                );
                return;
            }

            var data = response.data;
            var dom  = data.dominant_emotion;

            document.getElementById("dominantBox").textContent =
                "Dominant Emotion: " + dom.toUpperCase();

            EMOTIONS.forEach(function(em) {
                var score = data[em] || 0;
                document.getElementById(
                    "bar-" + em
                ).style.width = (score * 100).toFixed(1) + "%";
                document.getElementById(
                    "score-" + em
                ).textContent = score.toFixed(4);
            });

            document.getElementById("summaryText").innerHTML =
                data.formatted_output || "";

            results.style.display = "block";
        })
        .catch(function() {
            loader.style.display = "none";
            btn.disabled         = false;
            btn.textContent      = "Analyze Emotion";
            showError("Network error. Please try again.");
        });
}

function showError(msg) {
    var el = document.getElementById("errorMsg");
    el.textContent   = msg;
    el.style.display = "block";
    setTimeout(function() {
        el.style.display = "none";
    }, 5000);
}
